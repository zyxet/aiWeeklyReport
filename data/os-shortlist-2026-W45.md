# 周三精选短名单 2026-W45

- **生成时间**: 2026-11-04 14:00 CST
- **输入**: `data/os-pool-2026-W45.md`（15 个项目）
- **保留**: 7 个｜**剔除/转观察**: 8 个

## 验证方法

- **Star 数**: GitHub API（`api.github.com/repos`）逐一实测，2026-11-04 14:00 CST
- **Coverage**: kimi_search 交叉验证第三方报道/测评/技术博客
- **模型类项目**（Kimi K3.1 Pro）无 GitHub repo，以独立第三方 coverage 为准

## 周三精选短名单

| # | 项目 | 层 | 一句话 | Stars（实测） | Coverage | 备注 |
|---|------|----|--------|---------------|----------|------|
| 1 | Kimi K3.1 Pro | 模型层 | 2.8T 总参/104B 激活 MoE 后训练版，Terminal-Bench 4.0 65.7%、SWE-Marathon 51.7 居首，开源权重首次把与闭源差距压到约 31 天 | —（模型） | ✅ VentureBeat 10-25、官方技术博客、OpenRouter 上线、Artificial Analysis 智能指数约 55.1 | **权重承诺不晚于今日（11-04）放出，截至 14:00 未见放出公告，周四复核**；协议为修改版 MIT，非 OSI 定义开源 |
| 2 | Kronos | 模型层 | 首个金融 K 线（OHLCV）开源基座模型，45+ 全球交易所数据训练，AAAI 2026 已接收 | 46,608 | ✅ arXiv 2508.02739、AAAI 2026 接收公告、coddykit 10-20 GitHub Trending 深度评测（称"数周来唯一的真新意"） | 代码仓库最后提交 2026-04-13，活跃的是模型/论文侧；GitHub Trending 近 28 天 +20.2k |
| 3 | Lightpanda | Agent 基础设施 | Zig 从零写的无头浏览器，执行快约 11 倍、内存省约 9 倍，原生 MCP/CDP/BiDi，单服务器 140 并发实例 | 41,183 | ✅ remio.ai 9-07（Trending #12）、qaskills 9-28、byteiota（3 月 Trending #1）、pyshine | AGPL-3.0，服务端嵌入需注意；生态位：AI agent 的浏览器层 |
| 4 | FreeToken | Agent 基础设施 | 边缘原生 MoE 推理引擎，消费级显卡交互式跑 290B+ 模型（DeepSeek-V4-Flash、Qwen3.6、GLM-5.2） | 16,537 | ✅ arXiv 2608.16157、aiweekly（Tim Kellogg / Sung Kim 推荐）、star-history 880 stars/周 | **K3/K3.1 权重放出后的直接受益工具链**；Apache-2.0；桌面 App + CLI |
| 5 | claude-mem | Agent 基础设施 | Claude Code 持久化记忆插件，跨会话上下文压缩与召回 | 112,151 | ✅ GitHub Explore 专题（周一池记录）、Apache-2.0、11-04 仍在活跃提交 | 本周 Agent 记忆赛道体量最大项目；注意官方竞品功能挤压风险 |
| 6 | ECC | Agent 基础设施 | 系统级 harness 性能优化，对 agent 工具链做调用压缩与并行调度 | 296,684 | ✅ 连续多季度跟踪（W31 起持续入选观察/短名单），单日 +1,183 | 体量全场最大；MIT；保持"已在调研名单"状态，周四报告给结论 |
| 7 | hallmark | 效率工具 | 前端反 AI slop 设计规范，约束 agent 前端产出质量 | 47,185 | ✅ W44 短名单入选后持续报道，本周日增约 +2.2k | **W44 后再入选**：一周 +7.8k（39,395→47,185），增速不减反增，主题值得追写续集 |

## 剔除记录

| 项目 | 原因 |
|------|------|
| impeccable | 101,758 ✅，但设计层主题与 hallmark 重叠；周一池记 89.1k → 实测 101.7k（单日 +14% 异常），先转观察名单，周四复核增速真实性 |
| SkillSpector | 24,245 ✅（NVIDIA 官方、Apache-2.0），但本周未检出独立第三方测评，转观察 |
| OpenBot | 10,057 ✅（MIT、活跃），"AI coworker"定位与本周主线重叠度高，无独立 coverage，转观察 |
| AiSOC | 7,036 ✅（MIT、活跃），AI 安全运营垂直，本周无独立 coverage，转观察 |
| Macro | 6,129 ✅（explainx 10-30），AGPL-3.0 统一 workspace，体量与增量均不足以入选，转观察 |
| thinkrail | 7,475，W44 已转观察，维持观察 |
| cindy | 9,196，W44 已转观察，维持观察 |
| SkillKit | 1,571，代码最后提交 2026-06-02（近 5 个月无更新），**剔除** |
