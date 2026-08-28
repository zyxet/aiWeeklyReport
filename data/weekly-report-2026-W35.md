# AI 开源周报 · 2026-W35

> 本周观察：Agent 基础设施进入「记忆 + 治理 + 技能」三轴竞争时代。从团队级记忆中枢到图原生上下文基础设施，从自我改进型 Agent 到端侧微型模型——Agent 栈正在从单点工具向系统化平台进化。

---

## 重磅推荐：Prime Agent —— 自我改进型 RLM 编码 Agent

**仓库：** [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent)
**Stars：** ~8,400（持续高热）| **License：** MIT

Prime Intellect 推出的 Prime Agent 是本周最受瞩目的开源项目。它不是一个简单的编码助手，而是一个围绕「递归语言模型（RLM）」和「持续 Harness」两个抽象构建的**自我改进型 Agent 框架**。

**核心创新：**
- **持久化 IPython REPL**：将工具调用、子 Agent 启动全部内化为 Python 函数调用。`rlm("sub-task")` 启动子会话，非阻塞返回，结果通过 `agent_message.send(...)` 异步传递
- **Continual Harness 状态机**：将 Harness 状态形式化为 H = (ρ, G, K, M)——提示词、子 Agent、技能、记忆。每个组件都有 CRUD 接口
- **`/refine` 自我改进**：Agent 读取自身轨迹，应用最小化相关编辑，记录触发条件和结果。规划在后台运行，不阻塞对话
- **ARC-AGI-3 95.5%**：配合 Opus 5 在 ARC-AGI-3 的 RHAE Best@1 上达到 95.5%，Best@3 达到 99.97%

**为什么值得关注：**
Prime Agent 将「Agent 的自我改进」从概念推向了可运行的代码。它不只是一个能写代码的 Agent，而是一个能**持续从自己的经验中学习并改进自身 Harness** 的系统。这标志着 Agent 从「执行者」向「自进化系统」的关键跃迁。

---

## 一、工具框架类

### 1. Semantica —— 图原生 AI 上下文基础设施

**仓库：** [semantica-agi/semantica](https://github.com/semantica-agi/semantica)
**Stars：** ~10,200 | **License：** Apache 2.0

被称为「开源版 Palantir」的 Semantica 是本周最大的基础设施级发现。它不只是一个知识图谱工具，而是一套**面向高合规、高监管场景的确定性 AI 上下文基础设施**。

**核心能力：**
- **上下文图谱（Context Graphs）**：结构化、可查询的 Agent 知识图谱，替代向量索引的不可解释性
- **决策智能（Decision Intelligence）**：每个决策都是一等对象，可追溯、可按先例搜索、因果关联
- **确定性推理**：前向链、Rete 网络、Datalog、SPARQL——完全可解释，不依赖 LLM
- **W3C PROV-O 溯源**：每个事实都有完整审计链，可导出为 JSON/CSV/RDF
- **冲突检测与消解**：冲突事实被标记而非静默覆盖，支持时态快照（time travel）
- **多 Agent 共享内存**：基于 Agno 框架，多个 Agent 读写同一个上下文图谱

**架构亮点：**
- 多语言图谱存储：原生支持 RDF（Oxigraph/Blazegraph/Jena）和 LPG（Neo4j/FalkorDB/AGE/Neptune）
- 企业数据平台连接器：Databricks（Unity Catalog + Delta Lake）和 Snowflake 原生集成
- 多源摄入：文件、Web、数据库、Kafka、Kinesis、Git、邮件、MCP

**一句话判断：** 如果你的 Agent 需要向监管者解释「为什么做出这个决策」，Semantica 是目前开源界最完整的答案。

---

### 2. TencentDB Agent Memory —— 团队级 Agent 记忆中枢

**仓库：** [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)
**Stars：** ~7,800 | **License：** Apache 2.0

腾讯云开源的团队级 Agent 记忆系统，将「Agent 记忆」从个人会话级别提升到**团队协作级别**。

**四种记忆资产：**
| 资产类型 | 内容 | 用途 |
|---------|------|------|
| Chat Memory | 偏好、事实、决策、交互历史 | 跨会话用户理解 |
| Skill | 可复用的工作流和工具调用模式 | 经验沉淀 |
| LLM-Wiki | 文档结构和链接图谱 | 结构化知识检索 |
| Code-Graph | 代码调用图和影响范围 | 代码理解 |

**核心设计：**
- **分层蒸馏**：L0 原始对话 → L1 原子 → L2 场景 → L3 人格，层层提炼
- **固定绑定 + ACL**：不是把记忆全局注入提示词，而是根据 Team/User/Agent/可见性 精确控制谁能访问什么
- **按需调用**：Agent 先通过 `/v3/tools/list` 发现能力，再通过 `/v3/tools/call` 读取——知识只在需要时进入上下文
- **零代码集成**：一个 Proxy 层，改 base URL 即可接入 Claude Code 等客户端

**与 RAG 的区别：**
标准 RAG 回答「能找到什么？」；TencentDB Agent Memory 还回答「谁能用它、哪个版本有效、该给哪个 Agent？」

---

### 3. Code-Graph-RAG —— 代码库的知识图谱 RAG

**仓库：** [vitali87/code-graph-rag](https://github.com/vitali87/code-graph-rag)
**Stars：** ~3,200 | **License：** MIT

「The ultimate RAG for your monorepo」——用 Tree-sitter 解析代码，在 Memgraph 中构建结构知识图谱，通过自然语言查询和编辑代码库。

**技术栈：**
- **Tree-sitter AST 解析**：支持 13 种语言（Python、TS/JS、Rust、Go、Java、C/C++、C#、PHP、Lua、Dart，Ruby 部分支持）
- **Memgraph 图谱存储**：函数、类、模块、依赖关系全部图谱化
- **MCP Server 集成**：直接作为 Claude Code 的 MCP 服务器运行
- **死代码检测**：从入口点遍历调用图，未被触及的代码自动标记

**使用模式：**
```bash
cgr daemon up                          # 启动 Memgraph + Qdrant
cgr start --repo-path /path --update-graph  # 解析入库
cgr start --repo-path /path            # 交互式查询
```

**一句话判断：** 对于需要理解大规模代码库的 Agent 来说，向量 RAG 是「凭运气找相关代码」，Code-Graph-RAG 是「按结构精确导航」。

---

### 4. Macro —— 一体化团队工作空间（开源版）

**仓库：** [macro-inc/macro](https://github.com/macro-inc/macro)
**Stars：** ~6,200 | **License：** AGPL-3.0

一个用 Rust（后端，167 crates）+ SolidJS（前端）构建的「团队操作系统」，将邮件、聊天、文档、任务、CRM、Agent 统一到一个界面中。

**核心特色：**
- **双向图存储**：所有对象（邮件、任务、文档、联系人）通过 @ 链接形成双向图，跨模块引用是原生能力
- **CRDT 实时协作**：文档基于 CRDT + Cloudflare Durable Objects，协作延迟接近本地编辑
- **团队级 AI 记忆**：每晚从所有表面（邮件、消息、任务、文档、通话）综合合成记忆，通过 MCP 暴露给外部 Agent
- **内置 CRM**：邮件聚合按公司/联系人分组，Agent 可直接查询客户历史

**为什么值得关注：**
它不是又一个 Slack/Notion 替代品，而是**第一个把「团队 AI 记忆」作为核心架构设计的开源工作空间**。AGPL 协议意味着完全开源，没有 open-core 套路。

---

### 5. Anthropic Skills —— Agent Skills 标准化

**仓库：** [anthropics/skills](https://github.com/anthropics/skills)
**Stars：** ~149,000 | **License：** Apache 2.0（部分 source-available）

Anthropic 将其 Claude 的 Skills 系统开源，包含完整的 Agent Skills 规范（agentskills.io）和大量示例 Skills。

**关键内容：**
- **Skills 规范**：YAML frontmatter + 触发描述 + 结构化内容——目前最完整的 Skill 格式标准
- **文档处理 Skills**：docx、pdf、pptx、xlsx 的底层处理技能（source-available，非开源）
- **MCP 集成**：Claude Code 可直接通过 `/plugin install` 加载

**信号意义：**
Skills 正在成为 Agent 时代的「函数库标准」。Anthropic 开源其实现并推动 agentskills.io 标准，意味着社区正在从「每个 Agent 自己造轮子」走向「可共享、可复用的技能生态」。

---

## 二、模型与算法类

### Cactus Needle 2 —— 14MB 端侧工具调用模型

**仓库：** [cactus-compute/needle](https://github.com/cactus-compute/needle)
**Stars：** ~6,500 | **License：** MIT（代码）/ Apache 2.0（权重）

Cactus Compute 推出的 Needle 2 是一款**45M 参数、14MB 二进制、28MB RAM 峰值**的端侧工具调用模型，目标是跑在手表、ESP32 等微型设备上。

**核心数据：**
| 指标 | 数值 |
|------|------|
| 参数量 | 45M |
| 二进制体积 | 14MB（单文件，含权重） |
| 峰值内存 | ~28MB |
| 量化方式 | CQ2-bit（2-bit，训练时量化） |
| 上下文窗口 | 256 tokens（滑动窗口） |
| 预训练数据 | 115B tokens |

**架构激进之处：**
- **去掉 FFN**：用 Hadamard MLP 替代标准 Transformer 的前馈网络，证明纯注意力网络在匹配参数量下损失差距仅 0.006 nats
- **Simple Attention Network**：GQA 注意力 + engram KV 记忆 + 多通道超连接
- **置信度门控**：每个响应自带校准置信度，低于阈值时返回空调用（拒绝），可升级云端模型

**性能表现：**
- 树莓派 5：~500 tokens/s
- Quest 3S / Vision Pro：400-1500 tokens/s
- 200 美元以下手机：300-700 tokens/s

**一句话判断：** 这不是一个通用对话模型，而是一个「工具调用专用芯片」——在 14MB 里完成工具映射、设备控制和结构化提取。边缘 AI 的实用化里程碑。

---

## 三、数据观察

### GitHub AI 趋势热力图（2026-W35）

| 项目 | Stars | 周新增 | 主要语言 | 核心定位 |
|------|-------|--------|---------|---------|
| semantica-agi/semantica | ~10,200 | 高 | Python | 图原生 AI 上下文基础设施 |
| TencentCloud/TencentDB-Agent-Memory | ~7,800 | 高 | TypeScript | 团队级 Agent 记忆中枢 |
| PrimeIntellect-ai/prime-agent | ~8,400 | 持续 | TypeScript | 自我改进型 RLM Agent |
| cactus-compute/needle | ~6,500 | 高 | Python/Rust | 14MB 端侧工具调用模型 |
| macro-inc/macro | ~6,200 | 中 | Rust/SolidJS | 一体化团队工作空间 |
| anthropics/skills | ~149,000 | 稳 | 多语言 | Agent Skills 标准 |
| vitali87/code-graph-rag | ~3,200 | 中 | Python | 代码知识图谱 RAG |

### 本周趋势总结

1. **Agent 基础设施三轴化**：记忆（TencentDB Agent Memory）、治理（Semantica）、技能（Anthropic Skills）三条主线同时推进
2. **自我改进成为热点**：Prime Agent 的 `/refine` 机制代表 Agent 从「执行」到「自进化」的范式转移
3. **端侧 AI 实用化**：Needle 2 证明 45M 参数足以完成工具调用，边缘 AI 不再是「玩具」
4. **团队级记忆**：从个人 Agent 记忆走向团队共享记忆，成为本周最大架构趋势
5. **图原生基础设施**：Semantica 和 Code-Graph-RAG 代表「图优先」替代「向量优先」的新方向

---

## 四、推荐阅读

| 标题 | 类型 | 链接 | 推荐理由 |
|------|------|------|---------|
| Prime Agent: A Self-Improving RLM Harness | 论文 | arXiv:2608.23552 | 自我改进型 Agent 的完整技术方案 |
| A Controlled Study of Attention-Only Transformers | 论文 | arXiv:2607.18363 | Needle 2 的架构基础：FFN 可以被替代吗？ |
| Equipping agents for the real world with Agent Skills | 博客 | Anthropic Blog | Skills 标准化的设计哲学 |
| Agentic CRMs, AI Gateways, and Top GitHub Trending | 综述 | IndiaNIC Intelligence | 本周趋势全景分析 |

---

> **趋势判断：** W35 的核心信号是 Agent 栈的「系统化」。单一工具的时代正在过去，记忆、治理、技能、推理、执行正在被整合为统一平台。下一步的竞争将围绕「谁的 Agent 能从经验中持续学习」展开。

---

## 五、论文-开源联动分析

> 本节由周五论文-开源联动任务自动生成，对本周8篇精选论文与7个开源项目进行交叉映射分析。

### 联动分类总览

| 类型 | 定义 | 数量 |
|------|------|------|
| **A类** | 论文+官方代码/数据 | 0 |
| **B类** | 论文+社区复现/互补项目 | 8（全部入选论文） |
| **C类** | 论文先行，尚无对应开源 | 0 |
| **D类** | 项目先行（论文滞后或独立） | 0 |

### 核心联动对

| 论文 | 开源项目 | 联动类型 | 关联强度 |
|------|----------|----------|----------|
| Weighted Memory Tree | TencentDB-Agent-Memory, semantica | B类 | ⭐⭐⭐⭐ |
| Evaluating Skills, Not Just Agents | anthropic/skills | B类 | ⭐⭐⭐⭐ |
| AEGIS: MCP Cross-Domain Security | prime-agent, MCP 生态 | B类 | ⭐⭐⭐⭐ |
| Self-Speculation for Faster Reasoning | FlashKDA | B类 | ⭐⭐⭐ |
| SDAD: Spec-Driven Agentic Development | prime-agent | B类 | ⭐⭐⭐⭐ |
| Knowledge-Graph-Gated Defactualization | code-graph-rag | B类 | ⭐⭐⭐ |
| Personalized Privacy Control via Attention Heads | openhuman, needle | B类 | ⭐⭐⭐ |
| Two Heads: Multi-agent TTS | prime-agent | B类 | ⭐⭐⭐ |

### 六大主题速览

1. **Agent 记忆与上下文基础设施**: 论文加权记忆树 + TencentDB/semantica/macro 三项目互补
2. **Skills 标准化与持续评估**: 论文 Skill 评估框架 + Anthropic Skills 标准形成闭环
3. **Agent 安全与 MCP 治理**: AEGIS 填补 MCP 协议层安全空白，prime-agent 等驻留 Agent 急需
4. **推理加速双轨策略**: Self-Speculation 算法层 + FlashKDA 硬件层可叠加
5. **代码 Agent 工程化跃迁**: SDAD 方法论 + prime-agent 实践 + Two Heads 多 Agent 协作
6. **隐私保护与本地优先**: 注意力头级隐私控制 + openhuman/needle 市场力量

### 详细联动分析报告

完整分析（含联动矩阵、趋势判断、行动建议）见：
📄 `output/paper-os-linkage-2026-W35.md`

---

*周报完*

*本报告由 intelligence-system 自动生成  
*数据来源: arXiv / GitHub API / 技术媒体交叉验证  
*生成时间: 2026-08-28 19:00 CST*
