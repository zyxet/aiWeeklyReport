# 周一开源项目速览

**周期：** 2026-W43（10月13日–10月19日）
**生成日期：** 2026-10-19
**来源：** GitHub Trending / Hacker News / 社区博客 / TLDR

---

## 一、大模型层（模型权重 + 训练推理）

### 1. Meta Muse Wonder / Muse Wonder Full

- **地址：** 闭源 API（Meta Model API + Muse Code）
- **类型：** 模型发布（闭源，影响竞争格局）
- **热度：** 10月12日发布，全球技术媒体密集报道
- **亮点：** Meta 超级智能实验室重组 14 个月后首个前沿级模型。标准版 API 定价 $4/M 输入、$20/M 输出，1M context，多模态输入（文本/图片/视频/音频/PDF）。Artificial Analysis 智能指数：Wonder 52 分、Full 56 分，仅次于 Claude Opus 5.5 的 58 分。核心差异化能力是 **Active Memory**（跨会话保留任务相关信息，数天至数月）和 **Active Focus**（遇阻自动切换方案并从错误恢复）。
- **趋势信号：** "主动记忆" 成为模型竞争新维度——不再比谁 context window 大，而是比谁能在超长周期内保持任务连贯性。这对 agent 基础设施的设计有直接影响（记忆层可能要下沉到模型本身）。

### 2. Kimi-Linear-48B-A3B

- **类型：** 开源权重模型
- **协议：** MIT
- **亮点：** MoE 混合架构（3 层 KDA 线性注意力 + 1 层 MLA 全局注意力），48B 总参 / 3B 激活。1M context，5.7T 训练 token。关键意义：**证明了线性注意力可以在长上下文场景匹敌全注意力**，同时大幅降低推理成本。
- **趋势信号：** 线性注意力从 "学术玩具" 进入 "生产可用" 阶段。对自部署 agent 场景意义重大——3B 激活参数意味着消费级硬件也能跑 1M context。

### 3. Qwen3.6 GGUF 视频版

- **类型：** 模型量化更新
- **亮点：** 35B 总参 / 3B 活跃的 MoE 架构，GGUF 格式新增视频理解能力。进一步降低了多模态 agent 的本地部署门槛。
- **趋势信号：** 小激活参数 MoE + 多模态 + GGUF 正在 converging——单机可跑的 "全能 agent 底座" 不再是幻想。

---

## 二、Agent 基础设施层（框架 / 编排 / 运行时）

### 1. Leviathan ⭐ 673+（本周爆发）

- **地址：** github.com/elstongun/leviathan
- **语言：** Rust
- **协议：** Apache-2.0
- **类型：** Agent 深度记忆 / 数据索引
- **简介：** 单个静态二进制文件，将 JSONL/CSV/SQLite/数据库导出转为带排名的全文索引（SQLite FTS5 + BM25）。Agent 用自然语言查询，返回带引用的精简结果卡片——100 万条记录下每次回答仅 ~450 token，对比 grep 策略的 107K token，降低 **245 倍**。中位延迟 33ms。支持 MCP server、24 种 agent 框架的自动配置（`leviathan wrap`）、可选的 agent 读写记忆层。
- **为什么重要：** 解决了 agent 面对大数据集时的核心瓶颈——context window 不够。不是 RAG 那种 "先检索再塞 prompt"，而是把检索结果压缩到极小 token  footprint，让 agent 可以低成本查询海量记录。TLDR Data (10/12) 重点推荐。
- **本周动态：** 10月5日上架 GitHub，一周内登 Trending，TLDR 报道。

### 2. CLI-Anything ⭐ 44,255+（持续高增长）

- **地址：** github.com/HKUDS/CLI-Anything
- **语言：** Python
- **协议：** MIT
- **类型：** Agent-Native 计算机使用框架
- **简介：** 香港大学 HKUDS 团队出品。核心论点：GUI agent（截图+点击）从根本上不适配 agent 能力，应该把所有软件变成 CLI 接口。通过 7 阶段方法论，agent 可以分析任意软件的源码并自动生成完整的 Python CLI harness。配套 CLI-Hub 包管理器（`cli-hub list/search/install/launch`），已有 GIMP、Blender、LibreOffice 等现成 harness。
- **为什么重要：** 提出了 "Agent-Native Computer Use" 的完整范式——结构化命令、显式状态、确定性反馈，彻底绕开 GUI agent 的像素级脆弱性。已发布配套 arXiv 论文（2606.03854）。
- **本周动态：** 日增 star ~150，持续在 GitHub Python 热点榜。支持 Claude Code、OpenCode、Hermes、Cursor 四大 agent 平台。

### 3. Ruflo（原 Claude Flow）⭐ 74,513+

- **地址：** github.com/ruvnet/ruflo
- **语言：** TypeScript
- **协议：** MIT
- **类型：** Agent Meta-Harness
- **简介：** "Agent = Model + Harness" 的定义者。围绕 Claude Code / Codex 的执行层，提供 100+ 专业化 agent、swarm 编排、自适应记忆、跨机器联邦通信、企业安全护栏。35+ 插件、314+ MCP 工具。一个 `npx ruflo init` 就让 Claude Code 拥有 "神经系统"。
- **为什么重要：** 是目前最大的 agent harness 项目之一。它把 "agent 需要什么基础设施" 这个问题系统化——路由、记忆、学习循环、联邦、安全，每一层都有对应模块。Star 数已达 74K，周增数千。
- **⚠️ 注意：** 项目体量巨大（安装后生成大量文件和 hook），生产环境使用需谨慎审计。安全扫描发现过高危问题，建议 sandbox 先行。

### 4. ai-memory ⭐ 本周 Trending

- **地址：** github.com/akitaonrails/ai-memory
- **类型：** Agent 编码 CLI 长期记忆方案
- **简介：** 解决的核心问题：不同 agent vendor（Claude Code、Codex、Cursor）之间的记忆不互通。提供跨 vendor 的长期记忆存储和 handoff 方案。
- **为什么重要：** 随着开发者同时使用多个编码 agent，"记忆孤岛" 成为实际痛点。谁解决跨 agent 记忆共享，谁就成为基础设施。

### 5. orca ⭐ 本周 Trending

- **地址：** github.com/stablyai/orca
- **类型：** Agent Fleet 管理
- **简介：** 统一管理多个编码 agent（Grok Bot、Claude Code 等）的运行平台。支持桌面、移动端和远程运行时。可以用自己的订阅跑任何编码 agent。
- **为什么重要：** "一个 agent 不够用" 已成共识，fleet 管理是下一个必然需求。Orca 代表了 "agent 运维面板" 这个新品类。

---

## 三、应用/工具层（Skills / 终端工具 / 垂直场景）

### 1. answer-me-with-html ⭐ 2,200+

- **语言：** JavaScript
- **类型：** Agent Skill
- **简介：** 一个 agent skill，让 AI 用一页可交互的 HTML 回答复杂问题。支持图表、流程图、可交互组件，比纯文本回答信息密度高一个量级。
- **为什么重要：** 代表了 "agent 输出格式进化" 方向——不是给你一堆文字让你自己消化，而是直接生成可交互的知识制品。

### 2. VoiceStudio ⭐ 本周 Trending

- **地址：** github.com/debpalash/VoiceStudio
- **类型：** 开源语音 AI 套件
- **简介：** 完全本地运行的 ElevenLabs 替代品——语音克隆、语音设计、视频配音、听写、转录、有声书制作，支持 **646 种语言**。
- **为什么重要：** 语音是 agent 的重要 I/O 通道，ElevenLabs 是闭源付费服务。VoiceStudio 的开源替代意味着语音能力可以完全自托管。

### 3. muse-gadget-sdk ⭐ 1,707+

- **语言：** C
- **类型：** Meta Muse Gadget SDK
- **简介：** Meta 官方开源的 Muse gadget 开发 SDK。虽然 Muse Wonder 模型本身闭源，但 gadget 生态选择了开放路线。
- **为什么重要：** Meta 在 "模型封闭 + 工具开放" 和 "全面封闭" 之间走了一条中间路线。Gadget SDK 的开放意味着第三方开发者可以为 Muse 构建扩展——类似于 Chrome Extension 之于 Chrome。

### 4. ai-job-search ⭐ 本周 Trending

- **地址：** github.com/MadsLorentzen/ai-job-search
- **类型：** 求职 Agent 框架
- **简介：** 跑在你自己机器上的 AI 求职框架，基于 Claude Code。评估职位匹配度、定制简历、写求职信、准备面试。Fork 即用。
- **为什么重要：** Agent 从 "开发者工具" 走向 "个人生产力工具" 的代表案例。求职是高度个性化的场景，"跑在本地 + 用你自己的数据" 比通用 SaaS 更有优势。

### 5. claude-plugins-official ⭐ 本周 Trending

- **地址：** github.com/anthropics/claude-plugins-official
- **类型：** 官方插件目录
- **简介：** Anthropic 官方管理的 Claude Code 高质量插件目录。与社区目录互补，提供审核过的安全插件。
- **为什么重要：** Agent 插件生态正在复现 VS Code / Chrome 的 "官方目录 vs 社区目录" 双轨模式，标志着插件生态走向成熟。

---

## 四、本周趋势信号总结

| 趋势 | 信号强度 | 关键证据 |
|------|----------|----------|
| 模型竞争的下一个维度是 "主动记忆" | 🔥🔥🔥 | Meta Muse Wonder 将 Active Memory 作为核心卖点，跨天/周/月保持任务连贯 |
| 线性注意力进入生产可用阶段 | 🔥🔥 | Kimi-Linear-48B-A3B 用 MIT 许可证明 linear attention 可匹配 full attention |
| Agent 大数据集记忆成为基础设施 | 🔥🔥 | Leviathan 单周爆发，100万记录→450 token，245倍压缩 |
| Agent-Native 计算范式挑战 GUI Agent | 🔥🔥 | CLI-Anything 44K star + arXiv 论文，HKUDS 团队系统化推进 |
| Agent 跨 vendor 记忆互通成为痛点 | 🔥 | ai-memory、Leviathan memory 层都在解决 "记忆孤岛" |
| Agent Fleet 管理新品类出现 | 🔥 | orca、Ruflo federation 都在做多 agent 运维 |
| 开源编码 agent 市场分裂加剧 | 🔥🔥 | Ruflo(74K)、CLI-Anything(44K)、OpenCode(191K+) 三足鼎立 |

---

## 五、快速参考表

| 项目 | 地址 | 类型 | 本周热度 | 值得关注的理由 |
|------|------|------|----------|----------------|
| Meta Muse Wonder | Meta Model API (闭源) | 前沿模型 | 全球报道 | Active Memory 定义模型竞争新维度 |
| Kimi-Linear-48B-A3B | 开源权重 | 线性注意力 MoE | 新增收录 | MIT 许可，1M context，3B 激活 |
| Leviathan | elstongun/leviathan | Agent 记忆/索引 | ⭐ 673+ 本周爆发 | 1M 记录→450 token，245× 压缩 |
| CLI-Anything | HKUDS/CLI-Anything | Agent-Native CLI | ⭐ 44K 日增~150 | 让所有软件可被 agent 驱动 |
| Ruflo | ruvnet/ruflo | Agent Meta-Harness | ⭐ 74.5K | 最大 agent harness，314+ MCP 工具 |
| ai-memory | akitaonrails/ai-memory | 跨 Vendor 记忆 | Trending | 解决编码 agent 记忆孤岛 |
| orca | stablyai/orca | Agent Fleet 管理 | Trending | 多 agent 统一运维面板 |
| answer-me-with-html | Trending ⭐2.2K | Agent Skill | ⭐ 2,200+ | 可交互 HTML 回答复杂问题 |
| VoiceStudio | debpalash/VoiceStudio | 语音 AI | Trending | ElevenLabs 开源替代，646 语言 |
| muse-gadget-sdk | Meta 官方 | Gadget SDK | ⭐ 1,707+ | Muse 生态的开放扩展层 |
| ai-job-search | MadsLorentzen/ai-job-search | 求职 Agent | Trending | Claude Code 驱动的个人求职框架 |
| claude-plugins-official | anthropics/ | 官方插件目录 | Trending | Claude Code 插件生态的官方背书 |

---

*共收录 12 个项目，按领域分类。三层分类法：大模型层 / Agent 基础设施层 / 应用工具层。*
