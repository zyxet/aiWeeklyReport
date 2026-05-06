# 2026-W19 论文池 | LLM / Agent / Multi-Agent / RAG / Reasoning

> 来源: arXiv cs.AI / cs.CL / cs.LG 2026-05-04~05-05 更新
> 扫描条目: 50 (cs.AI recent top 50)
> 筛选关键词: LLM, Agent, Multi-Agent, RAG, Reasoning, Long Context, Prompt, Chain-of-Thought, 智能体, 大模型
> 排除条件: 纯医学AI (保留Agent/推理相关), 纯CV (保留VLM)
> 生成时间: 2026-05-06 09:20 (手动补跑, 原定时任务 5月5日 10:00 因 API rate limit 失败)

---

## A. Agent 架构与系统

| # | arXiv ID | 标题 | 核心贡献 |
|---|----------|------|----------|
| 1 | 2605.02682 | **CASA: Continuous Agent Semantic Authorization** | 多轮对话中Agent动态授权安全框架, 零信任拦截层 + 语义任务-工具匹配 |
| 2 | 2605.02709 | **Healthcare Agent Skills: An Empirical Analysis** | 首个医疗Agent技能大规模实证, 58,159个公开技能中557个医疗相关, 发现覆盖缺口 |
| 3 | 2605.02592 | **Foundation Models in Industrial Agents** | PRISMA系统综述88篇文献, 工业Agent 75%处于原型阶段(TRL 4-6), 谈判能力缺口-39% |
| 4 | 2605.02489 | **GRAIL: Granular Resonance-based Agent Discovery** | 子400ms Agent发现框架, SLM标签预测 + 伪文档扩展 + MaxSim匹配, 延迟降低79x |
| 5 | 2605.02503 | **DataClaw: Process-oriented Benchmark for Exploratory Data Analysis Agents** | 206万真实记录/492跨域任务, 当前Agent准确率<50%, 过程级评估里程碑 |
| 6 | 2605.02728 | **ORPilot: Open-Source Agentic AI for Business Optimization** | 生产级业务优化Agent, 对话访谈+数据采集+参数计算+求解器无关IR, 首创 |
| 7 | 2605.02669 | **HADES: Agentic System for Drug-Induced Liver Injury Risk** | 可审计药物毒性推理Agent, DILER基准, 假设生成Fuzzy Jaccard 0.16基线 |
| 8 | 2605.02765 | **U-Define: User-Defined Constraints for LLM Planning** | 硬/软约束分类 + 模型检查/LLM-as-judge验证, 用户意图对齐提升 |
| 9 | 2605.02411 | **FitText: Dynamic Tool Retrieval for Agents** | 迭代伪工具描述检索, Memetic进化选择, ToolRet排名从8.81→2.78 |
| 10 | 2605.02396 | **HeavySkill: Heavy Thinking as Inner Skill in Agentic Harness** | 并行推理→总结的两阶段内技能, RL可扩展, 无需编排层即可复杂推理 |

## B. 推理与认知

| # | arXiv ID | 标题 | 核心贡献 |
|---|----------|------|----------|
| 11 | 2605.02427 | **APPS: Auxiliary Particle Power Sampling for Reasoning** | blockwise粒子算法逼近p(x)^α, 短视界rollout未来值引导, 训练无关解码提升 |
| 12 | 2605.02545 | **SAGE: Strategy-Aware Optimization Modeling with LLMs** | 显式建模策略SFT+SW-GRPO, pass@1 72.7→80.3, 约束系统紧凑度+14.2% |
| 13 | 2605.02819 | **SCPRM: Schema-aware Cumulative Process Reward Model** | 前缀条件+schema距离累积奖励, MCTS多跳KGQA, Hits@k平均+1.18% |
| 14 | 2605.02395 | **Controllable Process Supervision for PRMs** | 模板感知错误注入+符号重计算验证, 首错定位比整体分类更难 |
| 15 | 2605.02442 | **How to Evaluate Reasoning in Language Models: A Guide** | 推理论证: 需证据自适应多步搜索, 主张过程评估而非仅最终答案准确率 |

## C. 多Agent与安全

| # | arXiv ID | 标题 | 核心贡献 |
|---|----------|------|----------|
| 16 | 2605.02751 | **Misalignment Contagion in Multi-Agent LLMs** | 多Agent社交困境中对齐传染发现, 隐性特质注入比系统提示重复更有效 |
| 17 | 2605.02398 | **SCHEMA: Evaluating Cognitive Collapse in Frontier Models** | 67,221记录/11模型, 8/11模型对抗压力下认知崩溃-30.2pp, "服从陷阱"识别 |
| 18 | 2605.02572 | **Horizon Length Bottleneck in LLM Agent Training** | 长时序Agent训练瓶颈实证, 探索困难+信用分配, 时序缩减原则稳定训练 |

## D. 人类-AI协同与评估

| # | arXiv ID | 标题 | 核心贡献 |
|---|----------|------|----------|
| 19 | 2605.02832 | **HAAS: Human-AI Adaptive Symbiosis** | 自适应任务分配框架, 规则治理+上下文赌博机, 制造领域治理减负增效 |
| 20 | 2605.02661 | **AcademiClaw: Benchmark for Academic-Level Agents** | 80真实学术任务/25+领域, 最佳模型仅55%通过率, 暴露能力断崖 |
| 21 | 2605.02452 | **How Can Graphs Help Large Language Models?** | 图减少幻觉/增强推理(CoT/ToT/GoT)/结构化数据理解, 三视角综述 |

---

## E. 其他相关

| # | arXiv ID | 标题 | 核心贡献 |
|---|----------|------|----------|
| 22 | 2605.02860 | **Knowledge Distillation from DeepSeek-R1 for Code Clone Detection** | 推理能力蒸馏到紧凑模型, LoRA适配器, 跨语言代码克隆检测 |
| 23 | 2605.02603 | **Counterfactual Reasoning in Automated Planning: A Survey** | 自动规划反事实推理综述, 分类: 改变什么/何时触发/为何如何改变 |

---

**总计**: 23篇匹配 / 50篇扫描 = 46% 命中率
**时间窗口**: 2026-05-04 ~ 2026-05-05 (arXiv cs.AI 两日更新)
**状态**: 手动补跑完成 (原定 2026-05-05 10:00 定时任务因 rate limit 失败)
