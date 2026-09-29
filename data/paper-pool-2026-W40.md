# 论文池 2026-W40

> 收集日期：2026-09-29（周二）
> 覆盖范围：2026-09-22 ~ 2026-09-28（arXiv Mon, 28 Sep 2026 批次）
> 来源：arXiv cs.CL / cs.LG / cs.AI API（HF Papers 直连不可达；PaperWeekly 无本周更新）
> 筛选关键词：LLM, Agent, Multi-Agent, RAG, Prompt Engineering, Chain-of-Thought, Reasoning, Long Context, Multimodal, 智能体, 大模型
> 排除：纯医学 AI、纯 CV（VLM 相关保留）

---

## 🤖 Agent / 智能体

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 1 | CAIRN: Dynamic Fact-Intent DAGs for Multi-Agent Exploration | https://arxiv.org/abs/2609.32700 | Agent, Multi-Agent, DAG | 用动态事实-意图 DAG 组织多 Agent 探索，解决长期自主系统中可靠性衰减问题。 |
| 2 | OptiArena: Can LLMs Improve Executable Algorithms under Fixed Resource Budgets? | https://arxiv.org/abs/2609.32227 | Agent, Coding, Benchmark | 预算控制测试台评估 LLM 作为编码 Agent 在有限资源下改进可执行算法的能力。 |
| 3 | AsynCodeBench: Benchmarking Collaboration of Asynchronous Multi-Agent Systems in Software Engineering | https://arxiv.org/abs/2609.32662 | Agent, Multi-Agent, Coding | 首个异步多 Agent 协作编码基准，评估复杂开发任务分解到不同专业 Agent 的协作效能。 |
| 4 | Choir: An Open Protocol for Distributed Multi-Agent Autoformalization | https://arxiv.org/abs/2609.31903 | Agent, Protocol, Formalization | 开放协议实现分布式多 Agent 数学形式化，打破单一团队集中运行所有 Agent 的算力瓶颈。 |
| 5 | On Evaluating and Improving Conversational Agents in Production | https://arxiv.org/abs/2609.32092 | Agent, Production, Evaluation | 大规模生产级多 Agent 购物助手的评估与改进框架，报告离线评估三大实际障碍。 |
| 6 | When Users Change Their Minds: Measuring and Repairing Intent Drift in LLM Agents | https://arxiv.org/abs/2609.32520 | Agent, Multi-Turn, Intent | 研究多轮交互中用户意图变更导致的 intent drift，提出测量与修复方法。 |
| 7 | Adaptive Consistency Graph for Long-Horizon Agents | https://arxiv.org/abs/2609.32754 | Agent, Long-Horizon, Consistency | 长序列依赖动作中 Agent 性能退化问题，用自适应一致性图维护执行状态。 |
| 8 | Clarify the User or Verify the World? Uncertainty Routing for Proactive Agents | https://arxiv.org/abs/2609.32255 | Agent, Tool Use, Uncertainty | 工具使用 Agent 在"向用户澄清"与"验证世界"间的不确定性路由决策。 |
| 9 | Do Audio LLMs Listen Before They Act? Diagnosing Acoustic-Context Gating in Voice Agents | https://arxiv.org/abs/2609.32536 | Agent, Audio, Benchmark | 音频 LLM Agent 是否真正"听懂再行动"——VGBench 诊断声学上下文门控能力。 |

## 🧠 Multi-Agent / 多智能体

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 10 | Agentsensus: Consensus-Compressed Shared Memory for Multi-Agent Story Worlds | https://arxiv.org/abs/2609.32297 | Multi-Agent, Memory, RAG | 多 Agent 故事世界中用共识压缩共享记忆替代私有记忆流，消除事件重复存储。 |
| 11 | Improving LLM Collaboration via Multi-Agent Preference Learning | https://arxiv.org/abs/2609.32827 | Multi-Agent, RL, Preference | 多 Agent 偏好学习改进 LLM 协作，解决构建可靠奖励信号的实际困难。 |
| 12 | Black-Box Auditing of Epistemic Reliability in Multi-Agent Debate Distillation | https://arxiv.org/abs/2609.32361 | Multi-Agent, Debate, Audit | 黑盒审计多 Agent 辩论蒸馏中弱验证器的认识可靠性，发现监控任务增益无法迁移。 |
| 13 | Multi-agent Scaling Across Disjunctive and Compensatory Tasks | https://arxiv.org/abs/2609.31563 | Multi-Agent, Scaling | 引入 Steiner 群体任务分类学，揭示多 Agent 系统规模扩展行为依赖任务结构。 |
| 14 | Financial Fragility in Societies of LLM Agents: Coordination Failures and Stabilizing Mechanisms | https://arxiv.org/abs/2609.30940 | Multi-Agent, Simulation, Finance | LLM Agent 社会的金融脆弱性：个体理性导致集体协调失败，提出稳定化机制。 |

## 🔗 Reasoning / 推理

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 15 | InterTab: Interleaved Visual-Structure Alignment for Multi-Modal Table Reasoning | https://arxiv.org/abs/2609.32660 | Reasoning, Multimodal, Table | 表格图像推理中交替视觉-结构对齐，逐步定位行列单元格。 |
| 16 | The Alignment Paradox: How Post-Training Amplifies Confident Hallucinations | https://arxiv.org/abs/2609.32617 | Reasoning, Alignment, Hallucination | 后训练放大自信幻觉——LLM 以高置信度产生事实错误答案，破坏基于不确定性的错误检测。 |
| 17 | MM-OPD: Towards One More Bottleneck Between Perception and Reasoning | https://arxiv.org/abs/2609.32690 | Reasoning, Multimodal, VLM | 揭示多模态 LLM 感知与推理之间的额外瓶颈，隐式假设的"无缝过渡"并不成立。 |
| 18 | Overwhelmed by Choice: Studying LLM Decision Making at Scale | https://arxiv.org/abs/2609.32809 | Reasoning, Benchmark, Choice | 大规模候选集下 LLM 决策能力研究——选项数量如何影响推理与决策评估。 |
| 19 | Does CoT-Pass@k Really Check the CoT? A Multilingual Mathematical Audit | https://arxiv.org/abs/2609.32622 | CoT, Reasoning, Multilingual | CoT-Pass@k 是否真正检查推理链？多语言数学审计质疑幸运猜测与可靠推理的等效处理。 |
| 20 | Explaining Textual Entailment with Lexical Entailments | https://arxiv.org/abs/2609.32491 | Reasoning, Entailment, LLM | 用 LLM 提供词汇关系支撑形式化文本蕴涵证明，探索 LLM 隐式词汇知识的实际利用程度。 |

## 📚 RAG / 检索增强

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 21 | LogicTree-RAG: Logic Tree-guided Retrieval-Augmented Generation for Long-form Patent Drafting | https://arxiv.org/abs/2609.30943 | RAG, Reasoning, Long-form | 逻辑树引导的 RAG 生成长篇专利文书，兼顾全局一致逻辑与事实准确性。 |
| 22 | Stale-Document Poisoning: When Outdated Retrieval Overrides Correct Model Answers | https://arxiv.org/abs/2609.31342 | RAG, Safety, Temporal | 过期检索文档可覆盖模型正确回答——识别 RAG 的时间错位风险。 |
| 23 | Distance-KV: Exploiting Relative Distance for Efficient Long-Context Inference | https://arxiv.org/abs/2609.32663 | RAG, KV Cache, Long Context | 利用相对距离优化长上下文推理的 KV cache 压缩策略。 |
| 24 | CoWindow Attention: Full Causal Coverage Is a Collective Property | https://arxiv.org/abs/2609.32704 | RAG, Attention, Efficiency | 全因果注意力是集体属性——CoWA 减少冗余计算与内存流量。 |

## ⚡ Efficiency / 推理效率

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 25 | PC-SubMax: Efficient Prompt Compression via Regularized Submodular Maximization | https://arxiv.org/abs/2609.32474 | Efficiency, Prompt Compression | 正则化子模最大化实现高效 prompt 压缩，缓解 lost-in-the-middle 现象。 |
| 26 | KV-Lingo: Learning KV-Cache Translators with Distillation | https://arxiv.org/abs/2609.32610 | KV Cache, Distillation | 学习跨模型 KV cache 翻译器，解决不同架构/权重模型间缓存表示不兼容问题。 |
| 27 | Routing Drift Alone Does Not Diagnose Failure in Merged MoE LLMs | https://arxiv.org/abs/2609.32821 | MoE, Model Merging | 合并 MoE 模型中的路由漂移 alone 不足以诊断失败，需更细粒度分析。 |
| 28 | CacheReforge: Bounded Recovery for Stale KV Caches under Evolving Adapters | https://arxiv.org/abs/2609.30884 | KV Cache, Adapter, Long Context | 轻量适配器演进导致 KV 缓存过期，提出有界恢复方法。 |
| 29 | The KV Cache Is the New Memory Wall | https://arxiv.org/abs/2609.30854 | KV Cache, Inference, Memory | 长上下文自回归推理的瓶颈从模型权重转移到 KV cache——内存带宽成为新瓶颈。 |

## 🔒 Safety / 安全与对齐

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 30 | LLM Alignment--Utility Asymmetry under Semantic-Preserving Transformations | https://arxiv.org/abs/2609.32717 | Safety, Alignment, Robustness | LLM 对齐在语义保持变换下的稳定性——对齐-效用不对称性揭示输入分布偏移风险。 |
| 31 | AnchorRep: Defending LLMs Against Cross-Model Adversarial Transfer via Representation Repulsion | https://arxiv.org/abs/2609.32602 | Safety, Jailbreak, Defense | 表示排斥防御跨模型对抗攻击转移，阻止白盒攻击者侵入架构不同的模型。 |
| 32 | Understanding the Role of Prompt Template in Knowledge Distillation for Safety Alignment | https://arxiv.org/abs/2609.30802 | Safety, Distillation, Alignment | Prompt 模板选择显著影响安全对齐蒸馏的鲁棒性，SFT 阶段的模板设计至关重要。 |

## 🏋️ Training / 训练与后训练

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 33 | Fewer Tokens, More Self-Teaching: On-Policy Self-Distillation for Extreme Visual Token Reduction | https://arxiv.org/abs/2609.32353 | Training, Multimodal, Distillation | 极端视觉 token 缩减下的 on-policy 自蒸馏，保持 MLLM 性能同时大幅加速。 |
| 34 | Understanding and Exploiting Anisotropy in Post-Training | https://arxiv.org/abs/2609.32792 | Training, RL, Fine-tuning | 理解后训练中的各向异性——SFT 前向 KL 与 RL 反向 KL 目标的空间分布差异。 |
| 35 | ScopeIF: Improving Scope-Aware Precise Instruction-Following via Graded Reward Modeling | https://arxiv.org/abs/2609.32189 | Training, Reward Model, Instruction | 分级奖励模型改进范围感知精确指令遵循，提升复杂应用场景的约束满足度。 |
| 36 | User Model Extraction via Belief Self-Distillation | https://arxiv.org/abs/2609.31603 | Training, Distillation, User Model | 通过信念自蒸馏提取 LLM 隐式用户模型，使不可视察的用户信念可因果操纵。 |

## 🖼️ Multimodal / 多模态

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 37 | From Knowing to Abstaining: Bridging the Representation-Action Gap in Vision-Language Models | https://arxiv.org/abs/2609.32653 | Multimodal, VLM, Abstention | VLM 的"知道"到"弃答"鸿沟——表示-行动差距使模型无法正确弃答不可答问题。 |
| 38 | Mandela-Bench: Multimodal Models Remember Canonical Images Instead of Seeing Them | https://arxiv.org/abs/2609.32763 | Multimodal, Benchmark, Safety | 多模态模型记住而非"看到"经典图像——AI 编辑检测的基准测试。 |
| 39 | EAServe: Encode-Aware Disaggregated Serving for Multimodal Large Language Models | https://arxiv.org/abs/2609.31551 | Multimodal, Serving, Disaggregation | 多模态 LLM 的感知编码器感知分离服务，优化 Prefill/Decode/Encode 三阶段资源分配。 |
| 40 | The Linear Representation Hypothesis for Vision-Language-Action Models | https://arxiv.org/abs/2609.30996 | Multimodal, VLA, Representation | 视觉-语言-动作模型中的线性表示假设验证，扩展 LLM 语义干预方法到 VLA。 |

## 📊 Benchmark / 评估

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 41 | LLMAdBench: A Human Preference Benchmark for Advertising in LLM Responses | https://arxiv.org/abs/2609.32533 | Benchmark, Advertising, Preference | LLM 回复中广告插入的人类偏好基准，评估广告对用户体验的影响。 |
| 42 | USAI-Quant: A Quantitative Reasoning Benchmark for Vision-Language Models in Built Environments | https://arxiv.org/abs/2609.32813 | Benchmark, VLM, Quantitative | 建筑环境中 VLM 定量推理基准，揭示遥感与空间 AI 的推理短板。 |

## 💡 Prompt / 提示工程

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 43 | The Decomposition Tax: LLM Pipelines Lose Up to 40 Accuracy Points at Their Own Interfaces | https://arxiv.org/abs/2609.32825 | Prompt, Pipeline, Decomposition | 四阶段 LLM pipeline 在自身接口处损失高达 40.5 个准确率点——分解税的量化研究。 |
| 44 | Learning an Anchored Prompt Space for Continual Adaptation of Large Language Models | https://arxiv.org/abs/2609.32499 | Prompt, Continual Learning, Adaptation | 锚定 prompt 空间实现 LLM 持续适应，联合调参与任务特定软 prompt 保持旧能力。 |

## 🔧 General / 其他

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 45 | MixDetect: Word-Level Localization and Quantification of AI Editing | https://arxiv.org/abs/2609.32625 | General, Detection, AI Editing | 词级别 AI 编辑定位与量化——区分全量 AI 生成与局部 AI 修改的检测方法。 |
| 46 | Attribution Gaps in Zero-Training LLM+OVOD Pipelines | https://arxiv.org/abs/2609.32567 | General, OVOD, Analysis | 零训练 LLM+开放词汇检测 pipeline 中定位精度与语义命名精度之间的归因差距。 |

---

📄 **本周候选论文池（46 篇）**
