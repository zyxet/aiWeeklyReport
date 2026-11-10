# 📄本周候选论文池（20篇）

> 收集时间：2026-11-10（周二）· 窗口：过去7天 · 来源：arXiv cs.CL / cs.LG / cs.AI

---

## 🤖 Agent / Multi-Agent

| # | 标题 | 链接 | 标签 | 摘要 |
|---|------|------|------|------|
| 1 | On Agentic Manipulation Policies | https://arxiv.org/abs/2611.09892 | Agent, Robotics | Apple 提出 AMP1 参考框架，让通用 AI 模型直接操控机械臂，零样本成功率 85.6%，远超专用 VLA/WAM 策略，展示 Agent 在物理世界的泛化潜力。 |
| 2 | Computer-Use Agents Are Embodied Generalists | https://arxiv.org/abs/2611.09847 | CUA, Agent | 论证 Computer-Use Agent 通过屏幕截图和键鼠操作即可胜任具身任务，同一设计在四个 ECCV 竞赛中获奖，无需任务特定调优。 |
| 3 | How Much Conversation History Does an AI Agent Need? | https://arxiv.org/abs/2611.09662 | Agent, Long Context | 系统研究对话历史长度对 AI Agent 任务表现的影响，为上下文窗口设计提供实证依据。 |
| 4 | Language as Trait, Politeness as Strategy: Controlled Tests of Linguistic Effects in LLM Social-Deduction Agents | https://arxiv.org/abs/2611.09768 | LLM Agent, Social Deduction | 在社交推理场景下控制变量测试 LLM 的语言风格与策略选择，揭示语言特征对 Agent 决策的因果影响。 |
| 5 | Phantom Consensus: Measuring Social Reasoning in Multi-Agent LLM Decision-Making | https://arxiv.org/abs/2611.08971 | Multi-Agent, NeurIPS 2026 | 发现多 Agent LLM 系统中的"幻影共识"现象——公开决策被模糊社会信号带偏，引入 PHANTOM-Bench 进行度量。 |
| 6 | MARS: Training Multilingual Search Agents for Retriever-Free Evidence Acquisition | https://arxiv.org/abs/2611.09090 | Agent, RAG, Multilingual | 训练多语言搜索 Agent 直接获取证据，绕过传统检索器，在跨语言证据获取任务上取得突破。 |
| 7 | From Procedures to Permissions: Learning Precise Subagent Authorization from Agent Skills | https://arxiv.org/abs/2611.08905 | Agent Security | 提出从 Agent 技能描述中自动学习精确子 Agent 授权策略的方法，缩小 Agent 权限攻击面。 |
| 8 | MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory | https://arxiv.org/abs/2611.09721 | Agent Security, Memory Poisoning | 首个针对 LLM Agent 记忆投毒攻击的基准测试，揭示持久化记忆引入的新型安全风险。 |
| 9 | Knowing When to Intervene: Causal Evaluation of AI Agents | https://arxiv.org/abs/2611.09792 | Agent Evaluation, Causal Inference | 用因果推断框架评估 AI Agent，解决"何时该人工介入"的问题，超越传统的端到端准确率度量。 |
| 10 | ABHBench: Evaluating Moral Decision-Making of Foundation Models from an Agentic Perspective | https://arxiv.org/abs/2611.09326 | Agent Evaluation, Ethics | 从 Agent 行为视角评估基础模型的道德决策能力，发现当前模型在复杂伦理场景中的系统性缺陷。 |

## 🧠 Reasoning / Chain-of-Thought

| # | 标题 | 链接 | 标签 | 摘要 |
|---|------|------|------|------|
| 11 | Alignment by Confident Debate: Preference Learning from Multi-Agent Debate | https://arxiv.org/abs/2611.09568 | Multi-Agent, Reasoning, Preference Learning | AbCD 方法将多 Agent 辩论轨迹转为偏好训练数据，无需黄金标签，跨五个模型家族提升共识准确率最高 21.5pp。 |
| 12 | Failure Profiling and Reachable Trajectory Selection for Reasoning Distillation | https://arxiv.org/abs/2611.09042 | Reasoning, Distillation | 通过失败画像和可达轨迹选择优化推理蒸馏过程，让小模型更高效地学习大模型的推理能力。 |
| 13 | RPEG: Training Reasoning Language Models Scalably and Cost-Effectively | https://arxiv.org/abs/2611.09207 | Reasoning, RL, Efficiency | 提出可扩展且低成本的推理模型训练方法，降低后训练 RL 的计算门槛。 |
| 14 | Does Reasoning Improve Psychological Depth in Large Language Models? | https://arxiv.org/abs/2611.09061 | Reasoning, LLM Psychology | 探究推理能力是否让 LLM 在心理深度理解任务上表现更好，揭示推理与心理理解之间的非平凡关系。 |

## 🔍 RAG / Memory / Long Context

| # | 标题 | 链接 | 标签 | 摘要 |
|---|------|------|------|------|
| 15 | Compaction, Decay and Reinforcement in a Two-Tier Conversational Memory: A Paired Evaluation Against RAG | https://arxiv.org/abs/2611.09807 | Memory, RAG | 提出双层对话记忆架构（压缩+衰减+强化），与标准 RAG 进行配对评估，为 Agent 记忆设计提供新范式。 |
| 16 | Query-Guided RoPE Modulation for Lost-in-the-Middle Mitigation in Long-Context LLMs | https://arxiv.org/abs/2611.09554 | Long Context, RoPE | 通过查询感知的 RoPE 调制缓解长上下文中的"中间迷失"问题，无需额外训练即可提升长文检索精度。 |

## 🖼️ Multimodal / VLM

| # | 标题 | 链接 | 标签 | 摘要 |
|---|------|------|------|------|
| 17 | ROSE: Risk-Aware Orthogonal Subspace Navigation for Lifelong Knowledge Editing in Multimodal LLMs | https://arxiv.org/abs/2611.09770 | MLLM, Knowledge Editing | 针对多模态大模型的终身知识编辑问题，提出风险感知的正交子空间导航方法，在编辑精度与模型稳定性间取得平衡。 |

## 🛠️ Prompt Engineering / Efficiency / Safety

| # | 标题 | 链接 | 标签 | 摘要 |
|---|------|------|------|------|
| 18 | FinEvolveKG: Controlled and Attributable Prompt Evolution for Financial Knowledge Graph Construction | https://arxiv.org/abs/2611.08643 | Prompt Engineering, Knowledge Graph | 提出可控、可归因的提示词演化框架，用于金融领域知识图谱构建，解决提示漂移和可追溯性问题。 |
| 19 | Forcing a Letter Suppresses Refusal: Mechanistic Evidence from WMDP | https://arxiv.org/abs/2611.08639 | LLM Safety, Mechanistic Interpretability | 通过机制可解释性方法揭示 LLM 拒绝行为被简单字符操纵压制的神经机制，为安全对齐提供新视角。 |
| 20 | BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design | https://arxiv.org/abs/2611.09825 | LLM Inference, Quantization | 提出原生 FP4 KV Cache 解码方法，通过算法-系统协同设计大幅降低 LLM 推理显存占用。 |

---

## 📊 筛选统计

| 维度 | 数量 |
|------|------|
| Agent / Multi-Agent | 10 |
| Reasoning / CoT | 4 |
| RAG / Memory / Long Context | 2 |
| Multimodal / VLM | 1 |
| Prompt Engineering / Efficiency / Safety | 3 |

> **排除说明**：本周过滤掉纯医学 AI（放射学 Agent 框架、医疗理赔分析）3 篇，纯 CV（运动预测、点云分割）4 篇。
> **来源覆盖**：arXiv cs.CL ✅ · arXiv cs.LG ✅ · arXiv cs.AI ✅ · HuggingFace Papers ❌（网络不可达）· PaperWeekly ❌（公众号内容无法直接抓取，已通过搜索间接覆盖）
