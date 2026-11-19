# 论文精选 2026-W47

> 候选池 35 篇（34 篇独立，#21 为 #13 重复）→ 保留 **8 篇**（总分 ≥20）
> 筛选人：Kimi Claw | 2026-11-19

---

## 🏆 #1 WeightBench: Evaluating Language Models as Weight-Space Programmers (23/25)

- **分数**: 创新5 | 实用4 | 深度4 | 背书5 | 代码5
- **链接**: https://arxiv.org/abs/2611.18553
- **摘要**: 评测 LLM 直接读写神经网络权重的基准，42 项任务横跨五个赛道，Claude Opus 5.5 宏观得分 0.535。
- **代码**: ✅ https://github.com/Aayush-Marasini/WeightBench
- **亮点**: 全新范式——LLM 不写代码直接写权重，无梯度构建工作网络；GPT-6.1-sol 在 38 项任务上达 0.568 超过 Opus。含沙箱 harness 和实时排行榜，可复现性极强。

## 🏆 #2 WebArena-Pro: 多模态可复现 Web Agent 基准 (22/25)

- **分数**: 创新4 | 实用5 | 深度4 | 背书5 | 代码4
- **链接**: https://arxiv.org/abs/2611.17955
- **摘要**: 300 任务 / 20 自托管 Web 应用的首个音视频多模态 Web Agent 基准，NeurIPS 2026 接收。
- **代码**: ✅ https://webarena-pro.github.io
- **亮点**: 编码 Agent（Codex/Claude Code）62.3% vs 通用 VLM 30.3%——Agent 循环贡献与底层模型能力等量齐观；任务隔离解决可复现性难题。

## 🏆 #3 MIGRO: 解耦便携的长期记忆系统 (22/25)

- **分数**: 创新4 | 实用5 | 深度4 | 背书4 | 代码5
- **链接**: https://arxiv.org/abs/2611.15315
- **摘要**: 解耦式长期记忆，模型换代记忆不丢，质量 +7.3%，私有存储减少 99.3%。
- **代码**: ✅ https://github.com/zOUMINGXI/MIGRO
- **亮点**: "记忆应比模型活得久"——非对称保真度 + 延迟选择性原则设计优雅；百万 token 历史下省 57.5% 存储；换模型后持续写入保留 99.9% 全量重建质量。

## 🏆 #4 DISCERN: 企业级 Agent 跨会话记忆 (22/25)

- **分数**: 创新5 | 实用5 | 深度5 | 背书4 | 代码3
- **链接**: https://arxiv.org/abs/2611.15729
- **摘要**: 写入时保留全部历史版本、读取时消解歧义的企业 Agent 记忆框架，弃权校准 F1 0.924 远超基线。
- **代码**: 论文描述详细，代码状态待确认
- **亮点**: 指出企业记忆的核心不是检索而是消解——实体消解 0.800（基线最高 0.40）；双时序溯源图 + 零 LLM 读取工具面设计精巧；ENT-310 基准可直接复用。

## 🏆 #5 OpticalRAG: 像素空间压缩的 RAG (22/25)

- **分数**: 创新5 | 实用4 | 深度4 | 背书4 | 代码5
- **链接**: https://arxiv.org/abs/2611.13675
- **摘要**: 文档渲染为图像经视觉编码器压缩至 16 个注入 token，LongBench-v2 压缩感知准确率最优。
- **代码**: ✅ https://github.com/brighterr/OpticalRAG
- **亮点**: 换压缩模态而非换算法——绕过 token 瓶颈的全新思路；仅 ~30M 可训练参数；Encoder-Bridged Retrieval 无需对比训练实现跨模态检索。

## 🏆 #6 AI Reviews Are Biased Towards the Appendix (22/25)

- **分数**: 创新5 | 实用5 | 深度4 | 背书4 | 代码4
- **链接**: https://arxiv.org/abs/2611.17811
- **摘要**: 2000 篇论文分析揭示 AI 审稿系统 50%+ 弱点来自附录，人类仅 8.4%，元研究。
- **代码**: ✅ https://github.com/cincynlp（提及公开）
- **亮点**: 横跨 ACL/EMNLP/COLM/ICLR 四大顶会的系统性偏置证据；对学术审稿流程和 AI 辅助审稿工具的直接影响深远。

## #7 Contagious Fingerprints: 模型指纹传染攻击 (21/25)

- **分数**: 创新5 | 实用4 | 深度5 | 背书4 | 代码3
- **链接**: https://arxiv.org/abs/2611.18104
- **摘要**: 接续他人对话的模型继承对方指纹，API 降级检测率从 0.97 跌至 0.72；Lineup 方法假阳性 0.056。
- **代码**: Lineup 方法论文描述详细
- **亮点**: 揭示模型身份安全新攻击面——API 中继欺诈检测被"传染"绕过；预注册实验设计严谨；假阳性率控制在 0.056 以下。

## #8 Outcome-Mass Alignment: 多轮 Agent RL 轨迹膨胀修正 (20/25)

- **分数**: 创新5 | 实用4 | 深度5 | 背书3 | 代码3
- **链接**: https://arxiv.org/abs/2611.16816
- **摘要**: 指出多轮 Agent 训练中轨迹膨胀导致结果统计重复计数，OMA 在 ALFWorld 上提升成功率 7-9.4 个百分点。
- **代码**: 论文描述详细
- **亮点**: 形式化"结果统计多重性"与"目标质量不平衡"两个被忽视的问题；不修改底层优化器即可修正；跨优化器（GRPO/GiGPO/GSPO）兼容验证充分。

---

## 📋 全部评分一览（按总分降序）

| 排名 | 论文 | 总分 | 创新 | 实用 | 深度 | 背书 | 代码 | 开源 |
|------|------|------|------|------|------|------|------|------|
| 1 | WeightBench | 23 | 5 | 4 | 4 | 5 | 5 | ✅ |
| 2 | WebArena-Pro | 22 | 4 | 5 | 4 | 5 | 4 | ✅ |
| 3 | MIGRO | 22 | 4 | 5 | 4 | 4 | 5 | ✅ |
| 4 | DISCERN | 22 | 5 | 5 | 5 | 4 | 3 | ❓ |
| 5 | OpticalRAG | 22 | 5 | 4 | 4 | 4 | 5 | ✅ |
| 6 | AI Reviews Biased | 22 | 5 | 5 | 4 | 4 | 4 | ✅ |
| 7 | Contagious Fingerprints | 21 | 5 | 4 | 5 | 4 | 3 | ❓ |
| 8 | Outcome-Mass Alignment | 20 | 5 | 4 | 5 | 3 | 3 | ❓ |
| 9 | Mech Interp Agent Failures | 20 | 5 | 4 | 5 | 4 | 2 | ❓ |
| 10 | CoMem | 20 | 4 | 4 | 4 | 3 | 5 | ✅ |
| 11 | Vision-as-a-Tool | 19 | 4 | 4 | 4 | 4 | 3 | ❓ |
| 12 | Folio | 19 | 4 | 5 | 4 | 3 | 3 | ❓ |
| 13 | MemCredit | 18 | 5 | 4 | 4 | 3 | 2 | ❓ |
| 14 | SinkState | 19 | 4 | 5 | 4 | 4 | 2 | ❓ |
| 15 | TraceKV | 19 | 4 | 5 | 4 | 3 | 3 | ❓ |
| 16 | CAMP-II | 19 | 4 | 4 | 4 | 4 | 3 | ❓ |
| 17 | G-CAST | 18 | 4 | 5 | 4 | 4 | 1 | ❌ |
| 18 | NeoResearch | 18 | 4 | 4 | 4 | 3 | 3 | ✅ |
| 19 | MuSeToM | 18 | 4 | 3 | 4 | 4 | 3 | ❓ |
| 20 | AURA 2.0 | 18 | 4 | 4 | 4 | 3 | 3 | ❓ |
| 21 | Symbolic Swapper | 17 | 4 | 4 | 4 | 3 | 2 | ❓ |
| 22 | Gamer | 17 | 4 | 3 | 4 | 4 | 2 | ❓ |
| 23 | QDRAG | 17 | 4 | 4 | 4 | 3 | 2 | ❓ |
| 24 | Deep Latents Long Memory | 17 | 4 | 3 | 5 | 3 | 2 | ❓ |
| 25 | Fuse-All MoE | 17 | 3 | 5 | 4 | 4 | 1 | ❌ |
| 26 | MDU | 17 | 3 | 4 | 4 | 4 | 3 | ❓ |
| 27 | TreeAgent | 16 | 3 | 4 | 4 | 3 | 2 | ❓ |
| 28 | Cog Mapping of LbT | 16 | 4 | 3 | 5 | 3 | 1 | ❌ |
| 29 | MMDM | 16 | 3 | 4 | 3 | 3 | 3 | ❓ |
| 30 | MPPA | 16 | 4 | 3 | 4 | 2 | 3 | ❓ |
| 31 | AstroMemBench | 16 | 3 | 3 | 3 | 3 | 4 | ✅ |
| 32 | Agent-as-a-Judge | 15 | 3 | 4 | 4 | 3 | 1 | ❌ |
| 33 | RAG-FGO | 15 | 3 | 4 | 3 | 3 | 2 | ❓ |
| 34 | Edge-Native RAG | 14 | 3 | 4 | 3 | 2 | 2 | ❓ |

---

## 📊 本周趋势观察

1. **Agent 记忆研究爆发**：本周 6+ 篇论文聚焦长期记忆（MIGRO / DISCERN / MemCredit / Folio / TreeAgent / AstroMemBench），核心分歧点从"怎么检索"转向"写入时保留什么、读取时消解什么"
2. **轨迹膨胀问题被正式化**：Outcome-Mass Alignment 指出多轮 Agent RL 中失败轨迹膨胀导致隐式加权偏差，Agent RL 训练细节开始被仔细审计
3. **可解释性进入 Agent 时代**：机制可解释性工具首次系统应用于 Web Agent 失败分析，探针预测幻觉 + 方向修正的路线可行但脆弱
4. **RAG 压缩进入像素空间**：OpticalRAG 用视觉编码器绕开 token 瓶颈，16 个注入 token 的极端压缩比
5. **模型身份安全新攻击面**：Contagious Fingerprints 揭示 API 中继欺诈检测的新漏洞
6. **AI 审稿系统性偏置**：AI Reviews Are Biased Towards the Appendix 揭示 LLM 审稿对附录的异常依赖，影响学术评审流程
