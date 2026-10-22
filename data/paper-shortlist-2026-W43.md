# 📄 论文精选短名单 — 2026-W43

> 筛选时间：2026-10-22（周四）
> 候选池：12 篇 → 保留 8 篇（总分 ≥18，DLite 为关注级）
> 评分：创新性 / 实用性 / 技术深度 / 机构背书 / 代码可得性，每项 1-5，总分 25
> 🏆 = 论文+代码双料项目（代码已开源可复现）

## 本周围绕

本周候选池呈现 **Computer Use 赛道爆发**（OS-Helix 与 OpenGCUA 同周正面对决）、**长程 agent 训练理论深化**（TreeOPSD 的 closed-form 信用分配 vs CarryOn 的对象化上下文）、**agent 评测走向过程感知**（Into the Unknown 用 135 篇论文揭示科研 agent 天花板、LiveMACE 用真实市场诊断能力鸿沟）三条主线。开源诚意十足——12 篇中至少 6 篇附完整代码或模型。

## 📋 短名单

| # | 论文 | 标签 | 一句话摘要 | 总分 | 备注 |
|---|------|------|-----------|------|------|
| 1 | [OS-Helix](https://arxiv.org/abs/2610.22234) | Computer Use, GUI+Code, RL | 端到端训练原生 GUI+代码混合动作空间计算机使用智能体，OSWorld-Verified 66.44% SOTA | 22 | 上海AI Lab 领衔八校联合；模型/数据已放 HF，代码 coming soon |
| 2 | [OpenGCUA](https://arxiv.org/abs/2610.22200) | Computer Use, Open Source | 阿里 MAI 开源通用计算机使用全栈：视觉定位、文本定位、奖励建模全部开放 | 22 | 🏆 实现与 prompts 已 release，论文+代码双料 |
| 3 | [CarryOn](https://arxiv.org/abs/2610.18784) | Long Context, Context Management | 借鉴面向对象编程将智能体上下文封装为可复用任务对象，替代历史压缩 | 21 | Microsoft；长程 agent 上下文管理范式转换 |
| 4 | [Into the Unknown](https://arxiv.org/abs/2610.19159) | Benchmark, Science | DOE 联合 benchmark：9 个前沿 agent 就开放科学问题写 135 篇论文，0 篇全通过评审 | 21 | 🏆 代码数据公开；结论——科研 agent 远未及格 |
| 5 | [TreeOPSD](https://arxiv.org/abs/2610.23181) | RL, Long-Horizon | 无 critic 树感知后验自蒸馏：回合级 closed-form 信用分配，Deep Research +4.97 over GRPO | 21 | 清华+腾讯混元；理论扎实，未见开源 repo |
| 6 | [OpenMobile-2](https://arxiv.org/abs/2610.14157) | Mobile Agent, Open Source | 全开源移动智能体：35 个模拟商业 app 环境、数据、benchmark、模型一体开放 | 20 | 🏆 环境+数据+模型全链路开源 |
| 7 | [DiscoveryRSI](https://arxiv.org/abs/2610.23839) | Scientific Discovery, Self-Improvement | 递归自我改进框架驱动 LLM 自主进化科学假设，6.3% 产出可落地链接 | 20 | 🏆 GitHub Apache-2.0 + HF 模型，双料 |
| 8 | [DLite](https://arxiv.org/abs/2610.23787) | Inference, Speculative Decoding | 免历史投机解码：草稿模型复用目标隐状态做局部预测，agentic 负载下接受长 2-6 | 18 | 关注级；SJTU+清华+无问芯穹，未提及开源 |

## 📊 评分明细

| 论文 | 创新性 | 实用性 | 技术深度 | 机构背书 | 代码可得性 | 总分 |
|------|--------|--------|----------|----------|------------|------|
| OS-Helix | 4 | 5 | 5 | 5 | 3 | **22** |
| OpenGCUA | 4 | 5 | 4 | 4 | 5 | **22** |
| CarryOn | 5 | 4 | 4 | 5 | 3 | **21** |
| Into the Unknown | 4 | 3 | 4 | 5 | 5 | **21** |
| TreeOPSD | 5 | 5 | 5 | 4 | 2 | **21** |
| OpenMobile-2 | 3 | 4 | 4 | 4 | 5 | **20** |
| DiscoveryRSI | 4 | 4 | 4 | 3 | 5 | **20** |
| DLite | 4 | 4 | 4 | 4 | 2 | **18** |
| AgentGarten | 4 | 3 | 3 | 3 | 4 | 17 |
| MoHGE | 3 | 4 | 3 | 3 | 4 | 17 |
| LiveMACE | 4 | 3 | 4 | 3 | 2 | 16 |
| ACT3D | 4 | 3 | 4 | 3 | 2 | 16 |

## 📝 落选说明

- **AgentGarten**（17）：大规模并发环境方向有意思，但当前仅 neural renderer 可用，完整 code worlds 尚未放出，基础设施类工作实用价值待验证。
- **MoHGE**（17）：⚠️ 池子标注为"agentic reasoning"，实际论文为 ACL 2026 Industry Track 的高效 MoE 架构（异构分组专家），与 agent 关联弱，MoE 改进方向已较成熟。
- **LiveMACE**（16）：金融市场过程感知评估有价值，但领域特定性强、未提及代码开源，通用参考性有限。
- **ACT3D**（16）：VLM 3D 主动探索思路新颖，但 3D 场景应用面窄，未提及代码开源。

## 🔍 本周观察

1. **Computer Use 双雄同周**：OS-Helix（端到端 RL 训练路线，SOTA 66.44%）vs OpenGCUA（全栈开源路线）。GUI+Code 混合动作空间已从 prompt 技巧共识走向训练范式共识——naively 加 code tool 反而会掉点，路由能力必须内化训练。
2. **长程 agent 的两种解法**：TreeOPSD 从 RL 信用分配切入（理论优美，closed-form bounded teacher），CarryOn 从上下文管理切入（对象化运行时）。一个治标一个治本，值得跟踪两者是否在长 horizon 上殊途同归。
3. **开源诚意罕见地高**：12 篇候选中 6 篇有完整代码/模型，与此前数周"论文先行、代码画饼"的趋势明显不同。Computer Use 和 Mobile Agent 两个赛道都在用开源换生态位。
4. **科研 agent 的现实检验**：Into the Unknown 的 0/135 通过率是一记清醒剂——agent 辅助科研的叙事很热，但放到真实开放问题上，距同行评审通过还有相当距离。

---

*由 thursday-paper-filter 任务自动生成 | intelligence-system*
