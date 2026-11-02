# 周一开源项目速览

**周期：** 2026-W45（10月27日–11月2日）
**生成日期：** 2026-11-02
**来源：** GitHub Trending / GitHub Explore / Hacker News / 社区博客 / 官方公告

---

## 一、大模型层（模型权重 + 训练推理）

### 1. Kimi K3.1 Pro 权重发布倒计时 —— 本周最大悬念

- **类型：** 开放权重模型（权重定于 11月4日 释放）
- **背景：** 10月23日 API 上线（详见 W44 报告），本周全周社区焦点都集中在即将到来的权重发布上。多家第三方分析（CometAPI、Superbash、Lorphic）在本周密集出稿，将其定位为"当前可自托管的最强开放权重模型"。
- **架构：** 2.8T 总参 / 104B 激活稀疏 MoE（896 专家、每 token 激活 16 个），1M context，文本+图像+视频输入
- **关键数据：** Artificial Analysis 智能指数 55 分（全球第 4）；Terminal-Bench 4.0 达 65.7%；Hallu Bench Hard 幻觉率从 K3 的 23.4% 降至 8.3%
- **API 价格：** $2.00/M 输入、$10.00/M 输出（K3 的约 1/3）；Highspeed 变体 2-3 倍速
- **意义：** 若如期释放，这将是史上最大规模的开放权重发布，自托管 + 微调的门槛被直接拉到 3T 级
- **注意：** 协议仍待确认（K3 使用自定义 Kimi K3 License，非 OSI 认证）；K3 的 llama.cpp 支持 PR 自 7 月至今未合并，本地运行需 vLLM / SGLang

### 2. FreeToken ⭐ GitHub Trending

- **仓库：** FlashML-org/FreeToken（Python）
- **定位：** 把数据中心级别的模型服务带到桌面端，本地高速运行大规模模型
- **协议：** 开源（GitHub Trending 持续在榜）
- **亮点：** 随着 K3.1 Pro 级别的大模型开放，"桌面端跑大模型"的需求被点燃，FreeToken 恰好卡位这个叙事
- **值得跟进：** 实际能跑多大的模型？显存策略是什么？

### 3. Kronos —— 金融市场语言基础模型

- **仓库：** GitHub Trending（Python）
- **定位：** 面向金融市场数据（行情、订单流）的基础模型，把市场当作一种"语言"来建模
- **意义：** 金融 + 基础模型的交叉点，和 TradingAgents（116k stars）这类多智能体交易框架形成上下游关系
- **值得跟进：** 训练数据来源与许可、回测表现

---

## 二、Agent 基础设施层

### 4. Lightpanda ⭐ GitHub Trending

- **仓库：** lightpanda（Zig）
- **定位：** 专为 AI 和自动化设计的 headless 浏览器
- **亮点：** 本周 GitHub Explore 官方推荐位；Zig 编写，性能开销远低于 Chromium 系方案；Agent 抓取的专用基础设施正在成为一个独立赛道（对标 browser-use、Stagehand）
- **为什么重要：** 2026 年的共识——Agent 的瓶颈不在推理而在"看世界"，浏览器是主要接口

### 5. AiSOC ⭐ GitHub Trending

- **仓库：** beenuar/AiSOC（Python）
- **定位：** 开源 AI 安全运营中心——告警融合、LLM Agent 分诊、MITRE ATT&CK 调查、可回放决策账本
- **协议：** MIT，自托管、零 API key 依赖
- **亮点：** 自带 MCP server，可直接接入 Claude / Cursor / Continue；把 SOC 的整套工作流用 Agent 重写了一遍
- **意义：** 安全是 Agent 落地最快的垂直领域之一，"LLM triage + 人类复核"的模式正在替代传统 SIEM 流水线

### 6. NVIDIA SkillSpector

- **仓库：** NVIDIA/SkillSpector（Python，22.1k stars）
- **定位：** AI Agent 技能（Skills）安全扫描器
- **功能：** 检测漏洞、恶意模式、prompt injection、数据外泄、供应链风险，覆盖 Claude Code / Codex / MCP skills
- **意义：** Agent skills 生态爆发（见趋势部分）之后，安全扫描成为刚需。NVIDIA 下场做这个，说明 skills 供应链已经被当成正经软件供应链对待

### 7. claude-mem ⭐ GitHub Trending

- **仓库：** thedotmack/claude-mem（TypeScript，101k stars）
- **定位：** 跨会话持久记忆——记录 Agent 做了什么、AI 压缩、在后续会话注入相关上下文
- **兼容性：** Claude Code、OpenClaw、Codex、Gemini CLI、Hermes、Copilot、OpenCode
- **本周动态：** 11月1日更新，占据 GitHub Explore 推荐位
- **意义：** 编码 Agent 的记忆赛道（claude-mem / Mem0 / Hindsight / Beads）正在分化出"会话记忆"与"知识记忆"两个子方向

### 8. OpenBot（CopilotKit 出品）⭐ GitHub Trending

- **仓库：** CopilotKit/OpenBot（TypeScript）
- **定位：** 开源 AI 同事——每个 Agent 拥有自己的"电脑"：浏览器、文件系统和工具；每个动作事前决策、事后记录
- **亮点：** 兼容 AG-UI 协议
- **注意：** 与 nightly-labs/openbot（1.5k stars，本地优先桌面工作区）撞名，是两个不同项目；后者主打"持久 AI 队友的本地桌面"，支持 Codex / Claude / Grok 多 Agent 协作
- **意义：** "computer use" 叙事从演示走向开源实现，2026 下半年该方向项目密度明显增加

### 9. JetBrains thinkrail

- **仓库：** JetBrains/thinkrail（TypeScript，3.9k stars）
- **定位：** 围绕 Pi 模型构建的轻量级 IDE，"vibe code"——IDE 会自适应你的工作方式
- **意义：** JetBrains 正式入场 Agent IDE 赛道；此前该赛道主要是 Cursor / Zed / VS Code 插件的天下

---

## 三、Agent 技能与编排层

### 10. ECC（Agent Harness 性能优化系统）

- **仓库：** affaan-m/ECC（JavaScript，~290k stars，10月27日单日 +1,183）
- **定位：** 面向 Claude Code / Codex / Opencode / Cursor 的 harness 优化系统——skills、instincts、memory、安全、research-first 开发流
- **意义：** 单一 Agent "调教包"类项目的星数天花板被持续抬高，说明"给现有 Agent 加外挂"比"造新 Agent"更受社区欢迎

### 11. hallmark（Nutlope）⭐ 日增速冠军

- **仓库：** Nutlope/hallmark（CSS，36.2k stars，单日 +2.2k——本周增速之最）
- **定位：** 反 AI slop 设计 skill——给 Claude Code / Cursor / Codex 注入设计品味
- **为什么火：** 审美疲劳是真实的社区情绪；"让 Agent 产出不那么像 AI"本身成了一个品类

### 12. impeccable

- **仓库：** pbakaus/impeccable（Rust，89.1k stars）
- **定位：** 让 AI harness 更擅长设计的"设计语言"
- **与 hallmark 的关系：** 同一赛道的两个头部——hallmark 是 skill 注入，impeccable 更偏设计语言系统
- **意义：** "设计层"正在从 Agent 工具链中独立出来成为专门一层

### 13. SkillKit —— Agent 技能的包管理器

- **仓库：** rohitg00/skillkit（1.5k stars，早期）
- **定位：** 从 400k+ skills、31 个源安装技能；在 46 种 Agent 格式间自动转换（Claude Code 的 SKILL.md、Cursor 的 .mdc、Copilot 的 .github/skills……）
- **功能：** `init` 探测环境、`recommend` 按技术栈推荐、`add` 安装、`sync` 全端同步
- **意义：** 这是 skills 生态的 "npm 时刻"——格式碎片化问题被正面解决；和 NVIDIA SkillSpector（安全扫描）合起来看，skills 正在完成"包管理 + 安全审计"的基础设施建设

### 14. cindy

- **仓库：** makecindy/cindy（TypeScript，6.4k stars，单日 +1.3k）
- **定位：** 开源、开箱即用的 AI Agent（"想到，就能做到"）
- **意义：** 又一个"零配置 Agent"尝试，该品类 2026 下半年持续有新项目冒头

### 15. Macro —— AGPL 一体化工作区

- **仓库：**  trending 约 5.2k stars（AGPL）
- **定位：** 把邮件、聊天、文档、任务、通话、CRM 连成一张双向图，夜间共享 AI 记忆，对编码 Agent 暴露 MCP 接口
- **意义：** "Agent 原生工作区"方向的代表——不改造旧工具，直接把整套协作栈重写为图结构

---

## 趋势观察与判断

1. **Skills 经济完成基础设施闭环。** 本周最重要的结构性信号：SkillKit（包管理）+ SkillSpector（安全扫描）+ ECC（性能优化）同时出现在视野里，Agent skills 的"npm 三件套"齐了。这意味着 skills 从"社区共享的提示词"正式升级为"可分发、可审计的软件制品"。建议：开始像管理依赖一样管理 skills，建立内部 skill registry 和审查流程。

2. **Agent 浏览器/电脑层加速独立。** Lightpanda（Zig headless 浏览器）、OpenBot（AI 同事电脑）、hex（本地语音输入）同时上榜，"Agent 的感官基础设施"正在从框架代码中剥离成专用项目。值得评估 Lightpanda 替代现有抓取方案的成本。

3. **Agent 安全从议题变成产品。** AiSOC（安全运营）和 SkillSpector（skill 供应链）两条线同时推进，说明 Agent 安全已经不只是讨论，开始有人做产品了。下周 K3.1 Pro 权重释放后，预计会有一波自托管 Agent 安全方案的跟进需求。

4. **框架层进入"后 1.0 整合期"。** 根据 10 月的框架横评：Microsoft Agent Framework 1.0（4月）成为 Semantic Kernel + AutoGen 的官方继任者，AutoGen 进入维护模式；Google ADK 2.0（5月）、Pydantic AI 2.0（6月）、AG2 1.0（7月）。框架选型窗口正在收窄，锁定成本在上升。

5. **下周核心事件：Kimi K3.1 Pro 权重（11月4日）。** 若如期释放，这将是 2026 年开源社区最大事件——2.8T 参数级开放权重 + 1M context + 多模态。建议提前确认：硬件需求（vLLM/SGLang 路径）、协议条款、llama.cpp 支持进展。届时会做专项跟踪。

6. **反 AI slop 成为显性需求。** hallmark 单日 +2.2k stars 是本周最强信号——"输出质量的下限被抬高了，但品味没有"。设计类 skill / 设计语言系统值得纳入日常工具链。

---

**下期：** 2026-W46（11月3日–11月9日），重点关注 Kimi K3.1 Pro 权重发布及首批自托管实测报告。
