# 🏆 本周论文精选短名单（W30, 2026-07-15 ~ 2026-07-21）

> 从14篇候选论文中按评估打分表筛选，保留总分≥22分的8篇。
> 评估维度：创新性(5) × 技术深度(5) × 实用价值(5) × 实验验证(5) × 影响力潜力(5) = 总分25

---

## 1. Understanding Reasoning from Pretraining to Post-Training ⭐ TOP1

- **arXiv**: https://arxiv.org/abs/2607.16097
- **标签**: LLM, Reasoning, RL, Pretraining, Chess, Scaling Law
- **中文摘要**: 以国际象棋为受控平台，首次量化证明预训练损失可预测RL后训练性能，且RL能在难题上发现SFT中几乎不存在的正确策略。
- **评分**: 24/25 | 创新5 深度5 实用4 实验5 影响5
- **一句话亮点**: 预训练到RL的接口终于被定量刻画了。
- **开源代码**: 未明确标注

---

## 2. Harmful Chain-of-Thought Transfers: From Trace Transplantation to Distilled Jailbreaks ⭐ TOP2

- **arXiv**: https://arxiv.org/abs/2607.15286
- **标签**: LLM, Chain-of-Thought, Safety, Jailbreak, Reasoning
- **中文摘要**: 有害CoT推理痕迹可跨模型转移，开源模型受害率超80%，蒸馏为系统提示后GPT-4.1上提升10倍，揭示推理层安全的紧迫性。
- **评分**: 24/25 | 创新5 深度4 实用5 实验5 影响5
- **一句话亮点**: 推理过程本身成了攻击向量——这是安全领域的新边疆。
- **开源代码**: 未明确标注

---

## 3. ActiveVision: A Benchmark for Active Visual Observation in Multimodal LLMs

- **arXiv**: https://arxiv.org/abs/2607.16165
- **标签**: MLLM, Multimodal, Benchmark, Active Observation, VLM
- **中文摘要**: 构建首个MLLM主动视觉观察基准，GPT-5.5仅解决10.6%而人类达96.1%，暴露感知-推理闭环的系统性缺口。
- **评分**: 23/25 | 创新5 深度4 实用4 实验5 影响5
- **一句话亮点**: 当前最强的多模态模型在"会看"这件事上，连人类的尾灯都看不到。
- **开源代码**: 未明确标注

---

## 4. AI Watermark Evidence Fails Forensic Readiness: An Empirical Evaluation

- **arXiv**: https://arxiv.org/abs/2607.16010
- **标签**: LLM, Watermark, Security, Forensics, Safety
- **中文摘要**: 首次以法庭取证标准评估LLM水印，发现语义保留改写后KGW和Unigram水印100%丢失，且不满足Daubert科学证据标准。
- **评分**: 23/25 | 创新4 深度4 实用5 实验5 影响5
- **一句话亮点**: 监管者以为水印能当法庭证据——这篇论文用846次实验告诉他们想多了。
- **开源代码**: 未明确标注

---

## 5. SciForge: An AI-Native, Multimodal Workbench for Scientific Discovery 🧪 论文+代码

- **arXiv**: https://arxiv.org/abs/2607.16038
- **标签**: Multimodal, AI Agent, Scientific Discovery, Workbench
- **中文摘要**: 首个AI原生多模态科研工作台，整合论文/代码/数据集/模型输出等异构工件为可审计研究状态，已开源。
- **评分**: 22/25 | 创新4 深度4 实用5 实验4 影响5
- **一句话亮点**: 科学发现需要的不是聊天机器人，而是一个能保留证据链的工作台。
- **开源代码**: ✅ 开源，系统已发布

---

## 6. Model Merging Matches Joint RL on AppWorld: Task Geometry Explains Why 🧪 论文+代码

- **arXiv**: https://arxiv.org/abs/2607.16062
- **标签**: LLM, Model Merging, RL, Agent, AppWorld
- **中文摘要**: 模型合并在AppWorld上统计显著地匹敌联合RL训练，因任务向量接近正交使合并退化为均匀平均，揭示了合并方法在此场景下不重要的几何原因。
- **评分**: 22/25 | 创新4 深度5 实用4 实验5 影响4
- **一句话亮点**: 你以为合并方法很重要？不，是任务几何说了算。
- **开源代码**: ✅ 已发布全部代码和统计数据

---

## 7. ContinuityBench: A Benchmark and Systems Study of Stateful Failover in Multi-Provider LLM Routing 🧪 论文+代码

- **arXiv**: https://arxiv.org/abs/2607.15899
- **标签**: LLM, System, Multi-Provider, Production, Failover
- **中文摘要**: 生产LLM部署中有状态故障转移基准，标准无状态故障转移连续性保持率接近0%，有状态代理可达99.20%。
- **评分**: 22/25 | 创新4 深度4 实用5 实验5 影响4
- **一句话亮点**: 你的多模型部署"可用"不等于"能用"——对话连续性才是隐形杀手。
- **开源代码**: ✅ 已发布 continuity-bench 评估框架

---

## 8. PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization

- **arXiv**: https://arxiv.org/abs/2607.16184
- **标签**: LLM, MoE, Quantization, Serving, Efficiency
- **中文摘要**: MoE服务新方案，动态量化专家权重并平衡KV缓存，实现FP16等效精度下72% GPU内存节省和1.94倍吞吐提升。
- **评分**: 21/25 | 创新4 深度4 实用5 实验4 影响4
- **一句话亮点**: MoE的内存和吞吐_tradeoff_终于被系统性地解开了。
- **开源代码**: 未明确标注

---

## 被筛除论文（总分≤21，供参考）

| 论文 | 总分 | 筛除原因 |
|------|------|----------|
| CRAFT (2607.16122) | 21 | 评估方法扎实但不如Top8突破性 |
| The Honest Quorum Problem (2607.16109) | 21 | 理论深刻但实验偏少，Agent基础设施尚未成熟 |
| FedGAMMA (2607.15687) | 19 | 联邦多模态图学习，场景较专业 |
| DADiff (2607.16090) | 19 | 扩散RL域适应，有代码但领域较窄 |
| CoWeaver (2607.15545) | 16 | 人机匹配引擎，创新性有限 |
| ICL with Linear Self-Attention (2607.15819) | 16 | 理论贡献为主，实验规模小 |

---

> 短名单生成时间: 2026-07-23 14:00 CST
> 筛选标准: 总分≥22分，优先保留论文+代码双料项目
> 下一步: 周五将本短名单与开源项目联动，生成本周最终周报
