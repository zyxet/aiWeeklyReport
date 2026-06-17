# 开源项目深度筛选短名单 — 2026-W25

> 筛选时间: 2026-06-17 14:00 CST (周三)
> 数据源: os-pool-2026-W25.md (本周候选池)
> 验证口径: GitHub API + 技术媒体测评 (2026-06-17)
> 入选项目: 6 / 18 (排除 12)

---

## 入选项目（按总分降序）

---

### 1. 🧠 MemPalace — 空间隐喻 AI 记忆系统

| 维度 | 评分 | 说明 |
|------|------|------|
| **创新性** | 5/5 | 将 2,500 年的 "记忆宫殿" 空间隐喻引入 AI 记忆系统，独创 Wings→Rooms→Drawers 四层结构 |
| **实用性** | 4/5 | 55K+ Stars，LongMemEval 96.6% Recall@5，但 benchmark 被独立审计指出方法论问题 |
| **技术深度** | 4/5 | 学术界有详细论文分析其架构，verbatim-first 存储哲学有理论价值，但核心检索依赖标准 ChromaDB |
| **机构背书** | 3/5 | 独立开发者，但学术争议吸引了大量技术讨论 |
| **社区热度** | 5/5 | 55,768 Stars，持续稳定增长，技术博客和论文双重覆盖 |

**实时数据**: Stars ~55,768 | MIT | Python | https://github.com/mempalace/mempalace
**一句话**: 将古罗马记忆术转化为 AI 记忆架构，四层空间层级 + 逐字存储哲学，零 LLM 推理成本写入。
**为什么选**: AI 记忆系统正从"提取摘要"转向"逐字存储+高效检索"。MemPalace 的学术争议（论文指出其核心性能实际来自 ChromaDB 而非空间隐喻）恰恰说明这个方向值得持续追踪。 verbatim-first 与 extraction-based 的路线之争，是 2026 年 AI 记忆的核心分歧。

---

### 2. 🪨 Caveman Claude — 极简语言 Token 优化 Skill

| 维度 | 评分 | 说明 |
|------|------|------|
| **创新性** | 4/5 | 用"洞穴人语言"约束模型输出，将 Brevity Constraints 论文转化为工程实践 |
| **实用性** | 4/5 | 73K+ Stars，平均 65% token 节省，实测在调试场景达 72% 节省 |
| **技术深度** | 4/5 | 有 2026 年 3 月 arXiv 论文支撑（Brevity Constraints Reverse Performance Hierarchies），在某些基准上提升 26% 准确率 |
| **机构背书** | 3/5 | 19 岁独立开发者 JuliusBrussee，MIT 协议，无机构背书但社区验证充分 |
| **社区热度** | 5/5 | 73,684 Stars，日增稳定，多个技术博客深度拆解，支持 40+ 工具 |

**实时数据**: Stars ~73,684 | MIT | JavaScript | https://github.com/JuliusBrussee/caveman
**一句话**: 教 Claude 用洞穴人语言交流，砍掉 65% 输出 token，不损失技术准确性，附带文言文模式。
**为什么选**: Token 优化不是"省钱技巧"，而是改变了模型输出质量。论文证明简短约束反而提升准确率。Caveman 将这个发现产品化，且 auto-clarity 机制（遇到安全/复杂场景自动恢复正常）说明设计者是懂用户的。73K stars 说明社区验证了这个方向。

---

### 3. 🗺️ codegraph — MCP 原生代码知识图谱

| 维度 | 评分 | 说明 |
|------|------|------|
| **创新性** | 5/5 | 将代码库索引为知识图谱，替代 AI 编码助手的 grep-glob-Read 扫描循环，减少 57% token 消耗 |
| **实用性** | 5/5 | 50K+ Stars，支持 21 种语言，8 个 Agent 集成，文件监听自动同步 |
| **技术深度** | 5/5 | Tree-sitter AST 解析 + SQLite FTS5 + MCP 三层架构，有完整技术测评和架构分析 |
| **机构背书** | 3/5 | 独立开发者 Colby McHenry，但多家技术媒体（Tosea.ai, Ry Walker, DevDigest）深度验证 |
| **社区热度** | 5/5 | 50,541 Stars，持续活跃，与 GitNexus 共同成为代码知识图谱双雄 |

**实时数据**: Stars ~50,541 | MIT | TypeScript | https://github.com/colbymchenry/codegraph
**一句话**: 为 Claude Code/Cursor 等编码 Agent 提供预索引的代码知识图谱，替代反复扫描文件的低效循环。
**为什么选**: AI 编码助手每处理一个任务都要重新"发现"代码库结构，这是巨大的 token 浪费。codegraph 将代码库索引为可查询的知识图谱，从根本上解决这个问题。当 Cursor 在 2026 年 3 月加入依赖图谱时，说明这个方向已被主流认可。codegraph 是独立、开源、MCP-native 的替代方案。

---

### 4. 🧩 Mastra — TypeScript 原生 Agent 框架

| 维度 | 评分 | 说明 |
|------|------|------|
| **创新性** | 4/5 | Observational Memory（四层记忆架构）LongMemEval 94.87%，行业领先 |
| **实用性** | 5/5 | 25K+ Stars，300K+ npm 周下载，$13M YC 融资，v1.0 已发布 |
| **技术深度** | 4/5 | TypeScript 原生设计，Zod schema 全链路类型安全，内置工作流引擎和评估框架 |
| **机构背书** | 4/5 | Gatsby.js 团队（YC W25），Replit/Factorial/Counsel Health 生产使用 |
| **社区热度** | 4/5 | 25,154 Stars，Discord 5,500+ 成员，稳定而非爆发式增长 |

**实时数据**: Stars ~25,154 | Apache 2.0 | TypeScript | https://github.com/mastra-ai/mastra
**一句话**: TypeScript 生态唯一原生 Agent 框架，Observational Memory 94.87% LongMemEval，生产 benchmark 9/10。
**为什么选**: 当 LangChain/LangGraph 主导 Python 生态时，Mastra 是 TypeScript 的"唯一正确答案"。Observational Memory 的成本优势（$0.80/天 vs 传统 RAG $3.20/天）对企业部署有实际意义。但注意：API 仍在 0.x 阶段，版本锁定建议 `~0.12.0`。

---

### 5. 💻 Terax AI — 本地优先 AI 终端

| 维度 | 评分 | 说明 |
|------|------|------|
| **创新性** | 4/5 | 将终端、编辑器、文件浏览器、AI 工作流整合为 ~7MB 单二进制，零遥测 |
| **实用性** | 4/5 | 7K+ Stars，支持 OpenAI/Anthropic/Google/Groq 等 94 家提供商，可离线通过 LM Studio |
| **技术深度** | 4/5 | Rust 后端 + Tauri 2 + React 19 + xterm.js + CodeMirror 6，技术栈现代且合理 |
| **机构背书** | 2/5 | 独立开发者 crynta，无机构背书，但 Apache 2.0 协议无厂商锁定 |
| **社区热度** | 4/5 | 7,147 Stars，稳定增长，技术博客有独立分析 |

**实时数据**: Stars ~7,147 | Apache 2.0 | Rust + Tauri + React | https://github.com/crynta/terax-ai
**一句话**: ~7MB 单二进制，零遥测、零账户，将终端和 AI 工作流整合的本地优先开发工具。
**为什么选**: 自托管 AI 从"小众需求"变为"行业标配"的趋势正在加速。Terax 的"本地优先、零遥测、零账户"哲学是务实的。与 odysseus（W24 入选）的全链路工作台不同，Terax 聚焦终端场景——这是开发者最高频的使用场景。Rust+Tauri 的技术栈也符合 AI 基础设施语言迁移的趋势。

---

### 6. 📈 TradingAgents — 多智能体金融分析框架

| 维度 | 评分 | 说明 |
|------|------|------|
| **创新性** | 4/5 | 多智能体协同（分析师、交易员、风险官）+ RAG + 自动化量化管道 |
| **实用性** | 4/5 | 86K+ Stars，单源码文件，低门槛安装，针对金融场景深度优化 |
| **技术深度** | 3/5 | 整合多智能体、RAG、LLM 代理，但技术深度不如纯基础设施项目 |
| **机构背书** | 2/5 | Tauric Research，无知名机构背书 |
| **社区热度** | 5/5 | 86,783 Stars，增长迅速，中文媒体有报道 |

**实时数据**: Stars ~86,783 | 待确认协议 | Python | https://github.com/TauricResearch/TradingAgents
**一句话**: 多智能体协同金融分析框架——研究员、交易员、风险官三角色协作，零门槛部署。
**为什么选**: AI Agent 在金融领域的应用是 2026 年的重要场景。TradingAgents 的"单源码文件"设计说明作者懂用户——金融从业者不想安装复杂依赖。但相比其他入选项目，其技术深度和通用性较弱，属于"垂直领域标杆"而非"基础设施"。入选是因为金融领域 AI 应用值得单独追踪。

---

## 排除项目

### ❌ OpenClaw — 全栈 Agent 平台

**排除原因**: 357K+ Stars 的体量无可争议，但已进入维护期而非突破期。本周无增量创新信号，属于"持续跟踪"而非"本周突破"。短名单保留给有新信号的项目。

**实时数据**: Stars ~357,000 | MIT | TypeScript | openclaw

---

### ❌ Hermes Agent — 闭环自进化 Agent 框架

**排除原因**: W24 短名单 Top 1（186K Stars），但本周无新增重大功能或数据突破。OpenRouter 日 Token 调用量 2910 亿的数据仍是 W24 的 news。属于"持续跟踪"而非"本周突破"。若下周有新版本或新数据，可重新评估。

**实时数据**: Stars ~195,564 | MIT | Python | NousResearch

---

### ❌ cc-switch — 跨平台 AI 工具管理器

**排除原因**: 从池中的 1,586 Stars 到实时的 102,886，增长过于异常（可能池数据错误或项目爆发）。但本质上是一个"工具管理工具"，而非"平台"或"基础设施"。在 AI 工具链中属于"胶水层"，单独入选价值有限。趋势已记录（多工具统一管理），无需单独占位。

**实时数据**: Stars ~102,886 | MIT | Rust | farion1231

---

### ❌ OpenMythos / rtk / coral / pi / forkd / zerostack / llmfit / presenton / Equibles

**排除原因**: 这些项目分别属于理论重建（OpenMythos）、图像工具（rtk）、知识管理（coral）、终端工具（pi）、语言处理（forkd）、技术栈（zerostack）、模型适配（llmfit）、决策工具（presenton）、金融数据（Equibles）——本质上是各垂直领域的"组件"或"工具"。它们共同验证了 AI 在细分领域的渗透趋势，但单独入选价值有限。短名单需要聚焦有平台级影响力的项目，而非生态组件。

**实时数据**:
- OpenMythos: 13,997 Stars
- rtk: 63,069 Stars
- coral: 5,131 Stars
- pi: 63,367 Stars
- forkd: 2,526 Stars
- zerostack: 1,308 Stars
- llmfit: 28,145 Stars
- presenton: 8,364 Stars
- Equibles: 157 Stars

---

## 本周主线总结

**主线一：AI 记忆进入"路线之争"**
- MemPalace 的学术争议（论文指出其核心性能来自 ChromaDB 而非空间隐喻）揭示了 AI 记忆的两个方向：verbatim-first（逐字存储） vs extraction-based（提取摘要）。Mem0 的 token-efficient 算法将 LongMemEval 从 ~49% 提升到 93.4%，说明 extraction 路线正在追赶。这场路线之争的胜负将决定 2026 年 AI 记忆的架构标准。

**主线二：Token 优化从"省钱"升级为"质量提升"**
- Caveman Claude 的 65% token 节省不是核心——核心是 Brevity Constraints 论文证明：限制模型输出简短回复，在某些基准上反而提升 26% 准确率。这意味着"简洁"不只是成本控制，而是 Prompt Engineering 的新维度。Caveman 的 auto-clarity 机制（安全场景自动恢复）说明这不是粗糙的截断，而是有设计感的约束。

**主线三：AI 编程从"聊天"进入"图谱"**
- codegraph 和 GitNexus 的崛起（代码知识图谱双雄）标志着 AI 编码助手从"对话式"进入"结构化理解"。当 Claude Code/Cursor 每处理一个任务都要重新扫描代码库时，预索引的知识图谱成为基础设施级需求。MCP 协议的标准化让这种"代码理解层"可以跨工具复用。

**主线四：TypeScript 成为 AI 基础设施的默认语言**
- Mastra（框架）、codegraph（代码图谱）、OpenClaw（平台）——本周入选的主要项目中 TypeScript 占主导。2025 年的 Python 主导格局正在改变，TypeScript 在 AI 应用层（而非模型层）的份额持续增长。

**主线五：本地优先从"选项"变为"默认"**
- Terax 的"零遥测、零账户、本地优先"设计与 W24 的 odysseus（自托管工作台）形成呼应。当企业 AI 采购将数据隐私合规列为硬性门槛时，本地优先架构从"选项"变为"必选项"。Terax 的 ~7MB 单二进制和 Apache 2.0 协议，使其成为这个趋势中最轻量的实现。

---

## 评分标准说明

| 维度 | 权重 | 5分标准 | 1分标准 |
|------|------|---------|---------|
| 创新性 | 20% | 全新架构/范式/方法论 | 微创新/模式复制 |
| 实用性 | 20% | 生产可用，协议友好 | 纯研究/协议限制 |
| 技术深度 | 20% | 理论扎实，工程完善 | 缺乏验证/浅层 wrapper |
| 机构背书 | 20% | 大厂/知名团队 | 独立开发者 |
| 社区热度 | 20% | Stars 增长迅猛，Issue 活跃 | 数据不足 |

---

> **人工介入点**: 短名单已生成，等待用户确认后继续周四论文精选流程。
> 如有项目需要补充验证或调整优先级，请在此文件基础上批注。
