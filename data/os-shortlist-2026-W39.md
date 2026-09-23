# 周三精选短名单 · W39 / 2026-09-23

> 筛选来源：`data/os-pool-2026-W39.md`（10 个候选 + 2 个延续观察项）
> 筛选规则：Star < 100 且无媒体 coverage → 淘汰；候选全部通过 Star 门槛，按主题代表性、技术测评、媒体 coverage 精选至 7 个
> 数据验证时间：2026-09-23 14:00 CST（GitHub API 实时 star / 媒体检索）

---

## 一、本周短名单（7 个）

### AI Agent 基础设施层（5）

| 项目 | 定位 | 实时 Star | 技术测评要点 | 媒体 Coverage | 风险/备注 |
|------|------|-----------|--------------|---------------|-----------|
| **ECC** (affaan-m/ECC) | 多 Harness 兼容优化层 | **265,600** | Skills / instincts / memory / security 一体化；同时兼容 Claude Code、Codex、OpenCode、Cursor；JS，MIT，fork 39.7k；9/22 仍在 push | 本周 GitHub Trending 持续在榜（9/20 单日 +837），聚合站密集收录 | Harness 碎片化（W38 趋势 #2）的直接应验；体量最大但需跟踪其实际优化效果是否配得上 265k star |
| **agent-skills** (addyosmani) | 生产级工程技能集（KOL/社区侧） | **98,515** | 24 个覆盖"规格→上线"全生命周期技能，带 slash 命令；JS，MIT，fork 10.4k；9/23 push | Addy Osmani（Google）个人背书，与厂商技能同周共振被多站并提 | 个人项目，技能质量依赖作者维护节奏；与厂商技能包存在定位重叠 |
| **Pi** (earendil-works/pi) | 统一 Agent 工具包（LLM API + Agent 循环 + TUI + CLI） | **108,636** | TS，MIT，fork 13.8k；8 月月增 20,142（月度榜第 2），本周仍 +2,497；9/22 push | 持续增长曲线被 TrendShift 月度榜收录 | 在 Claude Code / Codex 两分格局下走"不锁定单一厂商"路线，商业化路径不清晰 |
| **financial-services** (anthropics) | Anthropic 官方金融场景技能库 | **36,518** | Claude Code 垂直行业技能包；Python，Apache-2.0，fork 5.3k；9/21 push（本周活跃） | 官方发布即 Trending；厂商技能标准化信号的核心证据 | 行业深度有限（金融单场景），是"厂商 know-how 编码化"的首批样本而非终态 |
| **security-audit-skill** (cloudflare) | 编码 Agent 多阶段安全审计技能 | **20,339** | 审计发现独立可验证、机器可读（structured findings），直接挂载 Claude Code / Codex；JS，MIT；9/14 push | 官方发布即 Trending（本周约 +2,375）；aitoolly 等站专题报道 | 叠加 W38 CVE-2026-82533 背景，安全审计 Skill 有真实需求锚点；多阶段流程实际检出率待评测 |

### Agent 输出与交互层（2）

| 项目 | 定位 | 实时 Star | 技术测评要点 | 媒体 Coverage | 风险/备注 |
|------|------|-----------|--------------|---------------|-----------|
| **cua** (trycua) | Computer-Use 2.0（跨 OS 设备群 + 训练/评估基准） | **26,023** | 开源 drivers + 跨 OS fleets + 数据生成基准三件套；MIT，fork 1.8k；9/23 push，维护活跃 | 本周 Trending 持续在榜（9/20 单日 +1,012） | open issue 1,044 偏高，设备群管理的稳定性待验证 |
| **json-render** (vercel-labs) | 生成式 UI 框架（JSON → 可渲染界面） | **18,119** | Agent 输出结构化 JSON 直接渲染为 UI；TS，Apache-2.0；9/23 push，Vercel Labs 官方背书 | 本周 Trending 在榜，与 cua / agent-native 同周被并提为"Agent 输出离开聊天框"三箭 | 与 MCP/AG-UI 等 UI 协议的关系待厘清；早期 API 变动风险 |

---

## 二、淘汰清单（3 个）及理由

| 项目 | 淘汰理由 |
|------|----------|
| BuilderIO/agent-native | 6,334★，与 json-render 同属"agent-native UI"赛道（趋势 #3），两者取一保留 Vercel Labs 背书、Apache-2.0 授权的 json-render；agent-native 的配套 skills 包周下载约 12.7k，生态验证尚弱。GitHub API license 字段为空（README 自述 MIT），元数据欠账。移入观察池 |
| coder/coder | 16,617★，2021 年创建的老项目，本周凭官方描述改为"developers and their agents"重回 Trending——属营销语言级更新，非产品级新事件；AGPL-3.0 对商用有传染性约束。移入观察池 |
| higgsfield-ai/higgsfield | 5,637★，Breakout 属实（gitnova 评分 6.9，9/20–9/23 持续在榜，单日峰值 +465），但 repo 创建于 2018、最近 release 停在 2024-03（v0.0.4-rc），代码主体为 Jupyter Notebook，工程化程度与其"万亿参数训练编排"的定位不匹配；且模型层故事与本周 Skills 主线偏离。移入观察池 |

### 延续观察项（延续 W38 规则，不计入榜单）

| 项目 | 处理 |
|------|------|
| Kimi K3（Moonshot） | 权重类项目，非代码仓库生态，本周社区微调/量化分支持续活跃，继续观察 |
| Apertus 1.5（ETH/EPFL） | 同上，100% 开源标杆案例，学术界引用持续发酵，继续观察 |

---

## 三、本周核心判断

1. **Skill 是 Agent 时代的新交付单元，且已分两层**：厂商层（Cloudflare 安全审计、Anthropic 金融）负责把领域 know-how 编码成标准技能分发；社区层（Addy Osmani 24 技能、ECC 技能体系）负责长尾工程实践。个人 KOL 与一线厂商在同一抽象层收敛，这是社区-厂商共识形成的标志，而非又一场标准之战的苗头——两边都在吃 Agent Skills 标准（SKILL.md）的红利。
2. **Harness 碎片化正式催生横向中间层**：ECC 以 265k star 验证 W38 的趋势判断 #2——当 Harness 超过三个，"跨 Harness 的兼容与优化层"成为刚需。这与浏览器大战催生 jQuery 是同一规律，值得跟踪其是否会出现"中间层反噬 Harness"的谈判筹码问题。
3. **Agent 的输出正在离开聊天框**：json-render（生成界面）、cua（操作设备群）同时入榜，加上被淘汰但值得观察的 agent-native 和 coder——前端基建团队已把"Agent-native 交互"当作明确赛道，下周关注 AG-UI / MCP-UI 等协议层的动作。
4. **模型层的安静是注意力转移，不是停滞**：higgsfield 这类 2018 年的老训练框架能 Breakout，说明社区注意力在"发布频率放缓"后转向"如何自己训练/编排"。但该 repo 工程化欠账明显（release 停在 2024），本周不入榜，观察其能否借这波热度补齐工程短板。

---

*筛选：Kimi Claw · 2026-09-23 14:00 CST*
*下一步：thursday-paper-filter（周四论文精选）→ 周五周报引用本短名单*
*【人工介入点】请确认以上短名单后，回复"继续"以执行下一步。*
