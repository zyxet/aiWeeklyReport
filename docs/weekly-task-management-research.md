# 周期性任务管理方案调研报告

> **调研目标**: 执行频率为每天，循环逻辑为每周（当周内每天执行的内容/步骤不同）的任务管理方案
> **覆盖维度**: 计划 → 启动 → 执行 → 验证 → 补跑 → 总结
> **调研范围**: 开源项目（Apache Airflow, Dagster, Prefect, Cronicle, GitHub Actions）+ 技术博客/最佳实践
> **生成时间**: 2026-05-15

---

## 一、计划阶段

### 1.1 任务编排的核心模式：DAG + 时间分区

所有现代工作流编排工具都采用 **DAG（有向无环图）** 作为基础抽象，但处理"周内差异化"的方式不同：

| 工具 | 周内差异化机制 | 代表案例 |
|------|---------------|---------|
| **Apache Airflow** | `BranchPythonOperator` 基于 `execution_date.weekday()` 在运行时选择分支 | 周一执行全量数据抓取，周二-周五执行增量更新 |
| **Dagster** | `DailyPartitionsDefinition` + 条件资源加载，每个分区独立执行 | 每日作为独立分区，通过 `BackfillPolicy` 控制批量行为 |
| **Prefect** | 任务流内的条件逻辑 + 参数化运行（parameterized runs） | 通过 `prefect.flow` 的参数传入星期几，动态选择任务集合 |
| **Temporal** | Workflow 代码内的 `if/else` 或 `switch` 逻辑 | 用编程语言原生控制流实现周内分支 |

**关键设计原则**：
- **分区化（Partitioning）**：将每天视为一个独立的数据/执行分区，便于追溯和补跑
- **幂等性（Idempotency）**：同一天的任务多次执行结果一致，这是补跑的前提
- **声明式 vs 编程式**：Airflow/Dagster 偏声明式（YAML/DSL），Temporal 偏编程式（代码内逻辑）

### 1.2 调度触发方式

| 触发方式 | 适用场景 | 配置示例 |
|---------|---------|---------|
| **Cron 表达式** | 固定时间点启动 | `0 6 * * 1-5`（工作日每天6点） |
| **间隔触发** | 固定间隔，不关心具体时间点 | `@every 24h` |
| **事件触发** | 上游数据就绪后启动 | 新文件到达 S3 → 触发处理 |
| **手动触发** | 补跑、调试 | `workflow_dispatch`（GitHub Actions） |

**周内差异化的推荐做法**（以 Airflow 为例）：
```python
# 一个 DAG 覆盖整周，每天自动判断该做什么
from airflow.operators.python import BranchPythonOperator

def choose_daily_branch(**context):
    weekday = context['execution_date'].weekday()  # 0=周一
    if weekday == 0:
        return 'monday_full_scrape'      # 周一：全量
    elif weekday == 1:
        return 'tuesday_paper_radar'     # 周二：论文
    elif weekday in [2, 3]:
        return 'midweek_deep_filter'     # 周三/四：筛选
    else:
        return 'friday_weekly_report'    # 周五：周报

branch = BranchPythonOperator(
    task_id='choose_daily_task',
    python_callable=choose_daily_branch
)
```

---

## 二、启动阶段

### 2.1 启动前的依赖检查

生产级管道在启动前会检查：

| 检查项 | 目的 | 实现方式 |
|--------|------|---------|
| **上游数据就绪** | 避免空跑或基于不完整数据执行 | 传感器（Sensor）轮询文件/API 状态 |
| **资源可用性** | CPU/内存/磁盘/API 额度 | 资源配额检查或动态扩缩容 |
| **外部服务健康** | API、数据库、第三方服务 | 健康检查端点（health check） |
| **时钟同步** | 分布式环境下时间一致性 | NTP 同步校验 |

**Dagster 的传感器示例**：
```python
@dg.sensor(job=my_weekly_job)
def upstream_data_sensor():
    if check_github_trending_updated():  # 自定义检查逻辑
        return dg.RunRequest()
    return dg.SkipReason("GitHub Trending 尚未更新")
```

### 2.2 启动日志与审计

- **执行上下文记录**：记录触发方式（定时/手动/事件）、触发时间、执行者身份
- **版本追踪**：代码版本、数据版本、配置版本一并记录，确保可复现
- **环境快照**：记录运行时环境变量、依赖版本

---

## 三、执行阶段

### 3.1 执行策略：串行 vs 并行 vs 批量

| 策略 | 优点 | 缺点 | 适用场景 |
|------|------|------|---------|
| **单分区单运行（One per partition）** | 故障隔离最好，粒度最细 | 调度开销大（100天=100次启动） | API 有额度限制、需要逐日细粒度观察 |
| **批量运行（Batched）** | 减少开销，保持中等隔离 | 一批失败需整批重试 | 处理时间短（秒级）、初始回填 |
| **单运行全量（Single run）** | 开销最低 | 无故障隔离，失败需全量重跑 | Spark/Snowflake 等并行引擎、范围查询 |

**Dagster 的 `BackfillPolicy` 选择**：
```python
# 单分区 - 最细粒度
daily_partitions = dg.DailyPartitionsDefinition(start_date="2024-01-01")

@dg.asset(partitions_def=daily_partitions, backfill_policy=dg.BackfillPolicy.single_run())
def process_all_in_one():  # 一次性处理所有选中分区
    ...

@dg.asset(partitions_def=daily_partitions, backfill_policy=dg.BackfillPolicy.multi_run(max_partitions_per_run=10))
def process_in_batches():  # 每10个分区一批
    ...
```

### 3.2 执行中的容错与重试

| 机制 | 说明 | 配置示例 |
|------|------|---------|
| **自动重试（Retry）** | 瞬时失败（网络抖动、API 超时）自动重试 | `retries=3, retry_delay=5min` |
| **超时控制（Timeout）** | 防止任务无限挂起 | `execution_timeout=30min` |
| **断路器（Circuit Breaker）** | 连续失败多次后暂停，避免雪崩 | 连续5次失败后告警并暂停调度 |
| **降级执行（Degraded Mode）** | 部分失败时继续执行剩余部分 | 跳过不可用的数据源，标记为部分完成 |

---

## 四、验证阶段

### 4.1 数据质量门控（Data Quality Gates）

**核心原则**：不要假设"跑完=成功"。必须在下游消费前验证产出。

| 验证类型 | 检查内容 | 示例 |
|---------|---------|------|
| **行数/体积检查** | 产出数据量是否符合预期范围 | 日报应有 50-200 条记录，低于20条告警 |
| **格式/schema 校验** | 字段是否存在、类型是否正确 | 检查 `title`, `url`, `stars` 字段是否齐全 |
| **时效性检查** | 数据时间范围是否正确 | 论文池应包含本周新论文，而非旧数据 |
| **一致性检查** | 跨文件/跨表的关联数据是否一致 | `paper-shortlist` 中的论文应能在 `paper-pool` 中找到 |
| **异常检测** | 历史对比，识别异常波动 | 本周论文数比上周少80% → 可能API故障 |

**实践案例**（来自 Four Keys 和 DORA 框架）：
- 定义 SLA：数据必须在生成后 X 小时内可用
- 颜色编码：绿色（健康）、黄色（警告）、红色（失败）
- MTTD（平均检测时间）、MTTR（平均恢复时间）作为核心指标

### 4.2 验证失败的处置

| 处置方式 | 场景 | 操作 |
|---------|------|------|
| **标记为可疑（Quarantine）** | 数据通过基础检查但存在异常 | 产出文件加 `SUSPECT_` 前缀，通知用户 |
| **阻断下游（Block Downstream）** | 严重数据错误 | 停止触发下游任务，防止错误扩散 |
| **自动补跑触发** | 验证发现缺失数据 | 自动重新执行上游抓取任务 |
| **人工审批** | 关键报告发布前 | 周报生成后进入"待审核"状态，确认后发布 |

---

## 五、补跑阶段

### 5.1 补跑（Backfill / Catch-up）策略

这是"每周循环"场景最核心的能力之一——某天失败了，如何不破坏整周节奏地补上。

| 补跑类型 | 触发方式 | 实现要点 |
|---------|---------|---------|
| **时间分区补跑** | 发现某天数据缺失 | 指定 `start_date` + `end_date`，工具自动逐天重跑 |
| **单点重试** | 某天某一步骤失败 | 仅重跑失败任务，保留已成功步骤的结果 |
| **事件重放** | 上游数据修正后 | 重新触发特定日期分区的处理 |

**Airflow Backfill CLI**：
```bash
# 补跑 5月1日到5月10日的所有分区
airflow dags backfill weekly_intelligence \
    --start-date 2026-05-01 \
    --end-date 2026-05-10 \
    --reset-dagruns  # 重置已存在的运行记录
```

**Dagster 分区回填**：
- UI 上选择缺失的分区（以日历网格形式展示），一键回填
- 支持 `BackfillPolicy` 控制单分区/批量/单运行策略
- 回填时自动应用最新版本的代码

### 5.2 补跑的依赖处理

**关键问题**：补跑周二时，周五的周报已经跑完了，怎么办？

| 策略 | 说明 |
|------|------|
| **级联补跑（Cascading Backfill）** | 补跑周二 → 自动重新触发周三、周四、周五（因为下游依赖变了） |
| **范围补跑（Range Backfill）** | 指定"从周二到周五"，工具自动按依赖顺序重跑 |
| **手动标记（Manual Override）** | 仅补跑周二，周五周报保持不变（适合非核心数据） |

**推荐做法**：对于周报这种"下游汇总"场景，**补跑任何一天都应自动重新触发周五的汇总任务**，因为周报内容可能已改变。

### 5.3 补跑的状态追踪

- **回填进度条**：显示 `已完成 3/7 天`
- **回填日志**：独立记录，不覆盖原始执行日志
- **回填标记**：产出文件标注 `BACKFILLED_2026-05-06` 便于追溯

---

## 六、总结阶段

### 6.1 执行报告（Job Summary）

每次执行后自动生成结构化报告：

| 报告项 | 内容 | 示例 |
|--------|------|------|
| **执行时间** | 开始/结束/耗时 | `14:00-14:35 (35min)` |
| **任务状态** | 各步骤成功/失败/跳过 | `✅ 抓取 ✅ 筛选 ❌ 翻译（跳过） ✅ 输出` |
| **产出清单** | 生成的文件/记录 | `weekly-report-2026-W20.md (7.2KB)` |
| **异常记录** | 警告、非致命错误 | `API rate limit 触发，3篇论文延迟抓取` |
| **数据质量** | 质量门控结果 | `行数检查通过(45篇)，时效性通过` |

**GitHub Actions Job Summary** 示例：
```yaml
- name: Generate Job Summary
  run: |
    echo "## Weekly Intelligence Report W20" >> $GITHUB_STEP_SUMMARY
    echo "- ✅ Candidate pool: 40 projects" >> $GITHUB_STEP_SUMMARY
    echo "- ✅ Paper pool: 220 papers" >> $GITHUB_STEP_SUMMARY
    echo "- ⚠️ Translation skipped (API limit)" >> $GITHUB_STEP_SUMMARY
```

### 6.2 周级汇总仪表盘

| 维度 | 展示方式 | 工具 |
|------|---------|------|
| **每日状态墙** | 周一到周日，每天一格（绿/黄/红） | Markdown 表格、Status Badge |
| **失败趋势** | 近4周的失败率折线图 | Grafana、Streamlit |
| **执行时长趋势** | 识别性能退化 | CI/CD 内置图表 |
| **数据质量评分** | 综合质量指标 | 自定义 Dashboard |

**轻量方案：GitHub Status Badge + Markdown 看板**
```markdown
| 周次 | 周一 | 周二 | 周三 | 周四 | 周五 | 状态 |
|------|------|------|------|------|------|------|
| W20 | ✅ | ✅ | ✅ | ✅ | ✅ | 全绿 |
| W19 | ✅ | ❌ | ✅ | ✅ | ✅ | 周二补跑 |
```

### 6.3 通知与告警

| 触发条件 | 通知方式 | 最佳实践 |
|---------|---------|---------|
| **任务失败** | Slack/邮件/飞书 | 包含失败步骤、错误日志摘要、一键补跑链接 |
| **数据质量告警** | 降级通知 | 不阻塞但提醒用户关注 |
| **补跑完成** | 静默更新 | 在看板上更新状态即可，减少噪音 |
| **周报发布** | 主动推送 | 发送摘要 + 全文链接 |

### 6.4 经验沉淀

- **失败模式库**：记录常见失败原因和解决方案（如 "arXiv API rate limit → 改用凌晨调度"）
- **性能基线**：记录正常执行时长，识别异常慢的任务
- **数据演进追踪**：对比连续数周的数据特征，发现趋势

---

## 七、各方案对比与适用建议

| 方案 | 复杂度 | 监控能力 | 补跑能力 | 适合场景 |
|------|--------|---------|---------|---------|
| **GitHub Actions + 自研脚本** | 低 | 中等（Badge + Job Summary） | 手动/半自动 | 已有 GitHub 仓库、任务简单、不需要复杂编排 |
| **Cronicle / Ofelia** | 低 | 良好（Web UI + 日志） | 手动触发 | 单机/小集群、需要Web界面管理cron |
| **Apache Airflow** | 中高 | 强（完整UI + 回填） | 强（分区级/批量） | 成熟团队、任务复杂、需要精细控制 |
| **Dagster** | 中高 | 强（数据血缘 + 质量门控） | 强（分区策略丰富） | 数据管道为核心、强调数据质量 |
| **Prefect** | 中 | 强（现代UI + 事件驱动） | 中等 | 云原生、事件驱动、Python优先 |
| **Temporal** | 高 | 强（工作流级持久化） | 强（状态机级恢复） | 超大规模、长周期工作流、金融级可靠性 |

### 针对"每周情报周报"场景的推荐

**当前状态**：使用 OpenClaw Cron + 自研脚本，GitHub 作为数据出口

**渐进式优化路线**：

1. **立即可做（零依赖）**：
   - 在 `intelligence-system/status/` 下建立 `W20.md` 状态看板
   - 每次任务执行后追加一行状态记录
   - 失败时记录原因到 `failures.md`

2. **短期（使用现有工具）**：
   - 利用 GitHub Actions 的 `schedule` + `workflow_dispatch` 实现手动补跑按钮
   - 用 GitHub Job Summary 生成执行报告
   - README 加 Status Badge 展示本周状态

3. **中期（如需更强能力）**：
   - 引入 Dagster 或 Airflow 的轻量部署（Docker Compose）
   - 将每天定义为分区，获得自动回填能力
   - 添加数据质量校验步骤

4. **长期（规模化后）**：
   - 完整的分区化管道 + 自动级联补跑
   - 实时仪表盘 + 告警分级
   - 数据血缘追踪（论文→短名单→周报的全链路）

---

## 八、关键结论

1. **"周内差异化"的标准解法**：一个 DAG/Flow 覆盖整周，运行时根据 `weekday()` 选择分支，而非创建7个独立任务
2. **补跑是核心痛点**：方案选型时，回填（Backfill）能力应作为首要评估指标
3. **验证不能省略**：跑完≠成功，必须有数据质量门控防止"静默失败"
4. **GitHub 本身就是轻量看板**：README + Actions Badge + Job Summary 组合，零额外成本实现状态可视化
5. **渐进式升级**：从 Markdown 看板 → GitHub Actions → 专业编排工具，按痛点优先级逐步增强

---

*报告结束。如需深入某个具体工具的实践细节，或基于现有 OpenClaw Cron 架构设计迁移方案，可以继续展开。*
