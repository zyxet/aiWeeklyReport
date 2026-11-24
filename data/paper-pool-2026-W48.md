# 📄 本周候选论文池（25篇）

> **收集时间**: 2026-11-24（周二）| **覆盖区间**: 2026-11-17 ~ 2026-11-24 | **周次**: W48
> **来源**: arXiv API（cs.CL / cs.AI recent + 3 组关键词搜索）、PaperWeekly / 智能体周刊参考
> **注意**: HuggingFace Papers 页面网络超时未能访问；cs.LG API 返回缓存旧数据，已改用关键词搜索补充；PaperWeekly 本周精选未检索到新一期
> **筛选规则**: 保留 LLM / Agent / RAG / CoT / Reasoning / Long Context / Multimodal(VLM) 相关；排除纯医学 AI、纯 CV（非 VLM）、纯领域应用

---

## 🤖 Agent 系统与智能体（15 篇）

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 1 | The Evaluation Substrate Matters: Benchmarking Multi-Agent Serving Substrates (MASSys) | [arxiv.org/abs/2611.28671](https://arxiv.org/abs/2611.28671) | Multi-Agent, Benchmark, Systems | 同一多 Agent 工作流在不同服务环境下的排名会翻转（Star 从第1跌至第4，Chain 反之），提出跨服务基质的 MAS 评测基准，质量、延迟、成本、故障全记录 |
| 2 | Persuasion from Within: Model-Based Insider Attacks in Multi-Agent LLM Debate and Consensus | [arxiv.org/abs/2611.28660](https://arxiv.org/abs/2611.28660) | Multi-Agent, Security, World Model | 恶意 Agent 学习良性 Agent 的世界模型后实施最隐蔽的内部说服攻击，可迁移到更大群组和未见数据集，现有 Byzantine 防御无效；对抗训练可消除 |
| 3 | VeriLadder: A Multi-Agent Specification Refinement System for Tool-Verified Verilog Datasets | [arxiv.org/abs/2611.28617](https://arxiv.org/abs/2611.28617) | Multi-Agent, Dataset, Code | 五 Agent 协作 + EDA 工具形式验收构建 71.6 万设计级 Verilog 数据集，规格可重建率从 26.1% 升至 78.2%；微调 Qwen2.5-Coder-7B 后 VerilogEval v2 pass@1 从 31.7% → 50.0% |
| 4 | MADRec: Reliable Multi-Agent Reasoning with Evidence-Grounded Debate for Recommendation | [arxiv.org/abs/2611.28604](https://arxiv.org/abs/2611.28604) | Multi-Agent, RAG, Recommendation | 交互 Agent 与语义 Agent 结构化辩论 + 证据锚定 RAG + 裁判校准排名，三数据集上提升多 Agent 推荐推理的可靠性 |
| 5 | Muted Distillation: Token-Efficient Distillation for Agentic LLMs | [arxiv.org/abs/2611.28445](https://arxiv.org/abs/2611.28445) | Agent, Distillation, Efficiency | 面向 Agentic LLM 场景的 token 高效知识蒸馏，压缩推理 token 开销的同时保留 Agent 能力 |
| 6 | ALIoTh: Orchestrating Multi-Agent LLMs for Autonomous IoT Penetration Testing | [arxiv.org/abs/2611.25809](https://arxiv.org/abs/2611.25809) | Multi-Agent, Security, Self-RAG | 多 Agent + Self-RAG 架构经 LangGraph 编排自主执行 IoT 渗透测试全链路：枚举 → 漏洞评估 → payload 生成 → 反弹 shell → 提权 |
| 7 | Beyond Self-Critique: Multi-Agent Research Verification | [arxiv.org/abs/2611.27839](https://arxiv.org/abs/2611.27839) | Multi-Agent, Research | 多 Agent 协作交叉验证科研论断，超越单模型自我批评的验证范式 |
| 8 | Beznau Nuclear: Hierarchical LLM Agents for Power Plant Operations | [arxiv.org/abs/2611.27556](https://arxiv.org/abs/2611.27556) | Agent, Hierarchical, Industrial | 层级化 LLM Agent 框架应用于核电站运维决策，展示复杂工业场景下的多层级自主决策链路 |
| 9 | Belief-State Management and Rubric Rewards for Agentic Forecasting | [arxiv.org/abs/2611.27286](https://arxiv.org/abs/2611.27286) | Agent, RL, Forecasting | 显式信念状态管理 + 评分规则奖励改进预测型 Agent 的校准度与准确性 |
| 10 | RI-Bench: Role Integrity in LLM Agents | [arxiv.org/abs/2611.27139](https://arxiv.org/abs/2611.27139) | Agent, Benchmark, Evaluation | 评测 LLM Agent 在长程多轮交互中维持指定角色完整性的能力，揭示角色漂移模式 |
| 11 | ProbeAgent: Diagnosing and Fixing Agent Failures | [arxiv.org/abs/2611.26897](https://arxiv.org/abs/2611.26897) | Agent, Debugging, Tooling | 系统性诊断和修复 LLM Agent 执行失败的探针框架，定位失败根因 |
| 12 | ROGUE-AI: Replicating Agentic Security Events | [arxiv.org/abs/2611.26553](https://arxiv.org/abs/2611.26553) | Agent, Security, Red Team | 复现 Agentic 安全事件的方法论与工具链，支持红队演练和安全审计 |
| 13 | FinVeriQA: Financial Research Agents | [arxiv.org/abs/2611.25071](https://arxiv.org/abs/2611.25071) | Agent, Finance, Research | 面向金融研究场景的多 Agent 事实核查问答系统 |
| 14 | Attacks and Defenses in Decentralized Multi-Agent LLM Systems | [arxiv.org/abs/2611.25056](https://arxiv.org/abs/2611.25056) | Multi-Agent, Security, Decentralized | 分析去中心化多 Agent LLM 系统的攻击面并提出对应防御机制 |
| 15 | L2C: LLM-Guided Workflow Evolution for Red Teaming | [arxiv.org/abs/2611.24221](https://arxiv.org/abs/2611.24221) | Multi-Agent, Security, Auto-Evolution | LLM 引导红队工作流自动进化：从历史执行轨迹学习并生成新的攻击策略组合 |

## 🔍 RAG 检索增强（1 篇 + 1 篇交叉）

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 16 | SupportChain: Trace-Calibrated Aggregation of Quote-Grounded Reasoning Chains for Multi-Hop RAG with Small Readers | [arxiv.org/abs/2611.28519](https://arxiv.org/abs/2611.28519) | RAG, Multi-Hop, Efficiency | 9B 小模型 + 引用锚定推理链聚合在 MuSiQue 上达 63.0 F1，超越此前 20B 模型的 59.2；无需建索引，可靠性模型仅需 100 条训练数据 |
| 17 | MADRec（见 #4） | — | — | 兼具多 Agent 辩论与证据锚定 RAG 视角，已归入 Agent |

## 🧠 Reasoning / CoT / 推理（2 篇）

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 18 | BudgetPV: Budget-Constrained Theorem Proving with Heterogeneous LLM Solvers | [arxiv.org/abs/2611.26906](https://arxiv.org/abs/2611.26906) | Reasoning, Theorem Proving, Budget | 预算约束下调度异构 LLM 求解器组合进行定理证明，成本-准确率权衡 |
| 19 | Tracking Representations in LLM Reasoning Traces for Iterated Games | [arxiv.org/abs/2611.23403](https://arxiv.org/abs/2611.23403) | Reasoning, Interpretability, CoT | 机制可解释性分析迭代博弈中 LLM Agent 的 CoT 推理：模型在推理中构建并修正内部博弈状态表征，但一旦过早承诺错误信念极少恢复 |

## 📏 Long Context 与记忆（2 篇）

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 20 | MemOnce: A Scalable Memory Architecture for Large Language Models | [arxiv.org/abs/2611.27973](https://arxiv.org/abs/2611.27973) | Long Context, Memory, Architecture | 可扩展记忆架构：将外部记忆与 LLM 推理解耦，支持高效的长程信息存取与复用 |
| 21 | LongCat Recall Sparse Attention: Advancing Long-Context Inference Efficiency | [arxiv.org/abs/2611.27233](https://arxiv.org/abs/2611.27233) | Long Context, Sparse Attention, Inference | 稀疏注意力机制提升长上下文推理效率，降低 KV cache 开销与计算延迟 |

## 🖼️ 多模态 VLM（2 篇）

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 22 | S-Mind: Internalizing Multi-View Geometry for Spatial Intelligence | [arxiv.org/abs/2611.28649](https://arxiv.org/abs/2611.28649) | VLM, Spatial Reasoning, MLLM | 紧凑空间 token 将多视角几何内化为 MLLM 内在能力，四基准平均超越 GPT-6-Astra / Kimi-K3.1-Pro / GLM-5.3-Flash，推理速度比工具型 Agent 快约 100 倍 |
| 23 | ForeSeek: Foresight-Driven Reasoning for Long-Form Video Understanding | [arxiv.org/abs/2611.26024](https://arxiv.org/abs/2611.26024) | VLM, Video Agent, Reasoning | 视频 Agent 从被动检索转向预测性探索：对未见时段形成视觉预期并定向验证，少看 2.5–4.4 倍帧数达到同等或更好精度 |

## 📝 Prompt Engineering（2 篇）

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 24 | Evaluating Prompting Strategies for Zero-Shot Multilingual Aspect-Based Sentiment Analysis | [arxiv.org/abs/2611.27807](https://arxiv.org/abs/2611.27807) | Prompt Engineering, Multilingual, Evaluation | 系统比较零样本多语言属性级情感分析的提示策略效果 |
| 25 | MELON: Multilingual Enhanced Localized News Generation | [arxiv.org/abs/2611.27750](https://arxiv.org/abs/2611.27750) | Multilingual, Localization, Generation | 多语言增强的本地化新闻生成：平衡文化适配与信息保真 |

## 🔒 安全与身份（1 篇）

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 26 | DistDNA: Language Model Fingerprinting | [arxiv.org/abs/2611.27831](https://arxiv.org/abs/2611.27831) | Security, Identity, LLM | 模型指纹蒸馏：将大模型指纹迁移至小模型，模型身份识别与溯源 |

---

## ❌ 排除记录（8 篇）

| 标题 | 排除原因 |
|------|---------|
| TEA-Bench-BR: Clinical Coding Agents | 纯医学 AI |
| SLP-Bench: Clinical Speech Processing | 纯医学 AI |
| RadBot-R1: Radiology Report Generation | 纯医学 AI |
| Brain-Language Alignment via Narratives | 神经科学，非 LLM 方法 |
| BioEmu2: Biomolecular Emulation | 纯生物计算 |
| Chemical Process Fault Detection with LLMs | 化工领域应用 |
| ChildAI-Gov: EdTech Policy Assessment | 教育政策领域应用 |
| FrontierOR Challenge: Agentic Optimization | 数学优化领域竞赛 |

---

## 📊 本周趋势观察

1. **多 Agent 安全成为主战场**：本周 5+ 篇论文聚焦多 Agent 系统安全（内部说服攻击、去中心化攻击、IoT 渗透测试、红队进化），"Agent 间的信任假设"被系统性打破——MASSys 发现评测结果依赖于服务基质，Persuasion from Within 证明恶意 Agent 可以学世界模型来隐蔽说服
2. **Agent 评测从"能不能做"转向"可不可靠"**：RI-Bench 测角色完整性、ProbeAgent 诊断失败根因、MASSys 测服务基质敏感性——评测维度从任务成功率扩展到可靠性、可维护性、可复现性
3. **RAG 小型化突破**：SupportChain 用 9B 模型 + 引用锚定链聚合超越了此前 20B 模型的最好成绩，无需建索引，100 条训练数据即可校准——RAG 的"大模型才能做好"假设正在松动
4. **多 Agent 用于数据构造**：VeriLadder 展示了多 Agent 协作 + 形式化工具验收的高质量控制数据生成范式（26.1% → 78.2% 可重建率），可迁移至其他代码/推理数据场景
5. **VLM 空间推理加速内化**：S-Mind 用紧凑 token 将 3D 空间推理内化为模型能力，推理速度比工具型 Agent 快 100 倍——工具调用 vs 能力内化的权衡继续向后者倾斜
