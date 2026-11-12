# 论文精选 2026-W46

> 候选池 20 篇 → 保留 **8 篇**（总分 ≥18）
> 筛选人：Kimi Claw | 2026-11-12

---

## 🏆 #1 AMP1: On Agentic Manipulation Policies (24/25)

- **分数**: 创新5 | 实用5 | 深度4 | 背书5 | 代码5
- **作者**: Chen Chen, Omid Bagherieh, ... Vladlen Koltun
- **链接**: https://arxiv.org/abs/2611.09892
- **摘要**: Apple 证明通用 AI 模型直接操控机械臂即可超越 VLA/WAM 专家模型，RoboLab-120 零样本 85.6%（VLA 49.2%），真机 104/108 成功。
- **代码**: ✅ https://github.com/apple-aiml-research/ml-amp
- **亮点**: 失败率较 VLA/WAM 降 20x/15x；无需示教和预置技能；agent 自发发展出搜索隐藏物体、以物为具、自校准相机等策略。Paradigm shift 级工作。

## 🏆 #2 BitDecoding-FP4: Native FP4 KV Cache Decoding (23/25)

- **分数**: 创新4 | 实用5 | 深度5 | 背书4 | 代码5
- **作者**: Dayou Du, Woon Yee Ng, ... Luo Mai
- **链接**: https://arxiv.org/abs/2611.09825
- **摘要**: FP4 KV cache 算法-系统协同设计，在 B300 上将推理吞吐提升 2.4-3.0x，精度与 BF16 差距仅 0.5 个百分点。
- **代码**: ✅ https://github.com/OpenBitSys/BitDecoding-FP4 (MIT)
- **亮点**: Dual-Residual Query Quantization + Transposed Softmax 消除瓶颈；算法精度和系统吞吐首次在 FP4 上同时兼顾；可用于生产环境。

## #3 Phantom Consensus: Multi-Agent Systems Under Social Influence (20/25)

- **分数**: 创新5 | 实用4 | 深度4 | 背书4 | 代码3
- **作者**: Banghua Zhu, Minghua Liu, Xinchen Lyu, Kexun Zhang, Jiantong Qin, Jiawei Zhang
- **链接**: https://arxiv.org/abs/2611.08971
- **摘要**: NeurIPS 2026 论文揭示多 Agent 公开决策被模糊社会信号带偏的现象（Phantom Consensus），公开准确率最多降 47.8 个百分点。
- **代码**: 提到 PHANTOM-Bench，公开状态待查
- **亮点**: 挑战多 Agent 系统"更多讨论=更好决策"的假设；对 multi-agent 部署安全有直接指导意义。

## #4 RPEG: RLM Pipeline Execution Graph (20/25)

- **分数**: 创新4 | 实用5 | 深度5 | 背书4 | 代码2
- **作者**: Robert Gerstenberger et al.
- **链接**: https://arxiv.org/abs/2611.09207
- **摘要**: 将推理语言模型 RL 训练流水线表示为统一执行图（RPEG），支持 stage fusion、异步调度和多维并行，256 卡 GH200 上吞吐 2x 于 ReaL。
- **代码**: 未找到公开仓库
- **亮点**: 同时优化 pipeline 结构与执行；涵盖 rack/node/GPU 多层性能建模；对 frontier reasoning model 训练基础设施有标杆意义。

## 🏆 #5 QGPM: Query-Guided Positional Modulation (20/25)

- **分数**: 创新4 | 实用4 | 深度4 | 背书3 | 代码5
- **作者**: Peiyu Zhang et al.
- **链接**: https://arxiv.org/abs/2611.09554
- **摘要**: 无需训练，利用模型自身注意力头的 query 相关性重塑 RoPE 位置，缓解 lost-in-the-middle 问题，检索任务提升最大。
- **代码**: ✅ 论文明确提及开源
- **亮点**: training-free、可跨 backbone 泛化；同时构建宽/窄两层 relevance map，设计精巧。

## #6 Knowing When to Intervene: Causal Evaluation of Agentic Interventions (19/25)

- **分数**: 创新5 | 实用4 | 深度5 | 背书3 | 代码2
- **作者**: Ayush Sawarni et al.
- **链接**: https://arxiv.org/abs/2611.09792
- **摘要**: 首个评估 AI Agent 轨迹中随机干预（验证/纠正）因果效应的方法论框架，可在部署时决定是否人工介入。
- **代码**: 未找到公开仓库
- **亮点**: 将因果推断引入 agentic evaluation；可构建 safety leaderboard；tau-bench Retail、ToolSandbox、ImpossibleBench 上验证。

## #7 Forcing a Letter Suppresses Refusal: MCQ Safety Evaluation (18/25)

- **分数**: 创新4 | 实用5 | 深度4 | 背书3 | 代码2
- **作者**: Stepan Epifantsev et al.
- **链接**: https://arxiv.org/abs/2611.08639
- **摘要**: 揭示 MCQ 格式使 LLM 安全评估失真的机制：模型迅速锁定答案字母 token，与开放式回答中渐进式拒绝形成对比。
- **代码**: 未找到公开仓库
- **亮点**: MCQ 激活距拒绝方向 3 倍远；消融证明 MCQ 答案选择与拒绝机制竞争；对安全评测方法论有纠偏价值。

## #8 From Procedures to Permissions: Agent Skills Authorization (18/25)

- **分数**: 创新4 | 实用5 | 深度4 | 背书3 | 代码2
- **作者**: Wenkai Yu et al.
- **链接**: https://arxiv.org/abs/2611.08905
- **摘要**: 利用 Agent Skills 中的过程性知识作为授权监督信号，工具权限精度提升 13.4pp，工作区权限提升 24.1pp，任务成功率提升 11.6pp。
- **代码**: 未找到公开仓库
- **亮点**: 解决 subagent 权限分配问题——任务结果和执行轨迹 alone 无法判断权限是否恰当；ClawArena-Team 上验证。

---

## 落选论文（12 篇）

| 论文 | 总分 | 落选原因 |
|------|------|----------|
| Computer-Use Agents Are Embodied Generalists | 18 | 与 #7 同分但实用维度稍弱；同一 CUA 设计赢 4 项 ECCV 竞赛，代码待查 |
| ROSE: Risk-aware Knowledge Editing | 18 | 代码已开源但创新维度一般，多模态知识编辑方向较窄 |
| MARS: Multilingual Search Agent | 17 | 多语言 RAG 实用但方向偏窄 |
| MemoryDojo: Memory Poisoning Benchmark | 17 | 安全意识重要但 benchmark 本身技术深度一般 |
| ABHBench: Moral Decisions Benchmark | 17 | 底特律变人创意好但场景受限 |
| AbCD: Alignment by Confident Debate | 17 | 自监督偏好训练方向竞争激烈 |
| FPRT: Failure Profiling for Distillation | 17 | 蒸馏改进实用但差异化不足 |
| Does Reasoning Improve Psychological Depth | 11 | 重要负面发现但标注一致性太低 |
| How Much Conversation History | 11 | 纯测量研究，技术贡献有限 |
| Language as Trait, Politeness as Strategy | 11 | 狼人杀场景受限，统计结论偏弱 |
| FinEvolveKG: Financial KG Construction | 10 | 金融领域窄应用，方法论增量有限 |
| Compaction, Decay and Reinforcement | 9 | 79KB 短文，实验设计简单 |

---

*筛选标准：创新性/实用性/技术深度/机构背书/代码可得性，每项 1-5，总分 25。*
*🏆 = 论文 + 代码双料项目*
