# AI 开源周报（2026 年第 W47 周）

> 生成时间：2026-11-20（周五）
> 覆盖周期：2026-11-16 ~ 2026-11-20
> 数据来源：周三开源短名单（7 项目）+ 周四论文短名单（8 篇）
> 本周主题：**K3.1 Pro 社区量化冲刺** · **Agent 中间层协议化** · **AI 审查可信度反思**

---

## 本周概览

| # | 项目 | 分类 | 一句话 | 本周最大变化 |
|---|------|------|--------|-------------|
| 1 | Kimi K3.1 Pro 社区量化生态 | 模型 | Unsloth GGUF 落地（1,509 GB Q4_XL），llama.cpp PR 待合并 | W45"权重落地"→ W46"现实检验"→ W47"社区接力"，三连冠叙事完成闭环 |
| 2 | alibaba/open-code-review | 工具 | 确定性规则引擎 + LLM Agent 混合代码审查 | ~33,000+ ⭐，+951/天，Trending 周榜第一，单周 +14,000 |
| 3 | ChromeDevTools/chrome-devtools-mcp | 工具 | Chrome 团队官方 MCP Server，Agent 全能力操控浏览器 | ~57,000 ⭐，+841/天，官方背书确立浏览器操控标准 |
| 4 | ag-ui-protocol/ag-ui | 协议 | Agent-User 交互协议（MCP 管工具，AG-UI 管人机） | ~16,500 ⭐，+791/天，四大云厂商集成，月 npm 下载破千万 |
| 5 | dream-num/univer | SDK | AI Office SDK，人和 Agent 共用同一编辑引擎 | ~22,200 ⭐，周增 +6,091，v1.0.3 稳定版后持续放量 |
| 6 | google-labs-code/stitch-skills | 技能 | Google 官方 Agent Skills 库（设计→代码双向回路） | ~6,400 ⭐，Apache-2.0，Skills 标准化竞赛的 Google 棋子 |
| 7 | backnotprop/plannotator | 工具 | Agent 编排工作台：批注计划、审查代码、一键回授 Agent | ~1,300+ ⭐，+696/天，多 Agent 时代"人保持在 loop"的桌面 |

**本周趋势一句话**：上周 Agent 基础设施在"感官-四肢-记忆"四个切面推进，本周叙事切换到**中间层的协议化与工具化**——7 个入选项目中 5 个在造"管道和扳手"（交互协议、调试协议、技能标准、编排工作台、文档引擎），而非 Agent 本身；同时 K3.1 Pro 的社区量化生态终于产出第一个可用的 GGUF（虽然要 1.5TB），"开放权重"从口号推进到工程交付；而阿里的 open-code-review 以"确定性工程 + LLM Agent"混合架构登顶 Trending，恰好撞上一篇揭示 AI 审稿系统性偏置的论文（AI Reviews Are Biased Towards the Appendix），给火热的 AI 审查赛道浇了一盆方法论冷水。

---

## 论文-开源映射表（A-D 分类）

> 详细联动分析见 output/weekly-report-paper-os-2026-W47.md（含六大主题 + 联动矩阵 + 趋势判断）
> 本周结构：**A类 5 · B类 0 · C类 3 · D类 7**

**A类：论文 + 官方代码（5 篇）— 可立即复现**

| 论文 | 分数 | 官方代码 | 联动开源项目 | 联动方式 |
|------|------|---------|-------------|---------|
| WeightBench 🏆 | 23 | ✅ github.com/Aayush-Marasini/WeightBench | K3.1 Pro 量化生态 | LLM 直接写权重（权重空间编程）↔ 社区量化压缩权重——同一枚硬币的两面 |
| WebArena-Pro 🏆 | 22 | ✅ webarena-pro.github.io | chrome-devtools-mcp | 编码 Agent 62.3% vs VLM 30.3% 证明"工具面+Agent循环"是决定性变量，chrome-devtools-mcp 正是标准化工具面 |
| MIGRO 🏆 | 22 | ✅ github.com/zOUMINGXI/MIGRO | plannotator | "记忆应比模型活得久" ↔ 多 Agent 工作台的状态持续管理——同一问题的两个侧面 |
| OpticalRAG 🏆 | 22 | ✅ github.com/brighterr/OpticalRAG | K3.1 Pro / univer | 像素空间压缩至 16 token ↔ 长上下文成本问题的另一条解路线 |
| AI Reviews Biased | 22 | ✅ github.com/cincynlp（提及） | open-code-review | AI 审稿 50%+ 弱点来自附录（人类仅 8.4%）——直接警示 AI 代码审查工具的设计 |

**C类：论文先行（3 篇）— 代码未随论文发布**

| 论文 | 分数 | 对应方向 | 跟进建议 |
|------|------|---------|---------|
| DISCERN | 22 | 企业级 Agent 跨会话记忆 | 核心洞察"企业记忆的关键不是检索而是消解"——关注 ENT-310 基准和代码释放 |
| Contagious Fingerprints | 21 | 模型指纹传染攻击 | API 中继欺诈检测新攻击面——降级检测率 0.97→0.72，Lineup 方法假阳性 0.056 |
| Outcome-Mass Alignment | 20 | 多轮 Agent RL 训练修正 | 轨迹膨胀导致结果统计重复计数，跨优化器（GRPO/GiGPO/GSPO）兼容，ALFWorld +7-9.4pp |

**D类：项目先行（7 个）— 暂无对应论文**：Kimi K3.1 Pro 量化生态、alibaba/open-code-review、chrome-devtools-mcp、ag-ui、dream-num/univer、google-labs-code/stitch-skills、backnotprop/plannotator

**B类（社区复现）连续第四周空缺**（W44-W47 均为 0）——放码策略"全放/不放"两极分化固化：5/8 官方放码（A类），3/8 完全不放（C类），中间地带持续缺席。

**本周观察**：论文代码开放率从 W46 的 3/8 回升至 5/8（62.5%），C 类占比降至 37.5%——NeurIPS 2026 截稿季后的代码释放窗口正在打开。最强联动：**AI Reviews Biased（学术揭示 AI 审查偏置）× open-code-review（工程交付 AI 审查工具）**——论文证明 LLM 审稿对附录的异常依赖（50%+ vs 人类 8.4%），而 open-code-review 的"确定性规则引擎"恰好是对"LLM 自由审查不可靠"的工程回应：把不能出错的环节（文件筛选、规则匹配、行号定位）从模型手中收回。学术诊断与工程处方在同一周交汇。

---

## 🔥 重磅推荐

### Kimi K3.1 Pro 社区量化生态 — 三连冠收官：从权重落地到 GGUF 交付

**来源**: [Hugging Face](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) · 量化发布 2026-11 中旬 · W45 权重落地 → W46 现实检验 → W47 社区接力
**License**: Kimi K3.1-Pro License（MIT 风格主体 + 两条附加条款）

W45 我们记录了权重落地的历史时刻，W46 记录了"跑不动"的现实检验，本周社区终于给出了第一份可用答卷。

**三个关键进展**：

1. **Unsloth 发布初步 GGUF**。UD-Q4_K_XL 1,509 GB / UD-Q8_K_XL 1,561.5 GB——是的，这仍然是一个"数据中心级"文件（对比：K3 的 UD-IQ1_S 为 594 GB，已需约 610GB 内存）。但这是 `kimi_k31` 架构的第一个社区量化交付，意味着"从 vLLM 专属到 llama.cpp 生态"的桥梁开始架设。
2. **llama.cpp `kimi_k31` 架构 PR 待合并**。GGUF 文件已就绪，只差上游合并。这是本周最关键的单一事件——合并后，K3.1 Pro 正式进入 llama.cpp 生态，社区量化（更多精度级别、更低比特）将加速涌现。
3. **多家社区量化版密集上架**。morphllm、bestfreewebresources、DataCamp、什么值得买等密集报道——中文和英文社区同时升温，量化军备竞赛正式开赛。

**冷静的现实**：即便 llama.cpp PR 合并，Q4_K_XL 1,509 GB 对桌面用户仍然遥不可及（参考 K3 经验，未来 2-3 个月可能出现 UD-IQ1_S 级别的激进量化至 ~600GB 量级）。W46 的成本数学结论不变：API 月调用量在数十亿 token 以下时，自托管没有经济性。但 GGUF 的出现改变了一件事——**选择权从"数据中心方案"扩展到了"llama.cpp 生态"**，这意味着更多推理引擎适配（Ollama、LM Studio、llama-server）、更多量化级别、以及社区驱动的迭代加速。

**技术上下文回顾**：2.8T 总参 / 104B 激活 MoE（896 experts，top-16）、原生 MXFP4 训练格式、1M token 上下文。Unsloth 的 Q4_K_XL 是在 MXFP4 基础上做的 GGUF 重打包——由于原生已是 4-bit 训练格式，进一步量化的信息损失空间比传统 FP16→Q4 路径更窄，这也是社区量化难度高的原因之一。

**为什么重要**：K3.1 Pro 的三周叙事（落地→检验→接力）是 2026 年"开放权重"故事最完整的一个切片：权重发布只是起点，架构适配、量化交付、生态跟进才是"开放"二字的真正含义。本周社区量化生态的冲刺证明：**当权重真的开放，社区有能力在两周内完成从"不可能"到"可用但昂贵"的跨越**。接下来的关键变量是 llama.cpp PR 的合并时间和更激进量化级别的出现速度。

**风险**：llama.cpp PR 合并时间未知；1,509 GB Q4_XL 的实际推理内存需求尚未验证；社区量化版的精度损失需要独立基准测试；激进量化（IQ1/IQ2 级别）在 MXFP4 原生权重上的信息损失可能大于传统路径。

---

## 工具框架类

### alibaba/open-code-review — 确定性工程 × LLM Agent 的混合审查管线

**仓库**: [alibaba/open-code-review](https://github.com/alibaba/open-code-review) · **License**: Apache-2.0 · **语言**: Go
**本周Stars**: ~33,000+ ⭐（+951/天，单周 +14,000）| **npm**: `@alibaba-group/open-code-review`（CLI: `ocr`）

阿里开源的 AI 代码审查 CLI，出身硬核：内部运行两年，服务数万开发者，识别数百万代码缺陷，执行超百万次审查任务。本周登顶 GitHub Trending 周榜第一（Claude Code 第二）。

**核心设计：把"不能出错"的环节从模型手中收回**：

- **确定性管线**：文件筛选、规则匹配、行号定位——用工程逻辑硬约束，消灭 LLM 的行号幻觉
- **LLM Agent**：只做动态判断和上下文检索——场景调优的 prompt + 蒸馏自百万次生产调用的工具集
- **内置多语言规则集**：NPE、线程安全、XSS、SQL 注入，覆盖 10 种语言
- **结果**：同等模型下精度更高、token 消耗约为通用 Agent 的 1/9

**审查流程三阶段**：变更 >50 行先做风险分析 → 主审查（每文件独立 goroutine，默认 8 并发，单文件 10 分钟超时）→ 上下文超限时自动三区压缩（冻结区/压缩区/活跃区）。

**集成面**：Claude Code、Codex、Cursor、Kimi Code、OpenCode 插件；GitHub Actions、GitLab CI、Gerrit 流水线；MCP Server 扩展；Session Viewer 浏览器回放。支持 Delegation Mode——编码代理用自身 LLM 执行审查，无需 OCR API key。

**基准**：AACR-Bench——50 仓库 × 200 PR × 10 语言，80+ 高级工程师交叉验证。官方数据：对比 Claude Code 等通用 Agent，Precision/F1 更高，token 消耗约 1/9。第三方实测（agentskillshub，gpt-6-astra）：8 个埋入缺陷找到 7 个，4 个干净 PR 误报 0 条，每 PR 耗时 7 分钟。

**为什么重要**：33K 星 + 单周 14K 增速是阿里 GitHub Org 下最热项目。它的方法论——**"确定性工程 + LLM Agent"混合架构**——是当前 AI 代码审查赛道上最务实的答案：纯 LLM 审查有幻觉和噪声问题（开发者因无用评论太多而忽视 AI 审查），纯规则审查覆盖面有限。OCR 用精度换召回（宁可少报，不可错报），直接回应了"AI 审查噪声"这个最大痛点。值得注意的是，本周论文 #6（AI Reviews Are Biased Towards the Appendix）从学术侧证明 LLM 审稿存在系统性偏置（50%+ 弱点来自附录 vs 人类 8.4%），恰好为 OCR 的"不信任纯 LLM 审查"设计哲学提供了独立证据。

**风险**：官方基准以 Claude Code 为对标对象，独立第三方验证仍有限（截至 11 月仅 1 家）；以精度换召回意味着漏报率可能高于竞品——对被审代码安全性要求极高的场景需补人工审查；自托管需要自行管理 LLM 配置和规则文件，对小团队有运维门槛。

### ChromeDevTools/chrome-devtools-mcp — 浏览器操控的官方标准答案

**仓库**: [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) · **License**: Apache-2.0
**本周Stars**: ~57,000 ⭐（+841/天）

Chrome DevTools 团队官方维护的 MCP Server，让 AI 编码助手（Claude、Cursor、Copilot、Gemini 等）直接操控完整 Chrome DevTools 能力：性能 trace 录制与分析、网络请求检查、Console 消息（含 source-mapped 堆栈）、内存堆快照、Lighthouse 审计、截图、Puppeteer 可靠自动化。

**连接方式**：Chrome 144+ 支持 `--autoConnect` 自动连接运行中的 Chrome 实例（需用户许可弹窗）；沙箱环境可用 `--browser-url` 手动指定远程调试端口。支持 headless 模式。

**工具面**：输入自动化（点击/拖拽/表单/键盘/文件上传 10 工具）、导航自动化（6 工具）、性能分析（trace 录制 + CrUX 真实用户数据）、网络分析（完整请求详情）、内存诊断（堆快照/比较/泄漏检测 11 工具）、控制台/Lighthouse/截图/录屏。

**集成面**：Claude Code、VS Code、JetBrains、Gemini CLI、Cursor、Windsurf、Antigravity。提供 MCP Server 和独立 CLI 双模式。experimentalPageIdRouting 支持多 Agent 并发独立页面。

**为什么重要**：57K 星、Chrome 团队官方背书、+841/天增速——这个项目的存在本身就定义了"Agent 操控浏览器"的上限和下限。与 W46 覆盖的 agent-browser（Vercel，a11y tree 路线）互补：agent-browser 给 Agent 极简的语义化视图，chrome-devtools-mcp 给 Agent 完整的调试/性能/网络专业能力。当本周论文 #2（WebArena-Pro）证明"编码 Agent + 工具循环"（62.3%）大幅超越"通用 VLM"（30.3%）时，chrome-devtools-mcp 恰好提供了最完整、最权威的工具面——**Agent 循环的质量上限取决于工具面的丰富度，而 Chrome 团队把天花板推到了 DevTools 级别**。

**风险**：默认收集使用统计（可 `--no-usage-statistics` 关闭）；性能工具可能向 Google CrUX API 发送 trace URL（可 `--no-performance-crux` 关闭）；暴露浏览器实例完整内容给 MCP 客户端有隐私安全考量；官方仅支持 Chrome/Chrome for Testing，其他 Chromium 浏览器可能有兼容问题。

---

## 协议与标准类

### ag-ui-protocol/ag-ui — Agent 与人之间缺失的那一层协议

**仓库**: [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) · **License**: MIT
**本周Stars**: ~16,500 ⭐（+791/天）| **npm**: `@ag-ui/core` 月下载量 ~10.3M（2026-10 数据）

AG-UI（Agent-User Interaction Protocol）由 CopilotKit 团队创建（2025 年 5 月开源），是一个开放的、事件驱动的、传输无关的协议层，标准化 Agent 后端与用户界面之间的通信。一句话定位：**MCP 连接 Agent 与工具，A2A 连接 Agent 与 Agent，AG-UI 连接 Agent 与人**。

**协议设计**：客户端发送 `RunAgentInput`（thread ID、消息历史、可用工具、当前状态），Agent 返回有序事件流——约 16 种标准事件类型（TEXT_MESSAGE_START/CONTENT/END、TOOL_CALL_START/ARGS/END/RESULT、RUN_STARTED/FINISHED 等）。传输层不绑定 SSE/WebSocket——HTTP+SSE 为主，HTTP+Protobuf 和自定义绑定同样受支持。

**核心设计原则**：严格写者、宽容读者（生产者必须格式正确，消费者必须忽略不认识的事件——前向兼容）；仅 run 生命周期为强制（最小实现只需 RUN_STARTED + RUN_FINISHED）；完整事件流可回放（调试、评测、跨 UI 重放）。

**生态采纳**：LangChain、CrewAI、Mastra、PydanticAI、Google ADK 第一方集成；Microsoft Agent Framework 集成（2026-10 更新）；AWS、Oracle 支持。CopilotKit 本体 37,900+ ⭐，2026 年 5 月完成 $27M A 轮融资（Glilot Capital、NFX、SignalFire）。

**为什么重要**：AG-UI 的采纳曲线是协议类项目中最陡的——从 2025 年 5 月的单个开源项目到 2026 年中四大云厂商全部集成。月 npm 下载量破千万说明它已经不是"又一个协议提案"，而是实际运行在生产环境中的基础设施。与本周其他项目的关系：stitch-skills 解决"Agent 能做什么"（技能标准），ag-ui 解决"Agent 怎么跟人交互"（通信标准），plannotator 解决"人怎么管理 Agent"（管理界面）——三个项目共同勾勒出 Agent 人机协作层的三段式分工。**当 OpenAI 宣布 2026 年 8 月关闭 Assistants API 时，社区向标准化协议的迁移进一步加速，AG-UI 是这个趋势的最大受益者之一**。

**风险**：协议仍在快速演进（Draft 1.1），事件类型和语义可能变化；与 Google A2UI（v0.9）的路线竞争仍在进行；CopilotKit 的商业层（托管 Intelligence 服务）与开源协议的边界可能随公司策略调整。

### google-labs-code/stitch-skills — Google 的 Agent Skills 标准化棋子

**仓库**: [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) · **License**: Apache-2.0
**本周Stars**: ~6,400 ⭐（峰值 +250/天）

Google Labs 出品的 Agent Skills 库，遵循 Agent Skills 开放标准（agentskills.io），通过 Stitch MCP Server 桥接 Google Stitch 设计平台，实现"设计 ↔ 代码"双向回路。兼容 Claude Code、Cursor、Gemini CLI、Codex、Antigravity、OpenCode 六大编码 Agent。

**架构**：四层栈——编码 Agent → Skills（过程性指令）→ Stitch MCP Server → Stitch 设计平台。所有设计操作经 MCP 调用，Skills 不直接访问 Stitch REST API。

**技能面**：15 个技能分三个插件——stitch-design（设计生成/DESIGN.md 管理）、stitch-build（React/React Native 组件构建）、stitch-utilities（prompt 增强/静态 HTML 提取）。核心技能：design-md（58K 安装）、enhance-prompt（53K）、stitch-loop（51K）、react-components（51K）、shadcn-ui（48K）、remotion（37K）。

**关键模式**：stitch-loop 技能实现了"接力棒"（baton）自驱动循环——每次迭代从 baton 文件读取任务、生成页面、写入下一任务，跨多次 Agent 运行持续建站，无需人工逐步提示。

**为什么重要**：在 W46 我们记录了 google/skills（24K ⭐）与 anthropics/skills（~190K ⭐）的平台对峙。stitch-skills 是 Google 在同一战线的另一个落子——区别在于 google/skills 是通用技能框架，stitch-skills 是具体垂直（设计→代码）的技能交付。它的意义有三层：其一，验证了 **Agent Skills 开放标准的跨厂商兼容性**——同一套技能在 Claude Code、Cursor、Codex 上无需分叉；其二，**MCP-as-bridge 架构是干净的设计范式**——Skills 保持薄层，设计平台保持唯一事实源；其三，stitch-loop 的接力棒模式展示了"跨运行持续任务"的技能级解法——这与本周论文 MIGRO 的"记忆应比模型活得久"在哲学上同构（状态跨会话持续）。

**风险**：明示 "not an officially supported Google product"，无 Google 官方支持承诺；Skills 质量依赖 Stitch 平台本身——如果 Stitch 平台策略调整，技能库价值可能受损；安装量数据（数万次）与星数（6.4K）的差距提示实际活跃使用规模有限。

---

## Agent 协作与生产力

### backnotprop/plannotator — 多 Agent 时代"人保持在 loop"的工作台

**仓库**: [backnotprop/plannotator](https://github.com/backnotprop/plannotator) · **License**: Apache-2.0 / MIT 双许可
**本周Stars**: ~1,300+ ⭐（+696/天）

Plannotator 是一个本地浏览器端的 AI 编码 Agent 审查工作台：不做 Agent，做**管理和引导 Agent 的界面**。当 Agent 提出计划、生成 HTML、或完成编码时，工作在浏览器中打开，人进行批注、评论、发送反馈，Agent 直接接收并执行。

**核心能力**：
- **计划批注**：Agent 创建计划时自动打开 markdown 审查面，批注和评论直接回授 Agent
- **代码审查**：本地变更或远程 PR（GitHub/GitLab），批注 diff、建议代码，评论回授 Agent。支持 Git、GitButler、Jujutsu、Perforce
- **引导式审查**（Guided Review）：按 `Cmd+Shift+G`，Agent 将 diff 按章节排序——核心变更在前、影响次之、胶水代码最后——每章配概述
- **HTML 批注**：渲染的 HTML 文件或本地运行中的站点（`plannotator annotate http://localhost:5173`），通过本地代理批注真实页面，热重载保持工作
- **Inbox**：一个本地窗口聚合所有 Agent 的消息、问题、文件和审查请求
- **分享**：计划生成链接，队友批注后可导入反馈回授 Agent。小内容直接压缩进 URL fragment，大内容 AES-256-GCM 加密后上传（7 天过期）

**集成面**：Claude Code、Codex、Copilot CLI、Gemini CLI、OpenCode、Kiro、Droid、Amp、Pi、T3 Code。VS Code 扩展、Obsidian 自动保存、Bear/Notion 同步。

**安全**：每个发布二进制附 SHA256 sidecar，v0.17.2 起提供 SLSA provenance 认证，CycloneDX SBOM + Grype 漏洞扫描。

**为什么重要**：1,300 星看着不大，但 +696/天的增速和精准的定位使它值得关注。当 Agent 从单兵作战进化为多 Agent 并行（W46 的 worktrunk 解决代码并行，plannotator 解决人机协作），**"人如何在多个 Agent 之间保持知情和控制"成为新的 UX 难题**。Plannotator 的答案不是再做一个 Agent 仪表盘，而是一个**审查面**——人做的事情不变（审阅、批注、决定），变的是反馈直接回流到 Agent 而非通过聊天窗口转述。本周论文 MIGRO（记忆跨模型存活）和 DISCERN（企业级跨会话记忆）从学术侧论证了 Agent 状态的长期持续性，plannotator 从工程侧补上了人在这种状态持续中保持权威性的界面。

**风险**：1,300 星的项目处于极早期，API 和配置格式可能频繁变化；依赖 cookies 存储设置（因每次 hook 调用端口随机）的设计在隐私敏感场景需要额外审查；链接分享的加密模型虽对标 PrivateBin，但自托管 paste 服务的实际安全性需要社区审计。

### dream-num/univer — AI Office SDK：人和 Agent 共用同一引擎

**仓库**: [dream-num/univer](https://github.com/dream-num/univer) · **License**: Apache-2.0（开源内核）+ 商业扩展（Univer Pro）
**本周Stars**: ~22,200 ⭐（周增 +6,091）| **版本**: v1.0.3（2026-09-29 首个稳定版）

Univer 是 Luckysheet 的正统继任者（Luckysheet 16.6K ⭐ 已归档），一个 TypeScript 编写的 AI Office SDK。提供六种可组合内容类型：电子表格（公式/图表/透视表）、文档（富文本/页面布局）、演示文稿、关系型数据表（类 Airtable）、自由画布（白板/思维导图）、PDF 查看与编辑。

**三层 SDK 架构**：
- **Web SDK**：浏览器内嵌入编辑器，插件/预设/Facade API 扩展
- **Server SDK**：Node.js 无头运行——同一引擎可在服务端执行，工作簿可在无人浏览器打开时由 AI Agent 生成/编辑
- **AI SDK**：给 Agent 提供检查、编辑、验证 Office 内容的工具

**Agent 集成**：Agent 与人使用同一套开源 API——应用方提供模型和工具编排。官方示例展示报价工作流的编辑、计算、保存，无需 AI SDK 依赖。

**技术核心**：Canvas 渲染引擎、公式引擎（同代码在浏览器和 Node.js 运行）、插件架构、命令系统（跨功能编辑 + 统一 undo/redo）、Facade API。

**商业模型**：开源核心（Sheets/Docs 编辑能力）Apache-2.0 + 商业扩展（协同、导入导出、图表、透视表、打印）+ Univer Pro 模块。明确的功能对比表区分开源和商业边界。

**为什么重要**：22K 星 + 周增 6K + 81 天内 +8,721 星的增速曲线说明 v1.0 稳定版发布后项目进入了放量期。在"AI Office"叙事中，Univer 的定位独特：**不是做一个 AI 办公软件，而是做办公软件的基础设施**——让任何 SaaS 产品都能嵌入 Office 编辑能力，让任何 Agent 都能读写 Office 文件。与本周论文 OpticalRAG（文档渲染为图像压缩至 16 token）的关系值得关注：OpticalRAG 走"文档→像素→token"路线绕过文本解析，Univer 走"文档→结构化对象→API"路线保留语义完整性——两种范式在"Agent 如何消费文档"这个问题上形成对照。

**风险**：版本号 0.25.x→1.0.3 的 API 稳定性仍在验证期（部分评测指出 API 可能变化）；开源版与商业版的功能差距（协同、导入导出为商业版）可能限制开源场景的采用；与 OnlyOffice、Collabora Online 等成熟方案的竞争需要长期差异化。

---

## 数据观察

### 本周增速榜：open-code-review 单周 +14,000 领跑

| 项目 | 周三星数（11-18） | 增速 | 备注 |
|------|------------------|------|------|
| open-code-review | ~33,000+ | **+951/天** | 单周 +14,000，Trending 周榜第一 |
| chrome-devtools-mcp | ~57,000 | **+841/天** | 官方背书 + 工具面完整 |
| ag-ui | ~16,500 | **+791/天** | 协议采纳加速期 |
| plannotator | ~1,300+ | **+696/天** | 小而快，早期爆发 |
| univer | ~22,200 | **+6,091/周** | v1.0 稳定版后持续放量 |
| stitch-skills | ~6,400 | 稳定增长 | Google Labs 长尾 |

增速前四名的共同特征：**都是 Agent 基础设施（管道/扳手），而非 Agent 本体**。这与本周主题"中间层协议化与工具化"完全一致——社区正在用 star 投票表达对"造 Agent"到"造 Agent 需要的工具"的叙事切换。

### K3.1 Pro 三周叙事弧完成闭环

| 周 | 叙事 | 关键事件 |
|---|------|---------|
| W45 | 权重落地 | 11/4 权重上架 HF，1.56TB，MXFP4 |
| W46 | 现实检验 | 无 GGUF、无 llama.cpp、门槛 610GB 起，"跑不动" |
| W47 | 社区接力 | Unsloth GGUF 落地（1,509 GB Q4_XL），llama.cpp PR 待合并 |

三周完成"落地→检验→接力"的完整叙事弧。W46 的冷静判断（"API 仍是唯一经济选择"）在 W47 依然成立，但 GGUF 的出现意味着**选择的边界在扩张**——llama.cpp 生态的加入将带来更多推理引擎适配、更多量化级别、以及更低的进入门槛。

### 论文代码开放率回升：5/8（62.5%）

W46 的 3/8 → W47 的 5/8。NeurIPS 2026 截稿季后的代码释放窗口正在打开。5 篇 A 类论文中 4 篇提供了可直接使用的开源代码（WeightBench / WebArena-Pro / MIGRO / OpticalRAG），其中 WeightBench 附带沙箱 harness 和实时排行榜，MIGRO 和 OpticalRAG 的代码完整度尤其高。C 类 3 篇（DISCERN / Contagious Fingerprints / Outcome-Mass Alignment）值得关注代码释放——尤其 DISCERN 的 ENT-310 基准。

### Agent 记忆研究爆发：单周 6+ 篇

周四筛选池 35 篇中 6+ 篇聚焦长期记忆（MIGRO / DISCERN / MemCredit / Folio / TreeAgent / AstroMemBench）。核心分歧点从"怎么检索"转向"**写入时保留什么、读取时消解什么**"。这一学术爆发与开源侧的对应关系：W46 的 claude-mem（116K ⭐）是工程侧记忆系统的事实标准，本周没有新的记忆类项目入选短名单，但 plannotator 的"状态持续管理"与 MIGRO 的"记忆跨模型存活"在方法论上遥相呼应。

---

## 推荐阅读

1. **[Open Code Review：阿里开源硬核代码审查工具（hiwepy wiki, 2026-06-01）](https://wiki.hiwepy.com/docs/ddd4j-guide/ddd4j-guide-1hd1p1f4qlqm4)** — OCR 三阶段审查流程和并发架构的最完整中文拆解，含记忆压缩三区划分细节
2. **[阿里巴巴 open-code-review 深度分析（braindetox, 2026-06-21）](https://braindetox.kr/zh/posts/alibaba_open_code_review_2026.html)** — 与 CodeRabbit/Graphite 的全维度对比，含数据流向分析和自托管 vs SaaS 的决策框架
3. **[Open Source AI Reviewer That Out-Engineered Claude Code（flowtivity, 2026-09-12）](https://flowtivity.ai/blog/alibaba-open-code-review/)** — 第三方基准实测：8 个埋入缺陷找到 7 个，干净 PR 误报 0 条
4. **[CopilotKit & AG-UI Protocol 完全指南（rpabots.world, 2026-11-11）](https://rpabotsworld.com/copilotkit-ag-ui-protocol-open-source-agent-frontend-stack-guide/)** — AG-UI 协议设计原则、事件族拆解、与 MCP/A2A 的栈位关系，前端开发者必读
5. **[Stitch Skills: Google Labs' Agent Skills Bridge（pyshine, 2026-07-11）](https://pyshine.com/Stitch-Skills-Google-Stitch-Agent-Skills-Design-to-Code/)** — 设计→代码双向回路的架构分析，含 Agent Skills 开放标准参考实现拆解
6. **[Chrome DevTools MCP：让 AI 编码助手直接操控浏览器（腾讯云开发者社区, 2026-07-08）](https://developer.cloud.tencent.com/news/4217504)** — 工具面全览（输入/导航/性能/网络/内存/控制台），含配置和集成路径

---

*由 friday-report 任务生成 | intelligence-system*
*数据源：data/os-shortlist-2026-W47.md + data/paper-shortlist-2026-W47.md*
*联动分析：output/weekly-report-paper-os-2026-W47.md*
