# 候选池 2026-W19

## 收集周期
2026-05-03 → 2026-05-09

## 生成时间
2026-05-04 02:00 UTC

## 执行类型
cron 自动采集（周一情报收集）

---

## 🔥 1. zilliztech/claude-context
Stars: 10.6k · License: MIT · Tag: MCP · Dev infra

定位：语义代码搜索 MCP 服务器，让任意编码 Agent 查询整个代码库作为上下文。

Why：解决大型代码库中 Agent "grep 30 秒才回答" 的痛点——将代码库索引到向量数据库，仅返回相关代码片段，大幅节省上下文窗口和 API 费用。Claude Code、Cursor、Windsurf 等主流工具均可接入。

URL: https://github.com/zilliztech/claude-context

---

## 🔥 2. badlogic/pi-mono
Stars: 43.9k · License: MIT · Tag: Agent toolkit · CLI

定位：AI Agent 工具包 monorepo，包含编码 Agent CLI、统一 LLM API、TUI/Web UI 库、Slack Bot、vLLM pods。

Why：Mario Zechner 的作品。各组件设计为可互换零件——200 行代码即可用统一 LLM API（封装 Anthropic/OpenAI/Google/Groq）搭建自定义 Agent。附带真实 OSS 会话数据以改进 Agent 表现。

URL: https://github.com/badlogic/pi-mono

---

## 🔥 3. huggingface/ml-intern
Stars: 8.1k · Maintainer: Hugging Face · Tag: Agentic ML · Open

定位：自主 ML 工程师——读论文、找数据集、微调模型、上传训练 traces，完成 ML 任务无需逐行 babysit。

Why：Agentic 循环最高 300 次迭代，内置敏感操作审批门控。关键细节：每次会话 traces 上传到私有 HF 数据集，可调试、可分享。是"真正的自主编码 Agent"的参考实现。

URL: https://github.com/huggingface/ml-intern

---

## 🔥 4. TauricResearch/TradingAgents
Stars: 62.6k · License: Apache-2.0 · Paper: arxiv.org/abs/2412.20138

定位：多 Agent 交易框架，模拟真实交易公司的组织架构。

Why：五类 Agent（基本面分析师、情绪分析师、技术分析师、交易员、风控经理）拥有各自系统提示和工具权限，通过动态辩论投票产生交易决策。NeurIPS 关联会议发表，多 Agent 架构的 cleanest 实证——角色专业化确实击败单 Agent 巨无霸。

URL: https://github.com/TauricResearch/TradingAgents

---

## 🔥 5. warpdotdev/warp
Stars: 51.3k (+3,403 today, ~20K in 4 days)

定位：Agentic 开发环境，诞生于终端。

Why：Rust 构建的智能终端，原生整合 AI 代理能力。4 月底 12K stars 爆发式增长后持续保持 3K+/day 增速。定位"编排 Agent 的终端"已深入人心。

URL: https://github.com/warpdotdev/warp

---

## 🔥 6. mksglu/context-mode
Stars: 11.7k (+2.3K this week)

定位：上下文窗口优化器，MCP 服务器将工具输出沙箱化实现 98% 上下文压缩。

Why：跨 14 个 Agent 平台工作，用 SQLite + BM25 索引输出，解决"Agent 30 分钟后失忆"问题。长会话 Agent 的基础设施级工具。

URL: https://github.com/mksglu/context-mode

---

## 🔥 7. mattpocock/skills
Stars: 52.3k (+30.9K this week)

定位：Claude Code 的 skills 仓库，最热门的 `.claude` 目录。

Why：八天内从 23K 飙到 52K，Skills 生态的 stadium-filler。标志着 "Skills" 从 fad 变成 category——每个 Agent 平台都在构建自己的 curated skill marketplace。

URL: https://github.com/mattpocock/skills

---

## 🔥 8. 1jehuang/jcode
Stars: 2.3k (+404 today)

定位：Rust 编码 Agent 框架，轻量级 Agent 编排层。

Why：连续多日 400+/day 增长，小而精的增长曲线。反映开发者不再满足于简单代码补全，追求端侧执行能力 + 自动化技能框架的深度集成。

URL: https://github.com/1jehuang/jcode

---

## 🔥 9. browserbase/skills
Stars: 1.1k (+334 today)

定位：Claude Agent SDK + 远程浏览器自动化，反爬虫保护 + CAPTCHA 解决 + DevTools tracing。

Why："给 Agent 装上网络之眼"的工具包。与 mattpocock/skills、github/awesome-copilot 同期 trending，三个 skills 仓库同时上榜，确认 Skills 已成为独立品类。

URL: https://github.com/browserbase/skills

---

## 🔥 10. 777genius/claude_agent_teams_ui
Stars: 799 (+62 today)

定位：Agent-to-Agent 消息传递 + 看板监督。Agents 创建任务、跨团队沟通、互相 review。

Why：将人类定位为 executive 而非 operator 的"AI 团队经理"UX。Agent 编排 UI 品类 proliferating 的代表——人类作为监督者，Agent 作为自主工作者互相通信。

URL: https://github.com/777genius/claude_agent_teams_ui

---

## 🔥 11. Tencent/AngelSlim
Stars: 753 (+48 today)

定位：模型压缩工具包，支持剪枝、量化、蒸馏。

Why：腾讯出品，低调但实用——对需要在受限硬件上部署 LLM 的场景至关重要。端侧部署趋势下的基础设施。

URL: https://github.com/Tencent/AngelSlim

---

## 🔥 12. lukilabs/craft-agents-oss
Stars: 5,563 (+319 today)

定位：Google 开源的 CraftAgents 项目，TypeScript 构建的 Agent 工具包。

Why：帮助开发者快速创建可扩展的 AI 助手和自动化工作流。Google 在 Agent 工具链领域的布局信号。

URL: https://github.com/lukilabs/craft-agents-oss

---

## 本周趋势总结

本周 GitHub Trending 被 Agent 全面占领。五个关键词：

1. **Skills 成为品类**：mattpocock/skills、browserbase/skills、github/awesome-copilot 三个 skills 仓库同时 trending，Skills 从 fad 变成独立 category。

2. **Agent 编排层爆发**：claude_agent_teams_ui、jcode、pi-mono 等项目密集涌现，多 Agent 协调层是下一波工具创新的主战场。

3. **终端 Agent 化**：Warp（51K stars 爆发增长）、DeepSeek-TUI、Claude Code 等终端原生 Agent 工具重塑开发者底层交互逻辑。

4. **上下文优化刚需**：context-mode（11.7K）、claude-context（10.6K）解决 Agent "金鱼记忆"和代码库查询效率问题。

5. **垂直场景落地**：TradingAgents（金融）、ml-intern（ML 工程）、AngelSlim（模型压缩）标志 AI 跨越通用能力普及期，进入场景驱动的技能闭环阶段。

---

## 参考来源

- GitHub Trending Digest — May 1, 2026 (0011011011.com)
- Top 5 Trending AI GitHub Repos — May 2026 (Week 18) (askglitch.com)
- GitHub 热榜项目- 日榜(2026-05-01) (CSDN)
- agents-radar / Hugging Face Trending Models (duanyytop/agents-radar)
- GitHub Ranking (EvanLi/Github-Ranking)
