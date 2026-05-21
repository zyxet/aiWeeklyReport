# 📄 本周候选论文池（42篇）

> 收集时间：2026-05-19（W21）
> 来源：arXiv cs.CL/cs.LG/cs.AI + Hugging Face Papers + PaperWeekly
> 筛选关键词：LLM, Agent, Multi-Agent, RAG, Reasoning, Long Context, Multimodal, VLM, MoE, Chain-of-Thought, Prompt Engineering

---

## 🤖 Agent / Multi-Agent

| 标题 | 链接 | 标签 | 一句话摘要 |
|------|------|------|-----------|
| Argus: Agentic Deep Research with Searcher-Navigator Cooperation | https://arxiv.org/abs/2605.16217 | Agent, Deep Research, MoE, RL | 提出Searcher-Navigator协作架构，将深度研究视为拼图组装而非并行暴力搜索，64个Searcher在BrowseComp达到86.2分，超越所有闭源Agent |
| Nexa: Hybrid Multi-Agent Collaboration via Response-Conditioned Policy | https://arxiv.org/abs/2605.15573 | Multi-Agent, Collaboration, Policy Learning | 提出可训练的混合范式，先并行执行再预测稀疏DAG通信图，学习到的通信策略可跨任务和Agent数量复用 |
| PROTEUS: Resource-Constrained Agent Architecture | https://arxiv.org/abs/2605.17210 | Agent, Edge Computing, Architecture | 面向资源受限环境的Agent架构设计，优化推理效率与任务执行能力的平衡 |
| RecMem: Recurrence-Based Memory Consolidation for Long-Running Agents | https://arxiv.org/abs/2605.16045 | Agent Memory, Long Context, Efficiency | 通过潜意识记忆层和轻量级嵌入模型减少87%的记忆构建token成本，同时超越SOTA记忆系统精度 |
| DimMem: Dimensional Memory Framework for LLM Agents | https://arxiv.org/abs/2605.15759 | Agent Memory, Structured Memory, Efficiency | 将记忆表示为带显式字段（时间/地点/原因/目的/关键词）的原子化维度单元，在LoCoMo-10和LongMemEval-S上达到SOTA |
| H-Mem: Hybrid Memory Mechanism for LLM-based Agents | https://arxiv.org/abs/2605.15701 | Agent Memory, Temporal Memory, Knowledge Graph | 通过时序语义树+知识图混合结构建模记忆演化，在三个Agent记忆基准上达到SOTA QA性能 |
| SMMBench: Source-distributed Multimodal Memory Benchmark | https://arxiv.org/abs/2605.15710 | Multimodal Agent, Memory, Benchmark | 评估Agent跨异构来源（对话/截图/表格/文档）检索、对齐和组合多模态证据的能力，含1877样本和264个来源 |
| AI Coding Agents for Scientific Discovery (AntiGravity + ERA) | https://arxiv.org/abs/2605.16191 | Coding Agent, Scientific Discovery, Tree Search | 将通用编码Agent与LLM驱动的树搜索结合，自主生成科学假设并迭代消除奖励黑客，发现更优3D光伏结构 |

---

## 🔍 RAG / Long Context / Reasoning

| 标题 | 链接 | 标签 | 一句话摘要 |
|------|------|------|-----------|
| Block Attention with Semantic Segmentation for RAG | https://arxiv.org/abs/2605.15913 | RAG, Long Context, Block Attention, Distillation | 构建30k+实例的语义分割数据集训练轻量级分割器，提出块蒸馏框架实现近全注意力性能，解决KV缓存复用难题 |
| SGR: Stepwise Graph Reasoning with External Subgraph Generation | https://arxiv.org/abs/2605.16117 | Reasoning, RAG, Knowledge Graph, Multi-step | 通过查询特定子图构建引导LLM多步推理，结合多条推理轨迹提升推理准确性和事实可靠性 |
| AmpliGraph: Multi-Query LLM Reasoning in Knowledge Graphs | https://arxiv.org/abs/2605.17175 | Reasoning, KG, Multi-Query | 在知识图上进行多查询LLM推理，增强复杂关系推理能力 |
| NCCE: Neural Collaborative Context Engineering | https://arxiv.org/abs/2605.15721 | Prompt Engineering, Context Engineering, Personalization | 将上下文工程建模为推荐问题，通过神经协同过滤动态为每个实例路由最优上下文策略，实现实例级性能提升 |
| CAM-Bench: Computational and Applied Mathematics in Lean | https://arxiv.org/abs/2605.17255 | Reasoning, Math, Formal Verification, Lean | 面向Lean的证明助手基准测试，评估LLM在计算和应用数学中的形式化推理能力 |
| Syntax Without Semantics: Teaching LLMs to Code in Unseen Language | https://arxiv.org/abs/2605.15607 | Code Generation, Transfer Learning, Reasoning | 发现LLM能快速学习新语言语法但无法迁移语义能力，存在"实现保真度差距"：拥有语言无关的算法理解但无法在不熟悉语言中表达 |

---

## 🧠 LLM 能力 / 评估 / 安全

| 标题 | 链接 | 标签 | 一句话摘要 |
|------|------|------|-----------|
| Value-based Persona Construction for Cross-Cultural LLM Surveys | https://arxiv.org/abs/2605.16193 | LLM, Persona, Cross-Cultural, Calibration | 基于核心价值观构建文本画像，从目标人口采样价值分布，校准后显著缩小主流与欠代表国家间的性能差距 |
| Evaluating Chinese Ambiguity Understanding in LLMs | https://arxiv.org/abs/2605.15635 | LLM, Chinese, Ambiguity, Evaluation, CoT | 构建首个基于潜在歧义理论的中文歧义数据集CHA-Gen（5712句），发现LLM在歧义检测上表现不佳但CoT可改善，指令微调导致过度自信 |
| Calibrating LLMs with Semantic-level Reward (CSR) | https://arxiv.org/abs/2605.15588 | LLM, Calibration, RL, Semantic Reward | 在语义空间直接校准LLM，结合正确性奖励和语义校准奖励，ECE降低40%，AUROC提升31%，优于语言化置信度基线 |
| ASRU: Activation-Redirected Safe Removal for MLLMs | https://arxiv.org/abs/2605.15687 | MLLM, Unlearning, Safety, Multimodal | 可控多模态遗忘框架，通过激活重定向诱导拒绝行为并优化细粒度拒绝边界，在Qwen3-VL上提升24.6%遗忘效果和5.8倍生成质量 |
| SPARTA: LLM Safety via Sparse Coding | https://arxiv.org/abs/2605.17188 | LLM, Safety, Sparse Coding, Mechanistic Interpretability | 通过稀疏编码实现LLM安全对齐，提供可解释的安全机制 |
| Artificial Intolerance: Stigmatizing Language Skews LLM Decision-Making | https://arxiv.org/abs/2605.17228 | LLM, Bias, Medical, Fairness | 揭示临床文档中的污名化语言导致LLM决策偏差，对医疗AI公平性提出警示 |
| Survey of GenAI and NLP for Cybersecurity | https://arxiv.org/abs/2605.17224 | GenAI, Security, Survey, NLP | 全面综述生成式AI和NLP在网络安全中的应用，覆盖威胁检测、漏洞分析和防御策略 |
| Simulation-Assisted Testing for LLM Cybersecurity | https://arxiv.org/abs/2605.17208 | LLM, Security, Testing, Red Teaming | 通过模拟辅助测试评估LLM安全性，提供系统化的红队测试框架 |
| Scaffolding Instruction via Gamification for LLM Training | https://arxiv.org/abs/2605.17186 | LLM, Training, Instruction Tuning, Gamification | 通过游戏化支架指令改进LLM训练，提升指令跟随能力和学习效率 |
| TRILL: Making LLM Pre-Training Data Tracking Practical | https://arxiv.org/abs/2605.17183 | LLM, Data, Pre-training, Provenance | 实用化的LLM预训练数据追踪系统，实现大规模训练数据的可追溯性和管理 |
| Aphasias in Language Models: Lesion Studies Reveal Functional Organization | https://arxiv.org/abs/2605.16222 | LLM, Mechanistic Interpretability, Neuroscience | 借鉴失语症研究，通过"损伤"模型参数发现LLM的功能组织：早期层主要影响句法语义，中后层影响语音流畅性 |
| Machine-Generated Text Detection with Multi-level Contextual Relations | https://arxiv.org/abs/2605.16107 | MGT Detection, LLM, Security | 提出多级上下文token关系建模框架，通过局部马尔可夫校准和全局规则推理，在跨LLM和跨域场景实现广泛提升 |
| Active Budget Allocation for Scaling Law Estimation | https://arxiv.org/abs/2605.17234 | Scaling Law, Efficiency, Optimization | 主动预算分配策略优化Scaling Law估计，以更少的计算资源准确预测模型性能 |
| Fidelity Probes for Specification-Code Alignment | https://arxiv.org/abs/2605.17246 | LLM, Code, Verification, Specification | 提出保真度探针评估LLM生成代码与规范的对齐程度，提升代码生成可靠性 |

---

## 👁️ VLM / Multimodal

| 标题 | 链接 | 标签 | 一句话摘要 |
|------|------|------|-----------|
| Is VLA Reasoning Faithful? Probing Safety of Chain-of-Causation | https://arxiv.org/abs/2605.17268 | VLA, Autonomous Driving, Safety, Reasoning | 探查视觉-语言-动作模型中因果链推理的忠实性和安全性，揭示自动驾驶决策中的潜在风险 |
| CatalyticMLLM: Graph-Text Multimodal LLM for Catalytic Materials | https://arxiv.org/abs/2605.17254 | MLLM, Chemistry, Graph, Science | 面向催化材料的图-文本多模态LLM，结合化学图结构和文本描述进行材料发现 |
| IntentBench: Benchmarking Intention Understanding in MLLMs | https://arxiv.org/abs/2605.17215 | MLLM, Benchmark, Intention Understanding | 评估多模态LLM对用户意图的理解能力，揭示当前模型在复杂意图推理上的不足 |
| Interactive Map Symbol Understanding with MLLM | https://arxiv.org/abs/2605.17193 | MLLM, Geography, Symbol Understanding | 利用多模态LLM交互式理解地图符号，提升地理空间智能 |
| VCG-Bench: Diagram-as-Code Benchmark for VLMs | https://arxiv.org/abs/2605.15677 | VLM, Diagram, Code Generation, Benchmark | 提出Diagram-as-Code新范式，构建1449图形的VCG-Bench基准，发现SOTA VLM在结构化保真度和指令遵循上存在显著挑战 |
| VLM Adaptivity in Mathematics Education | https://arxiv.org/abs/2605.16011 | VLM, Education, Adaptivity, Evaluation | 系统评估视觉语言模型在数学辅导中的自适应能力，发现当前VLM难以持续产生基于学习者模型的教学响应 |
| ChemVA: Visual Activation for Chemical Graph Understanding | https://arxiv.org/abs/2605.17221 | VLM, Chemistry, Graph Understanding | 视觉激活机制增强化学图理解，提升VLM在分子结构推理上的表现 |
| ForMaT: Format-Preserving Multilingual Translation | https://arxiv.org/abs/2605.15794 | Multimodal, Translation, Layout, PDF | 构建3956 PDF的15语言对平行语料，保持原始布局元数据，揭示当前MT系统在空间定位和几何同步上的不足 |
| S2ST-Omni 2: Typology-Informed Speech-to-Speech Translation | https://arxiv.org/abs/2605.16026 | SpeechLLM, Multilingual, Translation | 从平面语言标签转向结构化类型学先验，实现数据高效的多语言语音到语音翻译，仅用3小时监督数据即可工作 |

---

## ⚙️ MoE / Architecture / Systems

| 标题 | 链接 | 标签 | 一句话摘要 |
|------|------|------|-----------|
| FishBack: Pullback Fisher Geometry for Activation Steering in Transformers | https://arxiv.org/abs/2605.17231 | LLM, Activation Steering, Geometry, Mechanism | 利用拉回Fisher几何在Transformer中进行激活导向，实现对模型行为的精细控制 |
| MoE Application in IIoT Network Intrusion Detection | https://arxiv.org/abs/2605.17219 | MoE, IIoT, Security, Anomaly Detection | 将混合专家模型应用于工业物联网网络入侵检测，提升异常检测精度 |
| MoE Testability: Evaluating Expert Specialization | https://arxiv.org/abs/2605.17197 | MoE, Testability, Expert Specialization | 系统评估MoE模型的可测试性和专家专业化程度，为MoE可靠性提供度量标准 |
| Transformer-Based Detection of SDN Attacks | https://arxiv.org/abs/2605.17177 | Transformer, Security, SDN, Network | 将Transformer架构应用于软件定义网络攻击检测，展示注意力机制在安全领域的适用性 |

---

## 📚 LLM 应用（法律/公共/其他）

| 标题 | 链接 | 标签 | 一句话摘要 |
|------|------|------|-----------|
| LLM Legal Assistant with Search (Peruvian Legal System) | https://arxiv.org/abs/2605.17216 | LLM, Legal, RAG, Application | 面向秘鲁法律系统的LLM法律助手，结合搜索功能提供法律咨询服务 |
| LLM for Judicial Sentence Creation (Puerto Rico) | https://arxiv.org/abs/2605.17202 | LLM, Legal, Spanish, Application | 探索LLM在波多黎各司法判决创建中的应用，处理西班牙语法律文本生成 |
| COVID-19 Crisis Management with LLMs | https://arxiv.org/abs/2605.17168 | LLM, Public Health, Crisis Management | 利用LLM辅助COVID-19危机管理，支持决策和信息传播 |
| MHGraphBench: Mental Health Knowledge in LLMs | https://arxiv.org/abs/2605.15589 | LLM, KG, Mental Health, Benchmark | 基于PrimeKG构建心理健康知识评估基准，发现LLM在关系预测和两跳推理上存在持续差距 |
| Open-source LLMs for Quality Estimation in MT | https://arxiv.org/abs/2605.15763 | LLM, MT, Quality Estimation, Open Source | 证明<30B参数的开源LLM可作为专有模型的隐私保护替代方案，在质量估计上达到高度竞争力 |
| AI Cultural Capabilities Taxonomy | https://arxiv.org/abs/2605.15990 | LLM, Culture, Evaluation, Taxonomy | 提出AI文化能力三级分类法（文化意识/敏感度/胜任力），为 multicultural AI 评估提供概念清晰性 |

---

> 共计42篇候选论文
> 排除说明：已排除纯医学AI（如乳腺超声分割、放射影像分类、临床分诊等）、纯CV（图像分类）、以及纯工程/物理/量子计算等非AI论文
