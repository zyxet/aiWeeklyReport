# 论文池 2026-W39

> 收集日期：2026-09-22（周二）
> 覆盖范围：2026-09-15 ~ 2026-09-21（arXiv Mon, 21 Sep 2026 批次）
> 来源：arXiv cs.CL / cs.LG / cs.AI API（HF Papers 直连不可达，经 GitHub 镜像仓库获取 trending；PaperWeekly 无本周更新）
> 筛选关键词：LLM, Agent, Multi-Agent, RAG, Prompt Engineering, Chain-of-Thought, Reasoning, Long Context, Multimodal, 智能体, 大模型
> 排除：纯医学 AI、纯 CV（VLM 相关保留）

---

## 🤖 Agent / 智能体

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 1 | Value-Sensitive Delegation in Everyday AI Agent Use: Evidence from OpenClaw | https://arxiv.org/abs/2609.22067 | Agent, HCI, Value | 用 LLM 辅助分析 73,093 篇 Reddit 一手帖，归纳用户委托 AI Agent 的 21 种价值诉求（自主、效率、隐私等六组），揭示任务完成≠价值满足。 |
| 2 | MCP-GRANITE Benchmark: GRANularity Interface Testing for MCP-Based LLM Agents | https://arxiv.org/abs/2609.24161 | Agent, MCP, Benchmark | 系统评测 MCP 协议下工具粒度设计对 Agent 选工具与构参能力的影响，填补工具接口设计基准空白。 |
| 3 | DENSE: Distilling Agent Trajectories into Evidence-Grounded Shortcut Trees for Self-Refinement | https://arxiv.org/abs/2609.21423 | Agent, Self-Refinement, Distillation | 无需事后结果标注，从 Agent 执行轨迹中提取局部进展证据，蒸馏为可复用的快捷反馈树实现自我改进。 |
| 4 | ArenaFlow: From Trajectory Ranking to Hierarchical Credit Propagation for Open-Ended Agent RL | https://arxiv.org/abs/2609.21378 | Agent, RL, Credit Assignment | 将 pairwise 评估与层级信用传播结合，解决开放式 Agent 任务中可靠标量奖励难获取的 RL 训练瓶颈。 |
| 5 | CodeMidas: Scaling Agentic Coding RL Environments from Code Itself | https://arxiv.org/abs/2609.22068 | Agent, Coding, RL | 从代码库直接提取多样化 RL 训练任务（不依赖 issue/commit），扩大 Agent 编码 RL 环境规模。 |
| 6 | An Empirical Study of Harness Design for Coding Agents | https://arxiv.org/abs/2609.20804 | Agent, Coding, Harness | 固定执行循环、单变量对比三种 harness 组件，首次实现组件级编码 Agent harness 效能评估。 |
| 7 | When Better Turns Do Not Make Better Agents: Diagnosing the Gap Between Next-Turn Metrics and Workflow Success | https://arxiv.org/abs/2609.21187 | Agent, Evaluation | 发现 next-turn 评估协议的提升无法预测自主工作流执行成功率，对当前 Agent 评估范式提出质疑。 |
| 8 | RetireOPD: Self-Retiring On-Policy Distillation for Agentic Reinforcement Learning | https://arxiv.org/abs/2609.20784 | Agent, RL, Distillation | 发现特权信息 alone 不足以提升 Agentic 任务 OPD，提出自退役机制让 student 逐步摆脱对 teacher 依赖。 |
| 9 | Chronicle: Cut-Point Replay for Regression Testing of LLM Agents | https://arxiv.org/abs/2609.20625 | Agent, Testing, Regression | 记录-重放使 LLM Agent 失败可复现，支持代码变更后的回归测试，解决非确定性推理导致的调试困难。 |
| 10 | Scaling Discovery through Test-Time Communication | https://arxiv.org/abs/2609.21032 | Multi-Agent, Communication | 证明 test-time 通信可显著超越独立并行尝试，一个 Agent 的突破能推动整个群体前进。 |
| 11 | LEGIT: Credentialing Protocol for Trustworthy AI Agent Marketplaces | https://arxiv.org/abs/2609.21325 | Agent, Marketplace, Trust | 为 Agent 市场建立可验证的凭证协议，解决买家无法跨任务/软件/预算比较 Agent 性能的问题。 |
| 12 | Efficient Benchmarking in Production: A Study of an Evolving LLM Agent | https://arxiv.org/abs/2609.21267 | Agent, Benchmark, Production | 基于 574 次生产基准运行，研究如何高效地反复评估持续演进中的生产级 LLM Agent。 |
| 13 | Verify, Don't Trust: Agentic Model Development for Video Discovery Retrieval at Scale | https://arxiv.org/abs/2609.21257 | Agent, AutoML, Production | LLM Agent 自主提出-实现-评估模型变更的在线 autoresearch 实践，跨越周级时间尺度影响真实产品。 |
| 14 | The Missing Complement: State-Conditioned Minimal Sufficient Evidence for Coding Agents | https://arxiv.org/abs/2609.20050 | Agent, RAG, Evidence | 提出状态条件化的最小充分证据恢复问题，为 coding Agent 检索"决策所必需且最紧凑"的证据集。 |
| 15 | Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation | https://arxiv.org/abs/2609.20822 | Agent, Robotics, Safety | 首次评估 coding agent 在机器人操作中的安全性，引入障碍感知 harness 约束代码生成。 |

## 🧠 Multi-Agent / 多智能体

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 16 | Mind or Message? Auditing Theory of Mind in Multi-Agent Social Simulation | https://arxiv.org/abs/2609.24146 | Multi-Agent, Theory of Mind | 在 40 个多议题谈判中验证：多 Agent 社交模拟中的表现依赖"对话表面记录"而非对伙伴心智的真实建模。 |
| 17 | Bayesian Belief Layer for Controllable Opinion Dynamics in LLM Agents | https://arxiv.org/abs/2609.21997 | Multi-Agent, Belief, Simulation | 将 Agent 立场表示为概率分布并通过单一贝叶斯规则更新，实现社交模拟中信念变化的可控与可验证。 |
| 18 | Language-model groups overstate consensus when replaying human deliberation | https://arxiv.org/abs/2609.20543 | Multi-Agent, Consensus, Deliberation | 回放 100 组人类推理讨论发现 LLM Agent 组系统性地高估共识率，暴露集体认知评估偏差。 |

## 🔥 HF Trending / 社区热门

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 19 | RecreationWorld: Scalable and Verifiable Environments for Hybrid Computer-Use Agents | https://arxiv.org/abs/2609.22000 | Agent, Computer-Use, Benchmark | 混合 Computer-Use Agent 需要在 GUI 交互与代码开发间自主切换，本文提供可扩展可验证的训练环境。 |
| 20 | MintAct: A Unified Visual Agent for Digital Environments | https://arxiv.org/abs/2609.22083 | Agent, VLM, GUI | 统一 UI 定位、跨平台多步导航与视觉工具使用的 VLM 家族，2B/4B/8B 三档规模匹配闭源性能。 |
| 21 | EvoOntology: A Self-Evolving Ontology Layer for Data Agents | https://arxiv.org/abs/2609.15779 | Agent, Data, MCP | 首个自进化本体层，弥合 Agent 与异构数据间的 agent-data gap，作为 MCP 插件接入 Claude Code/Codex。 |
| 22 | GraphSkillEvo: Evolutionary Optimization of Graph-Structured Agent Skills | https://arxiv.org/abs/2609.21749 | Agent, Skill, Evolution | 用图结构表示 Agent 技能，在图上做进化优化以获得更好的搜索空间与技能组合。 |
| 23 | When AI Reviews Train AI Reviewers: Scientific-Judgment Collapse and Mitigation | https://arxiv.org/abs/2609.20942 | LLM, Peer Review, Recursive | 揭示 AI 同行评审的递归崩塌风险：模型生成评审进入训练语料后，后续评审者会从早期判断中学习并退化。 |

## ⚡ Inference Efficiency / 推理效率

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 24 | DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression | https://arxiv.org/abs/2609.19969 | KV Cache, Compression, DeepSeek | 面向长 horizon Agent 的输入密集型负载，大幅压缩 prefill 开销与 KV cache 存储/传输瓶颈。 |
| 25 | KV-COBRA: KV Cache Compression via Co-Optimized Bit-Rank Allocation | https://arxiv.org/abs/2609.24298 | KV Cache, Quantization | 联合优化每个注意力头的秩截断与位宽分配，在极低位率下突破 KV cache 压缩极限。 |
| 26 | H-Spec: Parallel Speculative Decoding Without a Drafter-Side KV Cache | https://arxiv.org/abs/2609.24197 | Speculative Decoding, KV Cache | 块扩散 drafter 免维护独立 KV cache，通过目标模型隐藏状态投影降低投机解码延迟。 |
| 27 | L0-MoE: Accelerating Dense LLMs via L0-regularized Mixture-of-Experts | https://arxiv.org/abs/2609.21672 | MoE, Acceleration | 用 L0 正则化将 dense LLM 稀疏化为轻量 MoE，近乎无损性能即可加速推理。 |
| 28 | RheoSampling: Resolving the One-Hole Dilemma in Stochastic Dynamic-Tree Speculative Decoding | https://arxiv.org/abs/2609.21827 | Speculative Decoding, Sampling | 解决 EAGLE-3 类动态树方法在随机解码下坍缩为 one-hot 分布的问题，恢复草稿分布多样性。 |
| 29 | Abstention and Noise Filtering: Two Missing Primitives of Softmax Attention | https://arxiv.org/abs/2609.22005 | Attention, Pretraining | 证明 attention 值通路门控提供了 softmax attention 缺失的"弃权"与"噪声过滤"两种原语。 |
| 30 | dQwen3.5: Hybrid-Attention Diffusion Language Models | https://arxiv.org/abs/2609.20751 | Diffusion LM, Hybrid Attention | 从混合注意力 AR 模型适配扩散语言模型，解决 RNN 层的双向化障碍以继承预训练权重。 |

## 🎯 Reasoning / 推理与蒸馏

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 31 | MIRAGE: Multi-Perspective Creative Language Model Reasoning with RL Guidance | https://arxiv.org/abs/2609.21554 | Reasoning, RL, Multi-Perspective | 受人类认知灵活性启发，动态切换心智视角的多推理路径框架，Agent 式引导提升数学/科学/逻辑任务。 |
| 32 | When Does Reasoning Help in Machine Translation? A Hierarchical Analysis | https://arxiv.org/abs/2609.21247 | Reasoning, MT, Analysis | 大规模分析推理模型的翻译推理轨迹：最佳推理语言因模型而异，推理长度与质量呈非单调关系。 |
| 33 | What Does Privileged Information Add to On-Policy Self-Distillation? | https://arxiv.org/abs/2609.20612 | Distillation, Reasoning | 构建 5,319 题数学推理套件系统量化特权信息对 OPSD 的贡献，发现大部分收益来自蒸馏本身。 |
| 34 | CogGym: Towards Large-Scale Comparative Evaluation of Human and Machine Cognition | https://arxiv.org/abs/2609.21259 | Reasoning, Cognitive Science, Benchmark | 大规模对比人类与机器认知的评估框架，系统刻画模型响应在何处类似/偏离人类。 |
| 35 | Calibrating Teacher-Student Discrepancy for On-Policy Distillation | https://arxiv.org/abs/2609.21619 | Distillation, Calibration | 发现 OPD 中的 teacher-student 差异混入 teacher 自身偏差，提出校准方法净化蒸馏信号。 |

## 📚 RAG / 检索增强

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 36 | RAILS: Retrieval-Augmented Incremental LLM Clustering at Scale | https://arxiv.org/abs/2609.24464 | RAG, Clustering, Scale | 将聚类转化为对增长标签池的循环检索，解决生产规模 LLM 聚类的吞吐量与标签空间爆炸问题。 |
| 37 | Predictable Failure in Multi-Hop Retrieval: Score-Distributional Confidence Scoring | https://arxiv.org/abs/2609.22056 | RAG, Multi-Hop, Abstention | 证明多跳检索失败聚集在结构可预测的子群中，提出置信评分与弃权机制实现可预测的失败规避。 |
| 38 | Think Thrice Before Reranking: Multi-perspective Evidence and Reasoning Integration | https://arxiv.org/abs/2609.20131 | RAG, Reranking, Reasoning | 单条推理轨迹的重排序易受推理错误影响，融合多视角证据与推理提升文本排序鲁棒性。 |

## 🔒 Safety / 安全与对齐

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 39 | CASCADE Against Jailbreaks: Combination Across Stages | https://arxiv.org/abs/2609.21793 | Safety, Jailbreak, Defense | 统一攻击成功率定义与实验设置，系统评估各阶段越狱防御的组合部署策略。 |
| 40 | Xeno-Interpretability: Investigating the Alien Minds of LLMs | https://arxiv.org/abs/2609.20408 | Interpretability, Xeno-Representation | 提出"异星可解释性"：LLM 可能拥有人类概念无法描述的内部表征结构，需要新的研究范式。 |
| 41 | Geopolitical Divisions Across Languages in Large Language Models | https://arxiv.org/abs/2609.20005 | Bias, Multilingual, GPT/Claude/Gemini | 让 GPT/Claude/Gemini 用 112 种语言评估乌克兰战争 20 条陈述（67,200 条回复），发现语言改变政治判断。 |
| 42 | SupportCal: Label-Free Calibration of Post-Trained LLMs | https://arxiv.org/abs/2609.24303 | Calibration, Post-Training | 利用对应预训练模型作为无标注参考，解决 post-training 后 LLM 过度自信且缺乏标定数据的问题。 |

## 🔧 Other Highlights / 其他亮点

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 43 | World Modeling in Transformers | https://arxiv.org/abs/2609.21748 | Interpretability, World Model | 通过 TaxiGPT 的机理分析与因果干预，证明 Transformer 的内部世界模型可能因行为故障而被遮蔽。 |
| 44 | MATCH: Model-Aware Tool Learning with Curriculum Scheduling | https://arxiv.org/abs/2609.20082 | Tool Learning, RL, Curriculum | 课程调度与层级门控奖励解决工具学习 RL 中课程与能力边界错位、参数级信用泄漏两大问题。 |
| 45 | On Emergent Capabilities and Model Merging | https://arxiv.org/abs/2609.24504 | Model Merging, Emergent | 首次研究模型合并对涌现能力的影响，发现权重算术可能保留也可能破坏未显式训练的行为。 |
| 46 | Opinion Leader Dynamics: How Sparse Attention Shapes Token Clustering | https://arxiv.org/abs/2609.24202 | Attention, Theory, Sparse | 将 token 建模为球面粒子，揭示稀疏注意力通过意见领袖机制塑造 token 表征演化的两个原理。 |

---

## 📊 统计

- 候选论文总数：46 篇
- 来源分布：arXiv API 筛选 106 篇 → 人工精筛 41 篇；HF trending 补充 5 篇
- 类目覆盖：Agent(15), Multi-Agent(3), HF Trending(5), Efficiency(7), Reasoning(5), RAG(3), Safety(4), Other(4)
- 本周趋势：Agent harness/评估成为最热门方向；KV cache 压缩持续升温；on-policy distillation 在 Agentic 场景遭遇挑战
