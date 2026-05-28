# 2026-W22 论文精选候选列表（7篇）

> **精选日期**: 2026-05-28（周四）| **来源池**: `paper-pool-2026-22.md`（22篇候选）
> **筛选标准**: 总分排序 + 领域均衡 + 代码可得性优先
> **评分维度**: 创新性(5) + 实用性(5) + 技术深度(5) + 机构背书(5) + 代码可得性(5) = 总分25

---

## 🥇 1. SkillOpt: Executive Strategy for Self-Evolving Agent Skills

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.23904](https://arxiv.org/abs/2605.23904) |
| **标题** | SkillOpt: Executive Strategy for Self-Evolving Agent Skills |
| **作者** | Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou, Zisu Huang, Yan Li, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Yuqing Yang, Dongdong Chen, Xue Yang, Chong Luo |
| **机构** | Microsoft, Shanghai Jiao Tong University, Tongji University, Fudan University |
| **领域** | Agent / Skill / Text-Space Optimization |

**一句话摘要**：为Agent技能设计首个文本空间优化器，通过可控编辑与验证门控实现技能稳定训练与跨模型迁移。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 5 | 首个系统化可控文本空间优化器，将skill视为可训练的外部状态 |
| 实用性 | 5 | 52/52最佳或并列，跨7模型/3执行环境，GPT-5.5提升+23.5点 |
| 技术深度 | 5 | 文本学习率预算、拒绝编辑缓冲、epoch级慢/元更新，方法论严谨 |
| 机构背书 | 4 | 微软研究院 + 上海交大 + 同济 + 复旦 |
| 代码可得性 | 5 | **官方代码**: https://aka.ms/SkillOpt；社区已有CodexOpt实现 |
| **总分** | **24** | |

**代码关联**：⭐⭐ **双料项目**。官方代码已开源，社区迅速跟进CodexOpt实现。与开源候选池中的`agentmemory`（记忆层基础设施）、`OpenViking`（上下文数据库）形成理念共振——三者共同回答"Agent如何积累、管理、优化可复用知识"这一基础设施命题。

---

## 🥈 2. Foundation Protocol: A Coordination Layer for Agentic Society

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.23218](https://arxiv.org/abs/2605.23218) |
| **标题** | Foundation Protocol: A Coordination Layer for Agentic Society |
| **作者** | Bang Liu, Ye Wang, Sirui Hong, Ao Xie, Chenyan Huang, Jiakai Tang, Xiuying Chen, Ming Zhang, Hao Sun, Yuhan Liu, Jiaqi Wang, Hongwei Liu, Yi Ren, Dongshan Zhou, Zhenglin Wang, Cheng Zhang, Heng Ji, Jian Sun, Qiang Yang, Xuelong Li, Yaowei Wang, Zhenguo Li |
| **机构** | 多机构（含UIUC Heng Ji, 港科大Qiang Yang等） |
| **领域** | Multi-Agent / Coordination / Protocol |

**一句话摘要**：构建Agent社会的基础协调协议层，以图结构统一异构实体并原生支持多Party协作与经济结算。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 5 | "Agentic Society"协议层是宏大且稀缺的叙事，graph-first架构+经济原语 |
| 实用性 | 4 | 协议设计需生态采纳才能产生网络效应，当前处于概念验证阶段 |
| 技术深度 | 4 | 统一异构实体，多Party组织机制，理论框架完整 |
| 机构背书 | 5 | 豪华阵容：Heng Ji(UIUC), Qiang Yang(港科大), Sirui Hong等 |
| 代码可得性 | 2 | 9MB论文暗示有实现，但未明确开源链接 |
| **总分** | **20** | |

**代码关联**：与开源候选池中的`12-factor-agents`（Agent生产化十二要素）理念共振。Foundation Protocol回答"Agent社会如何协调"，12-factor-agents回答"单个Agent如何生产化"——两者分别从宏观社会和微观工程两个维度定义Agent基础设施。

---

## 🥈 3. Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.23590](https://arxiv.org/abs/2605.23590) |
| **标题** | Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents |
| **作者** | Bowen Zhang, Wei Liu, Yihao Xu, Yuetian Xiao |
| **机构** | 未明确 |
| **领域** | Agent / ReAct / Rubric-Guided Reasoning |

**一句话摘要**：训练专用评分标准生成器为ReAct Agent提供逐步决策指导，提升搜索密集型多步推理任务效果。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 4 | Rubrics作为逐步协作者，将评估标准转化为行动指导，是ReAct的工程进化 |
| 实用性 | 4 | 可直接插入现有Agent，提升搜索密集型多步任务，Spearman rank-correlation reward |
| 技术深度 | 4 | GRPO训练rubric生成器，reward与下游效果相关性高 |
| 机构背书 | 2 | 作者机构未明确 |
| 代码可得性 | 5 | **官方开源**: https://github.com/ZBWpro/Co-ReAct |
| **总分** | **20** | |

**代码关联**：⭐⭐ **双料项目**。官方GitHub已开源。可与开源候选池中的编码Agent工具链（`opencode`, `qwen-code`, `Claude Code`）集成，作为ReAct风格Agent的步级决策增强插件。

---

## 🥈 4. Metacognition as Reward: Learning to Reinforce What We Know We Know

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.23384](https://arxiv.org/abs/2605.23384) |
| **标题** | Metacognition as Reward: Learning to Reinforce What We Know We Know |
| **作者** | Sirui Chen, Zheng Wang, Yibo Miao, Yunfei Xie, Haiyuan Li, Zhiqiang Xu, Dong Li |
| **机构** | 未明确 |
| **领域** | Reasoning / RL / Metacognition |

**一句话摘要**：将元认知知识与调控信号作为内在奖励，引导LLM推理过程实现22个基准上的持续性能提升。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 5 | 元认知即奖励，全新RL范式，区别于传统外部奖励模型 |
| 实用性 | 5 | 22个基准验证，Qwen3.5-9B逼近前沿模型，降低对外部reward model依赖 |
| 技术深度 | 5 | 过程级分析，metacognitive knowledge + regulation双信号 |
| 机构背书 | 2 | 作者机构未明确 |
| 代码可得性 | 2 | 未提及开源 |
| **总分** | **20** | |

**代码关联**：无直接对应开源项目。但方向与开源候选池中的推理增强类Agent工具链潜在互补——可将元认知奖励机制集成到`opencode`等编码Agent的自我纠错流程中。

---

## 🥉 5. OpenSkillEval: Automatically Auditing the Open Skill Ecosystem

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.23657](https://arxiv.org/abs/2605.23657) |
| **标题** | OpenSkillEval: Automatically Auditing the Open Skill Ecosystem for LLM Agents |
| **作者** | Jiahao Ying, Boxian Ai, Wei Tang, Siyuan Liu, Yixin Cao |
| **机构** | Singapore Management University, Fudan University (Institute of Trustworthy Embodied AI), JD (Joy Future Academy) |
| **领域** | Agent / Skill / Evaluation / Audit |

**一句话摘要**：建立动态任务实例自动评估框架，揭示开源技能与模型/框架的复杂交互关系及选型规律。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 4 | 自动化审计框架，填补skill生态系统安全评估空白 |
| 实用性 | 5 | 600+动态任务实例，30开源技能，直接指导生产选型 |
| 技术深度 | 4 | 系统化评估，trajectory trace分析技能使用行为 |
| 机构背书 | 3 | SMU + 复旦可信具身AI研究所 + 京东 |
| 代码可得性 | 4 | **项目网站**: https://yingjiahao14.github.io/OpenSkillEval-Web/ |
| **总分** | **19** | |

**代码关联**：⭐ **双料项目**（部分）。项目网站提供benchmark资源。与开源候选池中的`OpenViking`（上下文数据库）间接相关——两者分别从"技能评估"和"上下文管理"维度解决Agent生态的基础设施问题。

---

## 🥉 6. From Raw Experience to Skill Consumption: A Full-Lifecycle Study of Model-Generated Agent Skills

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.23899](https://arxiv.org/abs/2605.23899) |
| **标题** | From Raw Experience to Skill Consumption: A Full-Lifecycle Study of Model-Generated Agent Skills |
| **作者** | Yiqiao Jin, Minjing Zhao, Haowei Lin, Yihua Zhou, Jinjie Gu, Chengyue Gong, Ziyang Gong, Dongdong Chen, Xue Yang, Chong Luo |
| **机构** | Microsoft（与SkillOpt同团队） |
| **领域** | Agent / Skill / Full-Lifecycle |

**一句话摘要**：系统研究模型生成Agent技能全生命周期，揭示提取器与消费者的非对称效用并构建元技能指导框架。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 4 | 全生命周期研究，meta-skill概念，揭示"R2E"匹配模式 |
| 实用性 | 4 | 跨5领域系统实验，指导skill提取与消费实践 |
| 技术深度 | 4 | 非对称效用分析，24个skill类型×6个axis框架 |
| 机构背书 | 4 | 微软研究院（与SkillOpt同一团队） |
| 代码可得性 | 3 | 微软通常开源，但未在arXiv页面明确链接 |
| **总分** | **19** | |

**代码关联**：与`SkillOpt`形成微软Agent技能研究的双子星——SkillOpt回答"如何训练skill"，From Raw Experience回答"skill从哪来、到哪去"。两者结合构成完整的skill生命周期方法论。

---

## 🥉 7. Model Collapse as Cultural Evolution

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.23054](https://arxiv.org/abs/2605.23054) |
| **标题** | Model Collapse as Cultural Evolution |
| **作者** | Dongxin Guo, Jikun Wu, Siu Ming Yiu |
| **机构** | The University of Hong Kong |
| **领域** | LLM Theory / Model Collapse / Cultural Evolution |

**一句话摘要**：借文化进化迭代学习理论解释模型崩溃机制，发现组合性非单调退化轨迹并提供自训练设计原则。

| 评分项 | 得分 | 说明 |
|--------|------|
| 创新性 | 5 | 文化进化理论全新视角，将model collapse reframe为文化传输现象 |
| 实用性 | 3 | 提供自训练管道设计原则（task-grounded filtering优于random filtering） |
| 技术深度 | 5 | 五预测+跨语言验证（英/德/土），Hedges' g > 1.6, BF10 > 100，R²=0.94匹配人类行为数据 |
| 机构背书 | 3 | 港大，Siu Ming Yiu为知名密码学/安全教授 |
| 代码可得性 | 2 | CoNLL 2026已接受，可能后续开源 |
| **总分** | **19** | |

**代码关联**：无直接对应开源项目。但研究结论对开源社区的自训练/迭代学习实践有直接指导意义——特别对`ml-intern`等自主ML Agent的自进化训练流程有警示价值。

---

## ❌ 淘汰论文说明（15篇）

| 论文 | 总分 | 淘汰原因 |
|------|------|---------|
| MemAudit | 17 | 安全审计方向已被OpenSkillEval覆盖，且OpenSkillEval有代码/网站 |
| EVE-Agent | 16 | 可验证自进化概念好，但无代码，工程实现复杂度高 |
| Parallel Context Compaction | 14 | 工程优化，技术深度不及入选论文 |
| DART | 15 | 工具恢复场景较窄，实用性有限 |
| Agentic Proving | 15 | 形式化验证niche领域，受众有限 |
| When Planning Fails... (EPC-AW) | 13 | 认知校准理论深度高但实用性有限 |
| GENSTRAT | 18 | 战略推理有趣，但与Metacognition as Reward同属推理方向，后者更具工程启发性 |
| The Efficiency Frontier | 14 | 成本-性能优化框架偏综述 |
| When Is Next-Token Prediction Useful? | 11 | 纯数学分析，无直接工程价值 |
| Personalized Agentic RL (PARPO) | 19 | 与From Raw Experience同属skill方向，后者覆盖全生命周期 |
| PathCal | 16 | 状态感知反思标记校准，轻量但影响面窄 |
| Positional Failures (CRE) | 17 | 揭示长上下文推理盲区，但已有论文覆盖更广 |
| Self-Improving ICL | 13 | 无需训练的ICL校准，技术深度不及入选 |
| ChartFI-Bench | 13 | VLM图表评估，偏离Agent/Reasoning主线 |
| SPACENUM | 12 | 空间数值理解诊断，揭示VLM缺陷但无直接解决方案 |

---

## 📊 本周精选汇总

| 排名 | 论文 | 总分 | 核心亮点 | 代码 |
|------|------|------|----------|------|
| 1 | **SkillOpt** | 24 | 首个skill文本空间优化器，52/52全胜 | ✅ [aka.ms/SkillOpt](https://aka.ms/SkillOpt) |
| 2 | **Foundation Protocol** | 20 | Agent社会协调协议，豪华作者阵容 | — |
| 2 | **Co-ReAct** | 20 | Rubrics逐步指导ReAct，直接可插拔 | ✅ [GitHub](https://github.com/ZBWpro/Co-ReAct) |
| 2 | **Metacognition as Reward** | 20 | 元认知即奖励，22基准验证 | — |
| 5 | **OpenSkillEval** | 19 | 开放skill生态自动审计，600+实例 | 🔶 [网站](https://yingjiahao14.github.io/OpenSkillEval-Web/) |
| 5 | **From Raw Experience** | 19 | Skill全生命周期研究，meta-skill框架 | — |
| 5 | **Model Collapse** | 19 | 文化进化解释模型崩溃，CoNLL接受 | — |

**领域分布**：Agent/Skill(3) · Multi-Agent(1) · Reasoning/RL(1) · Evaluation(1) · Theory(1)

**代码双料项目**：3/7 — SkillOpt（⭐⭐）、Co-ReAct（⭐⭐）、OpenSkillEval（⭐，部分开源资源）

**主题聚焦**：本周入选形成两条主线——
- **主线一：Agent技能基础设施** — SkillOpt（训练优化）+ From Raw Experience（生命周期）+ OpenSkillEval（评估审计）三篇形成"skill闭环"，标志着学术界对Agent技能这一新兴基础设施的系统性关注。
- **主线二：Agent可信与协调** — Foundation Protocol（社会协调）+ Co-ReAct（步级决策）+ Metacognition as Reward（自我监控）+ Model Collapse（自我训练风险）四篇从不同维度回答"Agent如何可信地自我运作"。

---

*精选人：Kimi Claw | 2026-W22 | 待用户确认*
