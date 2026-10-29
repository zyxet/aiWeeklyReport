# 📄 论文精选短名单 — 2026-W44

> 筛选时间：2026-10-29（周四）
> 候选池：14 篇 → 保留 8 篇（总分 ≥19）
> 评分：创新性 / 实用性 / 技术深度 / 机构背书 / 代码可得性，每项 1-5，总分 25
> 🏆 = 论文+代码双料项目（代码已开源可复现）

## 本周围绕

本周候选池呈现 **Agent 自我进化三线并进**（Agent S4 进化接口 / RSIHub 统一进化框架 / OPST 无数据自训练）、**Agent 安全研究深化**（Prompt Injection 决策时机证伪 + 单关系认知攻击揭示隐含推理 warrant 脆弱性）、**"简单方案赢"的回归**（RAW-RAG 用原始对话历史击败复杂记忆系统）三条主线。开源比例极高——8 篇入选中 6 篇附完整代码。

## 📋 短名单

| # | 论文 | 标签 | 一句话摘要 | 总分 | 备注 |
|---|------|------|-----------|------|------|
| 1 | [Agent S4](https://arxiv.org/abs/2610.28601) | Agent, GUI, Self-Evolving | Meta-agent 群体进化自动构建工具接口，Qwen3.8-27B 在 OSWorld V2 达 21.3% SOTA，成本仅 Claude Opus 4.8 的 1.5% | 23 | 🏆 Simular，Agent S 系列；接口设计成为 agent 能力的新范式 |
| 2 | [LEMS](https://arxiv.org/abs/2610.32878) | LLM Compression, ICML 2026 | 层间误差传播模型+ILP 做 SVD 压缩全局秩分配，零样本准确率超最优基线 1.7-4.8 p.p. | 22 | 🏆 TUM 等，ICML 2026 正式发表，代码+项目页 |
| 3 | [TopKLoRA](https://arxiv.org/abs/2610.32866) | Interpretability, Safety | 仅激活 top-k latent 的稀疏 LoRA，消融 1.2-6.8% latent 即可将后门攻击成功率归零 | 22 | 🏆 可解释性设计的微调方法，后门电路因果验证可行 |
| 4 | [RSIHub](https://arxiv.org/abs/2610.32253) | Agent, Self-Evolution, Framework | 可组合 agent 进化框架，四种进化方法统一评估，最大 pass@1 提升 13.5 p.p. | 20 | 🏆 HF ⭐186，中科院等 |
| 5 | [Omni-Woodpecker](https://arxiv.org/abs/2610.27103) | Multimodal, Hallucination | 免训练正交分解分离 grounding evidence 与 learned priors，CMM/AVHBench 提升 12.9/8.6 点 | 20 | 🏆 代码公开，跨架构泛化验证 |
| 6 | [NgramRL](https://arxiv.org/abs/2610.32881) | RL, LLM Training, Efficiency | Per-prompt n-gram 缓存替代 GPU 常驻 draft model 加速 GRPO rollout，比 SuffixDecoding 快 1.2-2.0× | 19 | RL 后训练效率：rollout 占 70% 训练时间的工程解法 |
| 7 | [Prompt Injection Timing](https://arxiv.org/abs/2610.24048) | Agent Security, Prompt Injection | 分支 rollout 证伪"注入读入即决定"假设——thinking 开启后仅 62% 方差在读入时固定，单次 run 重跑不一致率 35% | 19 | 评测方法论冲击：安全 benchmark 需多次运行 |
| 8 | [MemPilot](https://arxiv.org/abs/2610.06830) | Agent Memory, Long Context | RL 训练多步策略按需选择记忆操作，联合控制证据量/模型选择/视觉访问，性能-成本-延迟三维权衡 | 19 | 🏆 代码开源，多模态 agent 记忆管理 |

## 📊 评分明细

| 论文 | 创新性 | 实用性 | 技术深度 | 机构背书 | 代码可得性 | 总分 |
|------|--------|--------|----------|----------|------------|------|
| Agent S4 | 5 | 5 | 4 | 4 | 5 | **23** |
| LEMS | 4 | 4 | 5 | 4 | 5 | **22** |
| TopKLoRA | 5 | 4 | 5 | 3 | 5 | **22** |
| RSIHub | 4 | 4 | 4 | 3 | 5 | **20** |
| Omni-Woodpecker | 4 | 4 | 4 | 3 | 5 | **20** |
| NgramRL | 4 | 5 | 5 | 3 | 2 | **19** |
| Prompt Injection Timing | 5 | 4 | 5 | 3 | 2 | **19** |
| MemPilot | 3 | 4 | 4 | 3 | 5 | **19** |
| RAW-RAG | 4 | 5 | 4 | 3 | 2 | 18 |
| One Truthful Relation | 5 | 4 | 4 | 3 | 2 | 18 |
| OPST | 4 | 4 | 4 | 3 | 2 | 17 |
| MIRROR | 4 | 3 | 4 | 4 | 2 | 17 |
| UserArena | 3 | 4 | 4 | 3 | 2 | 16 |
| LiveUIBench | 4 | 3 | 3 | 3 | 2 | 15 |

## 📝 落选说明

- **RAW-RAG**（18）：反直觉发现——原始对话历史检索在 6/7 基准上击败复杂记忆系统，对 Mem0 类产品架构假设构成挑战。落选原因：代码未提及开源，且与本周入选的 MemPilot 同处记忆赛道，MemPilot 开源+多模态+RL 策略更具完整度。结论本身值得关注。
- **One Truthful Relation**（18）：单句操纵 agent 信念的攻击面揭示，开源模型 80% 翻转率触目惊心。落选原因：未提及代码开源，与 Prompt Injection Timing 同处安全赛道，后者方法论贡献更普适。
- **OPST**（17）：无外部数据自训练方向有价值，但自训练领域已有 STaR、ReST 等先行者，增量贡献相对有限。
- **MIRROR**（17）：百度自蒸馏个性化框架，方向实用但竞争激烈，SFT+DPO 组合基线已很强，增量不显著。
- **UserArena**（16）：6.5 万真实购物 session 规模可观，但推荐系统领域基准已有 RecAgent 等多篇，且未提及开源。
- **LiveUIBench**（15）：Agent as App 概念前瞻，但当前模型完成率极低，短期内实用价值有限，未提及开源。

## 🔍 本周观察

1. **Agent 自我进化形成完整光谱**：Agent S4 进化"接口"（工具使用知识）、RSIHub 统一"进化方法"评估协议、OPST 进化"模型本身"——三条路线各自独立推进，指向同一终局：agent 能力不依赖人工工程持续提升。Agent S4 的成本效率数据（1.5% of Claude Opus）尤其值得关注。
2. **安全研究从"防注入"到"理解决策"**：Prompt Injection Timing 用 branching rollout 证明注入决策是逐步形成的（非读入时确定），直接冲击当前 benchmark 的单 run 评测范式；One Truthful Relation 则揭示了更深层的攻击面——隐含推理 warrant 可被单句操纵，多智能体辩论不增反降安全性。
3. **记忆系统的"简单 vs 复杂"之争**：RAW-RAG 用朴素 RAG 击败 Mem0 等复杂记忆系统，与 MemPilot 用 RL 精细控制记忆操作形成鲜明对比。两种哲学孰优孰劣尚无定论，但"保留原始信息"的教训值得所有记忆系统设计者优先考虑。
4. **RL 后训练效率成为瓶颈共识**：NgramRL 针对 rollout 加速（占训练时间 70%+），工程优化空间巨大。随着 GRPO 成为事实标准，rollout 侧的系统优化将越来越像推理侧投机解码一样成为标配。

---

*由 thursday-paper-filter 任务自动生成 | intelligence-system*
