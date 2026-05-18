# OS Pool — 2026-W21

> 生成时间: 2026-05-18 10:00 CST (W21)
> 数据口径: GitHub Trending 日榜/周榜 + 社区信号聚合 (2026-05-12 ~ 2026-05-18)

---

## 1. rohitg00/agentmemory

| 属性 | 值 |
|------|-----|
| **Stars** | 8,142 (+1,379 today) |
| **License** | Apache-2.0 |
| **Language** | TypeScript |
| **URL** | https://github.com/rohitg00/agentmemory |

**定位**: AI 编码 Agent 的持久记忆层（Persistent Memory Layer）

**Why**: 本周 GitHub Trending 多日均在榜（5/13 #2, 5/14 #2, 5/15 #3），是 Agent 基础设施层最热的信号之一。提供四级记忆固化流水线（Working → Episodic → Semantic → Procedural），支持 BM25 + Vector + Knowledge Graph 三重混合检索，内置 50+ MCP 工具，兼容 Claude Code / Cursor / Codex CLI / OpenClaw 等 15+ 编码 Agent 客户端。解决当前编码 Agent "会话一关就失忆" 的核心痛点，Apache-2.0 协议使其在企业场景中采纳门槛极低。

---

## 2. tinyhumansai/openhuman

| 属性 | 值 |
|------|-----|
| **Stars** | 6,303 (+1,696 today) |
| **License** | GPL-3.0 |
| **Language** | Rust |
| **URL** | https://github.com/tinyhumansai/openhuman |

**定位**: 个人 AI 超级智能终端（Personal AI Super Intelligence）

**Why**: 本周 Trending 榜首常客（5/13 #1, 5/14 #1, 5/15 #2），Rust 实现，主打 Token 压缩与 100+ 第三方集成。定位为"私人、简单、非常强大"的本地化个人 Agent 终端。需要关注的是 GPL-3.0 的 copyleft 属性和早期 beta 状态的稳定性风险，适合技术爱好者尝鲜而非生产直接采用。Token 压缩能力在上下文窗口昂贵的当下具有显著成本优势。

---

## 3. trycua/cua

| 属性 | 值 |
|------|-----|
| **Stars** | 15,450+ |
| **License** | MIT |
| **Language** | Python / Rust |
| **URL** | https://github.com/trycua/cua |

**定位**: Computer-Use Agent 的开源基础设施栈（Sandbox + SDK + Benchmarks）

**Why**: 填补了 AI Agent "操控电脑" 领域最关键的基础设施空白：当模型具备看屏幕、点鼠标、敲键盘的能力后，谁来提供安全、可复现、跨平台的执行环境？CUA 提供 macOS / Linux / Windows 三平台沙箱、统一 SDK、评测基准（cua-bench）以及基于 Apple Virtualization.Framework 的高性能 VM 方案（Lume）。新推出的 cua-driver 可在后台静默操控原生 macOS 应用而不抢占光标焦点。被评价为 "Computer-Use 领域的 AWS"——自己不造 Agent，只做中立底层，让 BYO model + BYO harness 成为现实。

---

## 4. QwenLM/qwen-code

| 属性 | 值 |
|------|-----|
| **Stars** | 24,388 |
| **License** | 待确认（推测 MIT/Apache） |
| **Language** | 待确认 |
| **URL** | https://github.com/QwenLM/qwen-code |

**定位**: 开源终端 AI Agent（"An open-source AI agent that lives in your terminal"）

**Why**: 来自阿里 Qwen 团队的终端 AI 编码 Agent，24k+ Stars 说明社区关注度极高。与 Claude Code / Codex CLI 直接竞争，代表国产大模型团队进军 AI 编程 Agent 赛道的标志性项目。作为终端原生 Agent，预期深度集成 Qwen 系列模型能力，对中文开发者生态和本土模型-工具闭环有重要参考价值。具体技术细节和功能边界需进一步跟踪其 Release Note。

---

## 5. badlogic/pi-mono

| 属性 | 值 |
|------|-----|
| **Stars** | 40,600 |
| **License** | 待确认 |
| **Language** | Java / Kotlin |
| **URL** | https://github.com/badlogic/pi-mono |

**定位**: AI Agent 全栈工具包（Monorepo）

**Why**: 四月周榜增长 2,740 Stars，总星突破 40k。这是一个"Everything-monorepo"，包含：编码 Agent CLI、统一 LLM API 抽象层、TUI & Web UI 库、Slack Bot、vLLM Pods 等完整组件。对于需要自建 Agent 基础设施的团队来说，pi-mono 提供了一体化的 Java/Kotlin 生态方案，填补了该语言在 AI Agent 基础设施领域的空白。其 monorepo 架构适合作为中大型企业内部 Agent 平台的技术底座参考。

---

## 6. huggingface/ml-intern

| 属性 | 值 |
|------|-----|
| **Stars** | 6,700 |
| **License** | 待确认（推测 Apache-2.0） |
| **Language** | Python |
| **URL** | https://github.com/huggingface/ml-intern |

**定位**: 自主 ML 工程师 Agent（Autonomous ML Engineer）

**Why**: HuggingFace 官方出品，四月周榜增长 3,655 Stars。这是一个能读论文、训练模型、自动部署的 AI Agent——将 ML 工程师的完整工作流（文献阅读 → 实验设计 → 模型训练 → 模型交付）自动化。由 HuggingFace 核心团队维护，品质背书极强。对需要大规模自动化机器学习实验的团队极具吸引力，代表 "AI 替代 AI 研究者" 这一激进方向的早期落地形态。

---

## 7. zilliztech/claude-context

| 属性 | 值 |
|------|-----|
| **Stars** | 9,600 |
| **License** | MIT |
| **Language** | TypeScript |
| **URL** | https://github.com/zilliztech/claude-context |

**定位**: 面向 Claude Code 的代码检索 MCP（Code Search MCP Server）

**Why**: 四月周榜增长 3,062 Stars。基于向量检索技术，将整个代码库转化为 Claude Code（及其他编码 Agent）的可用上下文。解决大项目场景下 Agent "看不到全貌" 的痛点——当代码库超过上下文窗口容量时，通过语义搜索精准提取相关代码片段注入 Agent 上下文。Zilliz（Milvus 向量数据库团队）出品，技术路径与产品场景高度匹配。对于在大型遗留代码库中使用 Claude Code 的开发者，这是当前最有效的上下文扩展方案之一。

---

## 8. millionco/react-doctor

| 属性 | 值 |
|------|-----|
| **Stars** | 6,327 |
| **License** | MIT |
| **Language** | TypeScript |
| **URL** | https://github.com/millionco/react-doctor |

**定位**: AI 感知的 React 代码库健康扫描器

**Why**: 5月13日 GitHub Trending 上榜，当日增长 788 Stars。专门针对 AI Agent 生成的 React 代码进行质量检测——识别 vibe coding 常见的架构腐烂、类型安全漏洞、性能陷阱和可维护性问题。随着 AI 编码工具普及，"Agent 写的代码质量如何保障" 成为新痛点，react-doctor 是这个细分方向的代表性工具。支持将检测规则以 Agent Skill 形式集成到 Claude Code / Codex 等工作流中，实现 AI 生成 → AI 质检的闭环。

---

## 本周趋势总结

**主线一：Agent 记忆与上下文基础设施爆发**
- `agentmemory`（记忆持久化）、`claude-context`（代码库上下文检索）分别从"时间维度"和"空间维度"解决 Agent 的上下文局限。这是 Agent 从玩具走向生产工具的必经阶段。

**主线二：终端 AI Agent 竞争白热化**
- `openhuman`、`qwen-code` 与已成熟的 Claude Code / Codex CLI 形成四强格局。终端作为 AI 编程的主战场，各家的差异化在于：模型能力、上下文管理、Skill 生态、隐私/本地化程度。

**主线三：Computer-Use Agent 基础设施成型**
- `cua` 提供跨平台沙箱 + 评测基准，使"Agent 操控电脑"从 demo 走向可工程化的基础设施。这是 2026 年 Agent 领域最重要的能力跃迁之一。

**主线四：AI 编码的质量与信任层出现**
- `react-doctor` 代表的新品类——AI 生成代码的自动化质检工具。当 Agent 产出代码的速度超过人类 review 能力时，自动化质量守门成为刚需。
