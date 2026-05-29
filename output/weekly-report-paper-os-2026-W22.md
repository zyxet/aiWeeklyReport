# AI开源情报周报 — 2026年第22周 (W22) · 论文-开源联动分析

> **报告周期**: 2026-05-25 ~ 2026-05-31
> **生成时间**: 2026-05-29 17:00 (Asia/Shanghai)
> **执行类型**: cron 自动执行
> **情报来源**: GitHub Trending + arXiv cs.CL/cs.LG/cs.AI

---

## 一、论文-开源映射表

按 **A→B→C→D** 优先级排序。A类（论文+官方代码）置顶。

### A类：论文+官方代码（2篇）

| 论文 | arXiv | 机构 | 开源仓库 | 代码状态 | 备注 |
|------|-------|------|---------|---------|------|
| **SkillOpt** | 2605.23904 | 微软 + 上海交大 + 同济 + 复旦 | aka.ms/SkillOpt | ✅ 已发布 | 首个 skill 文本空间优化器 |
| **Co-ReAct** | 2605.23590 | 未明确 | ZBWpro/Co-ReAct | ✅ 已发布 | Rubrics 步级决策增强 |

### B类：论文+社区复现（0篇）

本周 A 类覆盖率回升至 2/7，但仍有高质量论文未释放代码。

### C类：论文先行暂无代码（5篇）

| 论文 | arXiv | 机构 | 状态 |
|------|-------|------|------|
| **Foundation Protocol** | 2605.23218 | 多机构（Heng Ji, Qiang Yang 等） | 🔶 9MB 论文暗示有实现，未明确链接 |
| **Metacognition as Reward** | 2605.23384 | 未明确 | ❌ 未提及开源 |
| **OpenSkillEval** | 2605.23657 | SMU + 复旦 + 京东 | 🔶 项目网站有资源，未明确代码 |
| **From Raw Experience** | 2605.23899 | 微软研究院 | 🔶 通常开源，未明确链接 |
| **Model Collapse** | 2605.23054 | 港大 | 🔶 CoNLL 2026 接受，可能后续开源 |

### D类：项目先行论文后发（6项）

| 项目 | Stars | 关联论文 | 论文时间 | 项目时间 |
|------|-------|---------|---------|---------|
| **12-factor-agents** | 22k | Foundation Protocol (W22) | 2026-05 | 2025-06 |
| **OpenViking** | 24.4k | SkillOpt / From Raw Experience (W22) | 2026-05 | 2025-08 |
| **opencode** | 55k | Co-ReAct / Metacognition (W22) | 2026-05 | 2025-10 |
| **ml-intern** | 9.7k | OpenSkillEval / Model Collapse (W22) | 2026-05 | 2025-12 |
| **cua** | 17k | Metacognition as Reward (W22) | 2026-05 | 2025-01 |
| **agentmemory** | 14.4k | SkillOpt / From Raw Experience (W22) | 2026-05 | 2025-11 |

---

## 二、重磅推荐

### A类精选：SkillOpt — Agent 技能的「训练工程」范式

**论文**: arXiv:2605.23904 | **代码**: https://aka.ms/SkillOpt | **机构**: 微软研究院

核心突破是将 skill 文档视为可训练的文本空间外部状态——不是写一次就冻结，而是通过 bounded 编辑 + 验证门控持续优化。52/52 全胜，跨 7 模型 / 3 执行环境迁移，GPT-5.5 提升 +23.5 点。

**关键数字**：
- 52/52 基准最佳或并列最佳
- 跨 7 模型 / 3 执行环境验证
- GPT-5.5 平均提升 +23.5 点
- 微软官方代码已开源

**开源价值**：这是本周**工程价值最高**的 A 类项目。SkillOpt 不是论文附属代码，而是一个「skill 训练器」——可以被任何 Agent 框架集成，让 skill 从「静态模板」进化为「可测量适应的外部状态」。

---

### A类精选：Co-ReAct — ReAct Agent 的「步级教练」

**论文**: arXiv:2605.23590 | **代码**: https://github.com/ZBWpro/Co-ReAct | **机构**: 未明确

核心突破是将评分标准（Rubrics）作为 ReAct Agent 的逐步协作者——不是等全部任务完成再评判，而是每走一步就给一次反馈。GRPO 训练 rubric 生成器，Spearman rank-correlation reward。

**关键数字**：
- 搜索密集型多步推理任务显著提升
- GRPO 训练 rubric 生成器
- 官方 GitHub 已开源

**开源价值**：可直接插入现有 ReAct 风格 Agent，作为步级决策增强插件。对编码 Agent（opencode, qwen-code）的多文件重构任务尤其有价值。

---

### C类关注：Foundation Protocol — Agent 社会的「宪法草案」

**论文**: arXiv:2605.23218 | **机构**: 多机构豪华阵容 | **代码**: 🔶 未明确

Graph-first 架构原生支持 multi-party 协作、经济原语（货币、交易、结算）和跨 Agent 边界安全交互。这是从单 Agent 走向 Agent 社会的关键基础设施。

**为什么值得关注**：
- 豪华作者阵容：Heng Ji (UIUC), Qiang Yang (港科大), Sirui Hong 等
- "Agentic Society"协议层是宏大且稀缺的叙事
- 如果代码开源，将定义 Agent 社会协调的基础标准

**趋势提示**: Agent 领域正在同时从两端逼近生产化——12-factor-agents 规范单体建筑，Foundation Protocol 定义社会协调规则。

---

### C类关注：Metacognition as Reward — LLM 的「自我觉知」

**论文**: arXiv:2605.23384 | **机构**: 未明确 | **代码**: ❌ 未提及

将元认知（metacognitive knowledge + regulation）转化为内在奖励信号，引导 LLM 推理过程。22 基准验证，Qwen3.5-9B 逼近前沿模型。

**为什么值得关注**：
- 元认知即奖励是全新 RL 范式，区别于传统外部奖励模型
- 降低对外部 reward model 的依赖，自我进化闭环
- 对编码 Agent 和 Computer-Use Agent 的自我纠错有直接价值

**趋势提示**: 编码 Agent 的竞争正在从"生成更多代码"转向"更少犯错、更快纠错"。

---

## 三、论文速递

### C类：论文已出，代码待跟进

| 论文 | arXiv | 核心贡献 | 开源状态 |
|------|-------|---------|---------|
| **OpenSkillEval** | 2605.23657 | 开放 skill 生态自动审计，600+ 实例 | 🔶 项目网站有资源 |
| **From Raw Experience** | 2605.23899 | Skill 全生命周期，meta-skill 框架 | 🔶 微软通常开源，待确认 |
| **Model Collapse** | 2605.23054 | 文化进化解释模型崩溃，CoNLL 接受 | 🔶 可能后续开源 |

> **开源比例**: 本周精选论文中 2/7 有官方代码（SkillOpt, Co-ReAct），约 28.6%。较 W21（12.5%）显著回升，但仍低于 W20（50%）。高质量 Agent 研究的代码释放正在波动，建议对 Foundation Protocol、Metacognition 设置代码发布监控。

---

## 四、联动观察

### 4.1 论文开源化比例

| 类别 | 数量 | 占比 |
|------|------|------|
| A类（论文+官方代码） | 2 | 28.6%（2/7精选） |
| B类（论文+社区复现） | 0 | 0% |
| C类（论文先行暂无代码） | 5 | — |
| D类（项目先行论文后发） | 6 | — |

**核心观察**：
- 精选论文中 **28.6% 已有官方代码**，较 W21（12.5%）显著回升
- 微软本周释放 SkillOpt 官方代码，是工业界团队开源的积极信号
- 但 Foundation Protocol（豪华阵容）、Metacognition as Reward（22 基准验证）等高质量工作仍无代码
- 中国团队方面：Co-ReAct 作者机构未明确，OpenSkillEval 有 SMU/复旦/京东参与且项目网站有资源

### 4.2 重点关注

1. **SkillOpt 的社区采用潜力**  
   作为本周 A 类核心项目，SkillOpt 的文本空间优化器如果被 agentmemory、OpenViking 等开源项目集成，可能成为 Agent skill 的「标准训练器」。建议跟踪 GitHub 仓库的 issue 和采纳情况。

2. **Foundation Protocol 的代码发布监控价值**  
   "Agentic Society"协议层是宏大叙事。如果论文作者后续释放代码，将定义 Agent 社会协调的基础标准。建议设置 arXiv 更新监控和作者社交媒体跟踪。

3. **Co-ReAct 与编码 Agent 的集成缺口**  
   官方代码已开源，但尚未见与 opencode、qwen-code 等编码 Agent 的集成案例。这是一个「代码已出、集成待跟进」的短期缺口。

### 4.3 趋势提示

**趋势1：Agent 技能从「手工作坊」进入「工业化训练」**  
SkillOpt 的文本空间优化器 + From Raw Experience 的全生命周期 + OpenSkillEval 的审计框架 = 学术界对 Agent skill 的系统性关注。skill 不再是「写得好不好」的手艺，而是「训练得对不对」的科学。

**趋势2：Agent 知识管理的三切面分化**  
SkillOpt（训练优化）+ agentmemory（记忆固化）+ OpenViking（上下文组织）= 三个独立但互补的切面。谁先定义统一接口，谁就成为 Agent 知识生态的中心节点。

**趋势3：编码 Agent 从「模型竞争」转向「决策质量竞争」**  
opencode 的 55k Stars 证明市场接受社区驱动产品。Co-ReAct 的步级 rubric + Metacognition 的自我监控 = 两条不依赖更大模型的差异化路径。

**趋势4：论文开源化比例波动需持续观察**  
W19（62.5%）→ W20（50%）→ W21（12.5%）→ W22（28.6%）。波动趋势说明 Agent 领域的高质量研究代码释放不稳定，可能与工业界团队占比上升、竞争加剧有关。

---

## 五、附录：原始数据来源

| 文件 | 路径 | 生成时间 |
|------|------|---------|
| 论文候选池 | `data/paper-pool-2026-22.md` | 2026-05-19 |
| 论文短名单 | `data/paper-shortlist-2026-W22.md` | 2026-05-28 |
| 开源候选池 | `data/os-pool-2026-W22.md` | 2026-05-27 |
| 开源短名单 | `data/os-shortlist-2026-W22.md` | 2026-05-27 |
| 论文精选分析 | `data/weekly-paper-selection-2026-W22.md` | 2026-05-28 |
| 主周报 | `data/weekly-report-2026-W22.md` | 2026-05-29 17:00 |
| 联动分析 | `output/paper-os-linkage-2026-W22.md` | 2026-05-29 17:00 |

---

*Generated by AI 开源情报周报系统 | W22 论文-开源联动分析报告*
