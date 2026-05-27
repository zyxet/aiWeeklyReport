# OS Pool — 2026-W22

> 生成时间: 2026-05-27 14:00 CST (W22)
> 数据口径: GitHub Trending 日榜/周榜 + 社区信号聚合 (2026-05-19 ~ 2026-05-27)

---

## 1. humanlayer/12-factor-agents

| 属性 | 值 |
|------|-----|
| **Stars** | 22,078 (+1,900 this week) |
| **License** | Custom (文档/原则集) |
| **Language** | TypeScript (示例代码) |
| **URL** | https://github.com/humanlayer/12-factor-agents |

**定位**: LLM Agent 生产化十二要素原则（The Twelve-Factor App for Agents）

**Why**: 本周 GitHub Trending 增长最快的 Agent 方法论项目。明确对标 Heroku 的 Twelve-Factor App，试图为 Agent 生产化建立架构共识。涵盖：prompt 与逻辑分离、会话状态管理、动作幂等性、决策可观测性等 12 条原则。被评价为"demo 原型与生产 Agent 之间的鸿沟填补者"。humanlayer 团队在近期 Claude Agent SDK / LangGraph / CrewAI 对比评测中被频繁引用。

---

## 2. volcengine/OpenViking

| 属性 | 值 |
|------|-----|
| **Stars** | 24,422 (+132 today) |
| **License** | 待确认（推测 Apache-2.0） |
| **Language** | Python |
| **URL** | https://github.com/volcengine/OpenViking |

**定位**: 专为 AI Agent 设计的开源上下文数据库（Context Database for Agents）

**Why**: 字节跳动/火山引擎出品。通过文件系统范式统一 Agent 所需的上下文（内存、资源、技能）管理，支持分层上下文传递和自我进化。被明确描述为"为 openclaw 等 Agent 平台设计"。填补了 Agent 上下文管理层面的关键空白——当 Agent 需要管理多种异构上下文（记忆、工具、知识、技能）时，OpenViking 提供了统一的数据层抽象。

---

## 3. anomalyco/opencode

| 属性 | 值 |
|------|-----|
| **Stars** | 55,167 (+1,433 in 28d) |
| **License** | 待确认 |
| **Language** | 待确认 |
| **URL** | https://github.com/anomalyco/opencode |

**定位**: AI 驱动的开源编码 Agent / 代码智能平台

**Why**: 五月 AI 编码 Agent 赛道增长最迅猛的新星之一。55k+ Stars 体量已进入第一梯队，与 Claude Code / Codex CLI / qwen-code 形成竞争。区别于大厂产品的地方在于其社区驱动属性——非大厂出品但增速惊人，可能代表了独立开发者在编码 Agent 领域的突破。

---

## 4. huggingface/ml-intern

| 属性 | 值 |
|------|-----|
| **Stars** | ~9,700+ |
| **License** | Apache-2.0 |
| **Language** | Python |
| **URL** | https://github.com/huggingface/ml-intern |

**定位**: 自主 ML 工程师 Agent（Autonomous ML Engineer）

**Why**: HuggingFace 官方出品，W21 已入选短名单并持续高热度。能读论文、训练模型、自动部署的完整 ML 工作流 Agent。代表 "AI 替代 AI 研究者" 方向的最可信实现者。会话追踪自动上传至私有 HF 数据集，每次运行都是可调试、可分享的可观测 artifact。

---

## 5. trycua/cua

| 属性 | 值 |
|------|-----|
| **Stars** | ~17,000+ |
| **License** | MIT |
| **Language** | Python / Rust |
| **URL** | https://github.com/trycua/cua |

**定位**: Computer-Use Agent 的开源基础设施栈

**Why**: W21 已入选。持续增长的 "Computer-Use 领域的 AWS"。macOS/Linux/Windows 三平台沙箱 + SDK + Benchmarks + cua-driver。新推出的后台静默操控原生 macOS 应用能力进一步巩固其基础设施地位。2026 年 Agent 操控电脑能力落地的核心基础设施。

---

## 6. rohitg00/agentmemory

| 属性 | 值 |
|------|-----|
| **Stars** | ~14,400+ |
| **License** | Apache-2.0 |
| **Language** | TypeScript |
| **URL** | https://github.com/rohitg00/agentmemory |

**定位**: AI 编码 Agent 的持久记忆层

**Why**: W21 以 77% 周增速入选。本周持续高热度。四级记忆固化流水线（Working → Episodic → Semantic → Procedural），BM25 + Vector + KG 三重混合检索，50+ MCP 工具，兼容 15+ 编码 Agent 客户端。Agent 记忆基础设施方向的社区最热信号。

---

## 7. tinyhumansai/openhuman

| 属性 | 值 |
|------|-----|
| **Stars** | ~22,000+ |
| **License** | GPL-3.0 |
| **Language** | Rust |
| **URL** | https://github.com/tinyhumansai/openhuman |

**定位**: 个人 AI 超级智能终端

**Why**: W21 入选但标记为「高风险高关注」。本周热度持续但增速放缓，说明第一波爆发已过。Rust 实现，Token 压缩 + 100+ 第三方集成。GPL-3.0 copyleft 和 beta 状态仍是主要采用障碍，适合持续观察而非直接推荐。

---

## 8. QwenLM/qwen-code

| 属性 | 值 |
|------|-----|
| **Stars** | ~24,500+ |
| **License** | Apache-2.0 |
| **Language** | TypeScript |
| **URL** | https://github.com/QwenLM/qwen-code |

**定位**: 开源终端 AI 编码 Agent

**Why**: W21 已入选。阿里 Qwen 团队出品，国产大模型进军 AI 编程 Agent 的标志性项目。786 open issues 提示稳定性仍在打磨，但社区规模（24k+ Stars）证明了市场需求。

---

## 本周趋势总结

**主线一：Agent 生产化方法论成型**
- `12-factor-agents` 试图建立 Agent 从 demo 到生产的架构共识，类比云原生时代的 Twelve-Factor App。这标志着 Agent 领域从"能跑"走向"能长期维护"。

**主线二：上下文管理基础设施层爆发**
- `OpenViking`（字节跳动）+ `agentmemory`（独立开发者）分别从"结构化上下文数据库"和"记忆持久化"两个维度解决 Agent 的上下文局限。这是 Agent 从玩具走向生产工具的必经阶段。

**主线三：编码 Agent 竞争白热化**
- `opencode`（55k Stars）异军突起，与 Claude Code / Codex CLI / qwen-code 形成四强竞争。编码 Agent 赛道正从"大厂独占"向"社区+大厂混战"演变。

**主线四：ML 研究 Agent 落地**
- `ml-intern` 持续验证 HuggingFace 在自主 ML 工程方向的投入，AI 替代研究者的工作流自动化进入可观测阶段。
