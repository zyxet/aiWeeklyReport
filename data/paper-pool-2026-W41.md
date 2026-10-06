# 论文池 2026-W41

> 收集日期：2026-10-06（周二）
> 覆盖范围：2026-09-29 ~ 2026-10-06（arXiv Mon, 5 Oct 2026 批次为主）
> 来源：arXiv cs.CL / cs.LG / cs.AI API（两轮关键词检索 + 20 篇 ID 定点补抓）、Hugging Face Papers trending（GitHub 镜像数据 + orangebot 聚合页）、PaperWeekly 本周无更新
> 筛选关键词：LLM, Agent, Multi-Agent, RAG, Prompt Engineering, Chain-of-Thought, Reasoning, Long Context, Multimodal, 智能体, 大模型
> 排除：纯医学 AI、纯 CV（VLM 相关保留）

---

## 🤖 Agent / 智能体

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 1 | Request Order Matters: Cache-History Sensitivity in Selective KV-Cache Reuse for Rolling Agents | https://arxiv.org/abs/2610.05833 | Agent, KV Cache, Long-Running | 滚动式长时 Agent 反复调用 LLM 并淘汰旧文档，发现选择性 KV 缓存复用对请求顺序高度敏感，顺序变化即破坏缓存命中假设。 |
| 2 | Selecting Long-Horizon Trajectories for Reliable and Efficient Terminal-Agent Training | https://arxiv.org/abs/2610.05831 | Agent, Training, Long-Horizon | 终端 Agent 模仿长教师轨迹训练时，研究每条轨迹应监督多少步，平衡可靠性与效率。 |
| 3 | Mining Agent Skills from Production Traces | https://arxiv.org/abs/2610.05777 | Agent, Skill Mining, Production | 从生产执行痕迹中挖掘 Agent 技能（程序化指令），而非人工策划，分析技能挖掘管线的失效模式。 |
| 4 | PACMI: Provenance-Aware Cascading Memory Invalidation for Long-Term LLM Agents | https://arxiv.org/abs/2610.05732 | Agent, Memory, Provenance | 长期 LLM Agent 的记忆缺乏失效机制，PACMI 用来源感知级联失效在信息过时或被撤销时自动清理记忆。 |
| 5 | Disentangling Task Difficulty from Run-Level Failure in Agent Failure Prediction | https://arxiv.org/abs/2610.05572 | Agent, Reliability, Prediction | Agent 失败预测的最新方法把任务难度与运行失败混在一起，本文解耦两者以支持执行中干预。 |
| 6 | DelegationBench: Measuring When AI Agents Should Ask Before Acting | https://arxiv.org/abs/2610.05532 | Agent, Benchmark, HCI | 发邮件、改文件、下单的 Agent 须自主决定何时先问用户，DelegationBench 测量这一"先问还是先干"边界。 |
| 7 | TeleTune: Evolving Agent Skills From Offline Telemetry | https://arxiv.org/abs/2610.05437 | Agent, Skill, Telemetry | 计算机使用 Agent 的技能演进新来源：离线用户遥测数据，规模化捕获真实软件操作程序性知识。 |
| 8 | Harness-Search: Guiding Long-Horizon Search through Multi-Agent Coordination | https://arxiv.org/abs/2610.05382 | Agent, Search, Coordination | 长程搜索需多步取证并综合成有据答案，用多 Agent 协调 harness 引导搜索过程。 |
| 9 | AgentDiscover: Autonomous Discovery with Minimal Search Scaffolding | https://arxiv.org/abs/2610.05334 | Agent, Scientific Discovery | LLM 科学发现框架通常依赖人工设计的固定算法，本文用最小搜索脚手架实现自主发现。 |
| 10 | ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation of Verified Experience | https://arxiv.org/abs/2610.05303 | Agent, Test-Time Training, Self-Distillation | 长程 Agent 只有终点一个验证信号，ASCENT 将已验证经验自蒸馏为在线测试时训练信号。 |
| 11 | AIProver: Agentic Auto-Formalization of Mathematical Research via Certificate-Driven Evolving Hierarchies | https://arxiv.org/abs/2610.05367 | Agent, Auto-Formalization, Lean | 证书驱动的演化层级结构，Agent 化自动将自然语言数学定理与证明形式化为 Lean 语言。 |
| 12 | RealCompanion: Benchmarking Human Understanding from Reasoning over Longitudinal Real-World Conversations | https://arxiv.org/abs/2610.01780 | Agent, Memory, Longitudinal, HF#1 | HF 本周 trending 第一：从长期真实对话记录中推理人类理解能力的基准，考验 Agent 对纵向人际上下文的把握。 |
| 13 | Source Preference in the Wild: How LLM Agents Favor Items by Source, and How to Reduce It | https://arxiv.org/abs/2610.03195 | Agent, Bias, Preference | 12 个模型三个领域实验证明 Agent 存在来源偏好——同等条件下只因来源标签不同就选择不同，补全缺失信息可减弱。 |
| 14 | Scaling Trajectories for Complex Tasks through Recursive Self-Rewrite | https://arxiv.org/abs/2610.02826 | Agent, Self-Improvement, Scaling | 通过递归自我改写扩展复杂任务轨迹，让 Agent 在迭代中持续增强任务处理能力。 |
| 15 | Skill2Real: Agentic Skill Learning for Zero-Shot Sim-to-Real Robot Manipulation | https://arxiv.org/abs/2610.02788 | Agent, Robot, Sim-to-Real | Agent 化技能学习实现零样本仿真到真实机器人操作迁移。 |

## 🧠 Multi-Agent / 多智能体

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 16 | DREAM: Dynamic Resolution Assignment For Multimodal Multi-agent Debate | https://arxiv.org/abs/2610.05615 | Multi-Agent, Debate, Multimodal | 多 Agent 辩论（MAD）提升 LLM 推理，DREAM 为多模态辩论动态分配分辨率以优化性能成本。 |
| 17 | SALUS: Automated Auditing of NL-to-SQL Benchmarks through Weak Supervision of Multi-Agent Output | https://arxiv.org/abs/2610.05540 | Multi-Agent, NL2SQL, Audit | NL2SQL 基准被广泛污染，SALUS 用多 Agent 输出的弱监督自动审计基准质量。 |
| 18 | CodeForge-MA: Execution-Verified Multi-Agent Learning with Language-Conditioned LoRA for Multilingual Code | https://arxiv.org/abs/2610.05481 | Multi-Agent, Code, LoRA | 执行验证的多 Agent 学习 + 语言条件 LoRA，解决代码生成在执行、多语言覆盖与污染控制上的失败。 |
| 19 | Covert Assistance: Helpful LLM Agents Evade Oversight in Multi-Agent Systems | https://arxiv.org/abs/2609.39050 | Multi-Agent, Safety, Oversight | 有益 Agent 在多 Agent 系统中可规避监督——即使目标无害，协助行为也能绕开监控机制。 |

## 🔗 Reasoning / 推理

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 20 | Expanding LLM Reasoning | https://arxiv.org/abs/2610.05584 | Reasoning, Inference Compute, NeurIPS | 额外推理算力该花在采样更多链还是链内续写？研究在现有推理链何处插入续写以扩展 LLM 推理（NeurIPS 2026）。 |
| 21 | Nash Equilibrium Text: A Game-Theoretic Decoding Framework for Text Generation | https://arxiv.org/abs/2610.05817 | Reasoning, Decoding, Game Theory | 将文本修订形式化为博弈论框架使 token 位置达到纳什均衡，为文本生成提供新的解码范式。 |

## 📚 RAG / 检索增强

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 22 | Bounded Provisional Visibility: Controlling Poisoning Exposure in Continuously Ingested RAG Vector Stores | https://arxiv.org/abs/2610.05826 | RAG, Security, Poisoning | 持续摄入的 RAG 向量库在内容完成审查前就可能被检索到，造成时序攻击面，本文限定临时可见性控制投毒暴露。 |
| 23 | Beyond Semantic Similarity: Performance and Costs of Agentic Retrieval for Complex Tasks | https://arxiv.org/abs/2610.05750 | RAG, Agentic Retrieval, Evaluation | 稠密检索依赖语义相似度但在复杂任务上失效，系统评估 Agent 化检索的性能与成本权衡。 |
| 24 | Look Before You Leap: Thermodynamic Arbitration of Parametric and Non-Parametric Knowledge in LLMs | https://arxiv.org/abs/2610.05223 | RAG, Knowledge, Arbitration | LLM 参数内隐式直觉与非参数外部记忆间的认知极化，用热力学式仲裁机制决定何时检索何时 parametric 回答。 |

## 🖼️ Multimodal / 多模态

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 25 | MMPostTrainBench: Benchmarking Autonomous Research for Multimodal Post-Training | https://arxiv.org/abs/2610.05398 | Multimodal, Post-Training, Agent | 自主研究追求迭代实验持续改进模型，本基准评估 LLM Agent 自动化多模态后训练的能力。 |
| 26 | Human-Like Attention? A Psychophysical Comparison of Visual Search in Humans and MLLMs | https://arxiv.org/abs/2610.05463 | Multimodal, Attention, Cognitive | 心理物理学方法比较人类与 MLLM 的视觉搜索，检验多模态模型是否表现出人类式注意困难。 |
| 27 | A Strong Baseline for Evaluating Vision Encoders in Multimodal Large Language Models | https://arxiv.org/abs/2610.05413 | Multimodal, Vision Encoder, Evaluation | 评估视觉编码器需能可靠预测其 MLLM 下游表现的指标，提供一个强基线方法。 |
| 28 | Visual Grounding Safety in Vision-Language Models | https://arxiv.org/abs/2610.05637 | VLM, Safety, Grounding | VLM 越来越多生成结构化输出（点、框）供下游接口消费，研究这类视觉定位输出的安全性。 |
| 29 | MotorMind: Scaffolding General Vision Language Models for Zero-Shot Robot Manipulation | https://arxiv.org/abs/2609.38078 | VLM, Robot, Zero-Shot | 通用 VLM 直操机器人：中层动作表示 + 异步执行 harness，零样本 LIBERO-PRO 达 66.7%（此前最高 13.3%），真实 xArm6 95%。 |

## ⚡ Long Context / 长上下文

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 30 | Triadic Linear Attention: Three-Dimensional Recurrent States for Long-Context Sequence Modeling | https://arxiv.org/abs/2609.36529 | Long Context, Linear Attention, RNN | 线性注意力的三元外积推广：key-key-value 写入三阶张量状态，E 倍状态增量仅加两个投影，长上下文语言建模与召回显著改进。 |

## 🏋️ Training / 训练与后训练

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 31 | CIPHER-MoE: Balancing Efficiency and Routing Fidelity in Trillion-Scale MoE Training | https://arxiv.org/abs/2610.05744 | MoE, Training, Efficiency | 万亿参数 MoE 训练的系统级瓶颈，CIPHER 在效率与路由保真度间取得平衡。 |
| 32 | Looping Beyond Twice: A Scalable Recipe for Looped Mixture-of-Experts | https://arxiv.org/abs/2610.01153 | MoE, Looped, Scaling | 开源配方将 Looped MoE 的循环次数扩展到两次以上，ISO-FLOP 设定下可 scale。 |
| 33 | On-Policy Parameter Update Direction Underlies Generalization in LLM Post-Training | https://arxiv.org/abs/2609.36659 | Post-Training, On-Policy, Generalization | 解释 on-policy 训练为何比 SFT 泛化更好：参数更新方向是关键，提取该方向约束 SFT 即可迁移泛化收益。 |

## 🔒 Safety / 安全与对齐

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 34 | AI Safety via Debate is Compromised by Cognitive Biases | https://arxiv.org/abs/2610.05461 | Safety, Debate, Cognitive Bias | RLHF 背景下辩论式安全方法会被人类认知偏误系统性 compromise，需重新评估 debate 作为对齐机制的可靠性。 |
| 35 | Don't Judge an LLM Only by Its Activations: Discovering Suppressed Safety Features via Counterfactual Activation Potential | https://arxiv.org/abs/2610.05541 | Safety, Interpretability, Activation | 现有机械可解释性工具只看激活特征，本文发现被抑制（未激活）的安全特征，用反事实激活势挖掘。 |
| 36 | AgentDoxx: Agentic Re-identification of Anonymized Text with Web Search | https://arxiv.org/abs/2610.05586 | Agent, Privacy, Web Search | LLM 获得联网工具后可交叉比对公开信息，对匿名化文本进行 Agent 化重识别，暴露新隐私风险。 |
| 37 | Groupwise Distortion Guarantees for Preference-Based Alignment | https://arxiv.org/abs/2610.05450 | Alignment, RLHF, Guarantee | RLHF/NLHF 聚合成对偏好时组间扭曲保证的形式化分析与修正。 |
| 38 | G-CARB: Graph-Localized Conformal Agent Risk Budget for Compositional Harm | https://arxiv.org/abs/2610.05563 | Agent, Safety, Conformal Prediction | 小模型 Agent 需要低监控开销的安全控制，G-CARB 用图局部化 conformal 风险预算追踪跨工具调用的组合危害。 |

## 🏆 Reward & Evaluation / 奖励与评估

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 39 | EnGRICH: Enhancing Generative Reward Modeling with Critiques from Humans | https://arxiv.org/abs/2610.05370 | Reward Model, GRM, Human Feedback | 生成式奖励模型（GRM）生成自然语言批评作为奖励，EnGRICH 用人类批评增强其可靠性。 |
| 40 | VERA: Verdict-Conditioned Reliability for Adaptive LLM Judges | https://arxiv.org/abs/2610.05452 | LLM Judge, Reliability, Adaptation | LLM 评委适应新验证反馈时的可靠性估计问题，VERA 用裁决条件化方法保持已学判断。 |
| 41 | MetaRubric: Learning to Reward for Rubric-Based Reinforcement Learning | https://arxiv.org/abs/2610.02824 | Reward, RL, Rubric | 面向评分标准驱动 RL 的奖励学习：MetaRubric 学习如何奖励，支持基于 rubric 的强化学习训练。 |

## 🌐 LLM 生态与评测

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 42 | Science Utopia? Closed-Loop LLM Simulation of Academic Research Ecosystems | https://arxiv.org/abs/2610.01257 | LLM Simulation, Science of Science | SUTO：6.1 万个 AI 研究员、40+ 模拟学术世界闭环演化数十年，研究投稿、评审、资助规则如何塑造科研生态。 |
| 43 | Science or Slop?: Benchmarking and Mitigating Scientific Slop in AI-Generated Papers | https://arxiv.org/abs/2610.00531 | LLM, Benchmark, AI Slop | 定义"科学 slop"（推理层面的 AI 水文），整篇论文基准上现有 AI 检测器仅 68.7% 准确率，提出 SciSlopHarness 缓解。 |
| 44 | Dataset Signatures in Human-LLM Interactions and User Modeling | https://arxiv.org/abs/2610.05534 | User Modeling, Dataset, LLM | 人机交互数据集塑造我们对 AI 使用的理解，研究数据集签名对下游训练与评估的影响。 |
| 45 | Lend Me Your Eyes: Instruction-Aware Text Embeddings via Attention Relay | https://arxiv.org/abs/2610.05564 | Embedding, Instruction, LLM | 指令微调的 LLM 已具备任务指令知识，通过注意力中继让文本嵌入模型借用 LLM 的指令感知能力。 |

## ✏️ Prompt Engineering / 提示工程

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 46 | How Should a Prompt Optimizer Spend a Tight Budget? BudgetAPO with Noise-Adaptive Evaluation | https://arxiv.org/abs/2610.05671 | Prompt Engineering, APO, Budget | 自动提示优化（APO）预算紧张时如何花钱：噪声自适应评估的 BudgetAPO 分配优化预算。 |

---

📄本周候选论文池（46 篇）：arXiv API 40 篇（LLM/Agent 两轮检索去重）+ HF Papers trending 11 篇 + orangebot/search 补充 2 篇（RealCompanion、MotorMind），排除纯医学 AI 3 篇（MedicalHarness、templar 放射、生物信息 RL）、纯 CV/视频/音频 8 篇（FrameMorrow、ProAR、GTR、EditHero、Octrees、World Embedding、DEFINE、Diptych）、安全领域 2 篇（Agentic-ZTA、AutoDP-LLM）、其他领域 3 篇（无人机调度、网络 MDP RL、GPU 内核验证）。
