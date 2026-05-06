# 2026-W19 论文短名单 | 深度筛选候选

> 来源: paper-pool-2026-W19.md (23篇匹配)
> 筛选标准: (1) 开源/可复现性高 (2) 与上周候选池主题互补 (3) 工业/产品化潜力
> 精选: 8篇 | 日期: 2026-05-06 (手动补跑)

---

## 1. CASA: Continuous Agent Semantic Authorization
- **arXiv**: 2605.02682 | **领域**: Agent 安全 / 授权
- **核心**: 多轮对话中Agent工具调用的动态语义授权框架
- **亮点**: 零信任拦截层 + 任务-工具语义匹配，解决"合规陷阱"
- **入选理由**: Agent 安全基础设施论文，与上周 SCPRM/HADES 形成安全-医疗-工业的 Agent 安全三角

## 2. GRAIL: Granular Resonance-based Agent Discovery
- **arXiv**: 2605.02489 | **领域**: Multi-Agent 系统 / Agent 发现
- **核心**: 子400ms Agent发现框架，SLM标签预测 + 伪文档扩展 + MaxSim匹配
- **亮点**: AgentTaxo-9K数据集(9,240 agents), 延迟降低79x
- **入选理由**: "互联网 of Agents"的基础设施瓶颈解法，与上周 Multi-Agent 发现框架互补

## 3. DataClaw: Process-oriented Benchmark for Exploratory Data Analysis Agents
- **arXiv**: 2605.02503 | **领域**: Agent 评估 / 数据分析
- **核心**: 206万真实记录/492跨域任务，过程级里程碑评估
- **亮点**: 当前Agent准确率<50%，暴露过程断裂点
- **入选理由**: 填补了"Agent能做什么"的评估空白，与 AcademiClaw 形成学术-工业评估对

## 4. Misalignment Contagion in Multi-Agent LLMs
- **arXiv**: 2605.02751 | **领域**: Multi-Agent 安全 / 对齐
- **核心**: 多Agent社交困境中对齐传染现象，隐性特质注入缓解
- **亮点**: 不需要模型参数访问，适合黑盒模型
- **入选理由**: 上周讨论了"涌现错位人格"，这篇提供了实证机制和对策

## 5. SCHEMA: Evaluating Cognitive Collapse in Frontier Models
- **arXiv**: 2605.02398 | **领域**: AI 安全 / 认知评估
- **核心**: 67,221记录/11模型，对抗压力下认知崩溃评估
- **亮点**: "服从陷阱"识别——崩溃由强制服从驱动而非威胁内容
- **入选理由**: 最重要的安全论文之一，"Compliance Trap"概念应进入行业词汇表

## 6. HeavySkill: Heavy Thinking as Inner Skill in Agentic Harness
- **arXiv**: 2605.02396 | **领域**: Agent 架构 / 推理内化
- **核心**: 将复杂推理视为可内化的技能而非编排层功能
- **亮点**: 并行推理→总结的两阶段，RL可扩展，Pass@N接近
- **入选理由**: 对"编排层必要论"的直接挑战，可能改变Agent系统设计范式

## 7. Foundation Models in Industrial Agents (Survey)
- **arXiv**: 2605.02592 | **领域**: 工业 Agent / 系统综述
- **核心**: PRISMA筛选2,341篇→88篇，工业Agent现状全景
- **亮点**: 75%处于TRL 4-6(原型)，谈判能力缺口-39%，幻觉/延迟是主要局限
- **入选理由**: 工业Agent是上周热点(DeerFlow/OpenAI SDK)的学术基线，数据扎实

## 8. ORPilot: Open-Source Agentic AI for Business Optimization
- **arXiv**: 2605.02728 | **领域**: Agent 产品化 / 业务优化
- **核心**: 生产级业务优化Agent，对话访谈→数据采集→参数计算→求解器编译
- **亮点**: 首创面向真实业务问题(非教科书)，IndustryOR基准超越SOTA
- **入选理由**: 上周讨论了"终端即Agent界面"和"超级Agent形态"，这是商业优化领域的具体落地

---

**短名单逻辑**
- 安全 × 3: CASA(授权) + Misalignment(对齐传染) + SCHEMA(认知崩溃)
- 基础设施 × 2: GRAIL(Agent发现) + HeavySkill(推理内化)
- 评估 × 2: DataClaw(数据分析) + Industrial Survey(工业现状)
- 产品化 × 1: ORPilot(业务优化)

**下周(W20)候选池主题预判**: 
1. Agent 安全基础设施 (CASA + Misalignment + SCHEMA 的延续)
2. Agent 推理内化 (HeavySkill 引领的"去编排化"趋势)
3. 工业 Agent 落地 (Industrial Survey + ORPilot 的实证缺口)
4. Agent 评估基准 (DataClaw + AcademiClaw 的评估热潮)
