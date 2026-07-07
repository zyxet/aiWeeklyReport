# 📄 本周候选论文池（2026-W28）

> 收集日期：2026-07-07（周二）
> 来源：arXiv cs.CL/cs.LG/cs.AI (2026-07-03批次)、Hugging Face Papers、PaperWeekly
> 筛选关键词：LLM, Agent, Multi-Agent, RAG, Reasoning, Chain-of-Thought, Multimodal, Long Context, Prompt Engineering
> 排除：纯医学AI、纯CV（除非VLM相关）

---

## 论文列表（共 22 篇）

### 1. LACUNA: Parameter-Level Localization for LLM Unlearning
- **链接**: https://arxiv.org/abs/2607.02513
- **标签**: LLM, Privacy, Alignment
- **一句话摘要**: 首个支持参数级定位的LLM遗忘测试平台，通过将合成PII注入预定义参数来直接评估遗忘方法是否真正擦除了知识，发现现有方法输出级表现好但参数级精度差，易受攻击复现。

### 2. DramaSR-LRM: Speaker Recognition via Large Reasoning Model with Multimodal Tool-Use
- **链接**: https://arxiv.org/abs/2607.02504
- **标签**: Multimodal, LRM, Tool
- **一句话摘要**: 基于大型推理模型（LRM）的多模态工具使用方法，用于长视频中的说话人识别，通过自主聚合听觉、语言和视觉线索实现高保真归属。

### 3. PAW: Program-as-Weights for Fuzzy-Function Programming
- **链接**: https://arxiv.org/abs/2607.02512
- **标签**: LLM, Tool, Program
- **一句话摘要**: 提出Program-as-Weights（PAW）框架，将模糊函数编程编译为小型语言模型（4B参数）的权重，实现可执行程序的功能性表达。

### 4. VRRL: Visually-Grounded RL Reflection for Large Vision-Language Models
- **链接**: https://arxiv.org/abs/2607.02490
- **标签**: Multimodal, Reasoning, RL
- **一句话摘要**: 为大型视觉语言模型引入视觉 grounded 的强化学习反射机制，通过视觉反馈增强推理和决策能力。

### 5. Scaling Laws for LLM Social Simulations
- **链接**: https://arxiv.org/abs/2607.02464
- **标签**: LLM, Agent, Scaling
- **一句话摘要**: 使用85个Qwen3架构模型（0.5B-70B）研究LLM社会模拟的扩展规律，发现计算规模能显著改善大多数行为模拟和观点建模任务，但纵向预测和代表性不足的观点扩展较慢。

### 6. MEDIAREF: A Reproducible Knowledge Store for Media Background Checks in RAG-Based Fact-Checking
- **链接**: https://arxiv.org/abs/2607.02383
- **标签**: RAG, LLM, Knowledge
- **一句话摘要**: 为RAG事实核查提供可复现的媒体背景知识库（200个媒体来源），支持低成本评估源可信度生成，提升自动事实核查的透明度和可靠性。

### 7. Steerability via Constraints: A Substrate for Scalable Oversight of Coding Agents
- **链接**: https://arxiv.org/abs/2607.02389
- **标签**: Agent, Tool/Planning, Security
- **一句话摘要**: 提出通过约束（访问控制、网络策略、编码规范）实现编码智能体的可扩展监督，小模型（Gemma 4B）审查代码后门检测召回率从54.5%提升至90.9%。

### 8. DRIFTLENS: Memory-Induced Reasoning Drift in Personalized Language Models
- **链接**: https://arxiv.org/abs/2607.02374
- **标签**: RAG, Reasoning, LLM, Personalization
- **一句话摘要**: 发现个性化LLM中的记忆注入会改变推理轨迹（即使最终答案不变），提出无真值框架量化推理漂移，并评估GRPO/DPO后训练方法的缓解效果。

### 9. HOLA: A Hippocampus for Linear Attention
- **链接**: https://arxiv.org/abs/2607.02303
- **标签**: RAG, LLM, Long Context, Architecture
- **一句话摘要**: 受互补学习系统启发，为线性注意力添加海马体补充—— bounded exact KV 缓存形成半参数化测试时记忆，340M参数在Wikitext上困惑度从27.32降至22.92，32k token needle recall 显著优于基线。

### 10. Autonomous Research Agents in Condensed Matter Physics
- **链接**: https://arxiv.org/abs/2607.02329
- **标签**: Agent, LLM, Scientific AI
- **一句话摘要**: 端到端自主研究智能体管道，从11,083篇凝聚态物理论文中自主构思研究方向、复现文献方法、进行第一性原理计算并撰写论文，通过新鲜上下文隔离和对抗性审查实现容错。

### 11. DecompRL: Decomposing Code Problems via RL for LLM Reasoning
- **链接**: https://arxiv.org/abs/2607.02390
- **标签**: LLM, Reasoning, Tool/Planning, RL
- **一句话摘要**: 通过强化学习将代码问题分解为独立可解的子函数，k个模块实现可组合成k^n候选解，将GPU token成本降低约50倍，在LiveCodeBench和CodeContests上超越标准基线。

### 12. HERMES: Hierarchical Data Mixture Labeling for Pre-training
- **链接**: https://arxiv.org/abs/2607.02266
- **标签**: LLM, Pre-training, Data
- **一句话摘要**: 提出分层数据混合标签系统（HERMES），通过学习语义变换和残差向量量化将文档标注为粗到细的代码，1B参数预训练在16任务宏平均提升+0.0253。

### 13. LLM-as-a-Judge in Multilingual and Low-Resource Settings: Problems and Recommendations
- **链接**: https://arxiv.org/abs/2607.02235
- **标签**: LLM, Evaluation, Multilingual
- **一句话摘要**: 系统分析650篇ACL论文中LLM-as-a-Judge在多语言/低资源设置中的使用，发现评估不一致、过度信任LLM判断、依赖单一模型等问题，并提出使用建议。

### 14. SpeechCombine: Instruction-Following Speech Language Models Without Instruction Tuning
- **链接**: https://arxiv.org/abs/2607.02214
- **标签**: Multimodal, LLM, Speech
- **一句话摘要**: 提出SpeechCombine方法，通过权重组合将文本LLM的指令遵循能力迁移到语音领域，无需任何语音指令调优，仅用30k小时语音预训练即实现有效的指令遵循。

### 15. DALorRA: Data-Adaptive LoRA for Uncertainty Quantification in LLMs
- **链接**: https://arxiv.org/abs/2607.02182
- **标签**: LLM, Alignment, LoRA
- **一句话摘要**: 提出变分贝叶斯稀疏框架DALorRA，在LoRA秩级别进行不确定性量化，通过随机掩码实现贝叶斯正则化，在保持推理准确率的同时实现出色的校准。

### 16. Bias-Aware LLM-as-a-Judge for Top-k Identification
- **链接**: https://arxiv.org/abs/2607.02104
- **标签**: LLM, Evaluation, Reasoning
- **一句话摘要**: 提出考虑特定偏见（冗长性、位置效应）的贝叶斯推理框架，结合Top-k感知主动获取规则，在16个真实LLM评委上实现准确排序，中低端模型召回率从0.5-0.6提升至0.84-1.0。

### 17. Neuron-OPSD: Annotation-Free Self-Distillation via Neuron Activations for LLMs
- **链接**: https://arxiv.org/abs/2607.02460
- **标签**: LLM, Alignment, Self-Distillation
- **一句话摘要**: 利用内部神经元激活指导训练数据选择和教师上下文构建，实现无需任何标注的LLM自蒸馏，在域内任务提升的同时保持跨域泛化能力，避免校准崩溃。

### 18. HULAT2: LangGraph-Based Multi-Agent Workflow for Translation
- **链接**: https://arxiv.org/abs/2607.02381
- **标签**: Agent, RAG, Multilingual
- **一句话摘要**: 基于LangGraph的多智能体翻译工作流，结合Gemini 2.5 Flash和RigoChat-7B，通过并行生成、事件-条件-动作路由和可控编辑，在MER-TRANS 2026西班牙语赛道取得最佳SARI分数。

### 19. CheckRLM: Retrieval-Augmented Generation for Reasoning Language Models
- **链接**: https://arxiv.org/abs/2607.02262
- **标签**: RAG, Reasoning, LLM
- **一句话摘要**: 为推理语言模型（RLM）提出CheckRLM框架，通过及时检查推理链中的事实错误并利用外部知识进行最小成本精确修正，显著减轻长程推理中的错误累积。

### 20. HaloGuard 1.0: Constitutional Classifier for Input Safety
- **链接**: https://arxiv.org/abs/2607.02079
- **标签**: LLM, Alignment, Safety
- **一句话摘要**: 开源的宪法分类器实现，基于46条政策和2,940个子类别生成合成数据，0.8B模型在7个提示安全基准上达到平均F1 90.9，超越参数大30倍的基线模型。

### 21. Memory Contracts for Long-Horizon LLM Agents in Slay the Spire 2
- **链接**: https://arxiv.org/abs/2607.02255
- **标签**: Agent, LLM, Long Context, Memory
- **一句话摘要**: 提出有界记忆合约替代原始上下文追加，每个决策通过类型化检索从新鲜用户消息组装，提示保持有界，在Slay the Spire 2（数百决策的卡牌游戏）中显著优于基线。

### 22. PMI-OPSD: Mutual Information Based Self-Distillation for Long-CoT Reasoning Models
- **链接**: https://arxiv.org/abs/2607.02234
- **标签**: LLM, Reasoning, Chain-of-Thought, Alignment
- **一句话摘要**: 针对长思维链推理模型的自蒸馏失败问题，提出PMI-OPSD方法，通过点互信息分离参考诱导的不可迁移成分和条件可迁移成分，在4个长CoT模型上实现一致改进。

### 23. UA-ChatDev: Uncertainty-Aware Multi-Agent Software Development
- **链接**: https://arxiv.org/abs/2607.02186
- **标签**: Agent, LLM, Tool/Planning, Multi-Agent
- **一句话摘要**: 提出不确定性感知的多智能体软件开发框架，基于token级对数概率估计代理响应置信度，并在不确定性超过阈值时触发检索验证，在SRDD基准上超越现有单智能体和多智能体框架。

### 24. NeuFS: Neuron-Aware Active Few-Shot Learning for LLMs
- **链接**: https://arxiv.org/abs/2607.02423
- **标签**: LLM, In-Context Learning, Few-Shot, Hallucination
- **一句话摘要**: 提出NeuFS框架，利用神经元激活模式表示样本，通过双标准选择策略（多样性+信息性）主动选择最具价值的少样本示例，在推理和文本分类任务上优于现有基线。

---

## 补充来源：其他重要论文（2026年会议/预印）

| 标题 | 来源 | 标签 | 说明 |
|------|------|------|------|
| ExtAgents: Scaling External Knowledge via Multi-Agent Collaboration | ACL 2026 | Agent, Multi-Agent, Long Context | 多智能体协作扩展外部知识输入 |
| MemGraphRAG: Memory-based Multi-Agent Graph RAG | KDD 2026 | RAG, Multi-Agent, Graph | 基于记忆的多智能体图RAG系统 |
| Aligned Agents, Biased Swarm | ICLR 2026 | Agent, Multi-Agent, Bias | 多智能体系统中的偏见放大研究 |
| J1Bench: Benchmarking Legal Language Agents | ACL 2026 | Agent, Legal, Benchmark | 法律智能体动态环境基准测试 |
| Infherno: Agent-based FHIR Resource Synthesis | EACL 2026 Demo | Agent, RAG, Medical | 基于Hugging Face SmolAgents的临床笔记结构化 |
| ClawGuard: Runtime Security for Tool-Augmented LLM Agents | arXiv 2026 | Agent, Security | 工具增强LLM智能体的运行时安全框架 |
| LLM Collaboration with Multi-Agent RL | arXiv 2025 | Agent, Multi-Agent, RL | MA-GRPO多智能体强化学习协作 |
| Creativity in LLM-based Multi-Agent Systems | arXiv 2025 | Agent, Multi-Agent, Creativity | LLM多智能体系统创造力综述 |

---

## 趋势观察

1. **多智能体系统**持续火热——从协作翻译到软件开发，从记忆管理到偏见研究
2. **RAG与推理结合**——CheckRLM、MEDIAREF等论文将检索增强与推理链检查结合
3. **长上下文与记忆**——HOLA、Memory Contracts等探索超越传统上下文窗口的方法
4. **安全与对齐**——HaloGuard、Steerability、LACUNA等聚焦模型安全与可控性
5. **自蒸馏与自进化**——Neuron-OPSD、PMI-OPSD等无需标注的自我改进方法
6. **多模态扩展**——SpeechCombine、DramaSR-LRM等将LLM能力扩展到语音和视频

---

*生成时间: 2026-07-07 10:00 CST | 任务: tuesday-paper-collect | 前置任务: monday-collect ✅*
