# 📄 本周候选论文池（W30, 2026-07-15 ~ 2026-07-21）

> 来源：arXiv cs.CL / cs.LG / cs.AI recent | 筛选关键词：LLM, Agent, Multi-Agent, RAG, Prompt Engineering, Chain-of-Thought, Reasoning, Long Context, Multimodal, 智能体, 大模型
> 排除：纯医学AI、纯CV（除非VLM相关）

---

## 1. ActiveVision: A Benchmark for Active Visual Observation in Multimodal LLMs

- **链接**: https://arxiv.org/abs/2607.16165
- **标签**: MLLM, Multimodal, Benchmark, Active Observation, VLM
- **一句话摘要**: 当前前沿多模态大语言模型缺乏主动视觉观察能力——GPT-5.5在该基准上仅解决10.6%的任务，而人类平均达96.1%，揭示了感知-推理闭环的重大缺口。

---

## 2. CRAFT: Clustering Rubrics to Diagnose Weak LLM Capabilities and Generate Targeted Fine-Tuning Data

- **链接**: https://arxiv.org/abs/2607.16122
- **标签**: LLM, Fine-tuning, Evaluation, Reasoning, Data Generation
- **一句话摘要**: 将评估标准聚类转化为模型特定能力诊断工具，自动生成针对性微调数据，解决"模型在哪里失败"到"为什么失败"的评估升级。

---

## 3. Understanding Reasoning from Pretraining to Post-Training

- **链接**: https://arxiv.org/abs/2607.16097
- **标签**: LLM, Reasoning, RL, Pretraining, Chess, Scaling Law
- **一句话摘要**: 以国际象棋为受控测试平台，首次量化揭示预训练损失可预测RL后训练性能，且RL在难题上能发现SFT策略中几乎不存在的正确走法。

---

## 4. PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization

- **链接**: https://arxiv.org/abs/2607.16184
- **标签**: LLM, MoE, Quantization, Serving, Efficiency
- **一句话摘要**: MoE LLM服务新方案，动态量化专家权重并平衡KV缓存，实现FP16等效精度下72% GPU内存节省和1.94倍吞吐提升。

---

## 5. The Honest Quorum Problem: Epistemic Byzantine Fault Tolerance for Agentic Infrastructure

- **链接**: https://arxiv.org/abs/2607.16109
- **标签**: Agent, Multi-Agent, Distributed Systems, Fault Tolerance, EBFT
- **一句话摘要**: 智能体基础设施面临新型"认知故障"——即使诚实验证者也可能因推理错误支持无效状态转换，提出EBFT模型量化语义安全风险。

---

## 6. SciForge: An AI-Native, Multimodal Workbench for Scientific Discovery

- **链接**: https://arxiv.org/abs/2607.16038
- **标签**: Multimodal, AI Agent, Scientific Discovery, Workbench
- **一句话摘要**: 首个AI原生多模态科研工作台，将论文、代码、数据集、模型输出等异构工件整合为可审计的研究状态，保留GUI供人类判断。

---

## 7. Model Merging Matches Joint RL on AppWorld: Task Geometry Explains Why

- **链接**: https://arxiv.org/abs/2607.16062
- **标签**: LLM, Model Merging, RL, Agent, AppWorld
- **一句话摘要**: 模型合并在AppWorld智能体基准上统计显著地匹敌联合RL训练，因任务向量接近正交（余弦相似度0.06-0.10），使合并退化为均匀平均。

---

## 8. ContinuityBench: A Benchmark and Systems Study of Stateful Failover in Multi-Provider LLM Routing

- **链接**: https://arxiv.org/abs/2607.15899
- **标签**: LLM, System, Multi-Provider, Production, Failover
- **一句话摘要**: 生产LLM部署中有状态故障转移基准，揭示标准无状态故障转移的连续性保持率接近0%，而有状态代理可达99.20%。

---

## 9. AI Watermark Evidence Fails Forensic Readiness: An Empirical Evaluation

- **链接**: https://arxiv.org/abs/2607.16010
- **标签**: LLM, Watermark, Security, Forensics, Safety
- **一句话摘要**: 首次从法庭取证标准评估LLM水印，发现KGW和Unigram水印在语义保留改写后100%丢失，且不满足Daubert科学证据可采性标准。

---

## 10. CoWeaver: A Bi-directional, Learnable and Explainable Matching Engine for Mixed Human-Agent Science Collaboration

- **链接**: https://arxiv.org/abs/2607.15545
- **标签**: Multi-Agent, Human-Agent Collaboration, Science, Matching
- **一句话摘要**: 人机混合科学社区的双向可学习可解释匹配引擎，通过UCB探索与贪婪选择结合，在6/20任务上超越纯贪婪最优解。

---

## 11. Harmful Chain-of-Thought Transfers: From Trace Transplantation to Distilled Jailbreaks

- **链接**: https://arxiv.org/abs/2607.15286
- **标签**: LLM, Chain-of-Thought, Safety, Jailbreak, Reasoning
- **一句话摘要**: 有害CoT推理痕迹可跨模型转移——开源模型受害率超80%，蒸馏为系统提示后GPT-4.1上提升10倍，揭示推理层安全的紧迫性。

---

## 12. FedGAMMA: Federated Multimodal Graph Foundation Learning with Semantic-Structural Alignment

- **链接**: https://arxiv.org/abs/2607.15687
- **标签**: Multimodal, Graph, Federated Learning, Foundation Model, Privacy
- **一句话摘要**: 联邦多模态图基础模型学习框架，通过语义-结构对齐和图感知提示微调，在12个数据集上超越基线最高12.96%。

---

## 13. DADiff: Diffusion-based Domain Adaptation for Reinforcement Learning

- **链接**: https://arxiv.org/abs/2607.16090
- **标签**: RL, Diffusion, Domain Adaptation, Generative Model
- **一句话摘要**: 基于扩散模型的RL域适应框架，利用源域与目标域生成轨迹的差异估计动态不匹配，理论上证明性能差异可被生成轨迹偏差界定。

---

## 14. In-context Learning with Linear Self-Attention: Closed-Form Solution via Layer Normalization

- **链接**: https://arxiv.org/abs/2607.15819
- **标签**: LLM, In-context Learning, Transformer, Linear Attention, Theory
- **一句话摘要**: 构建线性自注意力Transformer实现上下文学习最小二乘估计，通过层归一化获得解析解而非梯度下降近似，为ICL机制提供新理论视角。

---

*论文池由周二论文雷达自动生成 | 共14篇 | 生成时间: 2026-07-21*
