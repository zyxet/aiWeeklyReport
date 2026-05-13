# 📄 本周精选论文短名单（2026-W20）

> 筛选时间：2026-05-13 | 来源：paper-pool-2026-W20.md（22篇候选）
> 评分标准：创新性/实用性/技术深度/机构背书/代码可得性，每项1-5分，满分25分
> 从 22 篇候选中精选 8 篇

---

## 🏆 第1名：AI Co-Mathematician: Accelerating Mathematicians with Agentic AI
**总分：22/25** | 机构：DeepMind | arXiv: 2605.06651

| 维度 | 得分 | 说明 |
|------|------|------|
| 创新性 | 5 | 并行Agent架构定义"AI数学协作者"新范式 |
| 实用性 | 4 | FrontierMath Tier 4 取得48%新高，但场景限于数学 |
| 技术深度 | 5 | 多Agent协作机制设计扎实，实验覆盖完整 |
| 机构背书 | 5 | DeepMind |
| 代码可得性 | 3 | 未明确开源承诺，但DeepMind历史开源率较高 |

**入选理由**：DeepMind推出的AI数学协作者工作台，通过并行Agent实现文献检索、定理证明与开放问题探索。在FrontierMath Tier 4上取得48%的新高分数，是AI Agent在高端认知任务上的里程碑。多Agent分工（检索→证明→探索）为其他深度推理领域提供了架构参考。
**一句话摘要**：DeepMind通过并行Agent协作打造AI数学工作台，在顶级数学基准上刷新纪录，定义了深度推理Agent的架构范式。

---

## 🏆 第2名：Compiling LLM Reasoning into Symbolic Solvers for Efficient Program Synthesis
**总分：22/25** | arXiv: 2605.05485

| 维度 | 得分 | 说明 |
|------|------|------|
| 创新性 | 5 | 首次将LLM推理轨迹编译为可复用符号求解器，Neuro-symbolic新路径 |
| 实用性 | 5 | PBEBench-Hard上零LLM推理成本超越测试时缩放16.3个百分点 |
| 技术深度 | 5 | 理论框架完整，编译过程形式化，实验对比充分 |
| 机构背书 | 3 | 待查 |
| 代码可得性 | 4 | 方法本身产生可执行符号求解器，工程化程度高 |

**入选理由**：核心突破在于"把LLM的思考过程编译成传统符号程序"——既保留了LLM的灵活性，又获得了符号执行的确定性和零边际成本。这是对"测试时计算 scaling"路线的直接挑战：与其让LLM推理时想更多，不如一次性编译成可复用的求解器。
**一句话摘要**：将LLM推理轨迹编译为可复用符号求解器，在程序合成任务上实现零LLM推理成本且超越测试时缩放方法16.3%。

---

## 🏆 第3名：Agentic Discovery for Test-Time Scaling
**总分：20/25** | arXiv: 2605.08083

| 维度 | 得分 | 说明 |
|------|------|------|
| 创新性 | 5 | 让Agent在推理时主动发现知识并动态扩展上下文，新范式 |
| 实用性 | 5 | 无需预训练增强，直接提升测试时推理能力 |
| 技术深度 | 4 | 框架清晰，但实验规模待验证 |
| 机构背书 | 3 | 待查 |
| 代码可得性 | 3 | 待验证 |

**入选理由**：测试时计算扩展（Test-Time Scaling）是当前最热的推理增强路线之一。本文提出让Agent在推理时"主动发现"而非"被动消耗"更多计算，是对 scaling 范式的认知升级——从"算更多"到"找更好的知识"。
**一句话摘要**：提出Agent在推理时主动发现知识并动态扩展上下文，实现无需预训练增强的测试时推理能力提升。

---

## 🏆 第4名：AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop RAG
**总分：20/25** | arXiv: 2605.05245

| 维度 | 得分 | 说明 |
|------|------|------|
| 创新性 | 4 | gap-aware + 微查询生成，解决多跳RAG的冗余问题 |
| 实用性 | 5 | Token效率对生产环境RAG极其关键，2.6倍token节省 |
| 技术深度 | 4 | 显式gap追踪机制设计精巧 |
| 机构背书 | 3 | 待查 |
| 代码可得性 | 4 | 方法可工程化复现 |

**入选理由**：多跳RAG的token效率是生产环境的硬约束。本文以2.6倍更少的token达到最优证据F1，且通过"gap追踪"让组装过程可解释。对于需要长上下文多步推理的企业RAG应用，这是可以直接落地的技术。
**一句话摘要**：通过显式gap追踪与微查询生成，在多跳RAG中以2.6倍更少token达到最优证据组装效果。

---

## 🏆 第5名：The Cost of Context: Mitigating Textual Bias in Multimodal RAG
**总分：20/25** | arXiv: 2605.05594

| 维度 | 得分 | 说明 |
|------|------|------|
| 创新性 | 5 | 首次揭示"recorruption"现象——文本引入反而破坏视觉判断 |
| 实用性 | 4 | BAIR无参数干预框架可直接用于现有VLM-RAG系统 |
| 技术深度 | 4 | 偏置分析+干预设计完整 |
| 机构背书 | 3 | 待查 |
| 代码可得性 | 4 | 无参数干预易于复现 |

**入选理由**：多模态RAG是当前热门架构，但本文揭示了反直觉的风险：引入外部文本可能让VLM放弃原本正确的视觉预测。BAIR框架无需训练即可恢复视觉显著性，对正在部署VLM-RAG的团队有直接警示价值。
**一句话摘要**：揭示多模态RAG中"recorruption"现象——引入外部文本反而导致模型放弃正确视觉预测，提出无参数干预框架恢复视觉显著性。

---

## 🏆 第6名：Tool Calling is Linearly Readable and Steerable in Language Models
**总分：20/25** | arXiv: 2605.07990

| 维度 | 得分 | 说明 |
|------|------|------|
| 创新性 | 5 | 机制可解释性层面的突破，证明工具调用是线性可读可操控的 |
| 实用性 | 4 | 为工具使用能力的定向激活/抑制提供理论基础 |
| 技术深度 | 5 | 线性可读性的形式化证明，Steerability的实验验证 |
| 机构背书 | 3 | 待查 |
| 代码可得性 | 3 | 分析方法可复现 |

**入选理由**：工具调用是Agent的核心能力，但"为什么LLM能调用工具"一直是个黑箱。本文从机制可解释性角度证明这一能力是线性可读且可操控的——意味着未来可以精准地增强或抑制特定工具使用能力，而不影响其他行为。这是Agent可控性的基础科学贡献。
**一句话摘要**：通过机制可解释性分析证明工具调用能力在LLM内部是线性可读且可操控的，为工具使用能力的定向激活/抑制提供理论基础。

---

## 🏆 第7名：Your Language Model is Secretly Optimizing a Preference Graph (GraphDPO)
**总分：20/25** | arXiv: 2605.08037

| 维度 | 得分 | 说明 |
|------|------|------|
| 创新性 | 5 | 将DPO从成对比较推广到偏好有向图，利用全排名信息 |
| 实用性 | 4 | 在推理与代码合成任务上超越标准DPO，对齐社区关注 |
| 技术深度 | 5 | Plackett-Luce图目标函数的理论推导扎实 |
| 机构背书 | 3 | 待查 |
| 代码可得性 | 3 | 待验证 |

**入选理由**：DPO是对齐领域的主流方法之一，但一直受限于pairwise比较的信息损失。GraphDPO将偏好建模从二元比较推向图结构，是对DPO家族的重要范式扩展。对于正在用DPO微调模型的团队，这提供了潜在的直接升级路径。
**一句话摘要**：将DPO从成对比较推广到偏好有向图，通过Plackett-Luce图目标函数利用全排名信息，在推理与代码合成上超越标准DPO。

---

## 🏆 第8名：Cola DLM: Continuous Latent Diffusion Language Model
**总分：19/25** | arXiv: 2605.06548

| 维度 | 得分 | 说明 |
|------|------|------|
| 创新性 | 5 | 层次化连续潜空间扩散语言模型，非自回归文本生成的新架构 |
| 实用性 | 3 | 2B参数验证阶段，多模态统一建模前景待验证 |
| 技术深度 | 5 | 连续潜空间+扩散+语言模型的融合设计复杂且完整 |
| 机构背书 | 3 | 被多家媒体列为2026年度Top LLM论文候选 |
| 代码可得性 | 3 | 待验证 |

**入选理由**：自回归架构统治LLM多年，但扩散模型在图像/音频领域的成功让人期待文本领域的突破。Cola DLM在2B参数上验证了非自回归文本生成的强扩展性，如果被证明可 scale 到更大模型，可能改变整个LLM的训练和推理范式。多家媒体已将其列为年度候选，值得长期跟踪。
**一句话摘要**：提出层次化连续潜空间扩散语言模型Cola DLM，在2B参数规模上验证非自回归文本生成的强扩展性，为多模态统一建模开辟路径。

---

## ❌ 淘汰论文说明

| 论文 | 得分 | 淘汰原因 |
|------|------|---------|
| Ask Early, Ask Late | 15/25 | 澄清时机研究有价值，但对Agent设计的影响偏间接 |
| Learning CLI Agents | 18/25 | 结构化credit分配实用，但论文池中有更重磅的Agent行为机制研究 |
| How Expanded Recall Erodes Cooperative Intent | 18/25 | 反直觉发现重要，但偏理论洞察，工程落地路径不清晰 |
| Conformal Path Reasoning | 17/25 | KGQA场景较窄，专业性过强 |
| Rubric-Grounded RL | 18/25 | 奖励设计改进有价值，但与其他推理可靠性论文相比差异化不足 |
| Confidence-Informed Self-Consistency | 15/25 | 改进现有方法，创新性不足 |
| Abductive Reasoning with Probabilistic Commonsense | 13/25 | 偏学术探讨，工程价值有限 |
| A Comprehensive Tool-Calling Dataset for Biomedical | 18/25 | **按排除标准剔除**：纯生物医学场景，偏离核心AI/Agent主线 |
| Learning Accurate Hierarchical Low-Rank Representations | 16/25 | LoRA改进，创新性一般 |
| Beyond "I cannot fulfill this request" | 16/25 | 标签增强技术有用，但属渐进式改进 |
| How Value Induction Reshapes LLM Behaviour | 15/25 | 偏理论，对工程实践指导有限 |
| Schema-Conditioned Classification for LLM Safeguard | 15/25 | 安全防护方法，场景较窄 |
| Evaluation Awareness in Language Models | 15/25 | 重要发现但偏分析，缺乏直接工程应用 |
| Mech-Interp Must Disclose Identification Assumptions | 14/25 | 方法论立场论文，非技术突破 |

---

## 📊 本周趋势判断（基于短名单）

1. **Agent深层行为机制受关注**：短名单3篇Agent论文分别覆盖测试时扩展、多Agent协作、工具调用可解释性——Agent研究正从"搭框架"进入"理解内在机制"阶段。
2. **推理可靠性是多线并进**：符号编译（零成本推理）、保形预测（置信度保证）、Rubric奖励（减少hacking）三条路线同时推进，说明社区对"LLM推理不可信"的焦虑在加剧。
3. **RAG进入精细优化期**：AdaGATE的token效率、多模态RAG的recorruption风险，说明RAG不再是"能跑就行"，而是追求效率和正确性的精细化阶段。
4. **对齐范式扩展**：GraphDPO将偏好学习从pairwise推向graph-structured，是对DPO家族的重要扩展。
5. **架构创新冒头**：Cola DLM作为非自回归架构的代表，虽处早期但值得长期跟踪——如果scale成功，可能动摇Transformer的自垄断地位。

---

*--- 短名单结束 | W20 共 8 篇论文入选 ---*
*下次更新：周四 14:00 论文精选 → 周五 19:00 论文-开源联动*
