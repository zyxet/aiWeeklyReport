# AI 论文 & 开源项目周报系统 — 项目总结

> 本文档作为 Kimi「构建应用」的运营看板构建输入。
> 整理时间：2026-11-24 | 数据范围：2026-W15 ~ 2026-W48（约 34 周完整数据）

---

## 一、项目概述

一个全自动化的 AI 情报收集与分析系统，每周执行 6 个定时任务，从 GitHub Trending、arXiv、HuggingFace Papers、中文技术媒体等渠道抓取 LLM / AI Agent 领域的开源项目动态与前沿论文，经过筛选、评分、联动分析后，每周五生成两份中文周报：

1. **《AI 开源周报》** — 开源项目情报（模型 / 工具 / 协议 / SDK / 技能）
2. **《论文-开源联动周报》** — 论文与开源项目的映射分析（A/B/C/D 四类联动）

系统自 2026 年 4 月起持续运行，由 OpenClaw + Kimi AI 驱动，每次任务执行后自动 git commit 并推送。

---

## 二、GitHub 仓库

- **仓库地址：** `https://github.com/zyxet/aiWeeklyReport`
- **分支：** `master`
- **可见性：** 私有仓库（看板应用如需直接拉取数据，需要授权；也可以将数据文件作为知识库上传）
- **更新节奏：** 每个任务完成后自动提交，每周约 6 次 commit

---

## 三、定时任务一览（看板功能 ① 的数据源）

| 任务ID | 任务名称 | 计划时间 | 产出文件 | 说明 |
|--------|----------|----------|----------|------|
| `monday-collect` | 周一情报收集 | 周一 ~09:00 | `data/os-pool-YYYY-WW.md` | GitHub Trending / HF / 中文媒体，10-15 个候选项目 |
| `tuesday-paper-collect` | 周二论文雷达 | 周二 ~10:00 | `data/paper-pool-YYYY-WW.md` | arXiv cs.CL/cs.AI 关键词搜索，15-35 篇候选论文 |
| `wednesday-filter` | 周三深度筛选 | 周三 14:00 | `data/os-shortlist-YYYY-WW.md` | 验证 stars/媒体覆盖，9 候选 → 5-8 入选 + 剔除清单 |
| `thursday-paper-filter` | 周四论文精选 | 周四 14:00 | `data/paper-shortlist-YYYY-WW.md` | 逐篇评分（5 维 × /5），总分 ≥20 入选，通常 6-8 篇 |
| `friday-report` | 周五周报生成 | 周五 17:00 | `data/weekly-report-YYYY-WW.md` | 汇总短名单 + 论文，生成主周报 |
| `friday-paper-merge` | 周五论文-开源联动 | 周五 19:00 | `output/paper-os-linkage-YYYY-WW.md` + `output/weekly-report-paper-os-YYYY-WW.md` | 论文×开源 A/B/C/D 联动分类 + 六大主题 |

### 任务状态追踪文件（核心）

**`logs/execution-log-2026.md`** — 全年每一天的执行状态表，Markdown 表格格式：

```
| 日期 | 星期 | 周次 | 任务ID | 任务名称 | 计划 | 实际 | 产出文件 | 完成时间 | 备注 |
```

- `实际` 列取值：`✅ completed` / `⏳ pending` / `❌ error` / `⏸ rest`（周末）
- 每天任务完成后由系统自动更新对应行
- **看板「任务完成情况」模块应以此文件为准，而非扫描 data/ 目录**

---

## 四、目录结构

```
aiWeeklyReport/
├── data/                                  # 周度数据与中间产物
│   ├── os-pool-YYYY-WW.md                 # 周一：开源候选池（热点项目 + 趋势观察 + 信号）
│   ├── paper-pool-YYYY-WW.md              # 周二：论文候选池（按主题分类的表格）
│   ├── os-shortlist-YYYY-WW.md            # 周三：开源短名单（入选 + 剔除，带 stars/增速/媒体覆盖）
│   ├── paper-shortlist-YYYY-WW.md         # 周四：论文短名单（带五维评分）
│   └── weekly-report-YYYY-WW.md           # 周五：AI 开源周报（主周报）
├── output/                                # 深度分析产出
│   ├── paper-os-linkage-YYYY-WW.md        # 周五：论文-开源联动深度分析
│   └── weekly-report-paper-os-YYYY-WW.md  # 周五：联动周报（主周报的交叉引用副本）
├── logs/
│   └── execution-log-2026.md              # 全年任务执行日志（看板核心数据源）
├── config/
│   └── calendar-2026.yaml                 # 2026 年日历配置（周次映射）
├── cron/
│   ├── jobs.json                          # cron 任务定义
│   └── execution-log.json                 # 执行日志（JSON 副本）
├── scripts/                               # 任务辅助脚本（check-status.py 等 9 个）
├── docs/
│   └── architecture-review.md             # 技术架构审查文档
├── config.md                              # 系统配置与评分标准说明
└── README.md
```

命名规则：`文件名-YYYY-WW.md`，YYYY=年份，WW=ISO 周数（如 `2026-W48`）。

---

## 五、数据文件格式详解（看板功能 ② 的数据源）

### 1. `os-pool-YYYY-WW.md`（周一开源候选池）

三个固定章节，**非表格为主，是自然语言 + 加粗项目名**：

- `## 一、本周热点项目` — 每个项目 `**N. 项目名（机构）**` + 描述段落
- `## 二、领域趋势观察` — 编号趋势段落（如"评测基准全面 agentic 化"）
- `## 三、值得关注的信号` — 短信号列表

> ⚠️ 该文件结构化程度低，分类聚合需按加粗项目名切分 + 关键词归类。

### 2. `paper-pool-YYYY-WW.md`（周二论文候选池）

**结构化程度最高**，按主题分节的 Markdown 表格：

```
## 🤖 Agent 系统与智能体（15 篇）
| # | 标题 | 链接 | 标签 | 一句话摘要 |
```

主题节（emoji 开头）包括：Agent 系统与智能体 / RAG 检索增强 / Reasoning·CoT / Long Context / VLM / Prompt Engineering / 安全与身份。

文件头部有元信息行：收集时间、覆盖区间、周次、来源、数据源异常标注（如"HF Papers 超时"）。

> ✅ **看板「按主题分类」最直接的数据源：统计每周各主题节的论文数量即可得到主题趋势。**

### 3. `os-shortlist-YYYY-WW.md`（周三开源短名单）

Markdown 表格，结构化程度高：

```
| # | 项目 | 实时 Stars | 本周增速 | 媒体 Coverage | 一句话定位 | 入选理由 |
```

另有「剔除项目」表（项目 / stars / 剔除原因）和「关键趋势解读」段落。

> ✅ 可做 stars 增长趋势、入选率（候选→入选漏斗）统计。

### 4. `paper-shortlist-YYYY-WW.md`（周四论文短名单）

每篇论文一个区块：

```
## 🏆 #1 WeightBench: ... (23/25)
- **分数**: 创新5 | 实用4 | 深度4 | 背书5 | 代码5
- **链接**: https://arxiv.org/abs/...
- **摘要**: ...
- **代码**: ✅ github 链接 / ❓ 未知
```

五维评分各 /5，总分 /25，入选线 ≥20。

> ✅ **看板「评分维度」数据源：五维雷达图、周/月度高分论文榜。**

### 5. `weekly-report-YYYY-WW.md`（周五主周报）

- 本周主题行（3 个关键词）
- `## 本周概览` 表：`| # | 项目 | 分类 | 一句话 | 本周最大变化 |` — **「分类」列取值**：模型 / 工具 / 协议 / SDK / 技能 等
- 本周趋势一句话（长段落）
- `## 论文-开源映射表（A-D 分类）`：A类 论文+官方代码 / B类 论文+社区复现 / C类 论文先行 / D类 项目先行

### 6. `paper-os-linkage-YYYY-WW.md`（周五联动分析）

- A/B/C/D 四类清单（含数量统计，如"A类 5 · B类 0 · C类 3 · D类 7"）
- 六大主题（编号主题段落，如"Agent 记忆框架转换"）
- 联动矩阵、趋势判断、下周关注清单

> ✅ **看板「A-D 联动比例周趋势」数据源：从每周报头提取 "A类 X · B类 Y · C类 Z · D类 W"。**

---

## 六、看板功能需求映射

### 功能 ①：定时任务完成情况

数据源：`logs/execution-log-2026.md`

建议呈现：
- 本周/本月任务执行状态表（含完成时间、产出文件链接）
- 任务成功率趋势图（周维度：6 任务中成功数）
- 异常高亮（❌ error 行）
- 当前周进度条（今天之前的任务完成情况）

### 功能 ②：主题 / 热点分类汇总 + 可视化

| 维度 | 数据源 | 可视化建议 | 周期 |
|------|--------|-----------|------|
| 论文主题分布 | paper-pool 各主题节计数 | 堆叠柱状图 / 热力图（主题 × 周） | 周/月/季度 |
| 论文五维评分 | paper-shortlist 分数行 | 雷达图 / 平均分趋势线 | 周/月 |
| 开源项目分类 | weekly-report 概览表「分类」列 | 饼图 / 分类趋势 | 周/月/季度 |
| 开源 stars 热度 | os-shortlist Stars/增速列 | TOP N 排行 / 增速榜 | 周 |
| A-D 联动结构 | linkage 报头 A/B/C/D 计数 | 堆叠面积图（A-D 占比随周变化） | 周/月 |
| 候选→入选漏斗 | os-pool 候选数 vs os-shortlist 入选数 | 漏斗图 | 周 |
| 热点主题词 | 各周报「本周主题」行 + 趋势段落 | 词云 / 主题时间线 | 月/季度 |

时间维度：数据按 ISO 周组织，月/季度趋势需将 ISO 周映射到自然月/季度（注意跨月周的处理，如 W48 = 11.17-11.23）。

---

## 七、数据质量说明（已知坑，构建时需处理）

1. **历史命名不一致**（README 未同步）：
   - 旧名 `candidate-pool-*.md` / `shortlist-*.md` → 现名 `os-pool-*.md` / `os-shortlist-*.md`（W15 起统一）
   - `weekly-paper-selection-2026-24.md`（格式错误遗留）、`weekly-paper-selection-2026-W22/W23.md`（旧命名）
   - 部分文件带 `-orig.md` 后缀（补跑前的原始版本）
2. **缺失文件**：
   - `output/paper-os-linkage-2026-W18.md`、`W24` 缺失（当周任务异常）
   - W17 之前的联动周报副本命名不统一
3. **格式波动**：
   - os-pool 的章节标题措辞偶有变化（"一、本周热点项目" vs "一、大模型层"）
   - paper-pool 主题节数量随当周内容增减（3~8 个不等）
   - os-shortlist 表格列数在不同周有微调
4. **执行日志最可靠**：任务状态以 `logs/execution-log-2026.md` 为准，文件存在性仅作辅助校验。
5. **数据源异常记录**：paper-pool 文件头部会标注当周数据源故障（如"HF Papers 超时"），可用于看板的「数据质量」提示。

---

## 八、系统运行现状（截至 2026-11-24）

- 数据完整覆盖 W15（2026-04 中旬）~ W48，共约 34 周
- 6 个定时任务全部正常运作，W47 整周闭环，W48 已完成周一/周二
- 数据源：arXiv API（主）、GitHub Trending、HF Papers（间歇超时）、PaperWeekly（间歇停更）
- 每次执行自动 git commit + push，commit message 格式：`周报 WXX <任务名>`
