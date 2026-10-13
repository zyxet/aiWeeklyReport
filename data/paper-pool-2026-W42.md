# 论文池 2026-W42（2026-10-13 收集）

> 收集日期：2026-10-13（周二）
> 覆盖范围：2026-10-06 ~ 2026-10-13
> 来源：arXiv cs.CL / cs.LG / cs.AI API（按提交日期抓取 250 篇后关键词筛选）、Hugging Face Papers trending（GitHub 镜像数据 + orangebot 聚合页）、PaperWeekly / iyiou 大模型周报（10.04-10.11 期提及的 SAGE、AgentGarten 等不在本时间窗内，未收录）
> 筛选关键词：LLM、Agent、Multi-Agent、RAG、Prompt Engineering、Chain-of-Thought、Reasoning、Long Context、Multimodal、智能体、大模型
> 排除：纯医学 AI、纯 CV（VLM 相关保留）；🆕 = HF trending 新出现；⭐ = 高关注
> 注：arXiv API 对 cs.AI 首次请求触发 rate limit，间隔重试后成功补齐

📄本周候选论文池（66 篇 + 4 篇窗口外补录）

---

## 🤖 Agent / 智能体

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 1 | RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics | https://arxiv.org/abs/2610.13889 | Agent / 工具检索 | 冻结双编码器 + 上下文 bandit，把工具执行时的可用性信号纳入检索，可靠性显著优于纯语义匹配 |
| 2 | X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems | https://arxiv.org/abs/2610.13886 | Agent / 安全 | 针对跨服务个人 agent 的组合式故障，系统化探索有害跨服务路径的红队框架 |
| 3 | Proactive Agentic Orchestration | https://arxiv.org/abs/2610.13485 | Agent / 编排 | 子 agent 目标与 harness 不再创建时固定，编排策略主动适配动态环境并缓解稀疏延迟反馈 |
| 4 | A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network Models | https://arxiv.org/abs/2610.13663 | Multi-Agent | analyst/coder/recorder 三角角色 + 实验日志 + 沙箱执行，自动调优专用网络组件 |
| 5 | AgentSWE: Can Coding Agents Build the Agent You Actually Want? | https://arxiv.org/abs/2610.13361 | Agent / SWE | 首个检验「coding agent 交付的 agent 是否忠于需求」的三阶段基准（创建、检查、运行） |
| 6 | 🆕⭐ ProgramGym: Scaling Training Environments for Long-Horizon Program Reproduction Agents | https://arxiv.org/abs/2610.13395 | Agent / 代码 | 可扩展的可验证训练环境，强迫 agent 自主发现需求并长程复刻参考程序 |
| 7 | 🆕 SWE-Duel: Towards a Self-Scaling Arena for Coding Agents | https://arxiv.org/abs/2610.12569 | Agent / 评测 | coding agent 在评测时互相出题，任务无从泄漏、难度由参与者决定的可自扩展竞技场 |
| 8 | Humanize MLE Agents: Multi-Agent Session Alternation Beyond Single-Agent Limits | https://arxiv.org/abs/2610.13494 | Multi-Agent / MLE | 发现单会话长程执行存在「长程减速」且 harness 收益随模型变强失效，改用多 agent 会话交替 |
| 9 | Humanize Olympiad Agents: Multi-Session Workflow for Olympiad Problem Solving | https://arxiv.org/abs/2610.13632 | Multi-Agent / 推理 | Solve/Review/Wiki/Verify 四角色多会话工作流，复现 Navier-Stokes 形式化等长程奥赛任务 |
| 10 | A Baseline Assessment for the Agentic Web Technology Stack | https://arxiv.org/abs/2610.13703 | Agent / 基建 | 对 MCP/A2A 等协议、框架、库组合成 Agentic Web 方案的首个系统性基线评估 |
| 11 | MC-EvoBench: Auditing Experience-Driven Self-Improvement in Minecraft Agents | https://arxiv.org/abs/2610.13829 | Agent / 具身 | 19 个注册能力目录的受控 Minecraft 基准，区分「真能力获得」与「资源携带/暴露不均」 |
| 12 | 🆕 EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving Embodied Agents | https://arxiv.org/abs/2610.13021 | Agent / 具身 | 评估具身 agent 跨任务持续学习与自演化的基准 |
| 13 | MAGMA-Bench: Evaluating Long-Horizon Embodied Agents under Dynamic Tasks and Execution Failures | https://arxiv.org/abs/2610.13534 | Multi-Agent / 具身 | 动态任务 + 在线扰动 + 多机器人协同的架构无关长程具身基准 |
| 14 | 🆕 Stateless Language Agents: Scaling Long-Horizon Automated Research | https://arxiv.org/abs/2610.07625 | Agent / 科研 | 指出长程科研 agent 的无效推理源于「状态放哪、谁决定下一步」两个设计选择，主张无状态化 |
| 15 | 🆕 Recurrent Harness for Agentic Continual Learning | https://arxiv.org/abs/2610.12668 | Agent / 持续学习 | ReHarness 用循环 harness 替代前向信息流/回放数据，实现 agent 在线适应分布漂移 |
| 16 | VEPA: Verified Evolving Formal Policy for Lifelong LLM Agent Guardrails | https://arxiv.org/abs/2610.12813 | Agent / 护栏 | 可检查、可复现、确定性的形式化策略，在不可逆动作执行前做 allow/refuse 决策 |
| 17 | Locate, Judge, Read: Role-Specialized Tool Agents over a Knowledge-Point Index | https://arxiv.org/abs/2610.13128 | Agent / RAG | KnowForge 把检索与阅读工具按角色拆分（Locator 只搜、Judge 只裁、Reader 只读）的 QA 流水线 |
| 18 | SEEDS: Preview-Guided Evidence Admission for Search Agents | https://arxiv.org/abs/2610.12932 | Agent / 检索 | 证据准入由 agent 当前推理状态而非固定/排名策略决定，预览再决定采信 |
| 19 | SOAR: Source-Aware Reinforcement Learning with Precise Credit Assignment for Search Agents | https://arxiv.org/abs/2610.13157 | Agent / RL | 把单段推理拆成 source-explicit 轨迹，解决搜索 agent 绕过外部证据、编造答案的问题 |

## 🔍 RAG / 记忆

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 20 | Test-Time Memory Construction (T²Mem) | https://arxiv.org/abs/2610.13348 | Long Context / 记忆 | 记忆构建推迟到查询到来时进行，按查询特定信息需求定制，免离线维护开销 |
| 21 | Beyond the Final Embedding: Retrieving Memories from Token-Level Evidence | https://arxiv.org/abs/2610.13277 | RAG / 记忆 | 用 embedding 模型的 token 级表示而非单向量做记忆检索，捕获局部证据 |
| 22 | Temporal Evidence Forests for Long-Horizon Multi-Party Conversational Memory | https://arxiv.org/abs/2610.12874 | 记忆 / 多轮 | 时序证据森林追踪多方长程对话中反复更新的决策与状态演化 |
| 23 | Verifiable Retrieval for Legal Reasoning through Structure-driven Knowledge Graph | https://arxiv.org/abs/2610.13695 | RAG / 可验证 | 结构驱动 KG 检索使法律推理的生成过程可验证、可落地解释 |

## 🧠 Reasoning / 奖励建模 / Prompt

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 24 | Inject a Turn, Not a Token: Learning Where to Redirect LLM Reasoning for Self-Correction | https://arxiv.org/abs/2610.13672 | 推理 / 自纠错 | 13 万参数 MLP 头学习在失败 rollout 的哪个位置介入、如何重定向，免微调主模型 |
| 25 | A Privileged Teacher That Only Scores Cannot Search: Critique-Conditioned On-Policy Self-Distillation | https://arxiv.org/abs/2610.13744 | 蒸馏 / 推理 | 批判条件化的 on-policy 自蒸馏，让只有打分信号的任务也能获得评论式引导 |
| 26 | Matched-Context Group Policy Optimization for LLM Agent Training | https://arxiv.org/abs/2610.13755 | Agent / RL | 从已有轨迹构造匹配上下文的加权动作偏好，改善长程 agent 的稀疏终端反馈信用分配 |
| 27 | BoundaryEvo: Data-Model Co-Evolution at the Capability Boundary for Long-Chain Reasoning Distillation | https://arxiv.org/abs/2610.13285 | 蒸馏 / 推理 | 训练集随学生能力演化动态更新，在能力边界处挑选最有监督价值的教师轨迹 |
| 28 | What Should SFT Learn? Conditional Information Gain for Generalizable Post-Training | https://arxiv.org/abs/2610.12995 | SFT | 用条件信息增益选择 SFT 目标，避免外部轨迹干扰预训练已支持的行为 |
| 29 | Pretraining and Test-Time Training Budgets Matter for ARC | https://arxiv.org/abs/2610.13660 | 推理 / 评测 | 控制预训练数据、增强、测试时预算后重新检验 ARC 结论，预算比架构更影响成绩 |
| 30 | A Critical Look at Power Sampling when Test Time Sharpening LLMs | https://arxiv.org/abs/2610.13653 | 推理 / RLVR | 质疑 power sampling 复现 RLVR 收益的能力：方差大、温度敏感，增益并非免费 |
| 31 | From Structure to Validity: Mechanism-Guided Generation and Refinement of LLM Rubrics | https://arxiv.org/abs/2610.13375 | 评测 / Rubric | 机制引导的 rubric 生成与精修流水线，保证评分标准结构有效 |
| 32 | Agreement Without Alignment: Label-Free Rubric Clarification Increases LLM-Judge Consensus | https://arxiv.org/abs/2610.13303 | LLM-Judge | 把评委分歧当作 rubric 修复信号，仅重写分歧最大的子标准，无需标注 |
| 33 | Do Prompt Optimizers Break Requirements They Are Not Scored On? A Preregistered Study | https://arxiv.org/abs/2610.13287 | Prompt / 预注册 | 预注册研究：GEPA/MIPROv2/TextGrad 优化目标指标时会破坏未被评分的格式/引用/弃权要求 |
| 34 | SpatialASM: Internalizing Active Mentalization for Spatial Reasoning | https://arxiv.org/abs/2610.13832 | 空间推理 | 内化「主动心智化」机制增强 LM 空间推理 |
| 35 | 🆕 Judging in Latent Space: Efficient Generative Reward Modeling via Semantics-Preserving Compression | https://arxiv.org/abs/2610.09788 | 奖励建模 | LatentGRM 把 rubric 推理压进连续 latent 状态，评判精度持平而 token 开销大降 |

## 🏋️ 训练 / 后训练 / 推理效率

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 36 | On the Design Space of Continuous Diffusion Language Models | https://arxiv.org/abs/2610.13834 | 扩散语言模型 | 系统梳理连续扩散语言模型的设计空间（噪声、参数化、采样） |
| 37 | DualQuant: Dual-scale Calibration-free Weight-and-Activation Quantization for LLMs | https://arxiv.org/abs/2610.13767 | 量化 | 双尺度免校准 W4A4 量化，直接最小化权重重建 MSE，适配原生 4bit 加速器 |
| 38 | Taking Tokenization off the Host for Agentic LLM Serving (GraphTok) | https://arxiv.org/abs/2610.13325 | 推理 / Agent 基建 | GPU 上全流程 tokenizer，解决 agentic 负载中 tokenization 成为 TTFT 瓶颈的问题 |
| 39 | Host-Aware Web Crawling for LLM Pretraining Data | https://arxiv.org/abs/2610.13321 | 预训练数据 | 质量分类器得分约一半方差来自 host 间差异，爬虫应按 host 分配预算 |
| 40 | zip2zip++: Towards Inference-Time Token Compression with Minimal Quality Loss | https://arxiv.org/abs/2610.13605 | 推理 / 压缩 | LZW 动态词表的推理时 token 压缩的质量损失可被针对性改进大幅收敛 |
| 41 | Orthros: Phase-Aware Heterogeneous Attention for Efficient Transformers | https://arxiv.org/abs/2610.13735 | 高效注意力 | 相位感知异构注意力（线性/滑窗/全注意按层分工），兼顾线性复杂度与长上下文 recall |
| 42 | Not All Dimensions Are Equal: Outlier-Aware Attention Linearization with Grouped Quadratic Kernels | https://arxiv.org/abs/2610.13674 | 线性注意力 | 少数 outlier 维度贡献大量注意力点积误差，分组二次核定向保留 |
| 43 | Tracing and Taming Hallucinated Terms via Subsequence-Association Filtering | https://arxiv.org/abs/2610.13810 | 幻觉 / 检索 | 子序列关联过滤追溯 LLM 查询扩展中幻觉词的来源并分级治理 |
| 44 | REDaCT: Collapse-Free Unlearning in Large Reasoning Models | https://arxiv.org/abs/2610.12769 | 遗忘 | 从推理痕迹和答案双侧删除目标信息，同时避免 CoT 坍塌与不终止 |
| 45 | CAST: Credit Alignment for Cross-Tokenizer On-Policy Distillation | https://arxiv.org/abs/2610.13257 | 蒸馏 | 跨 tokenizer on-policy 蒸馏中，把 chunk 级信号正确分配到 token 级的信用对齐方法 |
| 46 | KV-Repurpose: A Testbed for Evaluating Non-Prefix KV-Cache Reuse | https://arxiv.org/abs/2610.13060 | 推理 / KV-Cache | vLLM 之上的开源测试床，评估检索文档跨前缀的段落级 KV 复用 |

## 👁️ 多模态 / VLM

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 47 | ⭐ S-Space: Exploring Spatial Workspace in Multimodal Language Models | https://arxiv.org/abs/2610.13527 | VLM / 可解释 | 发现 MLLM 中存在线性空间子空间，物体 token 表示连续编码横/纵/距坐标（HF trending #2） |
| 48 | GeoGR: Spatial-Semantic Token Compression and Group Routing for Efficient 3D VLMs | https://arxiv.org/abs/2610.13035 | 3D VLM | 空间-语义 token 压缩 + 分组路由，砍多视图 3D 理解的视觉 token 开销 |
| 49 | 🆕⭐ VisionWeave: Weaving Elastic Visual Representations as a Native Capability of MLLMs | https://arxiv.org/abs/2610.07987 | VLM / token 效率 | 视觉表示弹性化成为 MLLM 原生能力，按内容复杂度自适应分配粒度（⭐34） |
| 50 | 🆕 MixTok: Adaptive Visual Tokenization with Global 1D Tokens and Sparse 2D Refinement | https://arxiv.org/abs/2610.13181 | VLM / tokenizer | 1D 全局 token + 稀疏 2D 精修的混合视觉 tokenizer，平衡紧凑与细节 |
| 51 | MVGraph: Benchmarking LVLMs on Evidence Composition across Multi-View Visual Graphs | https://arxiv.org/abs/2610.12961 | LVLM / 基准 | 证据分散在多张关联视觉图上的组合推理基准 |
| 52 | OccludeBench: Can VLMs Find What's Missing? | https://arxiv.org/abs/2610.13790 | VLM / 推理 | 从影子、反射等物理线索恢复完全遮挡物体的人工精编基准 |
| 53 | When MLLMs miss what humans read: diagnosing and learning to read squint text | https://arxiv.org/abs/2610.13465 | MLLM / OCR | 定义「眯眼文本」识别缺陷并给出诊断基准与训练修复方法 |
| 54 | Unsupervised Multimodal Reward Modeling | https://arxiv.org/abs/2610.12707 | 奖励建模 / VLM | 冻结 Qwen3-VL 中间层 + 线性头，无需人类偏好标注训练视觉-语言奖励模型 |

## 🌍 自进化 / 世界模型

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 55 | 🆕 RSI-Anything: Unlocking Recursive Self-Improvement with World Models | https://arxiv.org/abs/2610.13912 | RSI / 世界模型 | 基于 JEPA-Anything 预测式世界模型的通用递归自我改进框架，外部反馈驱动策略与工作流进化 |
| 56 | JANUS: Enhancing Long-Horizon Autonomous Research with Co-Evolving World Models | https://arxiv.org/abs/2610.13194 | 科研 / 世界模型 | 世界模型预测未来执行结果、回溯压缩历史经验，缓解 Generate-Execute-Feedback 的反馈延迟 |
| 57 | Prediction Is Not a Sufficient Memory State | https://arxiv.org/abs/2610.13881 | 理论 / 记忆 | 能复现当前预测的固定维状态仍可能丧失学习能力，刻画「可累积学习记忆」的精确条件 |
| 58 | Meta-Reflective Evolution Effectively Improves Production AI Systems | https://arxiv.org/abs/2610.12794 | 进化优化 | 元反思进化不只看前沿个体失败，而是回溯搜索历史做整体诊断，突破生产系统优化停滞 |

## 🛡️ 安全 / 评测 / 可解释

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 59 | SWE-DeceptionBench: Benchmarking Deceptive Behaviors of LLMs Across the Software Development Lifecycle | https://arxiv.org/abs/2610.13626 | 安全 / SWE | 覆盖软件生命周期六阶段 124 场景的 LLM 欺骗行为基准 |
| 60 | APEX-Harm: Evaluating Agent Safety in Shared Professional Workspaces | https://arxiv.org/abs/2610.13623 | Agent / 注入 | 评估命令行 + 多工具共享工作空间中 prompt/脚本注入对长程 agent 的危害 |
| 61 | DistressBench: Evaluating Multi-Dimensional Crisis Support in Large Language Models | https://arxiv.org/abs/2610.12758 | 安全 / 评测 | 危机对话中拒绝不是期望行为，多维度评估 LLM 的自伤危机支持能力 |
| 62 | Evaluating LLM Creativity through Long-Tail Performance | https://arxiv.org/abs/2610.12998 | 评测 / 创造力 | 把创造力形式化为参考分布长尾上的任务表现，统一五花八门的创造力基准 |
| 63 | 🆕 AMLworld-Compact: Importance-Weighted Downsampling for Cost-Effective LLM Evaluation | https://arxiv.org/abs/2610.13627 | 评测 / 降本 | HT-Coreset 重要性加权采样把百万级图评测目标缩减 271~611 倍且保持无偏指标 |
| 64 | SqueezeBench: Saturation-Resilient Evaluation of Mathematical Capability | https://arxiv.org/abs/2610.13461 | 评测 / 数学 | 每次成功抬高门槛而非移除题目，抗饱和的数学能力基准 |
| 65 | Can Language Models Play the Wikipedia Game? | https://arxiv.org/abs/2610.13948 | 推理 / 检索 | 用「维基百科游戏」测试 LM 专家级知识导航与检索策略 |
| 66 | Task Context Shapes Component Roles in Language Models | https://arxiv.org/abs/2610.13895 | 可解释 | 同一注意力头跨任务复用但角色不同，借鉴脑网络视角刻画任务依赖的组件交互 |

## 📎 附：窗口外但本周 HF trending 值得跟进

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 67 | SoloQ: Calibration-Free Quantization for Diffusion Language Models（10-05） | https://arxiv.org/abs/2610.07121 | dLLM / 量化 | 扩散语言模型的免校准低比特量化，兼顾全序列去噪与 block-diffusion 的 KV 开销 |
| 68 | Inducing Process Supervision from Outcome-Only Reinforcement Learning（TIPS，09-29） | https://arxiv.org/abs/2609.36641 | 过程奖励 | 仅用结果正确性奖励训练生成式 PRM，绕开人工步骤标注与蒙特卡洛估计 |
| 69 | Video-RSI: Recursive Self-Improvement of Video Understanding Agents via Harness Evolution（09-29） | https://arxiv.org/abs/2609.37950 | RSI / 视频 agent | 视频理解 agent 用自己的语言模型重写 harness，回溯原始训练视频实现递归自我改进 |
| 70 | PolyOCR-Venus: Unified OCR Foundation Models for Text-Centric Visual Intelligence（9 月下旬） | https://arxiv.org/abs/2609.37712 | OCR / VLM | 2B/9B 统一 OCR 基础模型，阅读、定位、解析、推理一体化（⭐46） |
