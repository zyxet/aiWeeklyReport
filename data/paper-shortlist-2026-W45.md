# 📄 论文精选短名单 — 2026-W45

> 筛选时间：2026-11-05（周四）
> 候选池：26 篇 → 保留 8 篇（总分 ≥19）
> 评分：创新性 / 实用性 / 技术深度 / 机构背书 / 代码可得性，每项 1-5，总分 25
> 🏆 = 论文+代码双料项目（代码已开源可复现）

## 本周围绕

本周候选池呈现 **超长上下文注意力的工程突破**（LSA 隐空间聚类 10M token / ZHA 树索引数亿 token 双双抵达亚二次复杂度实用区间）、**Agent 系统效率四面开花**（RoboArchitect 自动进化机器人 harness / Mage-VL-Cowork 4B 混合操作 / ASTC 免训练上下文压缩 / Flide 决策模型推理引擎）、**Agent 安全从论文走向武器库**（SecPO 代码+数据+模型三箭齐发）三条主线。开源比例维持高位——8 篇入选中 5 篇附完整代码与权重。

## 📋 短名单

| # | 论文 | 标签 | 一句话摘要 | 总分 | 备注 |
|---|------|------|-----------|------|------|
| 1 | [LSA](https://arxiv.org/abs/2610.42147) | Long Context, Attention, Systems | 隐空间层次聚类实现亚二次注意力，10M token 预填充加速 22.7 倍 | 24 | 🏆 Apache 2.0 + SGLang 插件 + 蒸馏权重全发布，Prefrontal AI / ETH |
| 2 | [RoboArchitect](https://arxiv.org/abs/2610.42141) | Robotics, Agent, Self-Evolving | 编码模型观察 rollout 自动为冻结机器人策略进化 harness，成功率 9.7%→43.3% | 24 | 🏆 Stanford，代码开源；harness 工程成为机器人 agent 新瓶颈 |
| 3 | [Mage-VL-Cowork](https://arxiv.org/abs/2610.40747) | Computer Use, Multimodal, Microsoft | 4B 混合 GUI+代码+终端 agent，OSWorld-Verified 66.0%，完整训练配方 | 23 | 🏆 Apache 2.0 + HF 权重，进化 harness 蒸馏 + 混合 RL |
| 4 | [SecPO](https://arxiv.org/abs/2610.41998) | Agent Security, Prompt Injection | 对抗训练防御提示注入，AgentDojo ASR 从 78.8% 降至 8.8%，实用性不降 | 23 | 🏆 UC Berkeley，代码+训练数据+模型三发布 |
| 5 | [ASTC](https://arxiv.org/abs/2610.41291) | Agent, Context Compression | 免训练利用 GDN 循环动态压缩 agent 上下文，减少 50.68% 注意力对 | 22 | 🏆 MIT 协议开源，AppWorld 可复现评估 |
| 6 | [ZHA](https://arxiv.org/abs/2610.42112) | Long Context, Attention | 树索引亚二次注意力，支持数亿 token 级超长上下文 | 21 | Zyphra，与 LSA 殊途同归：层次化稀疏选择 |
| 7 | [LARC](https://arxiv.org/abs/2610.42149) | Multimodal, Latent Reasoning, NeurIPS 2026 | 连续潜空间推理统一多模态生成，GenEval 超 BAGEL 7 个百分点 | 20 | NeurIPS 2026，潜空间推理从文本扩展到图像生成 |
| 8 | [Flide](https://arxiv.org/abs/2610.42148) | Inference Engine, Decision Models, Systems | ForkAttention 决策模型推理引擎，比 vLLM/SGLang 快 9.5 倍且数学精确 | 19 | 决策模型（Jev 类）专用推理栈的开山之作 |

## 📊 评分明细

| 论文 | 创新性 | 实用性 | 技术深度 | 机构背书 | 代码可得性 | 总分 |
|------|--------|--------|----------|----------|------------|------|
| LSA | 5 | 5 | 5 | 4 | 5 | **24** |
| RoboArchitect | 5 | 5 | 5 | 5 | 4 | **24** |
| Mage-VL-Cowork | 4 | 5 | 4 | 5 | 5 | **23** |
| SecPO | 4 | 5 | 4 | 5 | 5 | **23** |
| ASTC | 5 | 5 | 4 | 3 | 5 | **22** |
| ZHA | 5 | 4 | 5 | 4 | 3 | **21** |
| LARC | 5 | 4 | 5 | 4 | 2 | **20** |
| Flide | 4 | 5 | 5 | 3 | 2 | **19** |
| ACCT | 4 | 5 | 4 | 3 | 2 | 18 |
| CRoS | 4 | 4 | 4 | 3 | 2 | 17 |
| DAMI | 3 | 4 | 4 | 2 | 4 | 17 |
| DecisionRank | 4 | 4 | 4 | 3 | 2 | 17 |
| BYOD | 4 | 3 | 4 | 2 | 4 | 17 |
| ETAPS | 3 | 4 | 4 | 4 | 2 | 17 |
| Stepwise-Querying | 4 | 4 | 4 | 2 | 2 | 16 |
| BlindToChange | 4 | 3 | 3 | 3 | 3 | 16 |
| TVQ | 3 | 4 | 4 | 3 | 2 | 16 |
| Latent-Lens | 4 | 3 | 4 | 2 | 2 | 15 |
| GraphNIAH | 3 | 3 | 3 | 2 | 3 | 14 |
| UpLoop | 4 | 3 | 4 | 2 | 1 | 14 |
| No Free Loop | 3 | 3 | 3 | 3 | 1 | 13 |
| KEEPER | 3 | 3 | 3 | 2 | 1 | 12 |
| Reasoning Consistency | 3 | 2 | 3 | 3 | 1 | 12 |
| Activation Steering | 3 | 2 | 3 | 2 | 1 | 11 |
| RangeSWA | 3 | 2 | 3 | 2 | 1 | 11 |
| Task Vectors TR/TL | 3 | 2 | 3 | 2 | 1 | 11 |

## 📝 落选说明

- **ACCT**（18）：跨模型 KV 缓存迁移，75% 压缩 + 6.5-21.2x 加速，部署价值极高。落选原因：代码未确认开源，且 NVIDIA 2608.03893 已有类似 closed-form ridge 映射先行工作，ACCT 的增量贡献主要在跨层选择策略。
- **CRoS**（17）：打乱 CoT 顺序做因果奖励是 RLVR 奖励设计的有趣视角，OOD 46.8% 有说服力。落选原因：仅在 Gemma-3-4B 上验证，规模偏小，与本周主线关联度不够紧密。
- **DAMI**（17）：门控线性注意力初始化改进，RULER +5.29~16.71pp。落选原因：属于改进型工作（在已有 GLA 框架上做初始化优化），创新性相对有限，代码可得但增量不显著。
- **DecisionRank**（17）：1.7B 决策模型超越 27B 生成式 teacher，方向实用。落选原因：reranker 赛道竞争激烈（BGE、ColBERT 等），且代码未确认开源。
- **BYOD**（17）：LoRA-only 将 AR 模型转为扩散 LM，概念新颖且有代码。落选原因：扩散 LM 生成质量仍有明显差距（perplexity 8.3-11.1 vs LLaDA 4.1），短期内实用价值有限。
- **ETAPS**（17）：Inderjit Dhillon 组的极端稀疏剪枝，50-90% 稀疏度超 ELSA。落选原因：方向成熟（结构化剪枝已有很多工作），增量有限。
- **Stepwise-Querying**（16）：黑盒推理蒸馏不需 teacher CoT。落选原因：与已有 works（e.g., CoT-free distillation 系列）差异化不够清晰。
- **BlindToChange**（16）：agent 主动感知 benchmark，揭示最高 27.5 分差距。落选原因：benchmark 类论文本周已有 LSA/ZHA 等更重头的系统工程，落选但并非无价值。
- **其余论文**（≤16）：多为分析型或 niche 方向，与本周三条主线关联度较低。

## 🔍 本周观察

1. **超长上下文进入"亚二次实用时代"**：LSA 和 ZHA 从两个方向（隐空间聚类 vs 树索引）同时抵达了同一个结论——注意力稀疏选择的层次化是通往 10M+ token 的唯一可行路径。LSA 的 22.7x 加速是在 GLM-5.3-Flash 和 Qwen3.8-27B 这种生产级模型上测出的，不再是 toy-scale proof-of-concept。两者的开源策略也值得关注：LSA 发布了 SGLang 插件 + 蒸馏权重 + 训练代码。
2. **"Harness 工程"成为 agent 能力的新瓶颈**：RoboArchitect 证明编码模型可以为冻结的机器人策略自动设计 harness（成功率提升 4.5x），Mage-VL-Cowork 的"进化 harness"为 4B 模型蒸馏出 66% OSWorld 性能。两篇论文独立验证了同一件事：**agent 的能力上限不只在模型权重里，更在围绕它的工程结构里**。
3. **Agent 安全从"论文"到"武器库"**：SecPO 是本周安全方向唯一入选但分数极高的原因——它不只是一个防御方法，更是一套完整的对抗训练 pipeline（代码 + 训练数据 + 防御模型全发布，AgentDojo ASR 从 78.8% 砍到 8.8%）。这标志着 agent 安全研究从"证明问题存在"转向"提供可用工具"。
4. **效率即主线**：8 篇入选论文中 5 篇的核心贡献直接与推理效率相关（LSA 加速、ASTC 压缩、Flide 引擎、ZHA 亚二次、Mage-VL-Cowork 减少模型调用 13%）。在长上下文和多步 agent 的双重压力下，"更快"和"更省"已经不再是优化目标，而是产品可行性的前提。

---

*由 thursday-paper-filter 任务自动生成 | intelligence-system*
