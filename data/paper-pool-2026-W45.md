# 📄 本周候选论文池（2026-W45）

> 收集时间：2026-11-03（周二）
> 覆盖范围：arXiv cs.CL / cs.AI / cs.LG 2026-10-30 ~ 2026-11-02 新提交论文
> 筛选关键词：LLM, Agent, Multi-Agent, RAG, Reasoning, Chain-of-Thought, Long Context, Multimodal, Prompt Engineering
> 排除：纯医学 AI、纯 CV（非 VLM）

---

## 🔥 高优先级（Agent / Reasoning / Long Context 核心方向）

### 1. Latent Sparse Attention: Towards Subquadratic Ultra-Long Context Attention
- **arXiv**: https://arxiv.org/abs/2610.42147
- **标签**: Long Context, Attention, Efficiency, Subquadratic
- **摘要**: 提出 Latent Sparse Attention (LSA)，通过层次化潜在空间聚类实现超长尾上下文注意力，在 10M token 上实现 22.7x prefill 加速，同时保持精度，可将有效上下文窗口扩展至数亿 token。

### 2. ZHA: Subquadratic Attention with a Hierarchical Tree-Structured Indexer
- **arXiv**: https://arxiv.org/abs/2610.42112
- **标签**: Long Context, Attention, Efficiency, Tree Index
- **摘要**: Zyphra 提出的层次树结构索引注意力，通过递归压缩 key 摘要构建树形索引，实现渐近亚二次注意力复杂度，超越 1M token 后显著优于现有方法，有潜力扩展至数亿 token 级上下文。

### 3. CRoS: Causality Reward on Scrambled CoTs Improves Accuracy and Reasoning Faithfulness
- **arXiv**: https://arxiv.org/abs/2610.42054
- **标签**: CoT, Reasoning, RLVR, Causality Reward, Faithfulness
- **摘要**: 提出 CRoS 因果奖励机制，通过打乱推理步骤顺序（不改变内容）来度量 CoT 的因果贡献，在 RLVR 训练中提升 OOD 精度、CoT 质量和忠实度，优于现有因果度量和结果奖励。

### 4. KEEPER: Learning Control-Sufficient Textual Memory for Long-Horizon LLM Agents
- **arXiv**: https://arxiv.org/abs/2610.41482
- **标签**: Agent, Long-Horizon, Memory, Control-Sufficient
- **摘要**: 为长时程 LLM Agent 学习控制充分的文本记忆，解决 agent 在长时间任务中的信息保留和决策问题。

### 5. In-Model Context Compression with Agentic Soft Tokens for Long-Horizon LLM Agents
- **arXiv**: https://arxiv.org/abs/2610.41291
- **标签**: Agent, Long-Horizon, Context Compression, Soft Tokens
- **摘要**: 提出 Agentic Soft Tokens 实现模型内上下文压缩，让长时程 LLM Agent 在有限上下文窗口内高效管理信息，26页，9图11表，附代码。

### 6. DAMI: Dual-Axis Memory Initialization for Enhanced Long-Context Retrieval in Gated Linear Attention
- **arXiv**: https://arxiv.org/abs/2610.41994
- **标签**: Long Context, Linear Attention, Gated DeltaNet, Memory Initialization
- **摘要**: 针对门控线性注意力的有限状态记忆瓶颈，提出双轴记忆初始化策略，在 GDN/KDA/Mamba-2/RWKV-7 上将 RULER 检索精度提升 5.29~16.71 个百分点。

### 7. Stepwise-Querying: Distilling Reasoning without Access to Teacher Chain-of-Thought
- **arXiv**: https://arxiv.org/abs/2610.41769
- **标签**: CoT, Distillation, Reasoning, Teacher-Free
- **摘要**: 提出逐步查询蒸馏方法，无需访问教师模型的 CoT 即可蒸馏推理能力，15页7图。

### 8. ACCT: Asymmetric Cross-LLM Context Transfer
- **arXiv**: https://arxiv.org/abs/2610.42116
- **标签**: LLM, KV Cache, Context Transfer, Efficiency, Multi-Model
- **摘要**: 实现同族不同规模模型间的 KV cache 迁移，将源模型的上下文计算结果转换为稀疏 KV 状态供目标模型直接使用，在压缩 75% KV cache 的情况下保持甚至超越原始推理性能，19K token 上下文下实现 6.5-21.2x 加速。

### 9. Does Reasoning Make Language Models Agree?
- **arXiv**: https://arxiv.org/abs/2610.41691
- **标签**: Reasoning, LLM, Agreement, Evaluation
- **摘要**: 研究推理能力是否让语言模型在判断上达成一致，分析多模型在推理任务上的行为一致性，涉及 cs.CL + cs.LG + cs.CY。

### 10. BlindToChange: AI Agents Can Find Changes When Asked But Do They Look When Needed?
- **arXiv**: https://arxiv.org/abs/2610.41435
- **标签**: Agent, Proactive Perception, Evaluation, Visual Change Detection
- **摘要**: 揭示 AI Agent 在被问到时能发现变化，但不会主动关注关键视觉变化的行为缺陷，对 agent 的主动感知能力提出 benchmark 和评估。

### 11. GraphNIAH: A Benchmark for Long-Context Reasoning over Real-World Graphs
- **arXiv**: https://arxiv.org/abs/2610.41704
- **标签**: Long Context, Benchmark, Graph Reasoning, NIAH
- **摘要**: 针对真实世界图结构的长上下文推理基准测试，评估 LLM 在图结构信息中的推理能力。

### 12. RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory
- **arXiv**: https://arxiv.org/abs/2610.42141
- **标签**: Agent, Robotics, Memory, Harness Design, Automated Optimization
- **摘要**: 展示 agent harness 设计可以自动化——coding model 观察机器人 rollout、诊断失败并迭代修订 harness，无需更新模型权重即可将成功率从 9.7% 提升至 43.3%，harness 还能自主演化持久记忆。

### 13. Mage-VL-Cowork: A Full Training Recipe to Learn Hybrid Computer Use From Evolved Harnesses
- **arXiv**: https://arxiv.org/abs/2610.40747
- **标签**: VLM, Computer Use, Agent, Training Recipe
- **摘要**: 完整训练配方，学习基于演化 harness 的混合计算机使用能力，属于 Vision-Language Model + Agent 方向。

### 14. Latent Reasoning in Continuous Space for Unified Multimodal Models
- **arXiv**: https://arxiv.org/abs/2610.42149 (NeurIPS 2026)
- **标签**: Multimodal, Latent Reasoning, Continuous Space, VLM
- **摘要**: 在统一多模态模型中引入连续空间潜在推理机制，NeurIPS 2026 接收。

---

## 📌 中优先级（LLM 架构 / 训练 / 安全方向）

### 15. SecPO: Principled Adversarial Training for Prompt Injection Security
- **arXiv**: https://arxiv.org/abs/2610.41998
- **标签**: Prompt Injection, Security, Adversarial Training, Agent Safety
- **摘要**: 针对 prompt injection 攻击提出理论指导的 SecPO 损失函数和高效对抗训练管线，在 AgentDojo 上将攻击成功率从 78.8% 降至 8.8%，同时保持正常任务性能无损。

### 16. ETAPS: Prune Gradually, Adapt Sparsely - Efficient Pruning of LLMs at Extreme Sparsity
- **arXiv**: https://arxiv.org/abs/2610.41968
- **标签**: LLM, Pruning, Sparsity, Efficiency
- **摘要**: 渐进式剪枝 + 稀疏适配方法，在 50%-90% 极端稀疏度下实现更低困惑度，90% 稀疏度时仅需单张 H200（ELSА 需四张）。

### 17. Trainable Vector Quantization for Large Language Models
- **arXiv**: https://arxiv.org/abs/2610.41822 (ECML PKDD 2026)
- **标签**: LLM, Quantization, Compression, Efficiency
- **摘要**: 面向 LLM 的可训练向量量化方法，ECML PKDD 2026 接收。

### 18. When Steering Shifts Discourse: Identifying and Intervening on Discourse-Level Changes due to Activation Steering in LLMs
- **arXiv**: https://arxiv.org/abs/2610.41661
- **标签**: Activation Steering, Interpretability, Control, Discourse
- **摘要**: 研究激活引导（activation steering）对 LLM 话语层面输出的影响，识别并干预由 steering 引起的话语级变化。

### 19. Latent-Lens: Visual Perception in Small Language Models Through Latent Communication
- **arXiv**: https://arxiv.org/abs/2610.41751
- **标签**: VLM, Small LM, Latent Communication, Multimodal
- **摘要**: 探索小语言模型通过潜在空间通信获得视觉感知能力，属于轻量级 VLM 方向。

### 20. BYOD: Build Your Own DLM - Efficient Autoregressive-to-Diffusion Language Model Conversion
- **arXiv**: https://arxiv.org/abs/2610.41574
- **标签**: Diffusion LM, Autoregressive, Model Conversion, Architecture
- **摘要**: 高效的自回归到扩散语言模型转换方法，21页8图，附 Gemma demo 和代码。

### 21. RangeSWA: Training-Free Length Extrapolation for Continuous Diffusion Language Models
- **arXiv**: https://arxiv.org/abs/2610.42084
- **标签**: Diffusion LM, Length Extrapolation, Training-Free
- **摘要**: 免训练的长度外推方法，用于连续扩散语言模型的上下文扩展。

### 22. Task Vectors Can Be Linearly Decomposed into Interpretable and Controllable Components
- **arXiv**: https://arxiv.org/abs/2610.41743
- **标签**: Task Vectors, Interpretability, Model Editing
- **摘要**: 证明任务向量可以线性分解为可解释和可控的组件，为模型编辑和控制提供新视角。

### 23. UpLoop: Training Looped Transformers via Upcycling at No Extra Pretraining Compute
- **arXiv**: https://arxiv.org/abs/2610.41720
- **标签**: Looped Transformer, Upcycling, Architecture, Efficiency
- **摘要**: 通过升级循环在零额外预训练计算下训练循环 Transformer，探索循环架构的效率潜力。

### 24. There Is No Free Loop: When Does Looping a Trained Model Pay for Its Inference Compute?
- **arXiv**: https://arxiv.org/abs/2610.42030
- **标签**: Looped Transformer, Inference Cost, Architecture
- **摘要**: 系统评估在已训练模型上添加循环层的收益与推理成本，发现仅小模型在固定参数预算下受益。

### 25. Flide: Accelerating Decision Inference with Exact State Forking
- **arXiv**: https://arxiv.org/abs/2610.42148
- **标签**: Decision Model, Inference Acceleration, State Forking
- **摘要**: 通过精确状态分叉加速决策推理，20页，带项目页面。

### 26. DecisionRank: On-Policy Distillation for Decision-Model Rerankers
- **arXiv**: https://arxiv.org/abs/2610.42128
- **标签**: Decision Model, Reranker, On-Policy Distillation
- **摘要**: 针对决策模型重排序器的 on-policy 蒸馏方法，25页8图。

---

## 📝 备注

- 本周 arXiv 10-30（周四）~ 11-02（周一）为一批集中提交日，以上论文主要来自 10-30 提交批次
- Hugging Face Papers trending 页面本周持续超时，未能获取；PaperWeekly 本周精选暂未发布
- cs.LG 中部分纯理论优化/隐私计算论文已排除（如 DP-SGD、收敛性分析等）
- 纯医学 AI（ICU 预测、ECG 分类等）已排除
- 时序预测（Chronos-2）偏应用，未纳入核心池

---

*收集者：周二论文雷达 | 数据源：arXiv API + kimi_search | 下一环节：周四筛选*
