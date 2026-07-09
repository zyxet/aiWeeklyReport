# 📄 本周论文精选短名单（2026-W28）

> 筛选日期：2026-07-09（周四）
> 来源：paper-pool-2026-W28.md（24篇候选）
> 保留：8篇（总分排序 + 领域多样性）
> 标记 🛠️ 为论文+代码双料项目

---

## 1. HOLA: A Hippocampus for Linear Attention ⭐25/25

- **链接**: https://arxiv.org/abs/2607.02303
- **标签**: RAG, LLM, Long Context, Architecture
- **中文摘要**: 受互补学习系统启发，为线性注意力添加有界精确KV缓存，形成半参数化测试时记忆，340M参数在Wikitext上困惑度从27.32降至22.92。
- **评分**: 创新性5 | 技术深度5 | 实用价值5 | 实验质量5 | 影响力潜力5
- **开源代码**: 未明确提及

> **入选理由**: 线性注意力模型的长期痛点是前缀压缩导致信息丢失，HOLA 用神经科学启发的双系统架构给出了优雅的工程解法。32k needle recall 大幅优于基线，且参数量极小（340M），验证成本低，是长上下文架构方向的重要突破。

---

## 2. DecompRL: Decomposing Code Problems via RL for LLM Reasoning ⭐25/25 🛠️

- **链接**: https://arxiv.org/abs/2607.02390
- **标签**: LLM, Reasoning, Tool/Planning, RL
- **中文摘要**: 通过强化学习将代码问题分解为独立子函数，k个模块可组合成k^n候选解，GPU token成本降低约50倍，在LiveCodeBench和CodeContests上超越标准基线。
- **评分**: 创新性5 | 技术深度5 | 实用价值5 | 实验质量5 | 影响力潜力5
- **开源代码**: 提及在LiveCodeBench和CodeContests上评估，代码未明确标注

> **入选理由**: 将组合爆炸从GPU推理转移到廉价CPU评估，这是测试时计算扩展的核心瓶颈问题。50倍成本降低和超越基线的性能，意味着对代码生成和推理任务都有范式级影响。

---

## 3. PAW: Program-as-Weights for Fuzzy-Function Programming ⭐24/25 🛠️

- **链接**: https://arxiv.org/abs/2607.02512
- **标签**: LLM, Tool, Program
- **中文摘要**: 提出Program-as-Weights框架，将模糊函数编程编译为4B参数小型语言模型的权重，0.6B解释器执行PAW程序可匹配Qwen3-32B直接提示性能，推理内存仅1/50。
- **评分**: 创新性5 | 技术深度5 | 实用价值5 | 实验质量4 | 影响力潜力5
- **开源代码**: 发布FuzzyBench（10M-example数据集）

> **入选理由**: 将LLM从"每输入求解器"重构为"工具构建器"，用离线编译换取在线效率。4B编译器→0.6B解释器的架构设计极具工程美感，对边缘部署和API成本敏感场景有直接影响。

---

## 4. Autonomous Research Agents in Condensed Matter Physics ⭐24/25

- **链接**: https://arxiv.org/abs/2607.02329
- **标签**: Agent, LLM, Scientific AI
- **中文摘要**: 端到端自主研究智能体管道，从11,083篇凝聚态物理论文中自主构思方向、复现文献方法、进行第一性原理计算并撰写论文，通过新鲜上下文隔离和对抗性审查实现容错。
- **评分**: 创新性5 | 技术深度5 | 实用价值5 | 实验质量4 | 影响力潜力5
- **开源代码**: 未明确提及

> **入选理由**: 科学AI的里程碑工作。不同于ML沙箱中的自动化，该工作在物理推理、工具链复现和文献锚定三个维度展示了真正的端到端自主研究。47次会话、2,162次文献查询的量化数据令人印象深刻。

---

## 5. LACUNA: Parameter-Level Localization for LLM Unlearning ⭐23/25 🛠️

- **链接**: https://arxiv.org/abs/2607.02513
- **标签**: LLM, Privacy, Alignment
- **中文摘要**: 首个支持参数级定位的LLM遗忘测试平台，将合成PII注入预定义参数直接评估遗忘方法是否真正擦除知识，发现现有方法输出级表现好但参数级精度差，易受攻击复现。
- **评分**: 创新性5 | 技术深度5 | 实用价值4 | 实验质量5 | 影响力潜力4
- **开源代码**: 发布LACUNA测试平台

> **入选理由**: 遗忘学习的关键盲区终于被揭露：输出层表现≠参数层擦除。LACUNA 提供了 ground-truth 的评估基础设施，这对隐私合规和模型安全领域至关重要。发现现有方法易受resurfacing攻击，有实际安全意义。

---

## 6. CheckRLM: Retrieval-Augmented Generation for Reasoning Language Models ⭐22/25 🛠️

- **链接**: https://arxiv.org/abs/2607.02262
- **标签**: RAG, Reasoning, LLM
- **中文摘要**: 为推理语言模型提出CheckRLM框架，从推理链中提取事实声明及时检查知识不一致，利用外部知识进行最小成本精确修正，显著减轻长程推理中的错误累积。
- **评分**: 创新性4 | 技术深度5 | 实用价值5 | 实验质量4 | 影响力潜力4
- **开源代码**: 代码和数据已公开（https URL）

> **入选理由**: RAG与推理链的结合是当前热点，CheckRLM 的"及时检查+最小成本修正"设计精确命中了长程推理的痛点。错误累积是推理模型不可用的主要原因，该框架有明确的工程落地价值。

---

## 7. HaloGuard 1.0: Constitutional Classifier for Input Safety ⭐22/25 🛠️

- **链接**: https://arxiv.org/abs/2607.02079
- **标签**: LLM, Alignment, Safety
- **中文摘要**: 开源宪法分类器实现，基于46条政策和2,940子类别生成合成数据，0.8B模型在7个提示安全基准上达到平均F1 90.9，超越参数大30倍的基线模型，46语言覆盖。
- **评分**: 创新性4 | 技术深度4 | 实用价值5 | 实验质量4 | 影响力潜力5
- **开源代码**: 开源权重模型发布

> **入选理由**: 小模型（0.8B）打败大30倍的guard模型，F1 90.9 且 FPR 仅4.3，说明安全不是参数量的函数而是数据工程的函数。46语言覆盖和持续对抗性红队测试，使其成为生产环境可用的安全基础设施。

---

## 8. Steerability via Constraints: A Substrate for Scalable Oversight of Coding Agents ⭐22/25

- **链接**: https://arxiv.org/abs/2607.02389
- **标签**: Agent, Tool/Planning, Security
- **中文摘要**: 提出通过访问控制、网络策略、编码规范等约束实现编码智能体的可扩展监督，小模型（Gemma 4B）审查代码后门检测召回率从54.5%提升至90.9%。
- **评分**: 创新性4 | 技术深度5 | 实用价值5 | 实验质量4 | 影响力潜力4
- **开源代码**: 未明确提及

> **入选理由**: 编码智能体的安全监督是落地前的必答题。该工作将"可扩展监督"从理论框架转化为工程约束系统，用4B小模型实现90.9%的后门检测召回率，证明约束驱动的监督比模型规模驱动的监督更可靠。

---

## 落选但值得关注的论文

| 论文 | 总分 | 落选原因 |
|------|------|----------|
| VRRL: Visually-Grounded RL Reflection | 21 | 多模态方向竞争激烈，实验场景较窄 |
| Memory Contracts for Long-Horizon LLM Agents | 21 | 方法论有价值，但游戏场景验证受限 |
| PMI-OPSD: Long-CoT Self-Distillation | 21 | 技术深度高，但受众较窄（长CoT模型） |
| Neuron-OPSD: Annotation-Free Self-Distillation | 21 | 与PMI-OPSD方向重叠，优先级略低 |
| UA-ChatDev: Uncertainty-Aware Multi-Agent Dev | 21 | 多智能体软件开发方向已有较多工作 |
| DRIFTLENS: Memory-Induced Reasoning Drift | 20 | 发现重要但缓解方案效果有限 |
| SpeechCombine: Speech LLM Without Instruction Tuning | 21 | 语音方向偏离本周核心关注 |
| Bias-Aware LLM-as-a-Judge | 19 | 评估方法论文，实用性受限 |

---

## 领域分布

- **Agent / 智能体**: 2篇（Autonomous Research, Steerability）
- **Architecture / 架构**: 1篇（HOLA）
- **Code / 代码生成**: 1篇（DecompRL）
- **Safety / 安全**: 2篇（LACUNA, HaloGuard）
- **RAG / 检索增强**: 1篇（CheckRLM）
- **Tool / 工具**: 1篇（PAW）

---

*生成时间: 2026-07-09 14:00 CST | 任务: thursday-paper-filter | 前置任务: wednesday-filter ✅*
