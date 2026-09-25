# 论文-开源联动分类分析 | 2026-W39

> 分析日期：2026-09-25
> 论文来源：data/paper-shortlist-2026-W39.md（8篇，46候选，入选率17.4%）
> 开源来源：data/os-shortlist-2026-W39.md（7个，10候选+2延续观察）
> 分析维度：A-D联动映射 × 6大主题 × 联动矩阵 × 趋势判断
> 前置状态：周一收集 ✅ / 周二雷达 ✅ / 周三筛选 ✅ / 周四精选 ✅ / 周五主周报 ✅（17:04）

---

## 一、联动映射总览

本周论文侧与 OS 侧**无同一仓库的直接重叠**，但主题共振强度为近四周最高——论文侧的 Skill 理论化（GraphSkillEvo / EvoOntology）与 OS 侧的 Skill 标准化周在同一抽象层（SKILL.md 标准 + MCP 分发形态）精确相遇。映射表按 A-D 优先级排序。

### A类：论文+官方代码（强关联）

| # | 论文/项目 | 代码/论文 | 关联强度 | 关联说明 |
|---|----------|----------|---------|---------|
| A1 | RecreationWorld（arXiv:2609.22000，24分） | 环境+基准+测试套件随论文全量开源 | ⭐⭐⭐ | 五平台混合 CUA 环境，以可运行参考程序为 oracle 提供执行级奖励。与 cua（26k★）构成"学术环境 ↔ 工程设备群"互为镜像：论文发现 GPT-6 Astra 全过程序化测试仅 2.8%，cua 的 fleets + 基准三件套正是这类训练/评测的工程载体 |
| A2 | EvoOntology（arXiv:2609.15779，22分） | github.com/ruc-datalab/EvoOntology | ⭐⭐⭐ | 自进化本体层封装为 **MCP server**，且作为 MCP 插件接入 Claude Code / Codex——学术界的 Agent 数据层研究选择以 MCP 插件作为分发形态，协议层的胜利在论文侧盖章。直接对应 OS 侧 Skill 标准化周的"协议层" |
| A3 | GraphSkillEvo（arXiv:2609.21749，21分） | github.com/ruisun7/GraphSkillEvo | ⭐⭐⭐ | 把 Agent 技能从非结构化自然语言升级为图结构（节点=执行步骤+操作指引，边=上下文迁移）再做种群进化。恰逢 ECC 292 技能 / Addy Osmani 25 技能的规模爆发，**"技能怎么进化"成为下一问**。对应 OS 侧"优化层"，是本周论文-开源共振的第一主线 |
| A4 | DeepSeek-V4.1-Flash（arXiv:2609.19969，24分） | huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash（权重开源，训练代码未放） | ⭐⭐ | KV cache 压至 890B/token（HBM 1/4、SSD 1/8），设计目标直接写明"长 horizon Agent 输入密集型负载"。与 ECC 的 token 优化指南（thinking tokens -70%、MCP ≤10 限额）构成 Agent 经济学的两层解：模型层扩容 × 应用层节流 |
| A5 | TrustReviewer（arXiv:2609.20942，20分） | 论文声明 open-source（仓库地址待核实） | ⭐⭐ | AI 评审递归训练导致判断多样性坍缩，训练期数据策展+测试期 activation steering 双阶段缓解。对 agent-skills 的 /review、ECC 的 code-review 流程是直接警示：**用 AI 评审 AI 产出的闭环必须带多样性保护，否则评审本身会退化** |

### B类：论文+社区复现（中关联）

| # | 论文 | 可复现载体/关联项目 | 关联强度 | 关联说明 |
|---|------|-------------------|---------|---------|
| B1 | Scaling Discovery through Test-Time Communication（arXiv:2609.21032，21分） | Pi / chord 运行时 | ⭐⭐⭐ | k 个通信 Agent 抵 4k 个独立 Agent 且随 k 扩大，ARC-AGI-3 与 MNIST 压缩赛双重验证。**Pi 的 chord（RPC + 复制状态运行时）恰是这类 test-time 通信的工程载体**——论文给出 scaling 证据，chord 给出基础设施。Caveat 同样诚实：算力受限或无进度信号时通信有害，这对"为通信而通信"的多 Agent 编排是一盆冷水 |
| B2 | CodeMidas（arXiv:2609.22068，19分） | ECC / agent-skills / Pi coding-agent | ⭐⭐ | 小米 MiMo：从代码库直接提取多样化 RL 任务（静态+动态分析，不依赖 issue/commit），回答"Agent 编码训练环境从哪来"。ECC 的 68 个 subagent、agent-skills 的 TDD 流程产出大量真实编码轨迹，正是这类环境的需求端 |
| B3 | CogGym（arXiv:2609.21259，20分） | 全部入选项目（横向） | ⭐⭐ | 258 个认知实验对比 50 个 LLM：最佳模型-人类拟合仅 R²≈0.59（人类分半信度 0.93），常识推理进步远慢于数学/编码。这对所有"Agent 技能按流程跑通就上线"的工程实践是底层警告：**形式推理提升 ≠ 人类式理解，流程化 Agent 在长尾常识场景会系统性翻车**。对 json-render 类"人机交互面"项目尤甚 |

### C类：论文先行（弱关联/待跟进）

本周无严格意义的 C 类——8 篇入选全部有官方开源 artifact 或明确复现路径。以下关注级论文接近 C 类边界：

| # | 论文 | 潜在关联方向 | 跟进建议 |
|---|------|------------|---------|
| C1 | DENSE（arXiv:2609.21423，18分，关注级） | 轨迹蒸馏 → Pi / ECC 会话数据 | 代码未放。若开源，其"从轨迹蒸馏证据快捷树"可直接消费 Pi 的 pi-durable 持久会话数据与 ECC Memory Vault 的会话记忆，形成"生产轨迹 → 自我改进"闭环 |
| C2 | Chronicle（arXiv:2609.20625，18分，关注级） | 失败重放 → 全部 harness | 代码已开源（github.com/theagentplane/chronicle）。cut-point 重放让 Agent 失败可复现、可做回归测试——多 harness 时代（ECC 兼容 10+）的跨 harness 调试基础设施，下周可能升档 |

### D类：项目先行（独立演进）

| # | 项目 | 技术领域 | 状态 | 论文跟进建议 |
|---|------|---------|------|------------|
| D1 | ECC（⭐267,122） | 多 Harness 优化层 | v2.2.1，9/21 三连安全修复 | 单维护者 + 292 技能的进化/去重问题正是 GraphSkillEvo 的靶心；学术侧缺"跨 harness 优化层"的对照研究（候选池 #6 Harness Design 是雏形）。68 个 subagent 间的通信效率可用 Scaling Discovery 的框架测量 |
| D2 | agent-skills（⭐98,950） | 生产级工程技能集（KOL/社区层） | 25 技能 + 9 slash 命令，9/23 质量基建合并 | 技能质量评估缺学术基准——GraphSkillEvo 的五基准可改造为 skill benchmark；/review 流程与 TrustReviewer 的多样性坍缩问题直接相关 |
| D3 | Pi（⭐109,246） | 统一 Agent 工具包（厂商中立路线） | pi-durable 加入 checkpoints，9/24-25 高频提交 | chord 运行时缺 test-time 通信的理论指导（Scaling Discovery 可补）；无内置权限系统的设计选择值得安全学术圈形式化 |
| D4 | financial-services（⭐37,447） | Anthropic 官方金融技能库 | 9/21 删除 claude-for-financial-advisors 目录（合规回撤） | 垂直领域 know-how 编码化的首个样本；金融合规约束下的技能设计（命名雷区、凭证处理）是案例研究素材 |
| D5 | security-audit-skill（⭐21,425） | 编码 Agent 多阶段安全审计 | last push 9/14，star 照涨（+1,086/48h） | 审计发现的"独立可验证、机器可读"格式是评测方法论贡献，值得论文形式化；与 CodeMidas 的静态+动态分析共享技术底座 |
| D6 | json-render（⭐18,275） | 生成式 UI 框架 | v0.21.0，实验性 composition API | Agent 输出的结构化渲染（JSON → 组件目录）缺形式语义研究；与 AG-UI / MCP-UI 的协议关系是下一个学术问题 |

---

## 二、六大主题深度分析

### 主题1：Skill 标准化与进化 🧬 —— 本周第一主线

**核心论文**：GraphSkillEvo (A3), EvoOntology (A2)
**核心项目**：ECC, agent-skills, financial-services, security-audit-skill

**联动分析**：
W38 我们记录了 Harness 碎片化；W39 社区在同一抽象层收敛出了答案：**Skill 成为 Agent 时代的新交付单元，且分层已经完成**。厂商层（Anthropic 金融 37k★、Cloudflare 安全审计 21k★）把领域 know-how 编码成标准技能分发；社区层（Addy Osmani 99k★、ECC 292 技能体系）覆盖长尾工程实践。两层共用 SKILL.md 标准——标准之战没有发生，因为两边在吃同一个标准的红利。

论文侧在同周完成了理论化，且恰好分成两层对应：**GraphSkillEvo 对应优化层**（技能图结构化 + 种群进化，五基准超 SkillOpt），**EvoOntology 对应协议层**（自进化本体封装为 MCP server，直接接入 Claude Code / Codex）。这是近四周第一次出现"论文两层 ↔ 工程两层"的精确对位。

更深一层的信号是 EvoOntology 的分发形态选择：学术界的 Agent 数据层研究，把 MCP 插件当作默认分发渠道——协议层的胜利已经从工程侧蔓延到论文侧。而 GraphSkillEvo 回答的问题是 ECC 们下个月就会遇到的：292 个技能怎么进化、怎么去重、怎么防止腐化。GPT-5.4-nano 上 +4.01% 的数字不大，但方向明确：**技能库的规模红利会耗尽，进化红利才刚开始**。

**趋势判断**：技能库将从"静态手册"转向"可进化种群"（GraphSkillEvo 范式）；MCP 插件成为学术成果分发的默认形态之一；2026Q4 将出现技能质量基准。

---

### 主题2：Agent 训练环境与数据供给 🏋️

**核心论文**：RecreationWorld (A1), CodeMidas (B2)，关注级 DENSE
**核心项目**：cua, Pi

**联动分析**：
三篇同周出现且全部入选/关注级——"Agent 数据/环境从哪来"正式取代"Agent 架构怎么搭"成为社区共识瓶颈。

RecreationWorld 从**环境**侧切入：五平台混合 CUA + 可运行参考程序作 oracle，提供执行级奖励，彻底解决 GUI Agent"奖励从哪来"的问题。CodeMidas 从**任务**侧切入：不依赖 issue/commit，直接从代码库静态+动态分析提取多样化 RL 任务，支撑 MiMo-V2.5 训练。DENSE 从**反馈**侧切入：无标注下从轨迹蒸馏证据快捷树。环境、任务、反馈——Agent 训练数据的三要素同周被三篇论文分别攻击。

工程侧的地基是 cua：开源 drivers + 跨 OS fleets + 训练/评估/数据生成基准三件套，是这类环境的"叉车供应商"。论文侧与工程侧在此主题的关系不是镜像而是接力：RecreationWorld 证明 oracle 式执行奖励可行，cua 提供让这种可行变成可扩展的设备群与数据管线。最刺眼的数字来自论文侧：GPT-6 Astra 在 RecreationBench 总分 58.1%，但全过程序化测试仅 2.8%——**头部模型在"GUI 操作 × 编码开发"混合任务上的脆弱性，正是这类环境要训练掉的东西**。

Pi 的 coding-agent + pi-durable checkpoints 是暗线：长会话状态可恢复性提升后，真实编码会话本身就成了环境数据来源。

**趋势判断**：环境供给将成为 Agent 公司的核心竞争力（类比 RL 时代的仿真器）；oracle 式执行奖励（可运行参考程序）会成为 GUI/编码 Agent 训练的标准配置；"从生产轨迹蒸馏改进信号"（DENSE 范式）是下一个开源热点。

---

### 主题3：推理效率与 Agent 经济学 ⚡

**核心论文**：DeepSeek-V4.1-Flash (A4)
**核心项目**：ECC, Pi

**联动分析**：
本周唯一"模型层炸弹"。552B MoE 以 CSA2+FP4 把 KV cache 压至 890B/token（HBM 足迹上代 1/4、SSD 1/8），设计目标白纸黑字写着"长 horizon Agent 的输入密集型负载"——工具返回、文件上下文、多轮轨迹正是 KV cache 的最大消费者。**推理效率研究与 Agent 需求正式合流，这不是通用降本，是对准 Agent 经济模型的定向武器。**

与 OS 侧的联动是两层解的会师：ECC 的 token 优化指南是应用层节流（thinking tokens 31,999→10,000 隐藏思考成本 -70%、MCP ≤10 限额、autocompact 95→50），V4.1-Flash 是模型层扩容。同一周成熟，方向相反，同时降低 Agent 部署成本曲线的两端。Pi 的 pi-ai 统一多厂商 API 则在这两层之下提供了第三个自由度——供应商切换的议价能力。

值得记录的反直觉点：ECC 的指南里写着"200k 上下文会被 MCP 描述吃掉一半"——这句话与 V4.1-Flash 的设计动机是同一枚硬币的两面：**Agent 时代的上下文不是稀缺到要省，而是膨胀到必须同时在模型层（压缩）和应用层（配额）双重治理**。

**趋势判断**：KV cache 压缩将进入"按负载类型定制"阶段（长 horizon Agent / 高并发 serving / 边缘部署各一套方案）；"Agent token 经济学"会成为部署文档的标配章节。

---

### 主题4：多智能体通信与运行时 🕸️

**核心论文**：Scaling Discovery (B1)
**核心项目**：Pi / chord, ECC

**联动分析**：
MSR/UW-Madison 的标杆结果：test-time 通信让 k 个 Agent 抵 4k 个独立 Agent，且在 ARC-AGI-3 与 MNIST 压缩赛上双重验证。这为"多 Agent 通信 scaling law"方向给出了第一个有分量的证据。

工程侧的现成载体是 Pi 的 chord——RPC + 复制状态的运行时，本周还在做不可变批量应用优化。ECC 的 68 个 subagent 则是需求端样本：subagent 之间的任务交接、证据供应（skill-comply 阻断失败步骤向下游供应证据）、Memory Vault 共享记忆，本质上都是 test-time 通信的具象化。

但本周最值钱的其实是论文的 caveat：**算力受限或无明确进度信号时，通信反而有害**。这对多 Agent 编排社区是一盆及时的冷水——当"编排多个 Agent"成为默认架构选择，"什么时候不该通信"比"怎么通信"更稀缺。ECC 的反模式警示（活跃工具 ≤80）和 Scaling Discovery 的边界条件在精神上一致：**Agent 系统的性能来自约束，不来自堆料**。

**趋势判断**：多 Agent 框架将从"固定拓扑编排"转向"通信带宽自适应"；test-time compute 的分配（通信 vs 独立探索）成为新的超参战场。

---

### 主题5：评估危机与认知边界 ✅

**核心论文**：CogGym (B3), TrustReviewer (A5)，关注级 EvoPilot
**核心项目**：security-audit-skill, agent-skills

**联动分析**：
三篇论文从三个角度指向同一个裂口：**LLM 的形式能力提升与真实可靠性之间的裂口在扩大**。

CogGym 从认知科学侧给出系统证据：258 个标准化认知实验对比 50 个 LLM，最佳模型-人类拟合仅 R²≈0.59（人类分半信度 0.93），且常识推理的进步速度远慢于数学/编码。Tenenbaum、Hawkins 等 60+ 作者的全明星阵容让这份证据很难被当作"又一个基准"。TrustReviewer 从科学共同体侧给出机制：AI 生成的评审进入训练语料后，评分分布压缩、语义多样性下降——**递归自我消费导致判断坍缩**。EvoPilot 从生产侧给出数字：37 天在线 autoresearch 实战里，无验证的 primitive 流程得出 -22pp 的错误结论，human-gated 验证才纠正回来。

工程侧的回应已经出现：security-audit-skill 把审计发现做成"独立可验证、机器可读"的 structured findings——这是把 TrustReviewer 的多样性原则工程化（结论必须能被独立复核，而非复述上游判断）。agent-skills 的 /build auto 模式"移除任务间人工 stepping 但不移除验证，每个任务仍走 TDD 并独立提交"——同样是"自动化但保留独立验证点"的设计哲学。

三条证据链 + 两个工程回应，共同勾勒出 Agent 时代的质量守恒式：**自动化可以扩展执行的规模，但验证的独立性必须按 1:1 保留**。

**趋势判断**：AI 生成内容进入训练语料的"递归污染"将成为 2027 年的数据治理主议题；独立可验证输出（structured findings）成为 Agent 工具的设计标配；认知拟合度（而非任务分数）将进入 Agent 选型指标。

---

### 主题6：Agent 输出离开聊天框 🖼️

**核心论文**：RecreationWorld (A1, GUI 操作面)
**核心项目**：json-render, cua

**联动分析**：
本周 Trending 的三支箭——json-render（JSON → 组件目录内生成 UI）、cua（操作跨 OS 设备群）、被淘汰但值得观察的 agent-native——共同宣告"Agent-native 交互"成为前端基建团队的明确赛道。json-render 的 guardrail 模式（"You set the guardrails, AI generates within them"）让 Agent 输出第一次有了可设计的渲染边界；渲染目标从 React/Vue/Svelte 到 react-three-fiber 3D 场景、react-email、终端 ink——同一个 JSON schema 从聊天窗口到邮件到 3D。

论文侧的呼应是 RecreationWorld 的混合 CUA：GUI 操作 × 编码开发自由切换，五平台覆盖。聊天框之外，Agent 的输出面有两种形态：**渲染给用户的界面**（json-render 层）和**操作物理/虚拟世界的动作**（cua / RecreationWorld 层）。两层本周同时在列。

交叉点值得关注：json-render 的组件目录本质上是结构化的"可允许动作空间"，与 CUA 环境的 action space 是同构问题——**一个定义 Agent 能渲染什么，一个定义 Agent 能点什么**。下周 AG-UI / MCP-UI 协议层的动作（OS 侧核心判断 #3 已预告）可能把这两层统一进同一套 schema。

**趋势判断**：Agent UI 协议层（AG-UI/MCP-UI）将在 4-6 周内爆发标准之争；组件目录设计将成为新的前端专业技能；"渲染边界即权限边界"的安全语义研究是空白。

---

## 三、联动矩阵

```
                      DS-V4.1-Flash  RecreationWorld  EvoOntology  ScalingDiscovery  GraphSkillEvo  CogGym  TrustReviewer  CodeMidas
ECC                        ⭐⭐             ⭐              ⭐⭐⭐          ⭐⭐             ⭐⭐⭐         ⭐         ⭐⭐           ⭐⭐
agent-skills               ⭐               ⭐              ⭐⭐            ⭐              ⭐⭐⭐         ⭐         ⭐⭐           ⭐⭐
Pi                         ⭐⭐             ⭐⭐             ⭐             ⭐⭐⭐            ⭐           ⭐          ⭐            ⭐⭐
financial-services          ⭐               -               ⭐⭐            -               ⭐⭐          -          ⭐             -
security-audit-skill        ⭐               -               ⭐             -                ⭐           ⭐         ⭐⭐           ⭐⭐
cua                        ⭐⭐             ⭐⭐⭐            ⭐             -                ⭐           ⭐          -             ⭐
json-render                ⭐               ⭐⭐             ⭐⭐            -                ⭐          ⭐⭐         ⭐             -
```

**矩阵解读**：
- **GraphSkillEvo 和 EvoOntology 是本周"论文侧枢纽"**（各关联 5-6 个项目）：Skill 主题横向贯穿全部 7 个入选项目中的 5 个，共振强度近四周最高
- **ECC 是"项目侧枢纽"**：作为唯一同时兼容 10+ harness 的优化层，它与论文侧的全部四个方法论主题（技能进化/通信/经济学/评审）都有接口
- **RecreationWorld ↔ cua 是本周最强单点联动（⭐⭐⭐）**：学术环境与工程设备群互为镜像，且方向互补（oracle 奖励 ↔ 扩展载体）
- **Scaling Discovery ↔ Pi/chord 暂时单向**：论文有证据、工程有载体，但 chord 尚未按论文框架做通信效率测量——行动建议中列为 P1
- **financial-services 和 security-audit-skill 横向关联最少**：垂直技能的强领域属性决定了它们只与对应方法论相连，这是特性不是缺陷

---

## 四、趋势判断与展望

### 🔥 热点趋势（已验证）

1. **Skill 成为新交付单元且分层完成**：厂商层（know-how 编码化）+ 社区层（长尾实践）共用 SKILL.md 标准，个人 KOL 与一线厂商同层收敛——社区-厂商共识形成的标志
2. **Agent 环境供给成为瓶颈赛道**：RecreationWorld + CodeMidas + DENSE 三篇同周，环境/任务/反馈三要素被分别攻击
3. **推理效率与 Agent 需求合流**：V4.1-Flash 直接为长 horizon Agent 设计，推理效率研究首次把 Agent 负载写进设计目标

### ⚡ 新兴趋势（苗头初现）

1. **技能进化红利**：GraphSkillEvo 证明技能库可种群化进化——ECC 292 技能的维护者下个月就会需要这个
2. **Agent-native UI 协议层**：json-render/cua/agent-native 三箭齐发，AG-UI / MCP-UI 的标准动作在下周
3. **递归污染治理**：TrustReviewer 揭示 AI 评审递归训练的判断坍缩——AI 生成内容回灌训练语料的治理将是 2027 数据主议题

### 📉 冷却趋势

1. **单 harness 绑定工具**：Pi 的厂商中立路线（8 月 +20,142/月）与 ECC 的 10+ harness 兼容同时跑赢单 harness 工具
2. **纯聊天框交互**："Agent 输出离开聊天框"三箭齐发，纯文本交互的项目在 Trending 榜单上消失
3. **无验证的自主研究**：EvoPilot 的 -22pp 误判案例给 autoresearch 社区上了human-gated 的一课

---

## 五、行动建议

### 对开源贡献者

| 优先级 | 建议 | 关联论文/项目 |
|--------|------|--------------|
| P0 | 用 GraphSkillEvo 的进化框架给 ECC 292 技能做去重/腐化检测试点 | GraphSkillEvo + ECC |
| P0 | 把 security-audit-skill 的 structured findings 格式引入 /review 流程，给 AI 评审加"独立可验证"约束 | TrustReviewer + agent-skills |
| P1 | 在 Pi/chord 上复现 Scaling Discovery 的通信实验，测量 68-subagent 级联场景的通信带宽收益 | Scaling Discovery + Pi/ECC |
| P1 | 用 RecreationWorld 的 oracle 思路给 cua 的基准加执行级奖励通道 | RecreationWorld + cua |
| P2 | 跟踪 DENSE 代码释放，接 Pi pi-durable 会话数据做"生产轨迹→自我改进"试验 | DENSE + Pi |
| P2 | 在 json-render 组件目录上加"渲染边界即权限边界"的声明式约束层 | 主题6 前瞻 |

### 对研究者

| 优先级 | 建议 | 理由 |
|--------|------|------|
| P0 | 建立 Skill 质量基准（可进化性/腐化率/去重难度），替代现有的"技能数量"指标 | GraphSkillEvo 有五基准但无社区级 skill benchmark |
| P0 | 实证 Scaling Discovery 的边界条件：什么信号算"明确进度"，通信成本怎么建模 | 论文 caveat 诚实但操作化定义缺失 |
| P1 | 形式化"渲染边界即权限边界"：json-render 组件目录的安全语义 | Agent UI 协议层爆发前的理论空窗 |
| P1 | 研究 MCP 插件作为学术成果分发形态的引用/复现计量学 | EvoOntology 开了先河，计量学跟不上 |
| P2 | 将 CogGym 的认知拟合指标引入 Agent 评测 harness（Pi/ECC 是现成载体） | R² 0.59 的认知拟合度与任务成功率的相关性未知 |

---

## 六、本周联动数据汇总

| 指标 | 数值 |
|------|------|
| 本周入选论文 | 8篇（46候选，入选率17.4%） |
| 本周入选开源项目 | 7个（10候选+2延续观察） |
| A类（论文+官方代码） | 5对（RecreationWorld / EvoOntology / GraphSkillEvo / DS-V4.1-Flash / TrustReviewer） |
| B类（论文+社区复现） | 3对（ScalingDiscovery / CogGym / CodeMidas） |
| C类（论文先行） | 0对（DENSE / Chronicle 接近 C 类边界，均在关注级） |
| D类（项目先行） | 6个（ECC / agent-skills / Pi / financial-services / security-audit-skill / json-render） |
| 强关联（⭐⭐⭐） | 6对 |
| 论文-代码双料 | 5个（EvoOntology / GraphSkillEvo / RecreationWorld / DS-V4.1-Flash / TrustReviewer） |
| 论文侧枢纽 | GraphSkillEvo、EvoOntology（各关联 5-6 项目） |
| 项目侧枢纽 | ECC（与全部四个方法论主题有接口） |
| 最强单点联动 | RecreationWorld ↔ cua（⭐⭐⭐，学术环境 ↔ 工程设备群互为镜像） |

---

*Generated by friday-paper-merge | Week 39, 2026*
*论文-开源联动分析完毕*
