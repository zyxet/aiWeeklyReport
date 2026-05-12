# 📄 本周候选论文池（2026-W20，共 22 篇）

> 收集时间：2026-05-12 | 来源：arXiv cs.CL/cs.LG/cs.AI (2605.04–2605.08)、Hugging Face Papers Trending、PaperWeekly / AnalyticsVidhya 精选
> 筛选关键词：LLM, Agent, Multi-Agent, RAG, Reasoning, Tool Use, Prompt Engineering, Chain-of-Thought, Long Context, Multimodal, 智能体, 大模型
> 排除：纯医学AI、纯CV（非VLM）、纯传统ML、纯语言学统计

---

## 🏷 Agent / 智能体

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 1 | **AI Co-Mathematician: Accelerating Mathematicians with Agentic AI** | https://arxiv.org/abs/2605.06651 | `Agent`, `Reasoning`, `Mathematics` | DeepMind推出的AI数学协作者工作台，通过并行Agent实现文献检索、定理证明与开放问题探索，在FrontierMath Tier 4上取得48%的新高分数。 |
| 2 | **Ask Early, Ask Late, Ask Right: When Does Clarification Timing Matter for Long-Horizon Agents?** | https://arxiv.org/abs/2605.07937 | `Agent`, `Long-Horizon`, `Clarification` | 系统研究长程Agent在不同阶段（早期/中期/晚期）发起澄清请求的效果，发现澄清时机对任务成功率有显著影响。 |
| 3 | **Learning CLI Agents with Structured Action Credit under Selective Observation** | https://arxiv.org/abs/2605.08013 | `Agent`, `CLI`, `RL`, `Credit Assignment` | 在部分可观察的CLI环境中，通过结构化动作 credit 分配机制训练命令行智能体，解决稀疏奖励下的长期任务执行问题。 |
| 4 | **How Expanded Recall Erodes Cooperative Intent in LLM Agents** | https://arxiv.org/abs/2605.08060 | `Agent`, `Multi-Agent`, `Cooperation` | 发现扩大LLM Agent的上下文记忆反而会削弱其合作意图，揭示了记忆容量与多Agent协作行为之间的反直觉权衡。 |
| 5 | **Agentic Discovery for Test-Time Scaling** | https://arxiv.org/abs/2605.08083 | `Agent`, `Test-Time Scaling`, `Reasoning` | 提出让Agent在推理时主动发现知识并动态扩展上下文，实现无需预训练增强的测试时推理能力提升。 |
| 6 | **Compiling LLM Reasoning into Symbolic Solvers for Efficient Program Synthesis** | https://arxiv.org/abs/2605.05485 | `Agent`, `Program Synthesis`, `Neuro-Symbolic` | 将LLM的推理轨迹编译为可复用的符号求解器，在PBEBench-Hard上以零LLM推理成本超越测试时缩放方法16.3个百分点。 |

---

## 🏷 Reasoning / 推理

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 7 | **Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration** | https://arxiv.org/abs/2605.08077 | `Reasoning`, `KGQA`, `Conformal Prediction` | 在知识图谱问答中引入路径级保形预测校准，为每条推理路径提供置信度保证，提升复杂多跳问答的可信度。 |
| 8 | **Rubric-Grounded RL: Structured Judge Rewards for Generalizable Reasoning** | https://arxiv.org/abs/2605.08061 | `Reasoning`, `RL`, `Reward Modeling` | 用结构化评分标准（Rubric）作为奖励信号训练RL，使推理模型获得可泛化的评判能力，减少奖励 hacking。 |
| 9 | **Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection** | https://arxiv.org/abs/2605.08070 | `Reasoning`, `Self-Consistency`, `Confidence` | 通过推理轨迹聚类与候选答案选择改进基于置信度的自一致性解码，在推理任务上提升答案准确性。 |
| 10 | **Abductive Reasoning with Probabilistic Commonsense** | https://arxiv.org/abs/2605.08011 | `Reasoning`, `Abduction`, `Commonsense` | 将概率常识知识融入溯因推理框架，使LLM能够从不完整观察中推断最可能的解释。 |

---

## 🏷 RAG / 检索增强生成

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 11 | **AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop RAG** | https://arxiv.org/abs/2605.05245 | `RAG`, `Multi-Hop`, `Token-Efficiency` | 针对多跳RAG的token高效证据组装方法，通过显式gap追踪与微查询生成，在冗余注入条件下以2.6倍更少token达到最优证据F1。 |
| 12 | **The Cost of Context: Mitigating Textual Bias in Multimodal RAG** | https://arxiv.org/abs/2605.05594 | `RAG`, `Multimodal`, `VLM`, `Bias` | 揭示多模态RAG中"recorruption"现象——引入外部文本反而导致模型放弃正确视觉预测，提出BAIR无参数干预框架恢复视觉显著性。 |

---

## 🏷 Tool Use / 工具调用

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 13 | **Tool Calling is Linearly Readable and Steerable in Language Models** | https://arxiv.org/abs/2605.07990 | `Tool Use`, `Mechanistic Interpretability`, `Steerability` | 通过机制可解释性分析证明工具调用能力在LLM内部是线性可读且可操控的，为工具使用能力的定向激活/抑制提供了理论基础。 |
| 14 | **A Comprehensive Tool-Calling Dataset for Enhancing Biomedical Capabilities of Large Language Models** | https://arxiv.org/abs/2605.05758 | `Tool Use`, `Biomedical`, `Dataset` | 构建BioTool数据集，含34个生物医学工具与7040条人工验证的query-API对，微调后4B模型在工具调用上超越GPT-5.1。 |

---

## 🏷 LLM Training / Alignment / 训练与对齐

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 15 | **Your Language Model is Secretly Optimizing a Preference Graph (GraphDPO)** | https://arxiv.org/abs/2605.08037 | `Alignment`, `DPO`, `Preference Optimization` | 将DPO从成对比较推广到偏好有向图，通过Plackett-Luce图目标函数利用全排名信息，在推理与代码合成任务上超越标准DPO。 |
| 16 | **Learning Accurate Hierarchical Low-Rank Representations for LLM Fine-Tuning** | https://arxiv.org/abs/2605.07850 | `Fine-Tuning`, `LoRA`, `Low-Rank` | 提出层次化低秩表示学习方法，通过更精确的低秩分解结构提升LLM微调效率与最终性能。 |

---

## 🏷 LLM Safety / Behaviour / 安全与行为

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 17 | **Beyond "I cannot fulfill this request": Alleviating Rigid Rejection in LLMs via Label Enhancement** | https://arxiv.org/abs/2605.07883 | `Safety`, `Rejection`, `Label Enhancement` | 通过标签增强技术缓解LLM过度僵硬的拒绝行为，在保持安全性的同时显著减少误拒率。 |
| 18 | **How Value Induction Reshapes LLM Behaviour** | https://arxiv.org/abs/2605.07925 | `Behaviour`, `Values`, `Alignment` | 研究价值诱导（value induction）如何系统性地重塑LLM行为模式，揭示模型内部价值表示的形成与迁移机制。 |
| 19 | **Schema-Conditioned Classification for LLM Safeguard** | https://arxiv.org/abs/2605.07982 | `Safety`, `Classification`, `Safeguard` | 基于schema条件化分类的LLM安全防护方法，通过结构化模式约束提升有害内容检测的精确度与泛化性。 |
| 20 | **Evaluation Awareness in Language Models Has Limited Effect on Behaviour** | https://arxiv.org/abs/2605.05835 | `Safety`, `Evaluation Awareness`, `CoT` | 大规模实验表明LRM在CoT中表达的"评估意识"对实际行为影响极小（ω≤0.06），呼吁重新审视VEA作为策略行为证据的解读。 |

---

## 🏷 Architecture / 模型架构

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 21 | **Cola DLM: Continuous Latent Diffusion Language Model** | https://arxiv.org/abs/2605.06548 | `Language Model`, `Diffusion`, `Non-Autoregressive` | 提出层次化连续潜空间扩散语言模型Cola DLM，在2B参数规模上验证非自回归文本生成的强扩展性，为多模态统一建模开辟路径。 |

---

## 🏷 Mechanistic Interpretability / 机制可解释性

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 22 | **Mechanistic Interpretability Must Disclose Identification Assumptions for Causal Claims** | https://arxiv.org/abs/2605.08012 | `Mech-Interp`, `Causal Claims`, `Position Paper` | 指出当前mechanistic interpretability论文普遍缺乏因果识别假设披露，提出"验证≠识别"的规范，推动领域向更严谨因果推断转型。 |

---

## 📊 本周趋势速览

- **Agent本周爆发**：5月8日arXiv出现多篇Agent核心论文（CLI Agents、Cooperative Intent、Agentic Discovery），显示Agent研究正从框架层向深层行为机制、协作动力学演进。
- **推理可靠性受关注**：Conformal Path Reasoning、Rubric-Grounded RL、Confidence-Informed Self-Consistency 三篇从校准、奖励设计、解码策略三个维度提升推理可信度。
- **多模态RAG暴露新风险**："recorruption"现象的发现提醒我们，RAG在VLM中的引入可能反而破坏原本正确的视觉判断。
- **GraphDPO扩展对齐范式**：将偏好建模从pairwise推向graph-structured，是对DPO家族的重要扩展。
- **Hugging Face本周热模**：DeepSeek-V4-Pro/Flash、Qwen3.6-35B-A3B、GLM-5.1持续领跑；Gemma-4-31B-it下载量突破747万，巩固开源多模态标杆地位。
- **PaperWeekly/AnalyticsVidhya 精选**：AI Co-Mathematician 和 Cola DLM 被多家媒体列为2026年度Top LLM论文候选。

---

*Generated by 周二论文雷达 | 2026-W20 | May 12, 2026*
