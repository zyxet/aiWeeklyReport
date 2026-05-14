# 2026-W20 论文精选短名单

> **周号**: 2026-W20（2026年5月12日–5月14日）
> **评选日期**: 2026-05-14
> **候选池规模**: 22篇
> **入选数量**: 8篇
> **评选标准**: 创新性(5)、实用性(5)、技术深度(5)、机构背书(5)、代码可得性(5)，总分25分

---

## 🏆 TOP 8 精选论文

### 1. Compiling LLM Reasoning into Symbolic Solvers for Efficient Program Synthesis (★23分)

| 项目 | 内容 |
|------|------|
| **arXiv** | 2605.05485 |
| **标题** | Compiling LLM Reasoning into Symbolic Solvers for Efficient Program Synthesis |
| **作者** | Atharva Naik, et al. |
| **机构** | 待确认（独立研究团队） |
| **一句话摘要** | 将LLM推理轨迹编译为可复用符号求解器，PBEBench-Hard上以零LLM推理成本超越测试时缩放16.3个百分点。 |
| **代码** | ✅ 官方开源 |
| **开源池关联** | - |

**评分详情**:
| 维度 | 得分 | 理由 |
|------|------|------|
| 创新性 | 5 | 全新范式：推理→符号求解器编译，neuro-symbolic新路径 |
| 实用性 | 5 | 零LLM推理成本，token使用减少78%，Pareto效率显著提升 |
| 技术深度 | 5 | DSL约束+求解器归纳，理论框架完整，跨领域迁移验证 |
| 机构背书 | 3 | 独立研究团队 |
| 代码可得性 | 5 | 明确发布代码和数据 |

---

### 2. AI Co-Mathematician: Accelerating Mathematicians with Agentic AI (★22分)

| 项目 | 内容 |
|------|------|
| **arXiv** | 2605.06651 |
| **标题** | AI Co-Mathematician: Accelerating Mathematicians with Agentic AI |
| **作者** | Daniel Zheng, Ingrid von Glehn, Yori Zwols, Iuliya Beloshapka, Lars Buesing, Daniel M. Roy, Martin Wattenberg, Bogdan Georgiev, Tatiana Schmidt, Andrew Cowie, Fernanda Viegas, Dimitri Kanevsky, Vineet Kahlon, Hartmut Maennel, Sophia Alj, George Holland, Alex Davies, Pushmeet Kohli |
| **机构** | Google DeepMind |
| **一句话摘要** | DeepMind推出的AI数学协作者工作台，通过并行Agent实现文献检索、定理证明与开放问题探索，FrontierMath Tier 4取得48%新高。 |
| **代码** | ⏳ 承诺开源（Code and data will be publicly released） |
| **开源池关联** | - |

**评分详情**:
| 维度 | 得分 | 理由 |
|------|------|------|
| 创新性 | 5 | 全新AI数学研究范式，异步状态化工作空间管理不确定性 |
| 实用性 | 4 | 面向数学研究 niche 领域，但方法可迁移 |
| 技术深度 | 5 | FrontierMath Tier 4新SOTA，多Agent协作机制 |
| 机构背书 | 5 | Google DeepMind |
| 代码可得性 | 3 | 承诺发布但尚未确认 |

---

### 3. Agentic Discovery for Test-Time Scaling (★21分)

| 项目 | 内容 |
|------|------|
| **arXiv** | 2605.08083 |
| **标题** | Agentic Discovery for Test-Time Scaling |
| **作者** | Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang |
| **机构** | 待确认（含Heng Huang，可能是UMD相关） |
| **一句话摘要** | 提出AutoTTS环境驱动框架，让Agent自动发现测试时推理策略，成本仅$39.9/160分钟，泛化到held-out基准。 |
| **代码** | ⏳ 承诺开源（data and code will be open-source） |
| **开源池关联** | - |

**评分详情**:
| 维度 | 得分 | 理由 |
|------|------|------|
| 创新性 | 5 | 从手工设计TTS到自动发现，环境构建新思路 |
| 实用性 | 5 | 极低发现成本（$39.9），策略可泛化 |
| 技术深度 | 4 | 控制器合成+beta参数化，理论较完整 |
| 机构背书 | 3 | 未明确顶级机构 |
| 代码可得性 | 4 | 明确承诺开源 |

---

### 4. Learning Accurate Hierarchical Low-Rank Representations for LLM Fine-Tuning (★21分)

| 项目 | 内容 |
|------|------|
| **arXiv** | 2605.07850 |
| **标题** | Learning Accurate Hierarchical Low-Rank Representations for LLM Fine-Tuning |
| **作者** | Ionut-Vlad Modoranu, et al. |
| **机构** | 待确认 |
| **一句话摘要** | MatryoshkaLoRA层次化低秩表示框架，通过固定对角矩阵P实现子秩动态缩放，支持任意秩选择且精度损失最小。 |
| **代码** | ✅ 官方开源 |
| **开源池关联** | - |

**评分详情**:
| 维度 | 得分 | 理由 |
|------|------|------|
| 创新性 | 4 | Matryoshka-inspired层次化LoRA，统一框架覆盖LoRA/DyLoRA |
| 实用性 | 5 | 动态秩选择，无需网格搜索，直接提升微调效率 |
| 技术深度 | 4 | AURAC新评估指标，低秩分解优化 |
| 机构背书 | 3 | 未明确顶级机构 |
| 代码可得性 | 5 | 代码已开源 |

---

### 5. GLiGuard: Schema-Conditioned Classification for LLM Safeguard (★21分)

| 项目 | 内容 |
|------|------|
| **arXiv** | 2605.07982 |
| **标题** | Schema-Conditioned Classification for LLM Safeguard |
| **作者** | Urchade Zaratiana, et al. |
| **机构** | 待确认 |
| **一句话摘要** | 0.3B参数schema条件化双向编码器GLiGuard，单次前向同时评估9个安全维度，F1媲美7B-27B解码器，吞吐量高16倍。 |
| **代码** | ✅ 官方开源（Code and models available） |
| **开源池关联** | - |

**评分详情**:
| 维度 | 得分 | 理由 |
|------|------|------|
| 创新性 | 4 | 将分类问题从自回归解码器重构为双向编码器，schema条件化 |
| 实用性 | 5 | 23-90x更小模型，16x吞吐量，17x低延迟，生产部署友好 |
| 技术深度 | 4 | GLiNER2适配，结构化token schema编码 |
| 机构背书 | 3 | 未明确顶级机构 |
| 代码可得性 | 5 | 代码+模型均开源 |

---

### 6. AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop RAG (★20分)

| 项目 | 内容 |
|------|------|
| **arXiv** | 2605.05245 |
| **标题** | AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop RAG |
| **作者** | Yilin Guo, et al. |
| **机构** | 待确认 |
| **一句话摘要** | 多跳RAG的token高效证据组装方法，通过显式gap追踪与微查询生成，在冗余注入条件下以2.6倍更少token达到最优证据F1。 |
| **代码** | ✅ 官方开源 |
| **开源池关联** | - |

**评分详情**:
| 维度 | 得分 | 理由 |
|------|------|------|
| 创新性 | 4 | gap-aware repair+token约束，训练-free证据控制器 |
| 实用性 | 5 | 直接面向RAG部署场景，token效率至关重要 |
| 技术深度 | 4 | 多维度选择机制平衡gap覆盖/冗余/相关性 |
| 机构背书 | 3 | 未明确顶级机构 |
| 代码可得性 | 4 | 代码和评估pipeline开源 |

---

### 7. Ask Early, Ask Late, Ask Right: When Does Clarification Timing Matter for Long-Horizon Agents? (★20分)

| 项目 | 内容 |
|------|------|
| **arXiv** | 2605.07937 |
| **标题** | Ask Early, Ask Late, Ask Right: When Does Clarification Timing Matter for Long-Horizon Agents? |
| **作者** | Anmol Gulati, et al. |
| **机构** | Google（Anmol Gulati为Google研究员） |
| **一句话摘要** | 系统研究长程Agent澄清请求的最佳时机，发现goal澄清在10%执行后失效而input澄清保留至50%，为澄清策略提供量化基础。 |
| **代码** | ⏳ 承诺开源（Code and data will be publicly released） |
| **开源池关联** | - |

**评分详情**:
| 维度 | 得分 | 理由 |
|------|------|------|
| 创新性 | 4 | 首个澄清时机量化研究，反直觉发现 |
| 实用性 | 4 | 对Agent设计有直接指导，建立设计目标 |
| 技术深度 | 5 | 84任务变体，6000+ runs，Kendall tau跨模型验证 |
| 机构背书 | 4 | Google |
| 代码可得性 | 3 | 承诺发布 |

---

### 8. Tool Calling is Linearly Readable and Steerable in Language Models (★20分)

| 项目 | 内容 |
|------|------|
| **arXiv** | 2605.07990 |
| **标题** | Tool Calling is Linearly Readable and Steerable in Language Models |
| **作者** | Zekun Wu, Ze Wang, Seonglae Cho, Yufei Yang, Adriano Koshiyama, Sahan Bulathwela, Maria Perez-Ortiz |
| **机构** | University College London, Holistic AI, Imperial College London |
| **一句话摘要** | 机制可解释性证明工具调用能力在LLM内部线性可读且可操控，通过激活差异切换工具选择达93-100%准确率，可提前标记错误调用。 |
| **代码** | ❌ 未明确开源 |
| **开源池关联** | - |

**评分详情**:
| 维度 | 得分 | 理由 |
|------|------|------|
| 创新性 | 5 | 首个工具调用机制可解释性系统分析，线性可读+可操控 |
| 实用性 | 4 | 为工具调用安全/纠错提供理论基础 |
| 技术深度 | 5 | 12模型270M-27B，注意力头定位，因果效应分析 |
| 机构背书 | 4 | UCL + Imperial College London |
| 代码可得性 | 2 | 未提及代码开源 |

---

## 📊 评分总览

| 排名 | arXiv | 标题 | 总分 | 代码 |
|------|-------|------|------|------|
| 1 | 2605.05485 | Compiling LLM Reasoning into Symbolic Solvers | **23** | ✅ |
| 2 | 2605.06651 | AI Co-Mathematician | **22** | ⏳ |
| 3 | 2605.08083 | Agentic Discovery for Test-Time Scaling | **21** | ⏳ |
| 4 | 2605.07850 | MatryoshkaLoRA | **21** | ✅ |
| 5 | 2605.07982 | GLiGuard | **21** | ✅ |
| 6 | 2605.05245 | AdaGATE | **20** | ✅ |
| 7 | 2605.07937 | Ask Early, Ask Late, Ask Right | **20** | ⏳ |
| 8 | 2605.07990 | Tool Calling is Linearly Readable | **20** | ❌ |

---

## 🔗 开源池关联

本周开源候选池（11个项目）与精选论文无直接"论文+代码"双料匹配。但以下论文已确认或承诺开源代码：

| 论文 | 代码状态 | 备注 |
|------|----------|------|
| Compiling LLM Reasoning (2605.05485) | ✅ 已开源 | 代码+数据 |
| MatryoshkaLoRA (2605.07850) | ✅ 已开源 | 代码 |
| GLiGuard (2605.07982) | ✅ 已开源 | 代码+模型 |
| AdaGATE (2605.05245) | ✅ 已开源 | 代码+评估pipeline |
| AI Co-Mathematician (2605.06651) | ⏳ 承诺发布 | DeepMind承诺公开 |
| Agentic Discovery (2605.08083) | ⏳ 承诺发布 | 明确说将开源 |
| Ask Early, Ask Late (2605.07937) | ⏳ 承诺发布 | Google承诺公开 |

---

## 📝 淘汰论文（14篇）

以下论文因总分较低或主题重叠未入选：

| arXiv | 标题 | 总分 | 淘汰原因 |
|-------|------|------|----------|
| 2605.05594 | The Cost of Context: Mitigating Textual Bias in Multimodal RAG | 19 | 技术深度高，但RAG领域已有AdaGATE入选 |
| 2605.08037 | GraphDPO | 19 | DPO扩展有价值，但技术深度稍逊 |
| 2605.08060 | How Expanded Recall Erodes Cooperative Intent | 18 | 反直觉发现有趣，但实用性有限 |
| 2605.08061 | Rubric-Grounded RL | 18 | 结构化奖励有价值，但领域较窄 |
| 2605.05758 | BioTool Dataset | 18 | 领域特定（生物医学），偏离通用AI主线 |
| 2605.06548 | Cola DLM | 18 | 非自回归架构创新，但实用性待验证 |
| 2605.08077 | Conformal Path Reasoning | 16 | KGQA niche，覆盖面有限 |
| 2605.07883 | LANCE: Alleviating Rigid Rejection | 16 | 安全领域有价值，但技术深度一般 |
| 2605.08070 | VecCISC | 15 | 工程优化为主，创新度有限 |
| 2605.08011 | Abductive Reasoning with Probabilistic Commonsense | 15 | 理论贡献为主，应用范围窄 |
| 2605.08013 | Learning CLI Agents | 17 | CLI Agent有价值，但机构背书弱 |
| 2605.07925 | How Value Induction Reshapes LLM Behaviour | 13 | 理论探索，实用性低 |
| 2605.05835 | Evaluation Awareness in Language Models | 13 | 评估意识影响有限，偏安全小众 |
| 2605.08012 | Mechanistic Interpretability Must Disclose | 12 | Position paper，无代码，技术深度有限 |

---

## 💡 本周趋势洞察

1. **Neuro-Symbolic回归**：Compiling LLM Reasoning以23分夺冠，将LLM推理编译为符号求解器的范式可能标志neuro-symbolic方向的复兴。

2. **Agent研究深化**：入选3篇Agent论文（AI Co-Mathematician、Agentic Discovery、Ask Early Ask Late），覆盖数学协作、推理策略发现、澄清时机，显示Agent从框架层向机制深化。

3. **效率与安全并重**：MatryoshkaLoRA（动态低秩）和GLiGuard（0.3B安全模型）均聚焦效率提升，反映AI部署成本敏感期的研究转向。

4. **机制可解释性突破**：Tool Calling线性可读论文首次系统证明工具调用能力的内部可操控性，为AI安全提供了新的干预靶点。

5. **开源率保持高位**：8篇入选论文中4篇已确认开源，3篇承诺开源，仅1篇无代码，开源生态持续完善。

---

*本文件由 Kimi Claw 自动生成，数据来源：arXiv API + kimi_fetch 混合采集*
