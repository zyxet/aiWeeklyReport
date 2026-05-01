# Paper Pool 2026-W18 (2026-04-28 ~ 2026-05-01)

> 来源：arXiv cs.CL / cs.LG / cs.AI recent (764 entries scanned)  
> 筛选关键词：LLM, Agent, Multi-Agent, RAG, Reasoning, Long Context, Prompt, Chain-of-Thought, 智能体, 大模型  
> 排除：纯医学AI、纯CV（保留VLM）  
> 生成时间：2026-05-01

---

## 精选论文列表

### Agent / Multi-Agent

- **Exploration Hacking: Can LLMs Learn to Resist RL Training?** | [arXiv:2604.28182](https://arxiv.org/abs/2604.28182) | `LLM` `RL` `Agent` `Reasoning` | 研究发现能力较强的LLM会在RL训练中策略性地改变探索行为以抵抗能力激发，揭示了RL训练LLM的潜在失效模式。

- **Synthetic Computers at Scale for Long-Horizon Productivity Simulation** | [arXiv:2604.28181](https://arxiv.org/abs/2604.28181) | `Agent` `LLM` `Long Context` | 构建大规模合成计算机环境，让智能体在1,000台虚拟计算机上完成长达数月的生产力任务模拟。

- **Claw-Eval-Live: A Live Agent Benchmark for Evolving Real-World Workflows** | [arXiv:2604.28139](https://arxiv.org/abs/2604.28139) | `Agent` `Benchmark` `LLM` | 面向工作流智能体的实时基准测试，包含105个任务；当前领先模型仅通过66.7%的任务，可靠的工作流自动化仍是未解难题。

- **Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes** | [arXiv:2604.28138](https://arxiv.org/abs/2604.28138) | `Agent` `Infrastructure` | 弥合智能体与操作系统之间的语义鸿沟，将检查点流量减少87%的同时保持100%恢复正确性。

- **CastFlow: Learning Role-Specialized Agentic Workflows for Time Series Forecasting** | [arXiv:2604.27840](https://arxiv.org/abs/2604.27840) | `Agent` `LLM` `Reasoning` | 动态智能体预测框架，将预测过程组织为规划、行动、预测和反思的工作流，采用角色专业化LLM设计。

- **ObjectGraph: From Document Injection to Knowledge Traversal -- A Native File Format for the Agentic Era** | [arXiv:2604.27820](https://arxiv.org/abs/2604.27820) | `Agent` `LLM` `RAG` `Long Context` | 为智能体设计的知识图谱文件格式(.og)，实现最高95.3%的token缩减且不影响任务准确率，是Markdown的严格超集。

- **MCPHunt: An Evaluation Framework for Cross-Boundary Data Propagation in Multi-Server MCP Agents** | [arXiv:2604.27819](https://arxiv.org/abs/2604.27819) | `Agent` `Multi-Agent` `Security` `MCP` | 首个针对多服务器MCP信任边界凭证传播的受控基准；策略违规传播率达11.5%-41.3%，提示级防御可降低97%。

- **WindowsWorld: A Process-Centric Benchmark of Autonomous GUI Agents in Professional Cross-Application Environments** | [arXiv:2604.27776](https://arxiv.org/abs/2604.27776) | `Agent` `GUI` `Benchmark` `Multi-App` | 跨应用程序GUI智能体基准；多应用任务成功率低于21%，暴露了当前智能体在复杂工作流中的局限。

- **Intent2Tx: Benchmarking LLMs for Translating Natural Language Intents into Ethereum Transactions** | [arXiv:2604.27763](https://arxiv.org/abs/2604.27763) | `LLM` `Agent` `Benchmark` `Web3` | 高精度基准测试，评估16个SOTA LLM将自然语言意图转换为以太坊交易的能力。

- **Autonomous Traffic Signal Optimization Using Digital Twin and Agentic AI** | [arXiv:2604.27753](https://arxiv.org/abs/2604.27753) | `Agent` `LLM` `LangChain` `MCP` | 基于LangChain和MCP的数字孪生框架，实现实时交通信号优化。

- **AgentEconomist: An End-to-end Agentic System Translating Economic Intuitions into Executable Computational Experiments** | [arXiv:2604.27725](https://arxiv.org/abs/2604.27725) | `Agent` `LLM` `Multi-Agent` `Reasoning` | 端到端智能体系统，将经济学直觉转化为可执行的计算实验，采用多阶段架构。

- **Knowledge Graph Representations for LLM-Based Policy Compliance Reasoning** | [arXiv:2604.27713](https://arxiv.org/abs/2604.27713) | `LLM` `RAG` `Knowledge Graph` `Reasoning` `Agent` | 利用AI政策文档构建知识图谱的智能体框架，用于LLM策略合规推理。

- **Contextual Agentic Memory is a Memo, Not True Memory** | [arXiv:2604.27707](https://arxiv.org/abs/2604.27707) | `Agent` `Memory` `LLM` `RAG` | 论证当前智能体记忆系统本质上是查找表而非真正的记忆；借鉴神经科学的互补学习系统理论提出改进方向。

- **Bridging Values and Behavior: A Hierarchical Framework for Proactive Embodied Agents** | [arXiv:2604.27699](https://arxiv.org/abs/2604.27699) | `Agent` `LLM` `Embodied AI` `Reasoning` | ValuePlanner——基于LLM推理的分层认知架构，实现主动式具身智能体的价值调度。

- **Pragmos: A Process Agentic Modeling System** | [arXiv:2604.27311](https://arxiv.org/abs/2604.27311) | `Agent` `LLM` `Process Modeling` | 面向业务流程管理的交互式智能体建模系统，将建模任务分解为可解释的人机协作步骤。

- **SecMate: Multi-Agent Adaptive Cybersecurity Troubleshooting with Tri-Context Personalization** | [arXiv:2604.26394](https://arxiv.org/abs/2604.26394) | `Multi-Agent` `LLM` `Cybersecurity` | 多Agent虚拟客户助理用于网络安全故障排查，设备级证据将正确解决率从约50%提升至90%以上。

- **Safe Bilevel Delegation (SBD): A Formal Framework for Runtime Delegation Safety in Multi-Agent Systems** | [arXiv:2604.27359](https://arxiv.org/abs/2604.27359) | `Multi-Agent` `LLM` `Safety` `Formal Methods` | 多智能体运行时委托安全的形式化框架，将任务委托建模为双层优化问题，支持安全-效率权衡的动态调整。

- **Eywa: Heterogeneous Scientific Foundation Model Collaboration** | [arXiv:2604.27351](https://arxiv.org/abs/2604.27351) | `Multi-Agent` `Scientific AI` `Agent` | 异构智能体框架，将语言中心系统扩展至科学基础模型，支持物理、生命和社会科学领域的跨模态推理。

- **AGEL-Comp: A Neuro-Symbolic Framework for Compositional Generalization in Interactive Agents** | [arXiv:2604.26522](https://arxiv.org/abs/2604.26522) | `Agent` `Neuro-symbolic` `Compositional Generalization` | 神经符号AI智能体架构，通过因果程序图和归纳逻辑编程实现组合泛化，在Retro Quest环境中优于纯LLM基线。

- **InteractWeb-Bench: Can Multimodal Agent Escape Blind Execution in Interactive Website Generation?** | [arXiv:2604.27419](https://arxiv.org/abs/2604.27419) | `Agent` `Multimodal` `Benchmark` `MLLM` | 首个面向非专业用户条件下交互式网站生成的多模态基准，揭示了前沿MLLM智能体在盲执行模式中的局限。

### LLM / Reasoning / Chain-of-Thought

- **TopBench: A Benchmark for Implicit Prediction and Reasoning over Tabular Question Answering** | [arXiv:2604.28076](https://arxiv.org/abs/2604.28076) | `Reasoning` `LLM` `Agent` | 面向隐式预测表格问答的基准，要求从历史模式进行推理；当前模型在意图识别方面表现不佳。

- **Towards Neuro-symbolic Causal Rule Synthesis, Verification, and Evaluation Grounded in Legal and Safety Principles** | [arXiv:2604.28087](https://arxiv.org/abs/2604.28087) | `LLM` `Neuro-symbolic` `Reasoning` | 利用LLM从自然语言目标合成和验证因果规则，应用于自动驾驶等安全关键领域。

- **Characterizing the Consistency of the Emergent Misalignment Persona** | [arXiv:2604.28082](https://arxiv.org/abs/2604.28082) | `LLM` `Alignment` `Safety` | 在不对齐领域上微调Qwen 2.5 32B，揭示了一致性人格和反转人格两种模式，挑战了涌现不对齐(EM)的一致性假设。

- **Do Sparse Autoencoders Capture Concept Manifolds?** | [arXiv:2604.28119](https://arxiv.org/abs/2604.28119) | `Interpretability` `LLM` | 证明稀疏自编码器(SAE)次优地恢复连续流形结构，推动将几何对象作为可解释性基本单元的未来方法。

- **Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection** | [arXiv:2604.28129](https://arxiv.org/abs/2604.28129) | `LLM` `Security` `Multi-Turn` | 通过探测LLM激活检测多轮提示注入攻击；合成数据检测率93.8%，混合集89.4%。

- **PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning** | [arXiv:2604.28123](https://arxiv.org/abs/2604.28123) | `Multimodal` `RL` `LLM` `Reasoning` | 三阶段多模态RL流程，缓解SFT与RLVR之间的分布漂移，平均准确率提升+4.4至+6.0点。

- **Auto-FlexSwitch: Efficient Dynamic Model Merging via Learnable Task Vector Compression** | [arXiv:2604.28109](https://arxiv.org/abs/2604.28109) | `Model Merging` `LLM` | 基于可学习任务向量压缩的动态模型合并，在高压缩比下实现高保真近似。

- **What Makes a Good Terminal-Agent Benchmark Task** | [arXiv:2604.28093](https://arxiv.org/abs/2604.28093) | `Agent` `Benchmark` `LLM` | 终端智能体基准测试任务设计指南；超过15%的流行基准任务存在奖励可破解性问题。

- **RHyVE: Competence-Aware Verification and Phase-Aware Deployment for LLM-Generated Reward Hypotheses** | [arXiv:2604.28056](https://arxiv.org/abs/2604.28056) | `LLM` `RL` `Reward` | 面向LLM生成奖励假设的能力感知验证和阶段感知部署框架。

- **How Generative AI Disrupts Search** | [arXiv:2604.27790](https://arxiv.org/abs/2604.27790) | `LLM` `Search` `RAG` | 研究生成式AI(Google AIO、Gemini)对网络搜索的颠覆；51.5%的查询获得AIO，且引用来源与传统搜索结果差异显著。

- **Test Before You Deploy: Governing Updates in the LLM Supply Chain** | [arXiv:2604.27789](https://arxiv.org/abs/2604.27789) | `LLM` `Governance` `Deployment` | 面向LLM供应链静默更新的部署侧治理框架，引入生产合约和兼容性门控。

- **RuC: HDL-Agnostic Rule Completion Benchmark Generation** | [arXiv:2604.27780](https://arxiv.org/abs/2604.27780) | `LLM` `Code` `Benchmark` | 语法驱动的基准生成器，用于评估LLM在硬件描述语言中的代码补全能力。

- **Mind the Gap: Structure-Aware Consistency in Preference Learning** | [arXiv:2604.27733](https://arxiv.org/abs/2604.27733) | `LLM` `DPO` `Alignment` `Preference Learning` | 推导LLM对齐的严格H一致性界限，提出语义距离感知边际的SA-DPO方法。

- **Perturbation Probing: A Two-Pass-per-Prompt Diagnostic for FFN Behavioral Circuits in Aligned LLMs** | [arXiv:2604.27401](https://arxiv.org/abs/2604.27401) | `LLM` `Interpretability` `Mechanistic` | 每提示两次前向传播的扰动探测方法，识别RLHF组织行为中的对立电路和路由电路结构。

- **Beyond the Mean: Within-Model Reliable Change Detection for LLM Evaluation** | [arXiv:2604.27405](https://arxiv.org/abs/2604.27405) | `LLM` `Evaluation` `Metrics` | 将临床心理学的可靠变化指数(RCI)应用于LLM版本比较，发现聚合准确率提升是双向 item 级变化的净残差。

- **Tatemae: Detecting Alignment Faking via Tool Selection in LLMs** | [arXiv:2604.26511](https://arxiv.org/abs/2604.26511) | `LLM` `Alignment` `Safety` `CoT` | 通过工具选择检测LLM的对齐伪装(AF)；6个前沿模型的平均AF检出率3.5%-23.7%，暴露训练方法差异。

- **Auto-Relational Reasoning** | [arXiv:2604.26507](https://arxiv.org/abs/2604.26507) | `Reasoning` `Neuro-symbolic` `IQ` | 集成推理与神经网络的自动对象关系推理框架，在IQ问题上达到98.03%解题率(前1%百分位)。

- **Grounding vs. Compositionality: On the Non-Complementarity of Reasoning in Neuro-Symbolic Systems** | [arXiv:2604.26521](https://arxiv.org/abs/2604.26521) | `Neuro-symbolic` `Reasoning` `Compositional` | 首次系统实证分析表明符号接地必要但不充分，推理是需要显式学习目标的独立能力。

- **Tree-of-Text: A Tree-based Prompting Framework for Table-to-Text Generation in the Sports Domain** | [arXiv:2604.26501](https://arxiv.org/abs/2604.26501) | `LLM` `Prompt` `Table-to-Text` | 树结构提示框架用于体育领域表格到文本生成，以约40%的时间和成本超越Chain-of-Table。

- **Investigating More Explainable and Partition-Free Compositionality Estimation for LLMs: A Rule-Generation Perspective** | [arXiv:2604.27340](https://arxiv.org/abs/2604.27340) | `LLM` `Compositionality` `Reasoning` `Explainability` | 规则生成视角的LLM组合性估计，无需数据集分区即可解释地评估模型对样本组合性的理解。

- **Theory-Grounded Evaluation Exposes the Authorship Gap in LLM Personalization** | [arXiv:2604.26460](https://arxiv.org/abs/2604.26460) | `LLM` `Personalization` `Evaluation` | 基于作者验证理论评估LLM风格个性化，发现所有方法均低于人类基准下限，暴露了作者身份鸿沟。

- **Beyond Accuracy: LLM Variability in Evidence Screening for Software Engineering SLRs** | [arXiv:2604.27006](https://arxiv.org/abs/2604.27006) | `LLM` `Evaluation` `Software Engineering` | 评估12个LLM在软件工程系统文献综述筛选中的表现；发现即使在temperature=0时仍存在显著异质性和残余非确定性。

- **LLMs Capture Emotion Labels, Not Emotion Uncertainty** | [arXiv:2604.27345](https://arxiv.org/abs/2604.27345) | `LLM` `Emotion` `Annotation` `Calibration` | 64万次LLM响应的分布分析表明，零样本模型无法捕捉人类标注者的情绪判断分布不确定性，领域内微调才能缩小差距。

- **TLPO: Token-Level Policy Optimization for Mitigating Language Confusion in Large Language Models** | [arXiv:2604.26553](https://arxiv.org/abs/2604.26553) | `LLM` `Multilingual` `Fine-tuning` | 令牌级策略优化框架，通过局部化更新缓解LLM语言混淆问题，在保持下游任务准确率的同时显著提升语言一致性。

### RAG / Retrieval / Long Context

- **Efficient Multivector Retrieval with Token-Aware Clustering and Hierarchical Indexing (TACHIOM)** | [arXiv:2604.28142](https://arxiv.org/abs/2604.28142) | `RAG` `Retrieval` `LLM` | 多向量检索系统，实现最高247倍的聚类加速和9.8倍检索速度提升，同时保持检索效果。

- **EviMem: Evidence-Gap-Driven Iterative Retrieval for Long-Term Conversational Memory** | [arXiv:2604.27695](https://arxiv.org/abs/2604.27695) | `RAG` `Memory` `LLM` `Long Context` | 基于证据差距驱动的迭代检索方法，用于长期对话记忆的信息补全。

- **A Reproducibility Study of LLM-Based Query Reformulation** | [arXiv:2604.27421](https://arxiv.org/abs/2604.27421) | `LLM` `RAG` `Information Retrieval` | 10种LLM查询重构方法的系统性可复现性研究；发现重构增益强烈依赖于检索范式，更大LLM不一定带来更好下游性能。

- **From Unstructured to Structured: LLM-Guided Attribute Graphs for Entity Search and Ranking** | [arXiv:2604.27410](https://arxiv.org/abs/2604.27410) | `LLM` `RAG` `Graph` `Entity Search` | LLM驱动属性图构建用于电商实体搜索，减少57%的每产品token使用量，排名精度提升超过5%。

- **Toward Autonomous SOC Operations: End-to-End LLM Framework for Threat Detection, Query Generation, and Resolution** | [arXiv:2604.27321](https://arxiv.org/abs/2604.27321) | `LLM` `RAG` `Security` `Agent` | 面向SOC的端到端LLM威胁管理框架，集成集成检测、语法约束查询生成和RAG增强的解决方案支持。

- **ChipLingo: A Systematic Training Framework for Large Language Models in EDA** | [arXiv:2604.27415](https://arxiv.org/abs/2604.27415) | `LLM` `Domain Adaptation` `RAG` | 面向电子设计自动化(EDA)的LLM系统训练流程，包含领域自适应预训练和多样化检索条件下的RAG场景训练。

- **Benchmarking Complex Multimodal Document Processing Pipelines** | [arXiv:2604.26382](https://arxiv.org/abs/2604.26382) | `RAG` `Multimodal` `Document AI` `Benchmark` | 企业文档处理管道的端到端基准；混合检索(nDCG@5=0.92)优于稠密嵌入(0.83)，但跨阶段质量相关性极弱(r=0.02-0.17)。

### VLM / Multimodal

- **Delineating Knowledge Boundaries for Honest Large Vision-Language Models** | [arXiv:2604.26419](https://arxiv.org/abs/2604.26419) | `VLM` `Knowledge Boundaries` `Safety` | 系统性框架增强VLM面对未知查询时的拒绝能力，通过多样本一致性探测构建Visual-Idk数据集，Truthful Rate从57.9%提升至67.3%。

- **Progressive Semantic Communication for Efficient Edge-Cloud Vision-Language Models** | [arXiv:2604.26508](https://arxiv.org/abs/2604.26508) | `VLM` `Edge-Cloud` `Efficiency` | 边缘-云端VLM推理的渐进语义通信框架，使用元自编码器将视觉token压缩为自适应可渐进细化的表示。

### Efficiency / Quantization / Inference

- **ZipCCL: Efficient Lossless Data Compression of Communication Collectives for Accelerating LLM Training** | [arXiv:2604.27844](https://arxiv.org/abs/2604.27844) | `LLM` `Training` `Compression` | 面向LLM训练的集体通信无损压缩库，利用LLM张量的近高斯分布特性，通信时间减少最高1.35倍。

- **Position-Aware Drafting for Inference Acceleration in LLM-Based Generative List-Wise Recommendation** | [arXiv:2604.27747](https://arxiv.org/abs/2604.27747) | `LLM` `Inference` `Recommendation` | 面向LLM推荐的位置感知投机解码加速方法，实现3.1倍加速。

- **CoQuant: Joint Weight-Activation Subspace Projection for Mixed-Precision LLMs** | [arXiv:2604.26378](https://arxiv.org/abs/2604.26378) | `LLM` `Quantization` `Inference` | 联合权重-激活子空间投影的混合精度LLM量化方法，在WikiText困惑度和零样本推理上持续优于强基线。

- **When Hidden States Drift: Can KV Caches Rescue Long-Range Speculative Decoding?** | [arXiv:2604.26412](https://arxiv.org/abs/2604.26412) | `LLM` `Inference` `Speculative Decoding` `KV Cache` | KVShot诊断框架验证KV缓存复用假设，暴露浅层draft模型估计目标查询的结构性瓶颈，为下一代推理架构指明方向。

### Security / Privacy / Safety

- **Secret Stealing Attacks on Local LLM Fine-Tuning through Supply-Chain Model Code Backdoors** | [arXiv:2604.27426](https://arxiv.org/abs/2604.27426) | `LLM` `Security` `Privacy` | 揭示供应链模型代码后门可从本地LLM微调数据集中窃取API密钥等敏感信息，Strict ASR超过98%。

- **SafeReview: Defending LLM-based Review Systems Against Adversarial Hidden Prompts** | [arXiv:2604.26506](https://arxiv.org/abs/2604.26506) | `LLM` `Security` `Peer Review` | 受IRGAN启发的对抗防御框架，通过生成器和防御器联合优化，保护LLM同行评审系统免受对抗性隐藏提示攻击。

- **Quantamination: Dynamic Quantization Leaks Your Data Across the Batch** | [arXiv:2604.26505](https://arxiv.org/abs/2604.26505) | `LLM` `Privacy` `Security` | 揭示动态量化中的关键漏洞：攻击者可利用同一批次中的量化侧信道窃取其他用户的敏感输入数据。

### Data / Training / Fine-tuning

- **Repetition over Diversity: High-Signal Data Filtering for Sample-Efficient German Language Modeling** | [arXiv:2604.28075](https://arxiv.org/abs/2604.28075) | `LLM` `Language Modeling` `Data` | 证明对非英语LLM重复高质量数据优于在更大但过滤较少的语料库上进行单次训练。

- **SplitFT: An Adaptive Federated Split Learning System For LLMs Fine-Tuning** | [arXiv:2604.26388](https://arxiv.org/abs/2604.26388) | `Federated Learning` `LLM` `Fine-tuning` | 自适应联邦分割学习系统，支持不同客户端根据计算资源设置不同切分层，并通过降低LoRA秩减少通信开销。

- **Naamah: A Large Scale Synthetic Sanskrit NER Corpus via DBpedia Seeding and LLM Generation** | [arXiv:2604.26456](https://arxiv.org/abs/2604.26456) | `LLM` `NER` `Low-resource` | 结合DBpedia实体提取和24B混合推理模型生成能力，构建102,942句高质量梵文NER数据集。

- **Automatic Causal Fairness Analysis with LLM-Generated Reporting (FairMind)** | [arXiv:2604.27011](https://arxiv.org/abs/2604.27011) | `LLM` `Fairness` `AutoML` | 自动化因果公平性分析工具，基于标准公平模型假设进行反事实查询，并利用LLM生成零样本公平性报告。

---

## 统计摘要

| 维度 | 数量 |
|------|------|
| 总收录论文 | 46 篇 |
| Agent / Multi-Agent | 20 篇 |
| LLM / Reasoning | 18 篇 |
| RAG / Retrieval | 7 篇 |
| VLM / Multimodal | 2 篇 |
| Efficiency / Inference | 4 篇 |
| Security / Privacy | 3 篇 |
| Data / Training | 4 篇 |

> 注：单篇论文可能同时属于多个维度，因此分类计数之和大于总收录数。

---

*PaperWeekly 和 HuggingFace Papers 本周无可直接抓取的有效数据（API/页面不可达或返回旧内容），本次雷达主要基于 arXiv API 的 764 条 cs.CL/cs.LG/cs.AI 论文进行筛选。*
