# AI开源情报周报 · 技术架构审查报告

> **审查日期**: 2026-05-07
> **审查范围**: 周一到周五完整6轮定时任务
> **目标**: 识别与 Kimi Claw / OpenClaw 的耦合点，评估移植可行性

---

## 一、系统架构总览

```
┌─────────────────────────────────────────────────────────────┐
│                    外部数据源层                                │
│  GitHub Trending │ arXiv cs.CL/LG/AI │ HuggingFace Papers    │
│  PaperWeekly     │ 机器之心/量子位    │ HackerNews            │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                    采集与处理层                                │
│  web_search / kimi_search  →  信息检索                       │
│  kimi_fetch               →  网页抓取（arXiv/GitHub）        │
│  exec (git/bash)          →  文件操作、版本控制              │
│  read/write/edit          →  Markdown 文件生成              │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                    存储与分发层                                │
│  GitHub 仓库  →  数据持久化、历史追溯                        │
│  本地文件系统  →  ~/.openclaw/workspace/...                  │
│  Feishu/Lark  →  通知推送、周报交付                          │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                    调度与执行层                                │
│  OpenClaw Cron  →  6个定时任务（周一~周五）                  │
│  Isolated Session →  隔离执行环境                            │
│  Kimi k2p5      →  大模型推理（分析、评分、写作）             │
└─────────────────────────────────────────────────────────────┘
```

---

## 二、组件清单与耦合度分析

### 2.1 数据源层（耦合度：低 ✅）

| 数据源 | 接入方式 | 是否可移植 | 替代方案 |
|--------|---------|-----------|---------|
| GitHub Trending | `web_search` / `kimi_search` | ✅ 完全可移植 | GitHub API, RSS, 直接抓取 |
| arXiv cs.CL/LG/AI | `kimi_fetch` 访问页面 | ✅ 可移植 | arXiv API, OAI-PMH, RSS feed |
| Hugging Face Papers | `web_search` | ✅ 完全可移植 | HF API, daily-papers 仓库 |
| PaperWeekly | `web_search` | ✅ 完全可移植 | RSS, 直接订阅 |
| 机器之心/量子位 | `web_search` | ✅ 完全可移植 | RSS, 官网 API |

**结论**: 所有数据源都是公开互联网服务，无 Kimi/OpenClaw 专属依赖。

### 2.2 采集工具层（耦合度：中~高 ⚠️）

| 工具 | 所属系统 | 功能 | 耦合度 | 替代方案 |
|------|---------|------|--------|---------|
| `kimi_search` | Kimi 插件 | 互联网搜索 | **高** | `web_search`(通用), Google/Bing API |
| `kimi_fetch` | Kimi 插件 | 网页内容抓取 | **高** | `web_fetch`(通用), curl, requests, Playwright |
| `web_search` | OpenClaw 通用 | 互联网搜索 | **低** | 任何搜索 API |
| `web_fetch` | OpenClaw 通用 | 网页抓取 | **低** | curl, wget, requests |
| `exec` (bash) | OpenClaw 通用 | Shell 命令 | **低** | 任何 shell 环境 |
| `read/write/edit` | OpenClaw 通用 | 文件操作 | **低** | 标准文件系统 API |
| `git` (via exec) | 系统级 | 版本控制 | **无** | 任何 git 客户端 |

**关键发现**:
- **周二、周四任务重度依赖 `kimi_fetch`** — 直接访问 arXiv 页面提取论文标题/作者/摘要/代码链接
- **周一、周三、周五任务依赖 `kimi_search` 或 `web_search`** — 搜索 GitHub/HuggingFace/技术媒体
- `kimi_fetch` 在 arXiv API rate limit 时作为 fallback 被大量使用（如 W19 周二补跑）

### 2.3 存储层（耦合度：低 ✅）

| 组件 | 耦合度 | 说明 |
|------|--------|------|
| GitHub 仓库 | **无** | 标准 git 操作，`git add/commit/push` |
| 本地 Markdown 文件 | **低** | 标准文件系统路径，仅需替换 `~/.openclaw/workspace/` 前缀 |
| 文件命名规则 | **无** | `filename-YYYY-WW.md` 是业务约定，与框架无关 |

### 2.4 通知/交付层（耦合度：高 🔒）

| 工具 | 所属系统 | 功能 | 耦合度 | 替代方案 |
|------|---------|------|--------|---------|
| `feishu_im_user_message` | OpenClaw Lark 插件 | 以用户身份发飞书消息 | **高** | 飞书 Bot API, Webhook, 邮件, Slack API |
| `message` (channel=feishu) | OpenClaw 核心 | 通道消息发送 | **高** | 任何 IM 的 Bot API |
| 硬编码 `receive_id` | 业务配置 | `ou_09155c31d3b9f3b2e47e1f703752b2e2` | **高** | 需替换为目标用户/群的 ID |

**关键发现**:
- 6个任务的 system prompt 中都**硬编码了飞书通知逻辑**
- 通知内容中使用了 `$(date)` 等 shell 变量替换，这在其他框架中需要适配
- 当前飞书 OAuth 已失效，实际通知功能已中断（W15~W19 均未成功推送）

### 2.5 调度与执行层（耦合度：极高 🔒🔒）

| 组件 | 所属系统 | 耦合度 | 替代方案 |
|------|---------|--------|---------|
| `openclaw cron` | OpenClaw 专属 | **极高** | Linux cron, systemd timer, GitHub Actions, Airflow |
| `sessionTarget: isolated` | OpenClaw 专属 | **极高** | 任何隔离执行环境（Docker, 独立进程） |
| `payload.kind: agentTurn` | OpenClaw 专属 | **极高** | 任何 LLM API 调用（OpenAI, Claude, 本地模型） |
| System Prompt 嵌入 cron | OpenClaw 专属 | **极高** | 需提取为独立 prompt 文件 |
| `kimi/k2p5` 模型 | Kimi 专属 | **高** | 任何 LLM（Claude, GPT, Llama, DeepSeek） |

**关键发现**:
- 所有业务逻辑（搜索什么、怎么评分、怎么筛选）都**嵌入在 cron 的 system prompt 中**
- 这不是配置，而是**完整的 prompt 工程**，包含详细的任务步骤、评分标准、输出格式
- 移植时需要将这些 prompt 提取为独立文件或函数

---

## 三、逐任务耦合度拆解

### 周一情报收集（collect-monday）

| 步骤 | 工具/依赖 | 耦合度 | 移植要点 |
|------|----------|--------|---------|
| 1. 搜索 GitHub Trending | `web_search` / `kimi_search` | 中 | 替换为通用搜索工具 |
| 2. 搜索 HF Papers | `web_search` | 低 | 直接移植 |
| 3. 搜索中文媒体 | `web_search` | 低 | 直接移植 |
| 4. 生成 Markdown | `write` | 低 | 标准文件操作 |
| 5. Git 提交 | `exec(git)` | 无 | 标准 git |
| 6. 飞书通知 | `feishu_im_user_message` | **高** | 需替换为其他通知渠道 |

**耦合度**: 中低。核心依赖是搜索工具，通知是可选功能。

### 周二论文雷达（paper-collect-tuesday）

| 步骤 | 工具/依赖 | 耦合度 | 移植要点 |
|------|----------|--------|---------|
| 1. 访问 arXiv cs.CL recent | `kimi_fetch` | **高** | 必须用 arXiv API 或通用抓取工具替代 |
| 2. 访问 arXiv cs.LG/AI | `kimi_fetch` | **高** | 同上 |
| 3. 搜索 HF Papers | `web_search` | 低 | 直接移植 |
| 4. 搜索 PaperWeekly | `web_search` | 低 | 直接移植 |
| 5. 筛选关键词匹配 | LLM 推理 | 中 | 任何 LLM 均可 |
| 6. 生成 Markdown | `write` | 低 | 标准文件操作 |
| 7. Git 提交 | `exec(git)` | 无 | 标准 git |
| 8. 飞书通知 | `feishu_im_user_message` | **高** | 需替换 |

**耦合度**: **中高**。`kimi_fetch` 是核心瓶颈，arXiv API rate limit 时 fallback 也依赖它。

### 周三深度筛选（filter-wednesday）

| 步骤 | 工具/依赖 | 耦合度 | 移植要点 |
|------|----------|--------|---------|
| 1. 读取候选池 | `read` | 低 | 标准文件操作 |
| 2. 验证 Star 数 | `web_search` | 低 | 直接移植 |
| 3. 搜索技术测评 | `web_search` | 低 | 直接移植 |
| 4. 筛选评分 | LLM 推理 | 中 | 任何 LLM |
| 5. 生成短名单 | `write` | 低 | 标准文件操作 |
| 6. 人工介入暂停 | OpenClaw 会话 | **高** | 需设计替代交互机制 |
| 7. Git 提交 | `exec(git)` | 无 | 标准 git |
| 8. 飞书通知 | `feishu_im_user_message` | **高** | 需替换 |

**耦合度**: 中。核心依赖是 LLM 推理，人工介入点需要重新设计。

### 周四论文精选（paper-filter-thursday）

| 步骤 | 工具/依赖 | 耦合度 | 移植要点 |
|------|----------|--------|---------|
| 1. 读取论文池 | `read` | 低 | 标准文件操作 |
| 2. 访问 arXiv 摘要页 | `kimi_fetch` | **高** | 必须用 arXiv API 或通用抓取替代 |
| 3. 提取标题/作者/摘要 | LLM + `kimi_fetch` | **高** | 页面解析逻辑需重写 |
| 4. 生成中文摘要 | LLM 推理 | 中 | 任何 LLM |
| 5. 论文评分（5维度） | LLM 推理 | 中 | 任何 LLM |
| 6. 关联开源池 | `read` + LLM | 低 | 标准文件 + 任何 LLM |
| 7. 生成精选文件 | `write` | 低 | 标准文件操作 |
| 8. 人工介入暂停 | OpenClaw 会话 | **高** | 需设计替代交互机制 |
| 9. Git 提交 | `exec(git)` | 无 | 标准 git |
| 10. 飞书通知 | `feishu_im_user_message` | **高** | 需替换 |

**耦合度**: **高**。`kimi_fetch` 访问 arXiv 并提取结构化信息是核心路径，且评分标准（25分制）嵌入在 prompt 中。

### 周五周报生成（report-friday）

| 步骤 | 工具/依赖 | 耦合度 | 移植要点 |
|------|----------|--------|---------|
| 1. 读取精选池 | `read` | 低 | 标准文件操作 |
| 2. 深度扫描项目 | `kimi_fetch` (GitHub README) | **高** | 需用 GitHub API 或通用抓取替代 |
| 3. 搜索相关文章 | `web_search` | 低 | 直接移植 |
| 4. 分类判断 | LLM 推理 | 中 | 任何 LLM |
| 5. 生成周报 | `write` | 低 | 标准文件操作 |
| 6. 发送到飞书 | `message` (channel=feishu) | **高** | 需替换为其他渠道 |
| 7. Git 提交 | `exec(git)` | 无 | 标准 git |
| 8. 飞书通知 | `feishu_im_user_message` | **高** | 需替换 |

**耦合度**: **中高**。`kimi_fetch` 抓取 GitHub README 是核心依赖。

### 周五论文-开源联动（paper-merge-friday）

| 步骤 | 工具/依赖 | 耦合度 | 移植要点 |
|------|----------|--------|---------|
| 1. 读取论文池+开源池 | `read` ×2 | 低 | 标准文件操作 |
| 2. 生成映射表 | LLM 推理 | 中 | 任何 LLM |
| 3. A-D 分类 | LLM 推理 | 中 | 任何 LLM |
| 4. 生成合并周报 | `write` | 低 | 标准文件操作 |
| 5. 发送到飞书 | `message` + `feishu_im_user_message` | **高** | 需替换 |
| 6. Git 提交 | `exec(git)` | 无 | 标准 git |

**耦合度**: 中。主要是文件读取和 LLM 推理，无外部抓取。

---

## 四、重度耦合组件清单

### 🔒 必须替换的组件

| 组件 | 当前实现 | 移植替代方案 | 工作量 |
|------|---------|-------------|--------|
| **定时调度** | `openclaw cron` | Linux cron / systemd timer / GitHub Actions / Airflow | 中 |
| **任务隔离** | `sessionTarget: isolated` | Docker 容器 / 独立进程 / GitHub Actions runner | 中 |
| **arXiv 抓取** | `kimi_fetch https://arxiv.org/list/cs.CL/recent` | arXiv API (OAI-PMH) / RSS feed / curl + 解析 | **高** |
| **论文摘要提取** | `kimi_fetch https://arxiv.org/abs/xxxxx` | arXiv API (export 格式) / curl + 正则解析 | **高** |
| **GitHub README 抓取** | `kimi_fetch https://github.com/...` | GitHub API (contents endpoint) / curl | 中 |
| **通知推送** | `feishu_im_user_message` + `message` | 邮件 / Slack API / Discord webhook / Telegram Bot | 中 |
| **Prompt 工程** | 嵌入在 cron systemPrompt | 提取为独立 `.prompt` 或 `.md` 文件 | 中 |
| **硬编码路径** | `~/.openclaw/workspace/...` | 配置化路径（env var 或 config file） | 低 |

### ⚠️ 需要注意的隐性耦合

| 问题 | 说明 | 影响 |
|------|------|------|
| **arXiv API rate limit** | 当前用 `kimi_fetch` 作为 API 的 fallback，移植后需自建 fallback 机制 | 周二任务可能频繁失败 |
| **LLM 输出格式一致性** | 评分、分类等依赖 LLM 遵循严格的输出格式（如 `| 创新性 | 4 |`） | 不同 LLM 的 JSON/表格输出稳定性不同 |
| **中文处理能力** | 任务要求生成中文摘要、中文周报 | 需确保替代 LLM 的中文能力足够 |
| **会话状态管理** | 周三、周四的"人工介入点"依赖 OpenClaw 的会话上下文 | 需设计替代的确认机制（如 PR review、issue comment） |

---

## 五、移植方案建议

### 方案 A: 最小改动移植（保留 Kimi 模型，替换框架层）

适合：另一个 OpenClaw 实例，或支持 MCP/Tool Use 的框架

```
保留: kimi_search, kimi_fetch, LLM (kimi/k2p5)
替换: openclaw cron → GitHub Actions / systemd timer
替换: feishu_im_user_message → 邮件 / Slack
替换: ~/.openclaw/workspace/ → 配置化工作目录
提取: system prompt → 独立 prompt 文件
```

**工作量**: 2-3 天
**风险**: 低

### 方案 B: 完全解耦移植（替换所有 Kimi 专属组件）

适合：Claude Code, Cursor, 或其他 ACP harness agent

```
替换: kimi_search → web_search / Google API / Bing API
替换: kimi_fetch → curl + 解析脚本 / Playwright / arXiv API
替换: LLM → Claude / GPT-4 / DeepSeek
替换: 定时调度 → GitHub Actions (最推荐) / Airflow
替换: 通知 → 邮件 / Slack / Discord
保留: Markdown 文件格式、评分标准、Git 工作流
```

**工作量**: 1-2 周
**风险**: 中（arXiv 抓取和 LLM 输出格式需要调试）

### 推荐：GitHub Actions 方案

```yaml
# .github/workflows/weekly-intelligence.yml
name: AI Weekly Intelligence
on:
  schedule:
    - cron: '0 1 * * 1'  # 周一 09:00 CST (01:00 UTC)
    - cron: '0 1 * * 2'  # 周二
    - cron: '0 6 * * 3'  # 周三 14:00 CST
    - cron: '0 6 * * 4'  # 周四
    - cron: '0 9 * * 5'  # 周五 17:00 CST
    - cron: '0 11 * * 5' # 周五 19:00 CST
jobs:
  intelligence:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Intelligence Task
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          # 或其他 LLM API key
        run: |
          python scripts/run_task.py --day $(date +%u) --week $(date +%V)
```

**优势**:
- 无需维护服务器
- GitHub 原生集成（git push 自动完成）
- 失败有邮件通知
- 公开仓库可免费运行

---

## 六、Prompt 资产清单（可复用的核心逻辑）

以下 prompt 工程是业务核心，应提取为独立文件：

| Prompt 文件 | 来源 | 复用价值 |
|------------|------|---------|
| `prompts/monday-collect.md` | 周一 systemPrompt | 搜索策略 + 输出格式 |
| `prompts/tuesday-paper.md` | 周二 systemPrompt | arXiv 筛选关键词 + 排除规则 |
| `prompts/wednesday-filter.md` | 周三 systemPrompt | 验证规则 + 评分标准 |
| `prompts/thursday-paper-filter.md` | 周四 systemPrompt | 论文评分5维度 + 中文摘要规范 |
| `prompts/friday-report.md` | 周五 systemPrompt | 周报模板 + 分类体系 |
| `prompts/friday-merge.md` | 周五联动 systemPrompt | A-D 分类 + 联动分析逻辑 |

---

## 七、结论

### 可移植性评级

| 模块 | 评级 | 说明 |
|------|------|------|
| 数据源接入 | ⭐⭐⭐⭐⭐ | 全部公开服务，零耦合 |
| 文件存储格式 | ⭐⭐⭐⭐⭐ | 标准 Markdown + Git，零耦合 |
| 业务逻辑（评分/分类） | ⭐⭐⭐⭐ | 依赖 LLM 能力，但逻辑可提取 |
| 网页抓取 | ⭐⭐⭐ | kimi_fetch 重度使用，需重写 |
| 定时调度 | ⭐⭐ | openclaw cron 专属，需替换 |
| 通知推送 | ⭐⭐ | feishu 专属，需替换 |
| 会话交互（人工介入） | ⭐ | OpenClaw 会话模型专属，最难替代 |

### 总体评估

**约 70% 的逻辑可低代价移植**，核心瓶颈在于：
1. `kimi_fetch` 对 arXiv 和 GitHub 的抓取（需重写为 API 调用或通用抓取）
2. 定时调度系统（需替换为 cron/Actions）
3. 飞书通知（可降级为邮件或移除）
4. 人工介入点（可改为异步确认，如 PR review）

**建议移植路径**:
1. 先提取所有 prompt 为独立文件（1天）
2. 用 GitHub Actions 替代 openclaw cron（1天）
3. 重写 arXiv/GitHub 抓取为 Python 脚本（2-3天）
4. 接入通用 LLM API（Claude/GPT/DeepSeek）（1天）
5. 替换通知渠道为邮件/Slack（0.5天）
6. 测试调试（2-3天）

**总工作量**: 1-2 周，风险可控。

---

*报告生成: 2026-05-07 by Kimi Claw*
*数据来源: intelligence-system 代码库、OpenClaw cron 配置、执行日志*
