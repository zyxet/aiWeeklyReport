# 周一开源项目速览 · W34 2026

> 收集窗口：2026-08-11 ~ 2026-08-17  
> 覆盖领域：LLM、AI Agent、编码智能体、多智能体编排、本地推理、代码审查

---

## 一、本周新星（New & Trending）

| 项目 | 语言 | Stars | 本周增量 | 一句话定位 |
|------|------|-------|----------|-----------|
| [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | TypeScript | ~9.0k | +2,483 | 自改进递归语言模型（RLM）智能体，支持长期自主任务与后台运行 |
| [OpenWork](https://github.com/openwork)（声明式多智能体编排引擎） | — | — | — | 类 Kubernetes 的 YAML 声明式配置，定义智能体协作关系与执行流 |
| [AgentWire](https://github.com/agentwire)（智能体互操作协议） | — | — | — | 能力描述语言（CDL），让智能体自动发现与调用彼此功能 |
| [FlashKDA](https://github.com/MoonshotAI/FlashKDA) | CUDA/C++ | — | — | 本地推理内核调度器，RTX 4090 上 Qwen-3-14B 吞吐量比 ollama 高 3.2× |
| [CodeReviewGraph](https://github.com/tirth8205/code-review-graph) | Python | ~30.2k | — | 构建代码语义知识图谱，AI 代码审查上下文缩减 65×（中位数） |
| [TerminalPilot](https://github.com/terminalpilot) | — | — | — | 分层规划终端 AI 编程助手，Planner → Coder → Tester → Security 流水线 |
| [PrivateInfer](https://github.com/privateinfer) | — | — | — | 基于 SMPC 的隐私保护推理，用户输入全程加密，云端模型也无法窥探 |
| [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | Rust/TS | ~8.0k | — | 本地优先个人 AI 超级智能，一键连接 118 个服务，几分钟构建数字分身 |
| [kvcache-ai/AgentENV](https://github.com/kvcache-ai/AgentENV) | Rust | — | — | 分布式智能体运行环境平台，支持大规模 Agent 部署 |

**本周最热信号**：`prime-agent` 单日 +2,293 stars，自改进（self-improving）+ 长期运行（long-running）+ 后台守护（daemon-backed）三大特性组合，代表了 Coding Agent 从"一次性对话"向"持续驻留进化"的范式跃迁。

---

## 二、持续升温（Rising）

| 项目 | 语言 | Stars | 近期趋势 | 核心看点 |
|------|------|-------|----------|----------|
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | Python | 108k+ | 持续上榜 | 让 AI Agent 真正操作浏览器，开源浏览器自动化层的事实标准 |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 227k+ | 稳定增长 | MIT 协议自改进 Agent 运行时，支持记忆、技能、cron、多平台消息 |
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | Python | 44k+ | 4 个月爆发 | 港大出品的轻量 Agent 框架，最小依赖最大灵活，LiteLLM 支持 100+ 后端 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Python | — | 热度持续 | 通用记忆层，解决长时运行 Agent 的上下文记忆问题 |
| [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | — | — | 新兴 | 图原生上下文/记忆工具，token 压缩与语义检索 |
| [OpenClaw/openclaw](https://github.com/openclaw/openclaw) | TypeScript | 386k+ | 长期霸榜 | 跨平台个人 AI 助手框架，ClawHub 技能市场 5,700+ 社区技能 |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Python | 144k+ | 稳如磐石 | Agent 工程平台中枢，工具+记忆+模型编排的 Python 生态基础设施 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | TS/Python | 84k+ | 持续活跃 | MCP 官方参考服务器集合，已捐赠给 Linux Foundation |

**趋势洞察**：社区投资重心正从" raw model API "转向三大编排层——**可复用技能（Skills）**、**持久记忆（Memory）**、**计算机/浏览器操作（Computer Use）**。

---

## 三、生态基建（Infra & Tools）

| 项目 | 定位 | 关键特性 |
|------|------|----------|
| [trycompai/crm](https://github.com/trycompai/crm) | Agent-first CRM | 开源 CRM 专为 AI Agent 设计，Agentic-first 架构 |
| [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | SaaS → Agent 网关 | 开源认证网关，通过 SDK/CLI/MCP/HTTP/OpenAPI 连接 1000+ SaaS 到 AI Agent |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | 企业级代码审查 | 确定性流水线 + LLM Agent 混合架构，阿里巴巴规模实战验证 |
| [DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | 终端编码智能体 | 围绕前缀缓存稳定性设计，可长期驻留终端运行 |
| [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | 终端 AI 编码助手 | 哈希锚定编辑、优化工具 Harness、LSP、Python、浏览器、子智能体 |
| [xintaofei/codeg](https://github.com/xintaofei/codeg) | 多 Agent 协作编码空间 | 聚合 Claude Code、Codex、OpenCode、Pi、Grok Build 等会话，桌面/自托管/Docker |
| [getpaseo/paseo](https://github.com/getpaseo/paseo) | 多 Agent 桌面编排器 | 从桌面和移动端编排多个编码智能体 |
| [vercel-labs/deepsec](https://github.com/vercel-labs/deepsec) | AI 驱动安全审计 | 由编码智能体驱动的代码库漏洞发现工具 |
| [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | 全本地隐私 Agent | 内置推理引擎，任何硬件即开即用，完全本地运行 |
| [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | 系统开源教材 | 《AI Agent：设计原理与工程实践》，10 章 + 94 个可运行实验，27k+ stars |

**核心公式**：`Agent = LLM + 上下文 + 工具` —— 来自李博杰开源教材，也是本周生态的底层共识。

---

## 本周关键词

`self-improving` · `long-running` · `daemon-backed` · `skills-as-code` · `local-first` · `MCP` · `code-review-graph` · `privacy-preserving` · `multi-agent orchestration`

---

*生成时间：2026-08-17 10:00 CST · 数据来源：GitHub Trending、Hacker News、技术社区聚合*
