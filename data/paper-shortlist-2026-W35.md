# 📄 本周精选论文短名单

> 筛选时间: 2026-08-27 | ISO周: W35 | 来源: arXiv 论文池 50 篇精选
> 本周开源短名单主题: 上下文工程 · Agent Skills · 自改进范式 · 本地优先

---

## 入选论文（8篇）

### 1. Weighted Memory Tree: Remembering What Matters for Long-Horizon LLM Agents
- **arXiv**: https://arxiv.org/abs/2608.20631
- **标签**: LLM, Agent, RAG, Reasoning, Long Context
- **分类**: cs.AI
- **亮点**: 提出加权记忆树结构，解决长程Agent执行历史膨胀问题，通过重要性权重动态剪枝记忆，使长程任务推理效率显著提升。
- **与开源联动**: 🔄 **TencentDB-Agent-Memory / semantica** — 同为Agent记忆基础设施方向，加权记忆树可与腾讯团队级记忆中枢的"4种记忆资产"互补，也为 semantica 的图原生上下文提供动态剪枝策略。

---

### 2. Evaluating Skills, Not Just Agents: Agentic Continuous Evaluation of Skills
- **arXiv**: https://arxiv.org/abs/2608.20614
- **标签**: LLM, Agent, RAG, agentic, tool use
- **分类**: cs.AI
- **亮点**: 提出从"评估Agent"转向"评估Skill"的范式转变，企业级Agent生产环境中可复用Skill的持续评估框架，附带证据链而非仅文本描述。
- **与开源联动**: 🔄 **anthropic/skills** — 直接呼应 Anthropic 的 Agent Skills 开放标准。Skills 标准化之后，如何持续评估 Skill 的质量和适用性成为关键，本文提供了方法论。

---

### 3. AEGIS: Preventing Cross-Domain Resource Abuse in MCP
- **arXiv**: https://arxiv.org/abs/2608.20481
- **标签**: LLM, Agent, RAG, Reasoning, Multimodal
- **分类**: cs.AI
- **亮点**: 针对 MCP (Model Context Protocol) 协议的安全漏洞分析，提出跨域资源滥用防护机制。MCP 作为 Agent 与外部系统交互的标准协议，其安全性直接影响整个生态。
- **与开源联动**: 🔄 **MCP 生态 / prime-agent** — MCP 是本周关键词之一，prime-agent 等长期驻留 Agent 依赖 MCP 连接外部工具，AEGIS 填补了 MCP 安全基础设施的关键空白。

---

### 4. Self-Speculation for Faster Reasoning Models
- **arXiv**: https://arxiv.org/abs/2608.20359
- **标签**: LLM, Agent, RAG, Chain-of-Thought, Reasoning
- **分类**: cs.CL
- **亮点**: 通过模型自身生成草稿token进行投机解码，在不损失质量的前提下加速推理模型。无需额外小模型，单模型自投机实现无损加速。
- **与开源联动**: 🔄 **FlashKDA** — 同为推理加速方向。FlashKDA 通过 CUTLASS 内核优化实现 H20 上 1.72×–2.22× 加速，Self-Speculation 则从算法层面提供另一种无损加速路径，两者可叠加。

---

### 5. SDAD: Spec-Driven Agentic Development for the AI-Native SDLC
- **arXiv**: https://arxiv.org/abs/2608.20341
- **标签**: Agent, Multi-Agent, RAG, Reasoning, language model
- **分类**: cs.AI
- **亮点**: 提出"规格驱动"的Agent开发方法论，利用大上下文窗口模型重构软件开发生命周期，将需求规格直接转化为可执行代码。
- **与开源联动**: 🔄 **prime-agent** — prime-agent 代表 Coding Agent 从"对话工具"到"驻留系统"的范式跃迁，SDAD 则从软件工程方法论层面为这种跃迁提供了系统化的开发框架。

---

### 6. Knowledge-Graph-Gated Defactualization for Style-Controllable and Fact-Preserving Generation in Agentic Conversational AI
- **arXiv**: https://arxiv.org/abs/2608.20393
- **标签**: LLM, Agent, language model, agentic, fine-tuning
- **分类**: cs.CL
- **亮点**: 利用知识图谱门控机制，在保持事实正确性的同时实现风格可控的Agent对话生成，解决客服等场景的事实敏感+风格多样双重需求。
- **与开源联动**: 🔄 **code-graph-rag** — 同为知识图谱+AI方向。code-graph-rag 构建代码语义知识图谱用于审查，本文则将知识图谱用于对话生成的事实约束，两者展示了 KG 在 Agent 系统中不同维度的价值。

---

### 7. Personalized Privacy Control in LLMs via Attention Head Intervention
- **arXiv**: https://arxiv.org/abs/2608.21209
- **标签**: LLM, Agent, RAG, prompt, agentic
- **分类**: cs.CL
- **亮点**: 通过注意力头级别的干预实现个性化隐私控制，精确调控LLM在不同上下文中对用户隐私信息的披露行为。
- **与开源联动**: 🔄 **openhuman / needle** — 本地优先和隐私保护是本周核心趋势。openhuman 追求"完全可控的个人AI"，needle 是14MB端侧模型，本文的注意力头级隐私控制为这种"数据主权回归"提供了技术保障。

---

### 8. Two Heads are Better Than One: Test-time Scaling of Multi-agent Collaborative Reasoning
- **arXiv**: https://arxiv.org/abs/2504.09772
- **标签**: Agent, Multi-Agent, RAG, Reasoning, language model
- **分类**: cs.AI
- **亮点**: 将测试时扩展(TTS)从单Agent推广到多Agent协作场景，多个Agent分工推理后整合结果，突破单Agent TTS 的可扩展瓶颈。
- **与开源联动**: 🔄 **prime-agent / AgentENV** — prime-agent 的长期自主运行需要多 Agent 协作能力支撑，AgentENV 提供分布式多 Agent 执行环境，本文的协作推理扩展方法可直接受益于这种基础设施。

---

## 主题聚类

| 主题 | 论文 | 对应开源项目 |
|------|------|-------------|
| **Agent 记忆与上下文** | Weighted Memory Tree | TencentDB-Agent-Memory, semantica |
| **Skills 标准化与评估** | Evaluating Skills | anthropic/skills |
| **MCP 安全基础设施** | AEGIS | MCP 生态, prime-agent |
| **推理加速** | Self-Speculation | FlashKDA |
| **代码 Agent 工程化** | SDAD | prime-agent |
| **知识图谱 × Agent** | Knowledge-Graph-Gated | code-graph-rag |
| **隐私与本地优先** | Personalized Privacy Control | openhuman, needle |
| **多 Agent 协作** | Two Heads | prime-agent, AgentENV |

---

## 双料项目统计

- **A类（论文+官方代码）**: 0 个
- **B类（论文+项目互补）**: 8 个（全部入选论文均与本周开源短名单形成明确互补联动）

---

*注: 双料项目指论文本身带有开源代码/数据发布。本周入选论文以方法论和框架为主，未标注代码仓库，但与开源项目形成强主题联动。*
