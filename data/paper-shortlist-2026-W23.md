# 2026-W23 论文精选候选列表（8篇）

> **精选日期**: 2026-06-03（周四）| **来源池**: `paper-pool-2026-W23.md`（40篇候选）
> **筛选标准**: 总分排序 + 领域均衡 + 代码可得性优先
> **评分维度**: 创新性(5) + 实用性(5) + 技术深度(5) + 机构背书(5) + 代码可得性(5) = 总分25

---

## 🥇 1. Dr.LLM: Dynamic Layer Routing in LLMs

| 项目 | 内容 |
|------|------|
| **arXiv** | [2510.12773](https://arxiv.org/abs/2510.12773) |
| **标题** | Dr.LLM: Dynamic Layer Routing in LLMs |
| **领域** | LLM / Efficiency / Dynamic Routing / Inference |

**一句话摘要**：基于 MCTS 监督的逐层动态路由机制，在不改变模型架构的前提下实现高效 LLM 推理加速。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 5 | MCTS 监督的逐层动态路由，不改变架构即可加速，思路巧妙 |
| 实用性 | 5 | 不改变架构意味着现有模型可即插即用，部署门槛极低 |
| 技术深度 | 5 | MCTS 与 LLM 推理的结合需要扎实的强化学习和优化理论基础 |
| 机构背书 | 4 | 论文机构待确认，但技术深度足以说明团队实力 |
| 代码可得性 | 4 | 推理加速方向通常伴随开源实现，待验证 |
| **总分** | **23** | |

**为什么选**: 推理效率是 LLM 规模化部署的核心瓶颈。Dr.LLM 的"不改变架构"设计是最大亮点——现有模型无需重训即可受益，这是工程落地角度的最优解。MCTS 与动态路由的结合为推理优化开辟了新路径。

---

## 🥈 2. Representation Forcing for Bottleneck-Free Unified Multimodal Models

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.31604](https://arxiv.org/abs/2605.31604) |
| **标题** | Representation Forcing for Bottleneck-Free Unified Multimodal Models |
| **领域** | LLM / Multimodal / VLM / Representation Learning |

**一句话摘要**：提出表示强制技术，消除统一多模态模型中的信息瓶颈，提升视觉语言模型的表示效率。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 5 | "表示强制"是全新的技术概念，针对多模态模型的信息瓶颈痛点 |
| 实用性 | 4 | 多模态模型是当前最活跃的研究方向之一，表示效率提升直接影响性能 |
| 技术深度 | 5 | 表示学习理论扎实，瓶颈消除有明确的数学/工程路径 |
| 机构背书 | 4 | 论文机构待确认，但技术方向属于前沿热点 |
| 代码可得性 | 3 | 待验证是否有官方开源实现 |
| **总分** | **21** | |

**为什么选**: 多模态模型是 2026 年 LLM 领域的主航道，而信息瓶颈是制约其性能的关键瓶颈。"Representation Forcing"如果经得住复现验证，可能成为 VLM 架构设计的标准组件。

---

## 🥈 3. StateKV: Linear-Time Video Prefill for Long-Video VLMs

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.31597](https://arxiv.org/abs/2605.31597) |
| **标题** | StateKV: Linear-Time Video Prefill for Long-Video VLMs |
| **领域** | LLM / VLM / Long Context / Video / Efficiency |

**一句话摘要**：通过固定容量重要性递归状态实现长视频 VLM 的线性时间预填充，无需微调或架构改动即可超越滑动窗口近似方法。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 5 | 固定容量重要性递归状态，线性时间复杂度，长视频预填充的突破性思路 |
| 实用性 | 4 | 无需微调或架构改动，即插即用，部署友好 |
| 技术深度 | 5 | 递归状态设计 + 重要性采样，工程实现有挑战性 |
| 机构背书 | 4 | 论文机构待确认，技术深度支撑可信度 |
| 代码可得性 | 3 | 待验证 |
| **总分** | **21** | |

**为什么选**: 长视频理解是 VLM 从"能看图片"到"能看视频"的关键跃迁。StateKV 的线性时间预填充直接解决了长视频计算爆炸问题，且无需架构改动——这意味着现有 VLM 可立即受益。

---

## 🥈 4. Formal Methods Meet LLMs: Runtime Monitoring and Formal Constraints

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.16198](https://arxiv.org/abs/2605.16198) |
| **标题** | Formal Methods Meet LLMs: Runtime Monitoring and Formal Constraints |
| **领域** | LLM / Safety / Formal Methods / Runtime Monitoring / Agent |

**一句话摘要**：将形式化方法引入 LLM Agent 的运行时监控，构建基于形式化约束的 LLM Agent 控制层。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 5 | 形式化方法 + LLM 是跨领域融合，运行时监控属于安全关键方向 |
| 实用性 | 4 | 随着 Agent 进入生产环境，安全监控是刚需，但形式化方法门槛较高 |
| 技术深度 | 5 | 形式化约束的建模和验证需要深厚的理论功底 |
| 机构背书 | 4 | 论文机构待确认，安全方向通常有学术传统支撑 |
| 代码可得性 | 3 | 待验证 |
| **总分** | **21** | |

**为什么选**: Cisco 披露的供应链攻击和 prompt injection 漏洞说明 Agent 安全已进入实战阶段。形式化方法提供的数学级保证是其他安全手段（如规则过滤）无法替代的。这篇论文代表了"从启发式安全到形式化安全"的方法论升级。

---

## 🥉 5. TOBench: A Task-Oriented Omni-Modal Benchmark for Real-World Tool-Using Agents

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.16909](https://arxiv.org/abs/2605.16909) |
| **标题** | TOBench: A Task-Oriented Omni-Modal Benchmark for Real-World Tool-Using Agents |
| **领域** | Agent / Benchmark / Tool-Use / Multimodal |

**一句话摘要**：包含 100 个可执行任务、27 个 MCP 服务器和 324 个工具，用于端到端多模态工具使用 Agent 的闭环验证。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 4 | 端到端多模态工具使用基准，MCP 服务器集成是实用亮点 |
| 实用性 | 5 | 100 个可执行任务 + 324 个工具，可直接用于 Agent 评估 |
| 技术深度 | 4 | 基准设计方法论成熟，工具集成工程量大 |
| 机构背书 | 3 | 论文机构待确认 |
| 代码可得性 | 4 | 基准测试通常伴随完整开源实现 |
| **总分** | **20** | |

**为什么选**: Agent 评估基准正在从"答对题"转向"办成事"。TOBench 的 100 个可执行任务和 MCP 服务器集成使其成为最贴近真实世界的 Agent 评估工具之一。当社区需要验证 Agent 的 tool-use 能力时，这是首选基准。

---

## 🥉 6. OrchMAS: Orchestrated Reasoning with Multi Collaborative Heterogeneous Scientific Expert Structured Agents

| 项目 | 内容 |
|------|------|
| **arXiv** | [2603.03005](https://arxiv.org/abs/2603.03005) |
| **标题** | OrchMAS: Orchestrated Reasoning with Multi Collaborative Heterogeneous Scientific Expert Structured Agents |
| **领域** | Agent / Multi-Agent / Reasoning / Scientific / Heterogeneous |

**一句话摘要**：面向科学领域的双层多模型编排框架，通过动态构建领域感知推理管道和异构专家 Agent 协作，实现多步科学推理的动态重规划。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 5 | 双层编排 + 动态领域感知管道 + 异构专家协作，架构设计复杂且完整 |
| 实用性 | 4 | 科学领域推理是 Agent 的高价值场景，但框架成熟度待验证 |
| 技术深度 | 5 | 动态重规划 + 领域感知管道，多 Agent 编排的理论深度高 |
| 机构背书 | 3 | 论文机构待确认 |
| 代码可得性 | 3 | 待验证 |
| **总分** | **20** | |

**为什么选**: 多 Agent 编排是 2026 年 Agent 架构的主航道。OrchMAS 的"双层 + 异构 + 动态重规划"设计代表了科学领域 Agent 的架构前沿。当 Agent 从"单兵作战"走向"团队协作"时，编排框架的质量决定了整体效能上限。

---

## 🥉 7. Giving Sensors a Voice: Multimodal JEPA for Sensor Understanding

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.31580](https://arxiv.org/abs/2605.31580) |
| **标题** | Giving Sensors a Voice: Multimodal JEPA for Sensor Understanding |
| **领域** | LLM / Multimodal / JEPA / Sensor / VLM |

**一句话摘要**：将多模态 JEPA 架构扩展至传感器理解领域，为具身智能和物理世界交互提供统一的表示学习框架。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 5 | JEPA 架构扩展至传感器理解，具身智能方向的跨界创新 |
| 实用性 | 3 | 传感器理解是具身智能的基础，但距离消费级应用较远 |
| 技术深度 | 5 | JEPA (Joint Embedding Predictive Architecture) 理论基础扎实 |
| 机构背书 | 4 | 论文机构待确认，JEPA 方向通常有 Yann LeCun 等权威背书 |
| 代码可得性 | 3 | 待验证 |
| **总分** | **20** | |

**为什么选**: 具身智能是 AI 从"数字世界"走向"物理世界"的必经之路。JEPA 架构作为 LeCun 力推的世界模型范式，向传感器理解扩展是具身智能基础设施的关键一步。虽然距离消费级应用较远，但方向正确且理论扎实。

---

## 🥉 8. RoadmapBench: Evaluating Long-Horizon Agentic Software Development

| 项目 | 内容 |
|------|------|
| **arXiv** | [2605.15846](https://arxiv.org/abs/2605.15846) |
| **标题** | RoadmapBench: Evaluating Long-Horizon Agentic Software Development |
| **领域** | LLM / Agent / Software Development / Long-Horizon / Benchmark |

**一句话摘要**：包含 17 个代码仓库中 115 个真实版本升级的长程 Agent 软件开发基准。

| 评分项 | 得分 | 说明 |
|--------|------|------|
| 创新性 | 4 | 真实版本升级作为评估目标，比 synthetic task 更贴近生产 |
| 实用性 | 5 | 17 个真实仓库 + 115 个版本升级，可直接评估编码 Agent 能力 |
| 技术深度 | 4 | 基准设计方法论成熟，真实数据收集工程量大 |
| 机构背书 | 3 | 论文机构待确认 |
| 代码可得性 | 4 | 基准测试通常伴随完整开源实现 |
| **总分** | **20** | |

**为什么选**: 编码 Agent 是 2026 年最活跃的赛道之一（Claude Code / Codex / opencode / qwen-code / goose），但缺乏真实场景的长程评估基准。RoadmapBench 的 115 个真实版本升级使其成为编码 Agent 能力验证的"黄金标准"候选。

---

## 备选论文（未入选但值得追踪）

| 论文 | 总分 | 未入选原因 |
|------|------|----------|
| DecisionBench | 19 | 与 TOBench 同为 Agent 基准，TOBench 的多模态 + MCP 集成更贴近实际 |
| Strat-Reasoner | 19 | 多 Agent 博弈推理方向，与 OrchMAS 重叠，OrchMAS 的异构编排覆盖更广 |
| FORGE | 19 | 多步系统 Agent 架构，与 OrchMAS 和 GraphBit 重叠，差异化不足 |
| CHI-Bench | 20 | 医疗工作流 Agent 基准，领域专精但通用性不如 TOBench |
| Agentic RAG | 20 | 与 RAG 方向已有大量研究，创新密度不及 Representation Forcing |
| MCTS-Style Planning | 19 | 与 Dr.LLM 的 MCTS 应用重叠，Dr.LLM 的工程落地价值更高 |
| Sparse Credit Assignment | 19 | 推理可解释性方向，技术深度高但实用性相对弱 |
| ClawForge | 18 | Agent 评估基准，与 TOBench/RoadmapBench 重叠，数据不够差异化 |

---

## 领域分布

| 方向 | 入选数 | 论文 |
|------|--------|------|
| **效率/推理优化** | 2 | Dr.LLM, StateKV |
| **多模态/VLM** | 2 | Representation Forcing, Giving Sensors a Voice |
| **Agent 基准/评估** | 2 | TOBench, RoadmapBench |
| **Agent 编排/架构** | 1 | OrchMAS |
| **安全/形式化方法** | 1 | Formal Methods Meet LLMs |

---

## 本周趋势判断

1. **推理效率与长上下文仍是双主线**: Dr.LLM（动态层路由）和 StateKV（线性视频预填充）分别从"模型内部"和"输入处理"两个维度解决效率问题，说明推理优化已进入多路径并行阶段。

2. **多模态从"能看"走向"能感":** Representation Forcing（消除信息瓶颈）和 Giving Sensors a Voice（JEPA 扩展至传感器）代表了多模态模型从视觉向更广义感知（触觉、听觉、传感器）扩展的趋势。

3. **Agent 评估基准进入"真实场景"时代**: TOBench（100 个可执行任务）和 RoadmapBench（115 个真实版本升级）的共同点是"用真实数据替代 synthetic task"，这标志着 Agent 评估从学术界走向工业界的成熟度拐点。

4. **形式化安全是 Agent 生产的必要条件**: Formal Methods Meet LLMs 的入选反映了社区对 Agent 安全的重视升级。当 Agent 获得操作文件系统、调用 API、编写代码的能力时，形式化约束不再是"学术理想"而是"安全底线"。

---

> **人工介入点**: 论文短名单已生成，等待用户确认后继续周五论文-开源联动流程。
> 如有论文需要补充验证或调整优先级，请在此文件基础上批注。
