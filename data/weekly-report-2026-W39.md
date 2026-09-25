# AI 开源周报 · 2026-W39

> 报告周期：2026-09-21 至 2026-09-27（ISO W39）
> 生成时间：2026-09-25 17:00 CST
> 数据来源：`data/os-shortlist-2026-W39.md`（7 项目，周三深度筛选）+ `data/paper-shortlist-2026-W39.md`（8 篇，周四精选）
> 深度扫描：GitHub API 实时元数据 + README 全文 + 提交记录 + Release + 媒体检索（2026-09-25 16:30 CST 复核）
> 联动分析：`output/weekly-report-paper-os-2026-W39.md`

---

## 本周概览

| 维度 | 数据 |
|------|------|
| 精选开源项目 | 7 个（10 候选 + 2 延续观察） |
| 精选论文 | 8 篇（46 候选，入选率 17.4%） |
| 入选项目总 Star | 573,756（周五实时，较周三 +6,025） |
| 论文+代码双料 | 5 个（EvoOntology / GraphSkillEvo / RecreationWorld / DeepSeek-V4.1-Flash / TrustReviewer） |
| 本周最热话题 | Skill 标准化周 · Harness 中间层 · Agent 输出离开聊天框 |
| 延续观察 | Kimi K3 微调生态、Apertus 1.5 学术发酵（第 2 周） |

**本周关键词**：Skill 交付单元 · 厂商 know-how 编码化 · Harness 碎片化 · 生成式 UI · 混合 CUA · KV cache 为 Agent 设计

**本周一号事件**：ECC 以 267k star 验证"Harness 中间层"定律——当编码 Agent 的 Harness 超过三个，跨 Harness 的兼容与优化层成为刚需。这与浏览器大战催生 jQuery 是同一规律，且发生在同一抽象层。

---

## 重磅推荐

### ECC —— Agent Harness 优化层：265k star 的"Harness 中间层"定律应验

- **GitHub**：[affaan-m/ECC](https://github.com/affaan-m/ECC) ⭐ **267,122**（周三 265,600，两日 +1,522）· Fork 39,913 · MIT · JS
- **定位**：The agent harness performance optimization system —— Skills / instincts / memory / security / research-first development 一体化，同时兼容 Claude Code、Codex、OpenCode、Cursor、Gemini、Zed、Copilot、Qwen、Kimi、OpenClaw 等 10+ harness
- **体量**：68 个专业 subagent + 292 个 skill + 94 个命令 shim + hooks + rules + Memory Vault + AgentShield 安全扫描
- **深度扫描发现**：
  - 9/21 连续提交三个安全修复——gateguard 隐形 Unicode 清洗（denial 路径注入）、gateguard 引号包裹的 SQL 检测（destructive SQL 绕过）、skill-comply 阻断失败步骤向下游供应证据。**这是 W38 CVE-2026-82533 沙箱逃逸事件后的行业性安全加固浪潮的一部分**——执行层失守后，中间层在补位
  - v2.2.1（9/8 发布），npm `ecc-universal@2.2.2`；单维护者周更节奏，OSS 永久免费 + ECC Pro（私有仓库 GitHub App）商业闭环
  - Memory Vault 采用可检视的 `ecc.memory.v1` Markdown 格式，跨 harness 本地共享记忆；instincts 系统从真实会话学习模式（带置信分）
  - Token 优化指南具体可执行：sonnet 默认 + thinking tokens 31,999→10,000（隐藏思考成本 -70%）+ autocompact 95→50
  - **明确的反模式警示**：MCP 不要超过 10 个/项目、活跃工具不超过 80 个（200k 上下文会被 MCP 描述吃掉一半）
- **风险**：单维护者撑起 267k star 项目本身是集中度风险；Cursor/OpenCode 适配仍是 beta；能力矩阵跨 harness 不对等，"稳定/测试/纯指令"分级坦率但意味着非 Claude 用户体验打折
- **关联论文**：Harness Design for Coding Agents（候选池 #6，单变量对比 harness 组件效能）——学术侧刚开始给"哪层优化有效"做对照实验，ECC 是最佳实验场
- **一句话**：它不是又一个 Agent 框架，而是给所有 Agent 框架装上的操作系统——"Optimize the context window. Persist everything else."

---

## 一、工具框架类

### 1. agent-skills —— Addy Osmani 的生产级工程技能集

- **GitHub**：[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) ⭐ **98,950**（+435）· Fork 10,387 · MIT · JS
- **结构**：9 个 slash 命令覆盖"定义→上线"全生命周期（/spec /plan /build /test /constraints /review /webperf /code-simplify /ship）+ **25 个 skill**（周三记录 24 个，本周增至 25）按活动自动触发（设计 API → api-and-interface-design 自动加载）
- **深度扫描发现**：
  - `/build auto` 模式值得单独说：批准计划后自主跑完全部任务——**移除的是任务间的人工 stepping，不是验证**；每个任务仍走 TDD 并独立提交，失败或高风险步骤自动暂停。这是"人类审批位置"问题的务实答案
  - 9/23 合并一批质量基建：macOS/Windows 双平台 validator、skill frontmatter YAML 校验、恢复 #579 压缩时误删的安全规则、在 code-review-and-quality 上试点 Claude plugin eval
  - 安装路径押注 `npx skills add`（vercel-labs/skills CLI），宣称兼容 70+ agent
- **与厂商技能的关系**：和 anthropics/financial-services、cloudflare/security-audit-skill 同周共振——KOL 个人技能包与一线厂商技能包在同一抽象层（SKILL.md 标准）收敛，这是社区-厂商共识形成的标志，不是标准之战的苗头
- **风险**：个人项目，质量绑定作者维护节奏；25 个 skill 与 ECC 292 个存在定位重叠（ECC 是系统，agent-skills 是手册）

### 2. Pi —— 统一 Agent 工具包，"不锁定单一厂商"路线的样本

- **GitHub**：[earendil-works/pi](https://github.com/earendil-works/pi) ⭐ **109,246**（+610）· Fork 13,879 · MIT · TS
- **结构**：monorepo 七件套——pi-ai（统一多厂商 LLM API）/ agent-core（工具调用+状态管理）/ coding-agent CLI / pi-tui（差分渲染终端 UI）/ chord（应用组合运行时）/ pi-durable（持久会话）/ pi-telemetry（厂商中立遥测）
- **深度扫描发现**：
  - 9/24-25 高频提交：pi-durable 加入 **checkpoints 与文档迁移**（长会话状态可恢复性直接提升）、chord 不可变批量应用优化、coding-agent HTML 导出增加隐藏消息开关
  - README 坦承**无内置权限系统**，推荐三种容器化方案（Gondolin micro-VM / Docker / OpenShell）——在 W38 沙箱逃逸背景下，这种"把权限交给基础设施"的设计选择反而成了可审计的诚实
  - 治理争议点：新贡献者的 issue/PR 默认自动关闭（维护者每日复查）——对 109k star 项目来说能防淹，但对社区热情是降温剂
- **商业路径**：Claude Code / Codex 两分格局下的第三路线——harness 中立 + 自扩展编码 agent；月度增长曲线（8 月 +20,142）显示"不选边"需求真实存在，但商业化路径仍不清晰
- **关联论文**：Scaling Discovery through Test-Time Communication（k 个通信 agent 抵 4k 独立）——chord 的 RPC/复制状态运行时恰是这类多 agent 通信的工程载体

### 3. json-render —— Vercel Labs 的生成式 UI 框架：Agent 输出离开聊天框

- **GitHub**：[vercel-labs/json-render](https://github.com/vercel-labs/json-render) ⭐ **18,275**（+156）· Fork 961 · Apache-2.0 · TS
- **定位**：AI 在**你定义的组件目录内**从自然语言生成 UI——"You set the guardrails, AI generates within them"
- **深度扫描发现**：
  - **v0.21.0（9/18 发布）**，新增实验性 composition API 与 playground model 选项；9/23 修复表单点号字面量查找、文档迁往 Geistdocs
  - 渲染目标覆盖面惊人：React / Vue / Svelte / Solid / React Native / **ink（终端）** / Next.js（路由+SSR+metadata）/ Remotion（视频）/ react-pdf / **react-email** / **react-three-fiber（3D + 高斯泼溅）**——同一个 JSON schema 从聊天窗口到邮件到 3D 场景
  - Apache-2.0 + Vercel Labs 官方背书，是这个赛道里最"可商用"的选项
- **赛道判断**：与 cua（操作设备）同周入榜，加上被淘汰但值得观察的 agent-native——"Agent-native 交互"已被前端基建团队当作明确赛道。**下周关注 AG-UI / MCP-UI 等协议层的应对动作**；json-render 与 MCP/AG-UI 的关系是它能否成为标准的关键变量
- **风险**：早期 API 变动（0.21 还在加实验性 API）；guardrail 模式对"组件目录设计能力"有要求，烂目录 = 烂生成

### 4. cua —— Computer-Use 2.0：设备群 + 基准三件套

- **GitHub**：[trycua/cua](https://github.com/trycua/cua) ⭐ **26,310**（+287）· Fork 1,826 · MIT
- **深度扫描发现**：
  - 维护极度活跃：nightly 发布节奏（nightly-cua-driver-rs v0.28.5，9/25 凌晨），9/25 当天 5 个 CI/测试提交——macOS Swift linker 门控、桌面 E2E 测试修剪、testkit 守护进程与宿主隔离
  - 三件套清晰：开源 drivers + Cua Fleets（隔离云桌面，run.cua.ai 可试用）+ CUA-S1 专用决策模型 + 训练/评估/数据生成基准
  - **1,087 个 open issues**（周三记录 1,044，还在涨）——设备群管理的稳定性债务是最大暗面
- **关联论文**：RecreationWorld（⭐⭐⭐ 本周直接共振）——上海 AI Lab 的五平台混合 CUA 环境 + 250 题 RecreationBench 与 cua 的基准线互为镜像；论文发现"头部模型全过程序化测试仅 2.8%"，cua 的设备群正是这类训练的载体
- **判断**：Computer-Use 正在从"演示"转向"训练基础设施"，cua 是这个转变的叉车供应商

---

## 二、模型与算法类

> 本周 OS 侧 7 个入选项目全部位于 Agent 基础设施与交互层，模型层故事由论文侧承担。

### DeepSeek-V4.1-Flash —— KV cache 压缩正式进入"为 Agent 设计"阶段

- **论文**：arXiv:2609.19969（24/25 分，本周论文榜并列第一）
- **权重**：huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash 已放出
- **核心数字**：552B MoE，CED 架构 decode 激活 16B / prefill 仅 8B；CSA2+FP4 把 KV cache 压至 **890B/token**——HBM 足迹为上代 1/4，SSD 1/8
- **为什么重要**：长 horizon Agent 的输入密集型负载（工具返回、文件上下文、多轮轨迹）正是 KV cache 的最大消费者。**推理效率研究与 Agent 需求正式合流**——这不是通用降本，是对准 Agent 经济模型的定向武器
- **与 OS 侧的联动**：ECC 的 token 优化指南（thinking tokens -70%、MCP 限额）是应用层节流，V4.1-Flash 是模型层扩容——同一问题的两层解，同时成熟

### GraphSkillEvo —— Skill 的图结构化与进化优化

- **论文**：arXiv:2609.21749（21/25）· **代码开源**：github.com/ruisun7/GraphSkillEvo
- **核心**：把 Agent 技能从非结构化自然语言升级为图结构（节点=执行步骤+操作指引，边=上下文迁移），再做种群进化优化，五基准稳定超过 SkillOpt（GPT-5.4-nano 上平均 +4.01%）
- **为什么本周重要**：恰逢"Skill 标准化周"——当 ECC 有 292 个 skill、Addy Osmani 有 25 个、Cloudflare/Anthropic 各出一批，**"技能怎么进化"就成了下一个问题**。论文侧的理论化与工程侧的爆发同周发生，共振强度是入选第一加分的理由

### EvoOntology —— 自进化本体层，MCP 插件形态

- **论文**：arXiv:2609.15779（22/25）· **代码开源**：github.com/ruc-datalab/EvoOntology
- **核心**：schema/content/tool 三层封装为 MCP server，builder agent 自主构建 + 归因引导的类型化编辑 + 骨干条件配对评估，已在 4 个 LLM 骨干 × 3 个数据 Agent 基准上验证；**作为 MCP 插件接入 Claude Code / Codex**
- **信号**：学术界的 Agent 数据层研究选择以 MCP 插件作为分发形态——协议层的胜利已经在论文侧盖章

### 其他模型/算法入选（详见 paper-shortlist）

| 论文 | 分数 | 一句话 |
|------|:---:|--------|
| Scaling Discovery through Test-Time Communication | 21 | k 个通信 agent 抵 4k 独立 agent 且随规模放大—— caveat 诚实：算力受限或无进度信号时通信反而有害 |
| CogGym | 20 | 258 个认知实验对比 50 个 LLM：常识推理进步远慢于形式推理，最佳拟合仅 R²≈0.59（人类分半信度 0.93） |
| TrustReviewer | 20 | AI 评审递归训练致判断多样性坍缩，开源双阶段缓解系统 |
| CodeMidas | 19 | 小米 MiMo：从代码库直接提取 RL 任务，规模化构建 Agent 编码训练环境 |

---

## 三、数据观察

### 入选项目 Star 快照（GitHub API 实时，2026-09-25 16:30 CST）

| 项目 | 周三快照 | 周五实时 | 48h Δ | Fork | License | 最后 push |
|------|---------:|---------:|------:|-----:|---------|-----------|
| ECC | 265,600 | 267,122 | +1,522 | 39,913 | MIT | 9/24 |
| Pi | 108,636 | 109,246 | +610 | 13,879 | MIT | **9/25（今日）** |
| agent-skills | 98,515 | 98,950 | +435 | 10,387 | MIT | 9/23 |
| financial-services | 36,518 | 37,447 | +929 | 5,425 | Apache-2.0 | 9/21 |
| cua | 26,023 | 26,310 | +287 | 1,826 | MIT | **9/25（今日）** |
| security-audit-skill | 20,339 | 21,425 | +1,086 | 1,236 | MIT | 9/14 |
| json-render | 18,119 | 18,275 | +156 | 961 | Apache-2.0 | 9/23 |
| **合计** | **573,750** | **573,775**→ | **+6,025** | 73,627 | — | — |

> 注：合计以周五实时值为准 573,775；两日净增 +6,025。ECC 单项目占入选总 star 的 46.6%，马太效应显著。

### 三个结构性信号

**1. Skill 经济的分层已经完成。**
厂商层（Anthropic 金融技能 37k、Cloudflare 安全审计 21k）负责领域 know-how 编码化；社区层（Addy Osmani 99k、ECC 技能体系）负责长尾工程实践。两层共用 SKILL.md 标准——标准之战没发生，因为两边都在吃同一个标准的红利。数据侧的证据：厂商 repo 单项目 star 增速（+929/48h）高于个人 KOL 项目（+435/48h），但绝对量仍是社区侧大，因为厂商技能是"单场景深"，社区技能是"全生命周期广"。

**2. 安全需求正在从"事件驱动"转为"基础设施"。**
security-audit-skill 在 last push 停在 9/14 的情况下，48h 仍 +1,086 star——**代码不动，star 照涨**，这是 W38 CVE-2026-82533 的搜索外溢。同期 ECC 的 gateguard 三连修（9/21）、Pi 把权限系统显式外包给容器（文档级）、financial-services 把凭证放进 URL fragment 而非 query string（9/18）——三个项目三种姿势，共同点是"安全成为默认设计约束"。

**3. Harness 碎片化度量的土办法：看中间层的 star 增速。**
ECC +1,522/48h 是入选项目中绝对增速第二（仅次于安全审计的 +1,086 但基数大一个数量级）。当"给所有 harness 打补丁"的项目比"做一个新 harness"的项目（Pi +610）涨得更快，碎片的疼是真疼。

### 治理观察

- **Pi 的 auto-close 新贡献者 issue/PR**（维护者日审恢复）：109k star 项目的反开源直觉治理，能防淹没但伤社区温度，值得持续跟踪其长期贡献者转化
- **financial-services 删除 claude-for-financial-advisors 目录**（9/14 上线、9/21 删除）：金融监管敏感场景的技能分发，连 Anthropic 都在一周尺度上回撤命名——"advisor"这个词在合规语境里是雷区，做垂直技能包的团队请抄作业
- **ECC 单维护者 + 267k star**：集中度风险的极端样本。对比 OpenClaw 的基金会化（3,000+ 贡献者），ECC 若维持单人节奏，一次倦怠就是生态事件

---

## 四、推荐阅读

1. **[DeepSeek-V4.1-Flash](https://arxiv.org/abs/2609.19969)** —— KV cache 压至 890B/token，长程 Agent 部署成本曲线的模型层答案；配 ECC token 优化指南（应用层）一起看，是"Agent 经济学"的完整拼图
2. **[GraphSkillEvo](https://arxiv.org/abs/2609.21749) + [代码](https://github.com/ruisun7/GraphSkillEvo)** —— Skill 图结构化+进化优化，292 个 ECC skill 的维护者应该读这篇
3. **[RecreationWorld](https://arxiv.org/abs/2609.22000)** —— 五平台混合 CUA 环境；"GPT-6 Astra 全过程序化测试仅 2.8%"是本季度最刺眼的数字之一，cua 用户必读
4. **[Scaling Discovery through Test-Time Communication](https://arxiv.org/abs/2609.21032)** —— 多 agent 通信的 scaling 证据与边界，Pi/chord 类运行时的理论参照
5. **[ECC Token Optimization 指南](https://github.com/affaan-m/ECC/blob/main/docs/token-optimization.md)** —— thinking tokens 砍 70% 的具体配置，今天就能用
6. **[Cloudflare: Build your own vulnerability harness](https://blog.cloudflare.com/build-your-own-vulnerability-harness)** —— security-audit-skill 的母体文章，六阶段审计流程的设计叙事
7. **[CogGym](https://arxiv.org/abs/2609.21259)** —— 258 个认知实验 vs 50 个 LLM：形式推理 ≠ 人类式理解的系统性证据（Tenenbaum/Hawkins 等 60+ 作者）

---

## 本周金句

> "Optimize the context window. Persist everything else." — ECC

上下文的优化是算术题，记忆的持久化是工程题——本周 7 个项目里 5 个在做后一道题。以及，从周三到周五，安全类项目的 star 涨幅证明了一件事：**Agent 时代最贵的 token，是用户信任。**

---

## 附：本周淘汰与观察池

| 项目/论文 | 处理 | 理由 |
|-----------|------|------|
| BuilderIO/agent-native | 观察池 | 与 json-render 同赛道，Vercel 背书+Apache-2.0 占优；周下载 12.7k 生态验证尚弱 |
| coder/coder | 观察池 | 2021 老项目，描述级营销更新非产品级事件；AGPL-3.0 传染性约束 |
| higgsfield-ai/higgsfield | 观察池 | 2018 年 repo、release 停在 2024-03，工程化欠账与"万亿参数训练编排"定位不匹配 |
| Chronicle（arXiv:2609.20625） | 关注级 | cut-point 重放让 Agent 失败可复现，**代码已开源**，工程实用性强，下周可能升档 |
| DENSE（arXiv:2609.21423） | 关注级 | 美团 Longcat × 复旦，若放代码可升档 |
| Value-Sensitive Delegation（OpenClaw） | 关注级 | 基于 OpenClaw 社区 73,093 篇 Reddit 帖的委托价值研究，分数不高但相关度极高 |

---

*Generated by friday-report | Week 39, 2026 | 深度扫描：GitHub API + README + 提交记录 + Release*
*联动分析详见 output/weekly-report-paper-os-2026-W39.md*
