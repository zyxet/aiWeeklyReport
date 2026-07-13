# 周一开源项目速览 — 2026年 W29（7月7日-7月13日）

> 数据收集时间：2026-07-13 10:00 CST
> 覆盖范围：LLM、AI Agent、MCP生态、编码Agent框架

---

## 一、本周热点

### 1. MCP 2026-07-28 规范发布候选版（RC）
- **状态**：7月5日进入RC阶段，最终规范锁定日期为7月28日
- **核心变化**：协议层实现无状态化（stateless），MCP服务器可在普通负载均衡器后运行，通过 `Mcp-Method` 头部路由流量
- **新特性**：客户端可缓存 tools/list 响应（支持 ttlMs 和 cacheScope）、Extensions 框架、Tasks 原语、MCP Apps、授权加固、正式弃用策略
- **影响**：这是MCP史上最大修订，意味着MCP从"实验性协议"正式走向企业级生产基础设施

### 2. AI Agent 框架 Q2 2026 密集发布潮延续
- **Microsoft Agent Framework 1.0**（4月3日GA）：统一Semantic Kernel和AutoGen，原生支持MCP + A2A，.NET/Python双栈
- **Pydantic AI V2**（6月23日稳定版）：harness-first重设计，capabilities作为核心原语，捆绑tools、hooks、instructions、model settings
- **LlamaIndex Workflows 1.0**（6月22日）：稳定版发布，支持持久化工作流
- **Claude Agent SDK**：新增分层subagent spawning（最多3层）、fallback model chains、社区MCP工具市场
- **CrewAI 1.14**：可插拔memory/knowledge/RAG/flow后端、Chat API、原生Snowflake Cortex支持

### 3. 编码Agent生态继续爆发
- **OpenCode**：16万+ Stars，900+贡献者，支持75+ LLM提供商，多平台（终端TUI/桌面IDE/IDE扩展），支持本地模型（Ollama/LM Studio）
- **OpenHands**（原OpenDevin）：多agent协作编码，持续活跃
- **Kilo Code**：基于OpenCode核心，2.1万Stars，支持VS Code/JetBrains/CLI
- **Goose**：转入Linux Foundation治理，长期中立化
- **Qwen Code**：Google Gemini CLI退役后，成为开源替代方案

---

## 二、项目速览

| 项目名称 | 组织/作者 | 语言 | Stars | 协议/许可证 | 核心定位 |
|----------|-----------|------|-------|-------------|----------|
| **OpenCode** | opencode | TypeScript | 160K+ | MIT | 多平台编码Agent Harness |
| **Microsoft Agent Framework** | microsoft | .NET/Python | - | MIT | 企业级Agent框架，原生MCP+A2A |
| **CrewAI** | crewAIInc | Python | 52K+ | MIT | 多Agent协作编排 |
| **LlamaIndex Workflows** | run-llama | Python | - | MIT | 持久化Agent工作流 |
| **Pydantic AI** | pydantic | Python | - | MIT | 类型安全Agent框架 |
| **MCP Servers** | modelcontextprotocol | TypeScript/Python | 84K+ | MIT | 官方MCP参考服务器集合 |
| **Browser Use** | browser-use | Python | 88K+ | MIT | AI浏览器自动化 |
| **Dify** | langgenius | Python/TS | 139K+ | Apache 2.0 | 可视化AI工作流平台 |
| **n8n** | n8n-io | TypeScript | 184K+ | Fair-code | 工作流自动化+AI节点 |
| **OpenClaw** | openclaw | TypeScript | 362K+ | MIT | 个人AI助手，多通道 |
| **Ollama** | ollama | Go | 169K+ | MIT | 本地LLM运行 |
| **Open WebUI** | open-webui | Python/Svelte | 132K+ | MIT | 本地LLM Web界面 |
| **bytedance/deer-flow** | bytedance | Python | 73K+ | Apache 2.0 | 长时程SuperAgent Harness |
| **calesthio/OpenMontage** | calesthio | Python | 12K+ | MIT | Agentic视频生产系统 |
| **rohitg00/agentmemory** | rohitg00 | TypeScript | 6.5K+ | Apache 2.0 | 编码Agent持久记忆层 |
| **obra/superpowers** | obra | Shell | 223K+ | MIT | Agent技能框架与方法论 |
| **jamiepine/voicebox** | jamiepine | TypeScript | 32K+ | MIT | 开源AI语音工作室 |
| **Mastra** | mastra | TypeScript | 23K+ | Apache 2.0 | TS原生Agent框架，Observational Memory |
| **A2A Protocol** | google/a2a | Python/JS/Java/Go/.NET | - | Apache 2.0 | Agent-to-Agent通信协议 |
| **LongCat-2.0** | meituan | Python | - | MIT | 1.6T MoE开源模型（6月30日发布） |

---

## 三、技术趋势

### 趋势1：MCP+A2A双协议成为事实标准
2026年Q2见证了协议层的统一：
- **MCP**（垂直集成：模型→工具）：Anthropic发起，现由Linux Foundation治理，190+成员组织，2026-07-28 RC是最大一次修订
- **A2A**（水平集成：Agent→Agent）：Google发起，150+组织采用，Azure AI Foundry/AWS Bedrock/Google Cloud原生支持
- **互补关系**：MCP解决"单个Agent如何调用工具"，A2A解决"多个Agent如何协作"。2026年企业级架构几乎必然同时采用两者

### 趋势2：Agent Skills 经济正式成型
- **obra/superpowers**（22万+Stars）、**anthropics/skills**、**openai/skills**、**addyosmani/agent-skills** 同时上榜，标志着"Agent技能市场"这个新物种的爆发
- **mukul975/Anthropic-Cybersecurity-Skills**：817个结构化网络安全技能，映射到6大框架（MITRE ATT&CK、NIST CSF 2.0等），代表垂直领域技能深度化的方向
- **garrytan/gstack**：23个 opinionated 工具，定义CEO/Designer/Eng Manager/Release Manager等角色技能
- 未来可能出现类似npm/pypi的"Agent技能包管理器"

### 趋势3：编码Agent从"单点工具"走向"多平台Harness"
- 2026年编码Agent的核心竞争维度：终端TUI + 桌面App + IDE扩展的三位一体
- **OpenCode** 的崛起验证了"模型无关+本地优先+多平台"路线的正确性
- **Claude Code**、**Codex CLI**、**Cursor**、**OpenCode** 四足鼎立，但开源阵营（OpenCode/Kilo Code/Goose）正在快速缩小与闭源产品的体验差距

### 趋势4：长时程Agent（Long-Horizon Agent）成为新战场
- **bytedance/deer-flow**：73K Stars，支持分钟到小时级别的任务，通过sandbox、memory、tool、skill、subagent、message gateway分层处理
- **OpenMontage**：12条pipeline、52个工具、500+技能，将编码Agent扩展为视频生产工作室
- Agent从"完成单次任务"向"管理长期项目"演进，记忆、规划、子agent委派成为关键能力

### 趋势5：企业级Agent框架大一统
- **Microsoft Agent Framework 1.0** 合并了Semantic Kernel（企业特性：session state、type safety、middleware、telemetry）和AutoGen（多Agent编排）
- 所有主流框架（LangGraph、CrewAI、Pydantic AI、LlamaIndex）均已原生支持MCP
- 生产级原语（持久化状态、子Agent、可插拔后端、Harness-first设计）从社区食谱变成框架标配

---

*本周报告由 cron 任务自动生成。如需深度技术分析，请在对话中指定项目名称。*
