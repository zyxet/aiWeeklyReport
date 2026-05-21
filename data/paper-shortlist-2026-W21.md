# 📄 2026-W21 论文精选候选列表（8篇）

> 精选日期：2026-05-21（周四）| 来源池：42篇候选 | 筛选标准：总分排序 + 领域均衡
> 评分维度：创新性(5) + 实用性(5) + 技术深度(5) + 机构背书(5) + 代码可得性(5) = 总分25

---

## 🥇 1. DimMem: Dimensional Memory Framework for LLM Agents

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.15759](https://arxiv.org/abs/2605.15759) |
| **作者** | Wentao Qiu et al. |
| **机构** | 未明确 |
| **领域** | Agent Memory |

**一句话摘要（50字内）**：将Agent记忆原子化为带显式维度字段的结构化单元，实现精准检索与低成本更新，4B提取器超越GPT-4.1-mini。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 4 | 维度化记忆结构是Agent记忆的新范式，原子化单元设计精巧 |
| 实用性 | 5 | LoCoMo-10达81.43%，per-query token降24%，直接可部署 |
| 技术深度 | 4 | 维度感知检索+学习化提取，多基准验证充分 |
| 机构背书 | 2 | 作者机构未明确 |
| 代码可得性 | **5** | **GitHub开源** ✅ [ChowRunFa/DimMem](https://github.com/ChowRunFa/DimMem) |
| **总分** | **20** | ⭐ 本周最高分 |

**代码关联**：🟢 **论文+代码双料项目** — GitHub仓库已公开，含完整实现。

---

## 🥈 2. Argus: Evidence Assembly for Scalable Deep Research Agents

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.16217](https://arxiv.org/abs/2605.16217) |
| **作者** | Zhen Zhang et al. |
| **机构** | 未明确（35B-A3B MoE backbone暗示工业界背景） |
| **领域** | Deep Research / Agent |

**一句话摘要（50字内）**：Searcher-Navigator协作将深度研究视为拼图组装，64 Searcher在BrowseComp达86.2分，首超所有闭源Agent。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 5 | 拼图式证据组装 vs 并行暴力搜索，范式级创新 |
| 实用性 | 5 | BrowseComp 86.2超越闭源，上下文控在21.5K，可直接产品化 |
| 技术深度 | 4 | RL训练Navigator，独立训练Searcher，MoE backbone |
| 机构背书 | 3 | 模型规模暗示资源充足的团队 |
| 代码可得性 | 1 | 未提及开源 |
| **总分** | **18** | |

**代码关联**：⚪ 未检测到公开代码。

---

## 🥉 3. RecMem: Recurrence-Based Memory Consolidation for Long-Running Agents

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.16045](https://arxiv.org/abs/2605.16045) |
| **作者** | Zijie Dai et al. |
| **机构** | ACL 2026 Findings 已接受 |
| **领域** | Agent Memory / Efficiency |

**一句话摘要（50字内）**：潜意识记忆层+轻量嵌入模型，仅在语义相似交互持续recurrence时触发LLM提取，省87% token成本且精度超SOTA。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 4 | recurrence触发consolidation是新的记忆管理哲学 |
| 实用性 | 5 | 87%成本削减+精度提升，对长运行Agent是刚需 |
| 技术深度 | 4 | ACL Findings接受，语义精炼机制完整 |
| 机构背书 | 3 | 顶会接受背书 |
| 代码可得性 | 1 | 未提及开源 |
| **总分** | **17** | |

**代码关联**：⚪ 未检测到公开代码。

---

## 4. NCCE: Neural Collaborative Context Engineering

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.15721](https://arxiv.org/abs/2605.15721) |
| **作者** | Jiachen Zhu, Weinan Zhang, Jianghao Lin, Yong Yu et al. |
| **机构** | 上海交通大学（Yong Yu / Weinan Zhang组） |
| **领域** | Prompt Engineering / Context Engineering |

**一句话摘要（50字内）**：将上下文工程重铸为推荐问题，通过神经协同过滤实现实例级动态路由，为每个输入匹配最优上下文策略。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 4 | Context-as-Recommendation范式转换，Context-CF Co-Evolution |
| 实用性 | 4 | 实例级性能提升，NCF轻量可部署 |
| 技术深度 | 4 | 理论证明+协同进化机制，实验覆盖全面 |
| 机构背书 | 4 | 上海交大，国内NLP强组 |
| 代码可得性 | 1 | 未提及开源 |
| **总分** | **17** | |

**代码关联**：⚪ 未检测到公开代码。

---

## 5. FishBack: Pullback Fisher Geometry for Activation Steering

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.17231](https://arxiv.org/abs/2605.17231) |
| **作者** | Sihan Wang et al. |
| **机构** | 未明确 |
| **领域** | Mechanistic Interpretability / Geometry |

**一句话摘要（50字内）**：揭示激活空间Fisher度量与欧氏空间偏离超97%，推导出闭合形式最优导向方程，迭代steering全面超越CAA等基线。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 5 | 微分几何视角切入激活导向，统一解释现有所有方法 |
| 实用性 | 3 | 当前仅在GPT-2验证，大规模模型部署待验证 |
| 技术深度 | 5 | 闭合形式推导，层递归分解，谱诊断预测性能差距 |
| 机构背书 | 2 | 独立研究者 |
| 代码可得性 | 1 | 未提及开源 |
| **总分** | **16** | |

**代码关联**：⚪ 未检测到公开代码。

---

## 6. Block Attention with Semantic Segmentation and Block Distillation

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.15913](https://arxiv.org/abs/2605.15913) |
| **作者** | Shuaiyi Li et al. |
| **机构** | 未明确 |
| **领域** | RAG / Long Context / Attention |

**一句话摘要（50字内）**：构建30k+语义分割数据集训练轻量分割器，块蒸馏框架以冻结全注意力教师指导块注意力学生，近全注意力性能。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 4 | 自动语义分割+块蒸馏组合，解决Block Attention两大瓶颈 |
| 实用性 | 5 | KV缓存复用是RAG核心痛点，方案可直接集成 |
| 技术深度 | 4 | block sink tokens / dropout / token-level weighting三组件 |
| 机构背书 | 2 | 独立研究者 |
| 代码可得性 | 1 | 未提及开源 |
| **总分** | **16** | |

**代码关联**：⚪ 未检测到公开代码。

---

## 7. CSR: Calibrating LLMs with Semantic-level Reward

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.15588](https://arxiv.org/abs/2605.15588) |
| **作者** | Ruijia Niu et al. |
| **机构** | 未明确 |
| **领域** | LLM Calibration / Alignment |

**一句话摘要（50字内）**：在语义空间直接校准LLM不确定性，无需语言化置信度接口，ECE降40%、AUROC升31%，跨分布鲁棒泛化。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 4 | 语义空间校准替代token级verbalized confidence |
| 实用性 | 4 | 医疗/法律等高后果场景亟需校准，四设置泛化验证 |
| 技术深度 | 4 | 正确性奖励+语义校准奖励双信号设计 |
| 机构背书 | 2 | 独立研究者 |
| 代码可得性 | 1 | 未提及开源 |
| **总分** | **15** | |

**代码关联**：⚪ 未检测到公开代码。

---

## 8. ASRU: Activation-Redirected Safe Removal for MLLMs

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.15687](https://arxiv.org/abs/2605.15687) |
| **作者** | Jiahui Guang et al. |
| **机构** | 未明确 |
| **领域** | MLLM Safety / Machine Unlearning |

**一句话摘要（50字内）**：通过激活重定向诱导拒绝行为再优化细粒度拒绝边界，Qwen3-VL上遗忘效果+24.6%且生成质量提升5.8倍。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 4 | 激活重定向+RL优化拒绝边界，多模态遗忘新框架 |
| 实用性 | 4 | Qwen3-VL实测，少量保留数据即可，安全部署刚需 |
| 技术深度 | 4 | 三目标平衡（遗忘/质量/效用），激活层面机制设计 |
| 机构背书 | 2 | 独立研究者 |
| 代码可得性 | 1 | 未提及开源 |
| **总分** | **15** | |

**代码关联**：⚪ 未检测到公开代码。

---

## 📊 本周精选汇总

| 排名 | 论文 | 总分 | 核心亮点 | 代码 |
|------|------|------|----------|------|
| 1 | DimMem | 20 | 维度化Agent记忆，4B超GPT-4.1-mini | ✅ 开源 |
| 2 | Argus | 18 | 拼图式深度研究，首超闭源Agent | — |
| 3 | RecMem | 17 | 省87% token的记忆consolidation | — |
| 4 | NCCE | 17 | 上下文工程即推荐，实例级路由 | — |
| 5 | FishBack | 16 | Fisher几何重塑激活导向理论 | — |
| 6 | Block Attention | 16 | 语义分割+块蒸馏解决KV缓存 | — |
| 7 | CSR | 15 | 语义空间校准，ECE降40% | — |
| 8 | ASRU | 15 | 激活重定向实现可控多模态遗忘 | — |

**领域分布**：Agent(3) · Mech-Interp(1) · RAG/Long Context(1) · Alignment(2) · Safety(1)

**代码双料项目**：1/8（DimMem）— 本周开源比例偏低，多数高质量工作尚未释放代码。

---

*精选人：Kimi Claw | 2026-W21 | 待用户确认*
