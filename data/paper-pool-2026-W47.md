# 📄 本周候选论文池（35篇）

> **收集时间**: 2026-11-17（周二）| **覆盖区间**: 2026-11-10 ~ 2026-11-17 | **周次**: W47
> **来源**: arXiv API（cs.CL / cs.LG / cs.AI，7 组关键词搜索）
> **注意**: HuggingFace Papers 页面连续 3 次网络超时，本周缺失该源；PaperWeekly 本周精选未检索到新一期
> **筛选规则**: 保留 LLM / Agent / RAG / CoT / Reasoning / Long Context / Multimodal(VLM) 相关；排除纯医学 AI、纯 CV（非 VLM）、纯领域应用

---

## 🤖 Agent 系统与智能体（16 篇）

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 1 | WeightBench: Evaluating Language Models as Weight-Space Programmers | [arxiv.org/abs/2611.18553](https://arxiv.org/abs/2611.18553) | Agent, Benchmark | 评测 LLM 直接读写神经网络权重的新范式（Weight-Space Programming），42 项任务，Claude Opus 5.5 宏观得分 0.535 |
| 2 | Can Mechanistic Interpretability Help Explain LLM Agent Failures? | [arxiv.org/abs/2611.18514](https://arxiv.org/abs/2611.18514) | Agent, Interpretability | 用机制可解释性分析 Web Agent 元素幻觉：线性探针可在生成前预测幻觉（0.80 AUC），方向 steering 修正 85% 幻觉 |
| 3 | NeoResearch: Literature- and Experience-Guided Autonomous Time Series Model Discovery | [arxiv.org/abs/2611.18235](https://arxiv.org/abs/2611.18235) | Agent, AutoML | LLM 作为自主研究者，挖矿文献 + 分层经验记忆闭环，自动发现领域时序预测模型 |
| 4 | WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark for Web Agents | [arxiv.org/abs/2611.17955](https://arxiv.org/abs/2611.17955) | Agent, Benchmark, Multimodal | 异构多模态可复现的 Web Agent 基准 |
| 5 | Adversarially Attacking Symbolic Vocabulary Vulnerabilities In LLM Planners | [arxiv.org/abs/2611.17910](https://arxiv.org/abs/2611.17910) | Agent, Planning, Security | Symbolic Swapper 攻击通过混淆符号词汇使 LLM 规划性能下降超 70%，揭示规划能力对词汇捷径的依赖 |
| 6 | G-CAST: Governed Continual Self-Training for E-Commerce Agents under Evolving Demands | [arxiv.org/abs/2611.17814](https://arxiv.org/abs/2611.17814) | Agent, Continual Learning | 带治理机制的电商 Agent 持续自训练框架，应对需求演进 |
| 7 | Vision-as-a-Tool: Visual Harness for Multimodal Agentic Coding | [arxiv.org/abs/2611.17797](https://arxiv.org/abs/2611.17797) | Agent, VLM, Coding | 将视觉能力作为工具接入编码 Agent，多模态 agentic coding 的可视化 harness |
| 8 | Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent | [arxiv.org/abs/2611.18397](https://arxiv.org/abs/2611.18397) | VLA, Agent, Game | 通用视觉-语言-动作基础模型，数万小时键鼠交互数据训练，云边推理引擎支持实时长程游戏任务 |
| 9 | Outcome-Mass Alignment: Controlling Length-Dependent Trajectory Influence in Multi-Turn LLM Agent RL | [arxiv.org/abs/2611.16816](https://arxiv.org/abs/2611.16816) | Agent, RL | 指出多轮 Agent 训练中轨迹膨胀导致结果统计重复计数，OMA 方法在 ALFWorld 上提升成功率 7-9.4 个百分点 |
| 10 | Folio: Recoverable Multi-Resolution Context Folding for Long-Horizon Language Agents | [arxiv.org/abs/2611.16627](https://arxiv.org/abs/2611.16627) | Agent, Long Context, Memory | 三层可恢复上下文折叠（笔记/事件清单/原始记录），75 任务上 66 题 vs 模型自压缩 54 题 |
| 11 | MemCredit: From Relevance to Utility for Decision-Time Memory in Long-Horizon Web Agents | [arxiv.org/abs/2611.15600](https://arxiv.org/abs/2611.15600) | Agent, Memory | 反事实干预估计记忆决策效用，发现语义相关 ≠ 决策有用；500 token 预算下 ALFWorld 86.57% vs BM25 65.67% |
| 12 | MIGRO: A Decoupled and Portable Long-Term Memory System for Language Models | [arxiv.org/abs/2611.15315](https://arxiv.org/abs/2611.15315) | Agent, Memory | 解耦式长期记忆：模型换代记忆不丢，质量 +7.3%，私有存储减少 99.3% |
| 13 | DISCERN: Preserve at Write, Resolve at Read for Persistent LLM-Agent Memory | [arxiv.org/abs/2611.15729](https://arxiv.org/abs/2611.15729) | Agent, Memory, RAG | 企业 Agent 跨会话记忆：写入时保留全部历史版本，读取时消解实体/时态歧义，弃权校准 F1 0.924 远超基线 |
| 14 | TreeAgent: Structure-Aware Memory Agent for Processing Long Hierarchical Data | [arxiv.org/abs/2611.13946](https://arxiv.org/abs/2611.13946) | Agent, Memory, Long Context | 结构感知记忆 Agent，处理长层级数据 |
| 15 | Coding Agent Memory Post-Training II: Unlocking Memory Potential via On-Policy Distillation | [arxiv.org/abs/2611.14009](https://arxiv.org/abs/2611.14009) | Agent, Coding, Memory | 通过 on-policy 蒸馏释放预训练文件操作的记忆潜力，长程编码任务 |
| 16 | AstroMemBench: A Benchmark for Memory Systems in Embodied Spacecraft Agents | [arxiv.org/abs/2611.16590](https://arxiv.org/abs/2611.16590) | Agent, Memory, Benchmark | 航天具身 Agent 记忆基准：16 子挑战 2240 实例，Mem0/Chain-of-Memory/RAG 对比，重启后会话记忆优势显著 |

## 🔍 RAG 检索增强（5 篇）

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 17 | RAG-FGO: Dynamic Optimization of Query-Rewriting Agents for Generative RAG | [arxiv.org/abs/2611.17788](https://arxiv.org/abs/2611.17788) | RAG, Agent | 将查询重写建模为离散-连续混合黑盒优化，进化搜索 + 精英记忆池，泛化检索策略 |
| 18 | Faithful in Steps (QDRAG): Improving Generalization and Citation in RAG via Query Decomposition | [arxiv.org/abs/2611.15538](https://arxiv.org/abs/2611.15538) | RAG, Multimodal | 原子子问题分解 + 去噪 rerank 消除过度引用，多模态 QA 引用忠实度超越 Gemini-Pro |
| 19 | Edge-Native Multimodal RAG: Hardware-Aware Quantization for Consumer GPUs | [arxiv.org/abs/2611.14924](https://arxiv.org/abs/2611.14924) | RAG, Multimodal, Edge | 消费级 GPU 上可运行的多模态 RAG：NF4 量化 + Florence-2 视觉解耦，8.37GB 显存占用，结构化提示恢复量化推理损失 |
| 20 | OpticalRAG: Pixel-Space Compression for Token-Efficient RAG | [arxiv.org/abs/2611.13675](https://arxiv.org/abs/2611.13675) | RAG, Long Context | 文档渲染为图像走视觉编码器压缩至 16 个注入 token，LongBench-v2 上压缩感知准确率最优 |
| 21 | DISCERN（见 #13）| — | — | 兼具 RAG 与记忆系统视角，已归入 Agent Memory |

## 🧠 Reasoning / CoT / 评测（5 篇）

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 22 | Agent-as-a-Judge | [arxiv.org/abs/2611.18067](https://arxiv.org/abs/2611.18067) | Agent, Evaluation, Survey | 主动取证式 Agent 评审综述：设计空间、分数对比、成本与治理挑战 |
| 23 | MuSeToM: Multi-Sensory Evaluation of Belief Revision with Textual Cues Across Six Senses | [arxiv.org/abs/2611.16662](https://arxiv.org/abs/2611.16662) | Reasoning, ToM, Benchmark | 2415 实例测 LLM 信念修正：模型常检测到该改信念但推断不出改成什么，对显著但证据不足的线索过度更新 |
| 24 | Cognitive Mapping of Learning by Thinking Mechanisms in Large Language Models | [arxiv.org/abs/2611.14382](https://arxiv.org/abs/2611.14382) | Reasoning, CoT, Analysis | 将 Reflective Reasoning / 合成记忆 / 内部模拟 / 概念自组织四种认知机制映射到 CoT、self-consistency、ToT 等方法，分析结构性失效 |
| 25 | MMDM: Measuring Massive Multitask Decision Making | [arxiv.org/abs/2611.14309](https://arxiv.org/abs/2611.14309) | Evaluation, Reasoning | 大规模多任务决策能力测量基准 |
| 26 | AI Reviews Are Biased Towards the Appendix | [arxiv.org/abs/2611.17811](https://arxiv.org/abs/2611.17811) | LLM Review, Meta-research | AI 审稿系统存在对附录内容的系统性偏置，元研究 |

## 📏 Long Context 与记忆压缩（4 篇）

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 27 | Deep Latents, Long Memory: Latent persistence explains temporal correlations in transformer activations | [arxiv.org/abs/2611.18089](https://arxiv.org/abs/2611.18089) | Interpretability, Long Context | 层间激活自相关的长衰减尾源于潜在变量的持续编码，深度越大持续越久 |
| 28 | Beyond Compressing Everything: Contrastive Memory Learning for Selective Context Compression | [arxiv.org/abs/2611.16384](https://arxiv.org/abs/2611.16384) | Long Context, Compression | 对比记忆学习实现选择性上下文压缩，替代"全压"策略 |
| 29 | Mask-Pattern Position Augmentation: Training-Free Long-Context Extrapolation for Diffusion LLMs | [arxiv.org/abs/2611.15029](https://arxiv.org/abs/2611.15029) | Long Context, Diffusion LLM | 免训练位置增强实现扩散 LLM 长上下文外推 |

## ⚡ 推理效率与系统（3 篇）

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 30 | Fuse-All MoE Inference Kernel with Load Balancing on TPUs | [arxiv.org/abs/2611.17857](https://arxiv.org/abs/2611.17857) | MoE, Inference, TPU | 全融合 MoE TPU 核：片上保留中间结果，PD 分离下吞吐提升 34.5% |
| 31 | SinkState: On-the-Fly SVD of Recurrent States for Efficient Hybrid LLM Serving | [arxiv.org/abs/2611.14246](https://arxiv.org/abs/2611.14246) | Inference, Hybrid LLM | 线性注意力循环状态低秩化：峰值显存降 2.6×，解码加速 1.58× |
| 32 | TraceKV: Policy-Preserving Low-Rank KV Cache Compression for Reasoning VLMs | [arxiv.org/abs/2611.15569](https://arxiv.org/abs/2611.15569) | VLM, KV Cache, Inference | 推理 VLM 的策略保持低秩 KV 压缩：on-policy 校准 + 敏感度 SVD，5.64× 压缩近无损，解码加速 1.83× |

## 🖼️ 多模态 VLM（2 篇）

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 33 | AURA 2.0: From User-Driven Responses to Model-Initiated Conversations in Streaming Video | [arxiv.org/abs/2611.17048](https://arxiv.org/abs/2611.17048) | VLM, Streaming, Agent | 流式视频 LLM 的模型主动发起对话（MIC）+ 流感知工具调用 + 交互式视觉定位 |
| 34 | MDU: Benchmarking Multilingual Document Understanding in Vision-Language Models | [arxiv.org/abs/2611.14758](https://arxiv.org/abs/2611.14758) | VLM, Benchmark | 23146 实例 5 语种 13 任务文档理解基准，45 个 VLM 评测远未饱和（最佳 69.0） |

## 🔒 安全与身份（1 篇）

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 35 | Contagious Fingerprints: When LLMs Inherit Another Model's Identity | [arxiv.org/abs/2611.18104](https://arxiv.org/abs/2611.18104) | Security, Identity, LLM | 模型指纹会"传染"：接续他人对话的模型继承对方指纹，API 降级检测率从 0.97 跌至 0.72；Lineup 方法假阳性 0.056 |

---

## ❌ 排除记录（10 篇）

| 标题 | 排除原因 |
|------|---------|
| Agentic induction of CDEs from sarcoma case reports | 纯医学 AI |
| Agentic AI for Fault-Tolerant Quantum Circuits | 量子计算领域应用 |
| LLM Agent for Battery Fast-Charging Control | 电池控制领域应用 |
| MineralExp: LLM Agents for Mineral Exploration | 地质领域应用 |
| Certified Thomson-Problem Improvements via LLM Agents | 数学/物理领域应用 |
| RMIT-ADM+S at TREC RAG 2026 | 竞赛赛道报告 |
| Chain of Physics: Fault Diagnosis | 工业故障诊断领域 |
| Dynamic Block-Online Streaming ASR | 语音识别，非 LLM |
| Hy ASR 3.0 Technical Report | 语音识别，非 LLM |
| Superfluid: Local AI Server for Distributed LLM Inference | 纯系统/基础设施 |

---

## 📊 本周趋势观察

1. **Agent 记忆研究爆发**：本周 6+ 篇论文聚焦长期记忆（MIGRO / DISCERN / MemCredit / Folio / TreeAgent / AstroMemBench），核心分歧点从"怎么检索"转向"写入时保留什么、读取时消解什么"
2. **轨迹膨胀问题被正式化**：Outcome-Mass Alignment 指出多轮 Agent RL 中失败轨迹膨胀导致隐式加权偏差，Agent RL 训练细节开始被仔细审计
3. **可解释性进入 Agent 时代**：机制可解释性工具首次系统应用于 Web Agent 失败分析，探针预测幻觉 + 方向修正的路线可行但脆弱
4. **RAG 压缩进入像素空间**：OpticalRAG 用视觉编码器绕开 token 瓶颈，16 个注入 token 的极端压缩比
5. **模型身份安全新攻击面**：Contagious Fingerprints 揭示 API 中继欺诈检测的新漏洞
