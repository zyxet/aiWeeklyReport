# 📄 本周候选论文池（18篇）

> **收集时间**: 2026-08-18  
> **周期**: W34 (2026-08-12 ~ 2026-08-18)  
> **来源**: arXiv cs.CL / cs.LG / cs.AI recent  

---

## 🔬 推理与思维链 (Reasoning & CoT)

**1. YOPO: You Only Pass Once**  
| [arXiv:2608.14465](https://arxiv.org/abs/2608.14465)  
| 标签: `Reasoning` `Steering` `Abstention`  
| 一句话摘要: 通过单次前向传播实现答案生成、推理引导和拒绝回答，在Qwen2.5上三任务准确率从0.375提升至0.798。

**2. On-policy Distillation for Long-Context to Short-Context**  
| [arXiv:2608.14277](https://arxiv.org/abs/2608.14277)  
| 标签: `Distillation` `Reasoning` `Long Context`  
| 一句话摘要: 将长上下文教师模型(SU-01)的推理能力迁移到短上下文学生模型，Intern-S2在ProofBench上提升21.2分。

**3. Behavioral Lift: Which Reasoning Behaviors Are Actually Associated with Correctness?**  
| [arXiv:2608.13760](https://arxiv.org/abs/2608.13760)  
| 标签: `Reasoning` `Training Analysis` `VLM`  
| 一句话摘要: 发现推理训练放大的是"自我纠正"等行为，但最高提升行为是"置信度校准"，两者存在放大-提升差距。

**4. LRM Batch Pruning**  
| [arXiv:2608.14003](https://arxiv.org/abs/2608.14003)  
| 标签: `Reasoning` `Efficiency` `Pruning`  
| 一句话摘要: 针对推理模型的批处理剪枝方法，减少推理成本。

**5. Multilingual GRPO: A Large-Scale Empirical Study**  
| [arXiv:2608.13698](https://arxiv.org/abs/2608.13698)  
| 标签: `RL` `Multilingual` `Reasoning`  
| 一句话摘要: 多语言GRPO大规模实证研究，发现母语推理训练与英语推理差距很小，但存在语言特定的能力退化。

---

## 🤖 Agent & Multi-Agent

**6. Envs-FORGE: Dynamic Environment Synthesis for Terminal Agent RL**  
| [arXiv:2608.14312](https://arxiv.org/abs/2608.14312)  
| 标签: `RL` `Agent` `Training`  
| 一句话摘要: 将验证器奖励转换为每种子环境合成动作的提示策略，在Qwen 3.5 35B上Pass@1提升9.2个百分点。

**7. InflationAgent: Token Cost-Aware Routing for Agent Workflows**  
| [arXiv:2608.13571](https://arxiv.org/abs/2608.13571)  
| 标签: `Agent` `Cost Optimization` `Routing`  
| 一句话摘要: 提出token膨胀概念，通过CoT分支熵预测任务难度，在GSM8K上以31%更少token达到94.7%准确率。

**8. Diverse Hypothesis Deliberation (DHD)**  
| [arXiv:2608.14375](https://arxiv.org/abs/2608.14375)  
| 标签: `Multi-Agent` `Reasoning`  
| 一句话摘要: 测量多Agent推理中"错误但有用"消息的价值，发现超40%的错误答案消息对最终推理有帮助。

**9. TeachMateGPT: Multi-Agent Science Assessment Generation**  
| [arXiv:2608.13708](https://arxiv.org/abs/2608.13708)  
| 标签: `Multi-Agent` `RAG` `Education`  
| 一句话摘要: 多Agent课程评估生成系统，含COPE层次知识库、SAVER验证协议，忠实度从0.68提升至0.96。

**10. HERMES: Multi-Agent Framework for Scientific Document Extraction**  
| [arXiv:2608.14055](https://arxiv.org/abs/2608.14055)  
| 标签: `Multi-Agent` `Document Understanding` `Science`  
| 一句话摘要: 从55卷古生物学专著中提取32,277个化石分类实体和451,878个属性，效率提升6倍。

---

## 🔍 RAG & Retrieval

**11. Hallucination in Legal RAG: A Fine-Grained Analysis**  
| [arXiv:2608.14210](https://arxiv.org/abs/2608.14210)  
| 标签: `RAG` `Hallucination` `Legal`  
| 一句话摘要: 对8个法律RAG系统进行细粒度幻觉分析，发现幻觉率在10%-50%之间，错误前提问题产生高幻觉率。

**12. IterCOMP: Iterative Prompt Compression for Multi-Hop RAG**  
| [arXiv:2608.13578](https://arxiv.org/abs/2608.13578)  
| 标签: `RAG` `Prompt Compression` `Multi-Hop`  
| 一句话摘要: 训练-free的多跳推理提示压缩框架，在MusiQue等数据集上提升EM和F1分数同时减少token预算。

---

## 🛡️ Safety, Evaluation & Alignment

**13. AdaPop: Adaptive Popularity Unlearning for LLMs**  
| [arXiv:2608.14229](https://arxiv.org/abs/2608.14229)  
| 标签: `Unlearning` `Privacy` `Safety`  
| 一句话摘要: 结合局部token置信度和事实流行度依赖指数的自适应遗忘方法，泄漏量减少约5倍。

**14. Function Calling Abstention**  
| [arXiv:2608.13959](https://arxiv.org/abs/2608.13959)  
| 标签: `LLM` `Function Calling` `Abstention`  
| 一句话摘要: 研究LLM函数调用中的拒绝回答机制。

**15. Principle-Bench: Evaluating LLM-as-Judge for Principle-Based Regulation**  
| [arXiv:2608.14329](https://arxiv.org/abs/2608.14329)  
| 标签: `Evaluation` `Regulation` `LLM-as-Judge`  
| 一句话摘要: 首个覆盖准确性、鲁棒性、对抗性和校准四个维度的原则性监管评估基准，发现120B模型在关键词填充攻击下准确率从0.74降至0.27。

**16. AnchorBench: Benchmarking Anchoring Effect in LLMs**  
| [arXiv:2608.14320](https://arxiv.org/abs/2608.14320)  
| 标签: `Evaluation` `Bias` `Cognitive`  
| 一句话摘要: 评估14个模型对锚定效应的敏感性，发现即使95%+准确率的前沿模型仍易受合理锚点影响。

---

## ⚡ Efficiency & Architecture

**17. BCMT: Blockwise Causal Memory Transformer**  
| [arXiv:2608.13578](https://arxiv.org/abs/2608.13578)  
| 标签: `Long Context` `Architecture` `Efficiency`  
| 一句话摘要: 通过指数因果记忆实现长上下文建模，保持与Dense Transformer相当的性能同时显著提升训练吞吐量和降低内存消耗。

**18. Many-to-Many Code Translation with Preference-Based RL**  
| [arXiv:2608.13854](https://arxiv.org/abs/2608.13854)  
| 标签: `Code` `RL` `Translation`  
| 一句话摘要: 基于GRPO的600语言对(25x24)代码翻译，4B模型在HumanEval-X++上平均提升13%。

---

## 📊 统计

| 类别 | 数量 |
|------|------|
| Reasoning & CoT | 5 |
| Agent & Multi-Agent | 5 |
| RAG & Retrieval | 2 |
| Safety, Evaluation & Alignment | 4 |
| Efficiency & Architecture | 2 |
| **总计** | **18** |

---

*收集完成于 2026-08-18 10:00 AM (Asia/Shanghai)*
