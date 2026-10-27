# 📄 本周候选论文池（14 篇）

> **收集日期：** 2026-10-27（周二）
> **覆盖周期：** 2026-10-20 ~ 2026-10-27
> **来源：** arXiv cs.CL/cs.LG/cs.AI recent、Hugging Face Papers trending、Atlas LLM Briefing（筛选 2774 条记录）、kimi_search 定向检索
> **备注：** arXiv API 直连超时，改用 kimi_fetch 逐篇抓取验证。含 3 篇周期边界外（10/16-19）但本周持续 trending 的论文，已标注。

---

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|------------|
| 1 | Agent S4: Evolving Agent Interfaces | https://arxiv.org/abs/2610.28601 | Agent, GUI Agent, Self-Evolving | Simular 的"计算机使用科学家"——meta-agent 通过群体进化自动构建和修订 agent 的工具接口，将开源 Qwen3.8-27B 在 OSWorld 2.0 上从 5.6% 提升到 21.3%（$1.10/任务），性能对标 Claude Opus 4.8 但成本仅 1.5%。 |
| 2 | LiveUIBench: Evaluating Agent as App Workflows | https://arxiv.org/abs/2610.27977 | Agent, Benchmark, App Generation | 提出 "Agent as App" 任务——agent 不仅生成个性化应用还需在使用中持续维护行为，基准测试显示当前模型局部检查通过率尚可但整体工作流完成率极低。 |
| 3 | RAW-RAG: Direct Retrieval from Raw Conversation History | https://arxiv.org/abs/2610.30755 | RAG, Memory, Long Context | 用密集检索+重排序直接从原始对话历史检索，在 7 个基准中的 6 个上击败所有复杂记忆系统（Mem0 等），质疑记忆抽取/摘要/改写模块的必要性。 |
| 4 | UserArena: Benchmarking Interactive User Simulation for Long-Horizon Shopping Agents | https://arxiv.org/abs/2610.30932 | Agent, Benchmark, User Simulation | 包含 11,010 个用户、64,729 个会话的长周期购物智能体用户模拟基准，系统评估了 RecAgent/Agent4Rec/SimUSER 等用户模拟方法。 |
| 5 | RSIHub: A Composable Framework for Agent-Evolution | https://arxiv.org/abs/2610.32253 | Agent, Self-Evolution, Framework | 可组合的 agent 进化框架，将 agent 自我进化拆为可复用 recipe，HF ⭐186，支持四种进化方法在两种种子 agent 上统一评估。 |
| 6 | NgramRL: Accelerating RL Post-Training via Rollout-Aware N-gram Speculative Decoding | https://arxiv.org/abs/2610.32881 | RL, LLM Training, Efficiency | 用 per-prompt n-gram 缓存替代 GPU 常驻 draft model 加速 GRPO rollout，稳态下每目标前向提交 3.6-7.8 token，比 SuffixDecoding 快 1.2-2.0×。 |
| 7 | OPST: On-Policy Self-Training — Data-Free Self-Improvement in LLMs | https://arxiv.org/abs/2610.32770 | Self-Training, Reasoning, Data-Free | 从粗粒度主题标签出发，模型自行生成问题/答案/推理链，经共识式伪验证过滤后用 EMA teacher 做 on-policy 自训练，实现无外部数据的自我提升。 |
| 8 | LEMS: Advancing SVD-based LLM Compression via Layer-Wise Error Model Search | https://arxiv.org/abs/2610.32878 | LLM Compression, Efficiency, ICML 2026 | 用层间误差传播模型+整数线性规划做 SVD 压缩的全局秩分配，零样本准确率超最优基线 1.7-4.8 个百分点（ICML 2026 正式发表）。 |
| 9 | TopKLoRA: Interpretable Sparse Fine-Tuning Enables Faithful Circuit Discovery | https://arxiv.org/abs/2610.32866 | Interpretability, Safety, LoRA | 仅激活 top-k adapter latent 的稀疏微调方法，使后门电路的因果验证成为可能，消融 1.2-6.8% latent 即可将攻击成功率归零。 |
| 10 | Omni-Woodpecker: Training-Free Cross-Modal Hallucination Correction for Omni LLMs | https://arxiv.org/abs/2610.27103 | Multimodal, Hallucination, VLM ⭐ | 免训练框架，通过正交分解分离隐藏状态中的 grounding evidence 与 learned priors，在 CMM/AVHBench 上提升 12.9/8.6 点（10/19 提交，本周 HF trending）。 |
| 11 | The Window Is in the Reasoning: When Prompt Injection Is Decided in LLM Agents | https://arxiv.org/abs/2610.24048 | Agent Security, Prompt Injection | 分支 rollout 实验揭示 prompt injection 并非在读入时即决定——thinking 开启后仅 62% 方差在读取时固定，单次 run 评测标签与重跑不一致率高达 35%。 |
| 12 | One Truthful Relation Is Enough: Cognitive Attack on LLM Agent Beliefs | https://arxiv.org/abs/2610.24873 | Agent Security, Cognitive Attack | 一句话操纵 agent 信念的"单关系攻击"——定位隐含推理 warrant 并用单句干预，开源模型 80% 翻转率，多智能体辩论反而将团队错误率从 50% 升至 59.5%。 |
| 13 | MemPilot: Agentic Memory Management for LLM Agents | https://arxiv.org/abs/2610.06830 | Agent Memory, Long Context | 智能体记忆管理系统，本周 HF Papers trending（10/6 提交，持续走热）。 |
| 14 | MIRROR: From Imitation to Internalization in LLM Personalization | https://arxiv.org/abs/2610.09795 | LLM Personalization, Self-Distillation | 百度的自蒸馏个性化框架——单模型兼任 teacher/student，用参考揭示的 on-policy 分布对齐将偏好从模仿转为内化，三个基准上领先 SFT 基线且灾难性遗忘更少（10/7 提交，本周持续被引）。 |

---

## 🔍 本周趋势观察

**Agent 自我进化是本周最热方向：** Agent S4（进化接口）、RSIHub（进化框架）、OPST（自训练）三篇从不同角度指向同一个问题——如何不更新模型参数而持续提升 agent 能力。

**Agent 安全受到空前关注：** Prompt injection 的决策时机（#11）和单句认知攻击（#12）表明安全研究正从"防注入"深入到"理解 agent 何时以及如何被说服"。

**记忆/RAG 架构在降温：** RAW-RAG 的结论值得注意——直接检索原始对话历史在多数场景下优于精心设计的记忆系统，这对 Mem0 类产品的架构假设构成挑战。

**RL 后训练效率成为工程瓶颈：** NgramRL 针对 GRPO rollout 加速，BF16 推理/训练对齐（2610.32951）解决数值稳定性，两篇都指向 RL post-training 的系统工程问题。
