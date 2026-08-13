# 📄 本周论文精选短名单（2026-W33）

> 精选时间：2026-08-13
> 来源：paper-pool-2026-W33.md（31篇候选）
> 筛选标准：创新性×技术深度×实用性×实验验证×清晰度，每项1-5分，总分25分
> 保留：8篇（总分≥21）

---

## 🏆 Top 1 | Skaling Law: Generalized Neural Scaling Law with Interaction Exponent
- **arXiv**: https://arxiv.org/abs/2608.07222
- **标签**: `Scaling Law` `Training` `Efficiency`
- **中文摘要**: 通过单一交互指数耦合模型容量与数据量，将MAPE降低1.5-3倍，可用10倍更少算力准确预测全网格性能。
- **评估打分**:
  | 创新性 | 技术深度 | 实用性 | 实验验证 | 清晰度 | **总分** |
  |--------|----------|--------|----------|--------|----------|
  | 5      | 5        | 5      | 4        | 5      | **24**   |
- **开源代码**: 未明确提及
- **入选理由**: 缩放律是LLM训练的基础设施级问题，本文的交互指数扩展形式优美且实用，对资源分配有直接影响。

---

## 🏆 Top 2 | Sharding Prevents LLM Oversight Failures and Adversarial Exploitation
- **arXiv**: https://arxiv.org/abs/2608.06422
- **标签**: `Safety` `LLM Judge` `Adversarial`
- **中文摘要**: 发现单次调用返回多verdict时LLM judge性能下降，提出分片策略将要求分组并行判断，弱judge可胜强judge。
- **评估打分**:
  | 创新性 | 技术深度 | 实用性 | 实验验证 | 清晰度 | **总分** |
  |--------|----------|--------|----------|--------|----------|
  | 5      | 4        | 5      | 5        | 5      | **24**   |
- **开源代码**: 未明确提及
- **入选理由**: 跨领域（研究复制/法律/临床试验）验证，对抗性测试充分，为LLM-as-a-Judge的安全性提供了立即可用的策略。

---

## 🏆 Top 3 | Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Document-Search (READ)
- **arXiv**: https://arxiv.org/abs/2608.06305
- **标签**: `RAG` `Agent` `Document Search` `MCP`
- **中文摘要**: 在780页政府财报上，传统稠密检索仅15.7%准确率，READ通过MCP暴露的确定性操作达58.8%，轨迹可审计。
- **评估打分**:
  | 创新性 | 技术深度 | 实用性 | 实验验证 | 清晰度 | **总分** |
  |--------|----------|--------|----------|--------|----------|
  | 5      | 4        | 5      | 5        | 5      | **24**   |
- **开源代码**: 未明确提及
- **入选理由**: 对结构化长文档RAG提出根本性质疑，MCP+确定性操作的组合设计精巧，统计检验严格，实际落地价值高。

---

## 🏆 Top 4 | TEXAS: Task-Expert-Aware Supervision for Downstream Mixture-of-Experts LLM Adaptation
- **arXiv**: https://arxiv.org/abs/2608.06396
- **标签**: `MoE` `Fine-tuning` `Task Adaptation`
- **中文摘要**: 通过正确性条件任务专家发现+令牌级监督分配，在18个设置中的17个达到最佳性能，平均提升1.3-1.5分。
- **评估打分**:
  | 创新性 | 技术深度 | 实用性 | 实验验证 | 清晰度 | **总分** |
  |--------|----------|--------|----------|--------|----------|
  | 4      | 4        | 5      | 5        | 4      | **22**   |
- **开源代码**: 未明确提及
- **入选理由**: MoE下游适应是工业界痛点，TEXAS不限制专家子集、不施加目标路由分布，方法优雅且普适性强。

---

## 🏆 Top 5 | FutureBridge: Token-Level LLM-SLM Collaboration
- **arXiv**: https://arxiv.org/abs/2608.06819
- **标签**: `LLM` `SLM` `Collaboration` `Reasoning`
- **中文摘要**: 不依赖LLM局部偏好，而是评估候选令牌对SLM后续推理的支持程度来进行联合排名，Qwen3-1.7B数学平均提升35.1%。
- **评估打分**:
  | 创新性 | 技术深度 | 实用性 | 实验验证 | 清晰度 | **总分** |
  |--------|----------|--------|----------|--------|----------|
  | 5      | 4        | 5      | 4        | 4      | **22**   |
- **开源代码**: 未明确提及
- **入选理由**: Token级协作的新范式——不以LLM为中心而以SLM的后续推理为中心，对边缘部署场景极具价值。

---

## 🏆 Top 6 | CreativeInstruct: Scalably Teaching LLMs to Balance Quality, Creativity, and Diversity
- **arXiv**: https://arxiv.org/abs/2608.07460
- **标签**: `Creativity` `Instruction Tuning` `RL`
- **中文摘要**: 通过注入[StartCreativity]跨度显式标注创造性区域，在保持质量的同时恢复多样性，人类评估70.3%认为更具创造性。
- **评估打分**:
  | 创新性 | 技术深度 | 实用性 | 实验验证 | 清晰度 | **总分** |
  |--------|----------|--------|----------|--------|----------|
  | 4      | 4        | 5      | 5        | 4      | **22**   |
- **开源代码**: 未明确提及
- **入选理由**: 后训练普遍牺牲创造性，本文用轻量级的跨度注入解决，且证明创造性基座对RL有额外收益（AMC+4%，MATH+5%）。

---

## 🏆 Top 7 | ADIAS: Automated Design of Interactive Agentic Systems
- **arXiv**: https://arxiv.org/abs/2608.06410
- **标签**: `Agent` `AutoML` `System Design`
- **中文摘要**: 以问题为中心的自动化Agent设计框架，用持久化问题状态替代候选中心策略，在5个交互基准上平均提升25.2%。
- **评估打分**:
  | 创新性 | 技术深度 | 实用性 | 实验验证 | 清晰度 | **总分** |
  |--------|----------|--------|----------|--------|----------|
  | 5      | 4        | 4      | 4        | 4      | **21**   |
- **开源代码**: 未明确提及
- **入选理由**: Agent设计自动化是减少手工prompt工程的关键方向，持久化问题状态的思路对迭代优化范式有启发意义。

---

## 🏆 Top 8 | Latent Fact-Checking: Detecting Misinformation through Activation Engineering ⭐双料
- **arXiv**: https://arxiv.org/abs/2608.06417
- **标签**: `Interpretability` `Safety` `Misinformation`
- **中文摘要**: 通过对比激活工程在残差流中提取虚假方向，无需微调或外部检索即可检测错误信息，跨11个模型验证有效。
- **评估打分**:
  | 创新性 | 技术深度 | 实用性 | 实验验证 | 清晰度 | **总分** |
  |--------|----------|--------|----------|--------|----------|
  | 4      | 4        | 4      | 4        | 4      | **21**   |
- **开源代码**: ✅ 明确可用（arXiv页声明"Code is available"）
- **入选理由**: 可解释性与安全性的交汇点，激活工程方法轻量且可复现，为事实核查提供了不依赖外部检索的新路径。

---

## 📊 落选的亮点论文（ honorable mention ）

| 排名 | 论文 | 总分 | 未入选原因 |
|------|------|------|-----------|
| 9 | Two-Hop Generalization in Transformers | 22 | 偏理论，机制分析虽深但即时应用性较弱 |
| 10 | Visual RAG for Diffusion Language Models (⭐有代码) | 22 | 领域较窄（扩散语言模型），与Top 3 RAG方向重复 |
| 11 | CoinRAG: Contextualized Information Nugget KV Cache Reuse | 21 | 与Top 3同属RAG效率方向，READ更具突破性 |
| 12 | PHASE-Tree: Multi-Timescale Character State Tree | 21 | Agent记忆方向，与ADIAS同属Agent设计，ADIAS更普适 |
| 13 | EntropyMoE: Entropy-Aware Sparse Expert Routing | 20 | MoE方向，TEXAS更全面 |
| 14 | Autonomy-of-Heads (AoH) | 20 | 注意力头诊断，技术扎实但应用场景相对有限 |

---

## 📈 本周趋势总结

**最强信号：**
- **安全与评估**成为独立赛道：Sharding（judge安全）+ Latent Fact-Checking（激活工程检测）同时入选
- **MoE架构**进入实用阶段：从路由优化（EntropyMoE）到下游适应（TEXAS），工业落地加速
- **Agent设计**范式转移：从候选中心（ADIAS）到问题中心，从静态记忆（PHASE-Tree）到动态演进

**值得关注：**
- Skaling Law的交互指数可能改变小规模实验到大规模训练的传统方法论
- FutureBridge的"以SLM为中心"的协作范式，可能比单纯的模型蒸馏更适合资源受限场景
- READ对稠密检索的根本质疑——在结构化长文档上，embedding可能不是最优解

---

*精选完成时间: 2026-08-13 14:00 CST | 共评估31篇，入选8篇，1篇确认开源代码*
