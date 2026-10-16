# AI 开源周报 · 2026-W42

> 生成时间：2026-10-16 17:00 CST | 收录项目 7 个
> 本周主题：Skills 标准战争收官 × Agent 基础设施层补齐 × 自进化实验启动

---

## 本周概览

| 排名 | 项目 | 本周增量 | 总 Star | 分类 | 一句话 |
|------|------|----------|---------|------|--------|
| 1 | obra/superpowers | — | 298,777 | Skills 框架 | Agentic Skills 框架 + 完整软件开发方法论，298K★ 逼近 GitHub 历史头部 |
| 2 | mattpocock/skills | — | 290,026 | Skills 库 | Matt Pocock 的 .agents 目录，38 个可组合工程技能，MIT |
| 3 | affaan-m/ECC | — | 278,725 | Harness OS | Agent Harness 性能优化系统，71 agents / 311 skills / AgentShield 安全扫描 |
| 4 | sst/opencode | — | 213,305 | Coding Agent | 开源终端编程 Agent，$10/月 Go 订阅两周内收支平衡 |
| 5 | Panniantong/Agent-Reach | — | 97,080 | 信息基础设施 | Agent 互联网访问能力层，15+ 平台零 API 费用 |
| 6 | zai-org/GLM-5.1 | — | 7,322 | 开源模型 | 744B MoE 编码模型，SWE-Bench Pro 58.4 曾登顶，全华为芯片训练 |
| 7 | razzant/ouroboros | — | 1,501 | 自进化实验 | 自我修改的自主 Agent，引发安全讨论与 CERT-FR 关注 |

---

## A 类：论文 + 官方代码

本周入选项目均为工程类，无直接对应的「论文+代码」双料项目。但论文侧 Stateless Language Agents（arXiv:2610.07625）与 RSI-Anything（arXiv:2610.13912）分别指向「状态设计」与「递归自改进」两个主题，与本周开源生态的演化高度共振。详见联动周报：output/weekly-report-paper-os-2026-W42.md。

---

## 🔥 重磅推荐

### 1. obra/superpowers — 298,777 ⭐

**Agentic Skills 框架 & 软件开发方法论。这可能是 GitHub 历史上增长最快的仓库之一。**

Superpowers 由 Jesse Vincent（obra）于 2025 年 10 月创建。从一个没人点赞的 Hacker News 帖子出发，12 个月内冲到 298K 星——这个速度在整个 GitHub 历史上屈指可数。它不是单一工具，而是一套完整的软件开发方法论：Brainstorming → Git Worktrees → Subagent-Driven Development → TDD → Systematic Debugging → Code Review。Skills 通过 bootstrap 指令自动触发，用户不需要记住何时激活——**「just works」是它爆发的核心原因**。

本周关注焦点：v6.0–v6.3 系列更新持续推送，Anthropic 插件市场官方收录。生态已裂变出 288 个 public repositories 匹配 superpowers topic，包括 DeepSeek Harness 适配版、Open WebUI 移植版、全栈开发模板等。

| 指标 | 数值 |
|------|------|
| 创建时间 | 2025-10 |
| 增长速度 | 12 个月 0 → 298,777★ |
| 协议 | MIT |
| 生态 | Anthropic 插件市场官方收录 |

**判断**：Skills 层的 Android 时刻。Superpowers 定义的不只是一套 prompt——它是在定义「Agent 应该如何做软件工程」的默认假设。298K★ 意味着这个假设已经被社区投票确认为事实标准。

---

### 2. mattpocock/skills — 290,026 ⭐

**"Skills for Real Engineers. Straight from my .agents directory." 38 个技能，MIT 协议，创建于 2026-02-03。**

Total TypeScript 作者 Matt Pocock 把自己实际使用的 .agents 目录原样开源。与 Superpowers 的「完整接管开发流程」不同，Matt Pocock Skills 的哲学是**「小而可组合」**——不替代你的流程，而是给你可以挑选、修改、组合的工程技能。38 个 SKILL.md 覆盖 TDD、debugging、planning、codebase architecture、grilling（苏格拉底式追问）等。

本周活跃数据：16 个 open PRs，最近一周持续合并。v1.0 引入 Progressive Disclosure 后 token 成本降低 63%。最新动态包括 wayfinder 研究路由优化、triage 分类改进、skills 版本化。已有第三方安全审计平台 SkillFlux 为其发布合格版本（1.0.0），附带完整性校验。

| 指标 | 数值 |
|------|------|
| 创建时间 | 2026-02-03 |
| 增长速度 | 8 个月 0 → 290,026★ |
| 协议 | MIT |
| 技能数 | 38 个 SKILL.md |

**判断**：与 Superpowers 的路线分歧清晰——一个是「完整方法论」，一个是「精选工具箱」。生态需要两者：Superpowers 给新手完整体验，Matt Pocock Skills 给老手精确控制。两者合计近 59 万星，SKILL.md 约定已经是事实标准。

---

### 3. affaan-m/ECC — 278,725 ⭐

**The Agent Harness Performance Optimization System. 把 Agent 外壳当操作系统来优化。**

ECC（曾用名 Agent Engineering Kernel）诞生于 2026 年 2 月的 Claude Code Hackathon（Cerebral Valley × Anthropic）。它的定位是跨平台的 Agent Harness 操作系统：同时支持 Claude Code、Codex、OpenCode、Cursor 等十余种运行时。**与模型解耦**是它的第一卖点。

五个核心模块：
- **Skills**（311 个）：按任务需要加载，不常驻上下文
- **Agents**（71 个）：带独立上下文和工具权限的隔离 worker
- **Instincts**：从真实会话学习模式，带置信度分数，需要时召回
- **Memory**：跨会话持久化 + 连续学习
- **AgentShield**：102 条静态分析规则扫描 Agent 配置安全（14 种 secrets 检测 / 权限审计 / hook 注入分析），可选三 Opus Agent 红蓝对抗审计

| 指标 | 数值 |
|------|------|
| 创建时间 | 2026-01-18 |
| 本周增量 | ~1,000+/天 |
| 协议 | MIT |
| 官网 | ecc.tools |

**判断**：ECC 是本周三强中平台化野心最大的——不只给 Skills，还给安全扫描（AgentShield）和持续学习（Instincts）。「harness OS」这个概念如果成立，ECC 就是 Agent 时代的 Windows。但 311 skills + 71 agents 的体量也带来维护成本——用户需要审慎评估 blast radius。

---

## 🛠️ 工具框架类

### 4. sst/opencode — 213,305 ⭐

**开源终端编程 Agent。$10/月 Go 订阅两周内实现收支平衡——开源 Agent 商业化的第一个正面样本。**

OpenCode 由 Anomaly 团队（SST 背后）开发，Go 语言构建，MIT 协议。核心免费，支持 75+ 模型提供商。付费层 Go（$10/月）聚合 14+ 开源模型（GLM-5.1/K2.6/DeepSeek V4/Qwen/MiniMax），Go Plus $40/月。一个 API key 可用于任何 Agent。

**本周核心事件**：Dax Raad 公开确认 Go 订阅两周内实现收支平衡——这在 AI coding 工具的补贴大战中是罕见的正向信号。Go 的模型阵容已扩至 19 个（仍以中国实验室为主，加入 Grok 4.5 和 GPT 5.6 Luna 作为例外）。背景故事：2026 年 1 月 Anthropic 封锁第三方 Claude 订阅凭证后，OpenCode 星数翻倍，团队快速转向推出 Go/Zen/Black 三条产品线。

| 指标 | 数值 |
|------|------|
| 月活开发者 | ~6.5M |
| 语言 | Go |
| 协议 | MIT |
| 商业化 | Go $10/月 · Zen 按量 · Black 企业 |

**判断**：OpenCode Go 证明了「开源 Agent + 低价模型聚合」的商业模式可以跑通。不是补贴换增长——是真实的单位经济模型。如果 $10/月能持续覆盖成本，它对 $20/月的 Claude Code 和 $100+/月的 Cursor 构成的威胁不是性能，是价格锚点。

---

### 5. Panniantong/Agent-Reach — 97,080 ⭐

**给 Agent 装上互联网之眼。15+ 平台零 API 费用，一个 CLI 打通东西方互联网。**

Agent-Reach 是开源的能力层框架——不负责底层读取，负责选型、安装、体检、路由。每个平台配置首选+备选工具链，失效自动切换。支持 Twitter/X、Reddit、YouTube、GitHub、B站、小红书、LinkedIn、V2EX、雪球等。

**架构亮点**：
- `agent-reach doctor` 一条命令诊断全平台可用状态
- Cookie/登录态支持（Twitter、小红书、Reddit 等）
- MCP Server 接口（8 工具）
- 隐私优先：cookie 本地存储，不上传
- 自愈合：主路由失效时自动切备选

| 指标 | 数值 |
|------|------|
| 创建时间 | 2026-02 |
| 语言 | Python |
| 协议 | MIT |
| 覆盖 | 15+ 平台（含中文平台） |

**判断**：Agent-Reach 补上的是 Agent 基础设施中最被低估的一层——信息访问。一个没有互联网访问能力的 Agent 就像一个只能背诵训练数据的实习生。97K★ 说明开发者已经达成共识：**Agent 的下一个瓶颈不是模型能力，是信息管道**。风险：上游工具链的可靠性不由 Agent-Reach 控制——它是一个路由层而非数据层，平台改版随时可能击穿路由。

---

## 🧠 模型与算法类

### 6. zai-org/GLM-5.1 — 7,322 ⭐

**744B MoE 开源编码模型（40B 激活/token），200K 上下文，MIT 协议。全华为芯片训练，无一 NVIDIA GPU。**

Z.ai（原智谱 AI）2026 年 4 月 7 日开源。发布时以 SWE-Bench Pro 58.4 登顶全球编码榜（超 GPT-5.4 的 57.7 和 Claude Opus 4.6 的 57.3——注意部分分数为自报）。200K 上下文窗口，支持 128K 输出。异步 Agent RL 后训练，支持 8 小时自主执行。

**核心意义不在基准而在硬件**：GLM-5 全系完全使用华为 Ascend 910B 训练，零 NVIDIA GPU。在美国芯片出口管制背景下，这是「非美硬件可以训练竞争性前沿模型」的第一个完整证明。API 价格 $0.98/$3.08 每百万 token，Coding Plan $3-30/月。

| 指标 | 数值 |
|------|------|
| 参数 | 744B 总参 / 40B 激活 |
| 上下文 | 200K |
| 协议 | MIT（HuggingFace: zai-org/GLM-5.1） |
| 训练硬件 | 全华为 Ascend 910B |
| API 价格 | ~$0.98/$3.08 每百万 token |

**判断**：GLM-5.1 已被 OpenCode Go 作为核心模型收录，被 ToFu 论文用作开源 baseline。它证明了两件事：一是 MIT 协议的前沿模型可以真实威胁闭源商业模式（价格 1/30）；二是中国实验室在非美硬件上做出了全球竞争力的编码模型。后续 GLM-5.2（1M 上下文）已于 6 月发布，但 5.1 的 7.3K★ 和生态集成度仍是 GLM 系列中社区基础最深的版本。

---

## 🐍 实验性项目

### 7. razzant/ouroboros — 1,501 ⭐

**自我创建的 AI Agent。能修改自己的实现代码，跨重启保持身份与记忆持续演化。**

Ouroboros 由 Anton Razzhigaev 于 2026 年 2 月 16 日创建。它是一个通用 AI Agent，可编辑范围覆盖应用代码、架构、prompts、工具和依赖。支持自主演化（Evolution campaigns）、跨重启持续身份、后台意识（Background consciousness）、并行专家 swarm 协调。

**本周状态**：v7.6.0（10/05 发布）。638 forks。

这个项目引发了超出代码本身的安全讨论：法国国家网络安全局 CERT-FR 在 2026-04-13  bulletin（CERTFR-2026-ACT-016）中将其列为典型案例——Agent 必须部署在隔离环境中，副作用操作需人工验证。批评者指出：一个可以修改自身规则的 Agent，实际上不受这些规则约束。

| 指标 | 数值 |
|------|------|
| 出生 | 2026-02-16 |
| 语言 | Python |
| 协议 | MIT |
| 最新版 | v7.6.0（10/05） |

**判断**：Ouroboros 是「自进化 Agent」方向最大胆的公开实验——比 Q00/ouroboros（同名但完全不同的 spec-first 工作流引擎，6.2K★）更激进。1.5K★ 的体量意味着它仍是实验性项目而非生产工具，但它提出的问题——**Agent 的治理边界应该由外部架构还是自身宪法定义**——是整个行业必须回答的。

---

## 📊 数据观察

### Skills 三强的生态位分化

| 维度 | Superpowers | Matt Pocock Skills | ECC |
|------|------------|-------------------|-----|
| 定位 | 完整方法论 | 精选工具箱 | Harness OS |
| 星数 | 298,777 | 290,026 | 278,725 |
| 规模 | 全套工作流 | 38 skills | 311 skills + 71 agents |
| 哲学 | 接管全流程 | 小而可组合 | 跨平台操作系统 |
| 安全 | 无内置扫描 | SkillFlux 第三方审计 | AgentShield 102 规则 |
| 协议 | MIT | MIT | MIT |

三者合计 867K★——SKILL.md 生态已经不是「一个热门项目」，是一个行业。六个月前全 GitHub 约有 2,000 个含 SKILL.md 的仓库，现在超过 24,000 个。10 倍增长，6 个月。

### OpenCode Go 的单位经济

$10/月，14+ 开源模型，三层用量限制（~$12/5h、$30/周、$60/月）。两周收支平衡意味着：
- 大多数用户远未触达用量上限
- 模型提供商（中国实验室）的 API 成本极低
- 「模型聚合」作为商业模式的毛利率可以非负

这是 2026 年 AI coding 工具补贴大战中第一个被验证的正向单位经济模型。

### 星际分布断层

本周 7 个项目呈极端双峰分布：Top 5 全部 ≥ 97K★，第 6 名骤降至 7.3K，第 7 名 1.5K。中间层（10K-90K）完全空缺。这反映了 GitHub AI 领域的**马太效应**——头部项目吸走绝大部分注意力，新项目要么快速冲榜要么被埋没。Agent-Reach 从 2 月的 ~0 到 10 月的 97K 是中间层最成功的一次突围。

---

## 🔗 与论文侧的联动（摘要）

本周论文侧与开源侧的共振异常强烈：

1. **Stateless Language Agents**（Stanford, 22 分）证明长程 Agent 的瓶颈在状态设计而非模型——这恰是 Skills 三强（Superpowers/Matt Pocock/ECC）崛起的技术基础：Skills 本质上是状态管理的最佳实践封装。
2. **RSI-Anything**（上海 AI Lab, 20 分）的递归自我改进框架与 razzant/ouroboros 的自我修改实验构成学术与工程的镜像。
3. **T²Mem** 的按需记忆构建与 ECC 的 Memory 模块、**RATED** 的工具可靠性感知与 Agent-Reach 的平台路由，分别指向同一目标：让 Agent 按需获取正确的外部信息。
4. **KV-Repurpose** 的段落级 KV 复用（命中率 63.9% vs 3.3%）和 **VisionWeave** 的弹性视觉表示（省 43% token）是推理成本持续压缩的最新证据——与 OpenCode Go 的 $10 经济学互为因果。

完整联动矩阵见 output/weekly-report-paper-os-2026-W42.md。

---

## 📚 推荐阅读

1. **[Superpowers: The Framework That Redefined Agentic Coding](https://kunalganglani.com/blog/superpowers-agentic-skills-framework)** — 298K 星的深度验证报告，覆盖从 HN 帖子到事实标准的完整历程
2. **[Write Skills That Load: Five Rules from 500K Stars](https://dev.to/max_quimby/write-skills-that-load-five-rules-from-500k-stars-4go7)** — 为什么大多数 SKILL.md 不会被 Agent 加载？五条结构性规则
3. **[OpenCode Go 经济学：$10/月的可持续性分析](https://www.tonyreviewsthings.com/opencode-go-review/)** — 从 9 模型到 19 模型，用量上限的实操体验
4. **[Zhipu GLM-5.1 in 2026: The Open Model Trained Without a Single NVIDIA GPU](https://convly.ai/zhipu-glm-explained-2026/)** — 硬件主权视角下的 GLM 分析
5. **[Ouroboros: The AI Agent That Refused to Stop](https://www.stroople.com/ouroboros-autonomous-ai-agent-security-risks/)** — CERT-FR 视角的自修改 Agent 安全分析

---

## 本周总结

W42 是 Skills 生态的「定鼎周」。Superpowers、Matt Pocock Skills、ECC 三个项目合计 867K★，SKILL.md 从约定俗成变成事实标准。开源 Agent 的商业化出现了第一个正向样本（OpenCode Go 两周收支平衡）。信息访问层（Agent-Reach）和模型层（GLM-5.1）分别补齐了基础设施的东西两翼。而 Ouroboros 和 RSI-Anything 从工程和学术两个方向同时启动了「Agent 能否自我改进」的深层问题。

**W41 的问题是「每层多少钱」，W42 的回答是：Skills 层免费（MIT），模型层 $10/月，信息层零 API 费用——整个 Agent 栈的单位成本正在趋向于零。当基础设施免费，真正的竞争将在编排质量和信息质量上展开。**

---

*Generated by Kimi Claw intelligence pipeline, 2026-10-16*
