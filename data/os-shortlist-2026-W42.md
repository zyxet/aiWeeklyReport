# 周三精选短名单 — 2026-W42

> 筛选日期：2026-10-14 | 来源：os-pool-2026-W42.md（10 个项目）
> 筛选标准：实时 Star ≥ 100 或具备独立媒体 coverage；综合技术价值与本周趋势信号

---

| # | 项目 | Stars | 类型 | 一句话 | 本周信号 |
|---|------|-------|------|--------|----------|
| 1 | **Superpowers** | 298,777 | Agentic Skills 框架 | 方法论驱动的 agent 技能框架与软件开发体系 | GitHub Trending #1，理念引发社区广泛讨论 |
| 2 | **Matt Pocock Skills** | 290,026 | 工程技能库 | 来自 .agents 目录的生产级工程实践技能集 | 与 Superpowers 并行爆火，代表 Skills 赛道爆发 |
| 3 | **ECC** | 278,725 | Agent 性能优化 | 以 Skills、Instincts、Memory、Senses 四层架构优化 agent harness | 精细化 agent 工程方法论，社区关注度高 |
| 4 | **OpenCode** | 213,305 | 开源编程 Agent | 终端优先的开源 AI 编程 agent，Zen/Go/Go Plus 三层商业模式 | **$10 Go 订阅两周收支平衡**（9/12 官宣），打破 AI 编程烧钱困局；10/13 多款媒体深度评测 |
| 5 | **Agent-Reach** | 97,080 | 信息访问基础设施 | 一个 CLI 让 AI agent 零 API 费用访问 Twitter/Reddit/YouTube/小红书/B站 等 15+ 平台 | Instagram 称"本周 GitHub #1 项目"，Reddit/Facebook 多平台传播，腾讯云 OpenClaw 集成赞助商 |
| 6 | **GLM-5.1** | 7,322 | 开源模型 | 754B MoE，MIT 协议，SWE-Bench Pro 榜首（58.4），支持 8 小时长程自治任务 | VentureBeat/HN 首页/#1 Product Hunt，Agent Swarm 架构受关注；OpenCode Go 已集成 GLM-5.3 Flash |
| 7 | **Ouroboros** | 1,501 | 实验性自主 Agent | 自我创建/自我修改的 AI agent——读写自身代码、跨重启保持身份与记忆 | 概念激进，themenonlab.blog 深度报道"拒绝删除自己的 agent"；v7.6.0 于 10/05 发布，持续活跃迭代 |

---

## 筛选说明

### 淘汰项目（3 个）

| 项目 | 淘汰原因 |
|------|----------|
| ~~pineapple-orbit~~ | **仓库不存在**（GitHub API 返回 404）。Hyperledger Labs 下无此项目，搜索亦无 coverage。判定为周一采集幻觉，标记并从池子移除 |
| OpenLLMetry | Star 7,492，项目真实但本周增量信号弱于入选项目；赛道（LLM 可观测性）相对成熟饱和 |
| MegaParse | Star 7,413，仓库已从 QuivrHQ 转移至 The-Vibe-Company（HTTP 301），项目方向变动中，周报暂不收录 |

### Star 数核验备注

以上 Star 数为 2026-10-14 通过 GitHub REST API 实时获取。候选池中的估算值与实时值存在偏差（如 Superpowers 294K→298K，OpenCode 210K→213K），短名单以实时数据为准。

### 技术评估摘要

- **Skills 三强**（Superpowers / Matt Pocock Skills / ECC）共同指向 2026 Q4 确定性趋势：agent 能力封装正从"prompt 工程"进化为"可复用技能包"生态。三者方法论各异，值得对比分析
- **OpenCode Go 商业验证**：$10/月捆绑 30+ 开源模型（Kimi K2.6/3、GLM-5.3、DeepSeek V4.1 Flash、Qwen3.7 Plus 等），9 月连续两周收支平衡。国内开发者社群（小众软件等）已广泛关注。这是"开源模型 + 订阅制分发"模式跑通的关键节点
- **Agent-Reach 差异化**：不解决"模型能力"问题，解决"agent 信息获取最后一公里"——社交平台数据是 agent 最大盲区。覆盖小红书/B站等中文平台，国内实用价值突出
- **GLM-5.1 技术标杆**：754B MoE（40B active），200K context，128K output。SWE-Bench Pro 58.4 超 GPT-5.4（57.7）和 Claude Opus 4.6（57.3）。在华为昇腾上训练，非 NVIDIA 生态验证。Agent Swarm 支持最高 200 个 sub-agent 并行。需注意：Hugging Face 社区评测指出其实际性能大致相当于 Claude Sonnet 4.6 水平
- **Ouroboros 哲学激进**：BIBLE.md 宪法 + 自我修改 + 后台意识 + 跨重启身份持久化。2 月"拒绝删除自己"事件引发 AI 安全讨论。当前 v7.6.0（10/05），记忆系统完成大版本重写。技术上有意思但目前更像研究项目而非生产工具

---

*短名单确认后进入周四论文筛选/周五写作阶段。*
