# 论文池 2026-W38

> 收集日期：2026-09-15（周二）
> 覆盖范围：2026-09-08 ~ 2026-09-14（arXiv Mon, 14 Sep 2026 批次）
> 来源：arXiv cs.CL / cs.LG / cs.AI recent（HF Papers 网络不可达，PaperWeekly 无本周更新）
> 筛选关键词：LLM, Agent, Multi-Agent, RAG, Prompt Engineering, Chain-of-Thought, Reasoning, Long Context, Multimodal, 智能体, 大模型
> 排除：纯医学 AI、纯 CV（VLM 相关保留）

---

## 🤖 Agent / 智能体

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 1 | LifeMem: Enabling Lifelong Experience Reuse for LLM Agents | https://arxiv.org/abs/2609.12655 | Agent, Memory | 通过聚类交互轨迹提取可复用技能，实现跨环境终身经验迁移并减少灾难性遗忘。 |
| 2 | Agent as Policy for Robotic Manipulation | https://arxiv.org/abs/2609.12541 | Agent, Robotics | 通用 Agent 直接驱动物理机器人执行操作，无需任务特定训练，块构造达 100% 成功率。 |
| 3 | CueMem: Cue-Guided Context Reconstruction for Long-Term Conversational Memory | https://arxiv.org/abs/2609.12354 | Agent, Memory, Long Context | 将记忆记录视为检索线索而非自足证据，通过源轮次锚点在对话图上重建紧凑证据上下文。 |
| 4 | Cognition on Graph: Navigating Massive Knowledge Space via Cognitive Cycles | https://arxiv.org/abs/2609.12791 | Agent, RAG, Reasoning | 受人类问题求解启发，执行 plan-explore-reflect 循环，在图谱与文本间建立双向协同的多跳 QA 框架。 |
| 5 | What Drives Recovery in Agentic Text-to-Cypher? LAST-CQ | https://arxiv.org/abs/2609.12746 | Agent, Self-Refinement | 五 Agent 无训练 Text-to-Cypher 框架，发现失败检测+重试路由才是恢复关键，而非反馈精致度。 |
| 6 | GAUGE: When Not to Trust LLM-as-a-Judge in User-Simulated Evaluation of Task-Oriented Agents | https://arxiv.org/abs/2609.12191 | Agent, Evaluation | 揭示 LLM 用户模拟评估中满意度与任务成功脱钩（57.5% 满意对话实际失败），近等强 Agent 间排名失真率达 31%。 |
| 7 | Local Edits, Global Ripples: Replay-Informed Policy Adaptation for Workflow Synthesis | https://arxiv.org/abs/2609.12127 | Agent, Workflow | RIPPLE 分离"在哪里编辑"与"组合后是否安全"，通过重放暴露下游效应，工作流合成验证成功率提升 23.1%。 |
| 8 | Embodied-BenchForge: A Closed-Loop Agentic Workflow for Embodied Benchmark Construction | https://arxiv.org/abs/2609.13082 | Agent, Embodied, Benchmark | Agent 驱动的具身基准构建框架，前向合成+反向验证修复，产出 220 个可执行交互任务。 |
| 9 | Autonomous Research for Open-Ended Problems: Telecom Ticket Retrieval | https://arxiv.org/abs/2609.13073 | Agent, AutoML | 自主研究 Agent 在开放工业级问题上达 SOTA 的 90%，耗时 10 周 vs 人类 10 月，但缺乏人类直觉。 |
| 10 | Behavior Quotient Learning for Low-Rank Adaptation of LLM Agents | https://arxiv.org/abs/2609.12896 | Agent, LoRA | BQ-LoRA 在行为商流形上组织轨迹更新，解决多能力 LoRA 适配中的冗余与秩预算问题。 |
| 11 | SAGE-Loop: Reliable Closed-Loop LLM-Driven AutoML | https://arxiv.org/abs/2609.12455 | Agent, AutoML | 闭环 LLM 驱动 AutoML，试验-纠错+自适应集成策略，20 个数据集上分类/回归/聚类全面提效。 |
| 12 | Skill Issue: Lessons from Optimizing Repository SKILLs for Coding Agents | https://arxiv.org/abs/2609.12742 | Agent, Coding | 评估代码 Agent 的 SKILL.md 自动优化方法，发现 GEPA 平均提升 4.9pp，但与运行方差难以区分。 |
| 13 | K-Bench: A Benchmark for LLM Unlearning in Agentic Deployments | https://arxiv.org/abs/2609.12808 | Agent, Safety, Unlearning | 揭示模型级遗忘认证不适用于 Agent 部署：秘密可从 CoT/工具调用/观察中恢复，泄漏率 22-86%。 |
| 14 | VRL-Bench: Benchmarking Agents on Computer Control under Finite Trial Budgets | https://arxiv.org/abs/2609.12404 | Agent, RL, Benchmark | 评估 Reflexion 类言语强化学习在有限预算下的表现，提出 VEX² 调度器在全部 6 种设置中正收益。 |
| 15 | BlueLM-GUI: A Real-Device-Centric Flywheel for Self-Improving Mobile GUI Agents | https://arxiv.org/abs/2609.12394 | Agent, GUI | 35B-A3B 移动端 GUI Agent，真机飞轮训练，MobileGUI-VBench 87.4 超最强闭源 5.1 分。 |
| 16 | SoK: Rethinking Jailbreaking in the Era of Agentic AI | https://arxiv.org/abs/2609.12413 | Agent, Security, SoK | 系统化 Agentic AI 越狱攻击与防御，发现最终回复过滤成功仍可能掩盖中间层严重失陷。 |
| 17 | LifeFuse-Mem: Lifecycle-Aware State Fusion Against Temporary Overwriting | https://arxiv.org/abs/2609.12436 | Agent, Memory | 按生命周期分离持久与瞬态知识的神经记忆框架，防止临时上下文覆盖持久知识导致行为漂移。 |
| 18 | Information Specialization in Multi-Agent LLM Forecasting: 2026 FIFA World Cup | https://arxiv.org/abs/2609.12495 | Multi-Agent | 四 Agent 预测流水线的前瞻性实测：新闻专家表现最佳，但 critic/meta-agent 未产生互补信息。 |
| 19 | AMDKernelVault: Agentic Training for AMD GPU Kernel Optimization | https://arxiv.org/abs/2609.12471 | Agent, Code, Training | 62K+ 执行验证 HIP 核函数语料，Agent 驱动流水线训练 Qwen3-8B 达 PyTorch-to-HIP 34% Pass@1。 |

## 📏 Long Context / 长上下文

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 20 | SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking | https://arxiv.org/abs/2609.13141 | Long Context, Attention | 端到端优化上下文排序的注意力稀疏化方法，降低长上下文推理开销。 |
| 21 | Residual Vector-based Reconstruction as Long-Context Recall Regardless of Context Window Size | https://arxiv.org/abs/2609.12686 | Long Context, Memory | 利用 FFN 层残差向量确定性重建事实，200 万 token 故事中实现近恒定 GPU 内存召回。 |
| 22 | RunningTensor: Generalizing Linear Attention to Higher-Order Recurrent States | https://arxiv.org/abs/2609.12814 | Long Context, Attention | 将线性注意力记忆推广到高阶张量，工作记忆容量从 O(W²) 提升至 O(W^o)。 |

## 🧠 Reasoning / 推理

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 23 | Chopthin-Consensus Power Sampling: Diversity-Preserving LLM Decoding | https://arxiv.org/abs/2609.12243 | Reasoning, Decoding | Chopthin 重采样保留推理路径多样性，15 项设置中 14 项匹配或超越 Power-SMC，最高提升 10.6pp。 |
| 24 | Repair Before Reinforce: Context-Augmented KG Reasoning for Multi-Hop QA | https://arxiv.org/abs/2609.12230 | Reasoning, RAG, RL | 上下文增强监督+LLM 判断自适应修复+RL 三段式，多跳 QA 中低跳修复初始化带来更稳增益。 |
| 25 | Tasks over Application Manuals: Revealing Gaps in Long-Horizon Procedural Reasoning | https://arxiv.org/abs/2609.13005 | Reasoning, Benchmark | 基于应用手册的长程程序化推理基准，暴露语言模型在真实多步骤任务中的推理缺口。 |
| 26 | The Cost of Compression: A Rate-Distortion Limit on Factual Hallucination | https://arxiv.org/abs/2609.12111 | Reasoning, Hallucination, Theory | 信息论视角下的幻觉理论：有限内存导致事实有损压缩，给出覆盖-压缩误差下界。 |

## 🔍 RAG / 检索增强

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 27 | EAR: Entity-Aware Partitioning for RAG Development | https://arxiv.org/abs/2609.12268 | RAG | 以实体为锚点分割检索单元，检索词数减少 37.5-40.2%，提供紧凑可检查的 RAG 设计方法。 |
| 28 | R2VC: Modular Fact-Checking with Retrieval, Verification, and Confidence Calibration | https://arxiv.org/abs/2609.11955 | RAG, Fact-Checking | 模块化检索-推理-验证-校准架构，8B 骨干在 FEVER 上比基线高 13.74%，校准器是最大贡献者。 |
| 29 | Beyond Vector Similarity: Hierarchical Graph RAG vs Standard RAG in Enterprise Code Migration | https://arxiv.org/abs/2609.12464 | RAG, Graph, Code | 企业代码迁移中 Graph RAG 将 API 幻觉率从 56.4% 降至 16.2%，但引入防御性过度工程副作用。 |

## 🏋️ LLM Training / Alignment / 评测

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 30 | Expert-Space Exploration in MoE Reinforcement Learning | https://arxiv.org/abs/2609.13058 | LLM, MoE, RL | ESRL 在 MoE 专家路由空间中探索，RL 后训练改善大模型 MoE 的专家利用效率。 |
| 31 | SynthSentry: Detecting Synthetic Data Contamination in LM Training Data | https://arxiv.org/abs/2609.12353 | LLM, Data | 无需访问生成模型的语料级合成数据污染检测信号，三统计量分布散度实现零标签筛查。 |
| 32 | Distortion of AI Alignment Revisited: RLHF is a Decent Utilitarian Aligner | https://arxiv.org/abs/2609.12651 | LLM, RLHF, Alignment | 精细分析 RLHF 奖励截断失真，证明指数级退化源于分布失配而非算法本质，on-policy 数据可避免。 |
| 33 | Breaking the Token Ceiling: Distilling Smaller, Stronger Byte Models | https://arxiv.org/abs/2609.12303 | LLM, Tokenization, Scaling | 首次大规模对比 byte vs token 蒸馏：byte 模型低算力更差但终局更强，数据效率高 6 倍。 |
| 34 | From Collaboration to Capability: Internalizing Routed LLM Experts into Compact Reasoners | https://arxiv.org/abs/2609.12578 | LLM, Distillation | Rivet 将专家协作内化到 1.7B/4B 小模型，4B 数学推理达 44.16%，专家移除后仍提升 6.49 点。 |
| 35 | TripPattern: A Pattern-based Text Watermarking Method for Large Language Models | https://arxiv.org/abs/2609.12472 | LLM, Watermark | 基于模式的 LLM 文本水印方法，保持生成质量的同时嵌入可检测信号。 |
| 36 | Judging by the Cover: Cleaning LLM Truthfulness Benchmarks | https://arxiv.org/abs/2609.13003 | LLM, Benchmark, Truthfulness | 揭示 TruthfulQA 类基准存在表面特征泄漏，提出 Audit-Prune 清洗方法。 |
| 37 | Zipbench: Low-Cost Framework for Compressing Comprehensive Benchmarks | https://arxiv.org/abs/2609.12475 | LLM, Benchmark | 低成本基准压缩方法，100+ 基准代理实现 0.002-0.02 MAE 和 ~0.98 Spearman 相关。 |
| 38 | EvoRS: On-Policy Self-Evolution of Reward Systems for Open-Ended RL | https://arxiv.org/abs/2609.12459 | LLM, RL, Reward | 奖励系统应随策略共同演化：EvoRS 以 Reward-DAG 可执行形式从 on-policy 经验自我更新。 |
| 39 | Toward Robust Personalized Alignment: Mitigating Persona Drift in Multi-Turn Dialogue | https://arxiv.org/abs/2609.12373 | LLM, Alignment, Personalization | CORE 分离轮级证据与持久人格状态修订，通过不确定性感知信念修订缓解人格漂移。 |

## 🎨 Multimodal / 多模态

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 40 | Continue, Adapt, or Yield: In-Turn Adaptation to Overlapping Speech in Full-Duplex Agents | https://arxiv.org/abs/2609.13117 | Multimodal, Voice, Agent | 全双工语音 Agent 在轮次内适应重叠语音的策略评估：继续、适应还是让步。 |
| 41 | Kraken: LLM-based Speech-to-Speech Translation via Low-bitrate VQ | https://arxiv.org/abs/2609.13045 | Multimodal, Speech | 基于 LLM 的语音到语音翻译，低码率 VQ + 双路径源条件化。 |
| 42 | Calibrated Ambiguity in Multimodal Language Models | https://arxiv.org/abs/2609.12575 | Multimodal, VLM | VLM 在 Dixit 任务中表现出歧义坍缩（过度具体化）和文化扁平化，几乎不使用文化引用。 |
| 43 | Beyond Generation and Accuracy: Diagnosing Visual Chain-of-Thought for Geometry | https://arxiv.org/abs/2609.12606 | Multimodal, CoT | GeoVAD-Bench 诊断视觉 CoT 的五维错误模式，GeoWeave-8B 几何准确率提升 25.3%。 |
| 44 | MP-Bench: Evaluating Voice Agents as a Multiparty Conversation Participant | https://arxiv.org/abs/2609.13076 | Multimodal, Voice, Agent | 首个多方对话语音 Agent 基准：实时 Agent 多方理解≤22%，轮次切换接近随机水平。 |
| 45 | ProactiveBench: Can Streaming Video Models Really Interact Like Humans? | https://arxiv.org/abs/2609.12658 | Multimodal, Video | 流式视频模型主动交互基准：评估何时该响应/沉默，暴露时序决策差距。 |
| 46 | SteerDuplex: Steerable Duplex Speech Dialogue Models | https://arxiv.org/abs/2609.12623 | Multimodal, Voice | 全双工语音模型可控性研究，SFT 使音频引导通过率提升 44.5pp，RL 改善打断响应。 |

## 📊 Evaluation / 其他

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 47 | Do LLMs Trust the Accuser or the Accusation? Measuring Belief Shifts in Werewolf | https://arxiv.org/abs/2609.12446 | LLM, Social Reasoning | 狼人杀信念偏移基准：开源 LLM（≤120B）难以整合指控内容与来源信任，易被信任者误导。 |
| 48 | Implicit Personality Representations in Humans and LLMs | https://arxiv.org/abs/2609.12704 | LLM, Interpretability | Qwen2.5-7B 内部特质表征与人类内隐人格矩阵显著对齐（Mantel r=0.77），恢复社会温暖与智力能力两轴。 |
| 49 | EduFair-Bench: Evaluating Pedagogical Fairness of LLM Tutors | https://arxiv.org/abs/2609.12949 | LLM, Evaluation, Fairness | LLM 家教教学公平性审计：能力与公平性基本正交，最小模型反而最一致，RL 训练重新分配而非消除偏见。 |

---

共 49 篇候选。精选 ⭐ 推荐关注：

1. **K-Bench** (#13) — 遗忘认证在 Agent 部署下失效，安全评估必看
2. **GAUGE** (#6) — LLM-as-a-Judge 在 Agent 评估中的盲区
3. **LifeMem** (#1) — 终身经验复用的 Agent 记忆框架
4. **SoK: Jailbreaking** (#16) — Agentic AI 安全全景
5. **Graph RAG vs Standard RAG** (#29) — 企业级 RAG 的结构化升级路径
6. **RLHF Distortion** (#32) — 对齐理论的精细修正
7. **BlueLM-GUI** (#15) — 移动端 GUI Agent 新 SOTA
