# 周三精选短名单 —— 2026年第35期（W35）

> 筛选时间：2026-08-26
> 筛选人：Kimi Claw（自动化深度筛选）
> 数据来源：候选池 os-pool-2026-W35.md + 实时验证

---

## 筛选说明

- **入选标准**：实时 Star ≥ 100 且有独立媒体 coverage
- **排除项目**：diagram-design（仓库 URL 信息不完整，无法交叉验证）
- **本周主题**：上下文工程成为 Agent 新基建，自改进 Agent 与 Skills 生态爆发

---

## 精选短名单（7个项目）

| 序号 | 项目名称 | 仓库 | 实时 Stars | 本周新增 | 技术测评 | 媒体 Coverage | 保留理由 |
|:---:|---------|------|:---------:|:-------:|---------|-------------|---------|
| 1 | **prime-agent** | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | ~8,400 | +9,400 | RLM 自改进范式，ARC-AGI-3 95.5%，持久化 IPython REPL，Continual Harness | explainx.ai, CryptoBriefing, 掘金, mushroom.cv, coddykit | 首个生产级自改进 Agent，论文 arXiv:2605.09998 支持 |
| 2 | **semantica** | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | ~10,200 | +8,300 | 图原生上下文基础设施，Agno 框架集成，原生 Datalog 推理引擎，10+ 框架适配 | GitHub Trending 多次，yanzhifeng.com，OpenGithubs 周榜 #12 | 上下文工程新基建代表，增长极快（月增 7,936⭐） |
| 3 | **TencentDB-Agent-Memory** | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | ~7,800 | +7,800 | 团队级记忆中枢，4 种记忆资产（Chat Memory/Skill/LLM-Wiki/Code-Graph），MCP 兼容 | StartupCorners 多次，GitHub Trending 报告 | 大厂出品，生产级记忆层，填补团队级 Agent 记忆空白 |
| 4 | **anthropic/skills** | [anthropics/skills](https://github.com/anthropics/skills) | ~149,000 | +12,000 | 官方 Agent Skills 标准，agentskills.io 开放标准，~40 客户端兼容，渐进式披露 | 学术论文多次引用，rywalker.com，Analytics Vidhya | Agent Skills 生态标准制定者，从 Claude 特性进化为行业标准 |
| 5 | **macro** | [macro-inc/macro](https://github.com/macro-inc/macro) | ~6,200 | +6,200 | 统一工作空间（邮件/聊天/文档/任务/Agent/CRM），CRDT 协作，双向图链接，团队级 AI 记忆 | GitHub Daily Trend podcast，macro.com 官方博客 | 开源 All-in-One Workspace 标杆，AGPLv3 完全开源 |
| 6 | **code-graph-rag** | [vitali87/code-graph-rag](https://github.com/vitali87/code-graph-rag) | ~3,200 | +4,100 | Monorepo 知识图谱 RAG，Tree-sitter 多语言解析，MCP Server 集成，语义代码搜索 | 掘金 #2 Trending，skillsllm.com，Pinakes 调研笔记 | 代码理解基础设施，开发者工具链关键拼图 |
| 7 | **needle** | [cactus-compute/needle](https://github.com/cactus-compute/needle) | ~3,900 | +3,900 | 14MB 端侧 foundation model，支持手机/可穿戴/智能家居/机器人，论文 arXiv:2607.18363 | AI Open Source Trends，OpenGithubs 周榜 | 端侧 AI 关键突破，小模型大趋势的代表 |

---

## 排除项目

| 项目名称 | 原因 |
|---------|------|
| diagram-design | 候选池 URL (`github.com/diagram-design/diagram-design`) 无法交叉验证；搜索到的同名项目 (`cathrynlavery/diagram-design`) 为 Claude Code 图表模板库，与候选池描述的"AI 生成图表设计库"不符。信息不完整，暂排除。 |

---

## 本周核心洞察

**1. 自改进 Agent 范式确认**

prime-agent 的 RLM + Continual Harness 架构不是噱头——95.5% 的 ARC-AGI-3 分数和 41 个 release 的迭代速度证明这个方向可行。关键突破在于把"改进"本身变成 Agent 可操作的对象，而不是每次重启从零开始。

**2. 上下文工程成为共识方向**

semantica（图原生上下文）、TencentDB-Agent-Memory（团队记忆中枢）、macro（统一工作空间记忆）三个项目从不同层级解决同一个问题：Agent 的上下文不能只在对话窗口里。这标志着社区从"Agent 能做什么"转向"Agent 如何可靠地长期运行"。

**3. Skills 生态标准化加速**

Anthropic 官方 skills 仓库 ~149k stars，agentskills.io 开放标准已被 ~40 个客户端采纳。Skills 不再是某个产品的特性，而是跨平台的 Agent 能力扩展协议。Addy Osmani 的 agent-skills 同日登榜说明大厂和社区在共同推动这个方向。

**4. 端侧小模型仍有价值**

needle 的 14MB foundation model 看似与"大模型"趋势相悖，但在隐私敏感场景（可穿戴、智能家居）和离线环境中有不可替代的价值。论文支持增加了技术可信度。

---

## 风险提示

- prime-agent 明确声明**不是安全沙箱**，执行模型生成的代码需使用隔离环境
- anthropic/skills 存在供应链风险：Skills 执行捆绑脚本，已有恶意 Skills  targeting Claude Code 用户的报告
- macro 采用 AGPLv3，商业使用需注意许可证兼容性

---

*本短名单由自动化流程生成，经人工复核后进入周五周报联动环节。*
