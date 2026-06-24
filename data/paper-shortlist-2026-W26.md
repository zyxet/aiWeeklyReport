# 📄 论文精选短名单 — 2026-W26

> 精选时间：2026-06-24 15:30 CST
> 来源：候选池 paper-pool-2026-W26.md（11篇）
> 与开源项目联动：7个精选项目

---

## 精选论文（8篇）

### 1. GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents ⭐联动
- **编号**: 2606.20318 | **链接**: https://arxiv.org/abs/2606.20318
- **标签**: #Agent #Memory #MultiAgent #Governance
- **一句话**: 提出多主体共享内存 Agent 的记忆治理基准，评估不同权限主体间的内存访问控制与冲突解决机制。
- **为什么精选**: 这是本周最直接的开源-论文联动。GateMem 提出的"共享内存治理"恰好命中 **claude-mem**（77k⭐）和 **agentmemory**（14k⭐）的核心场景——多个 Agent 如何安全地共享和持久化记忆。论文中的权限冲突模型可为这两个项目的设计提供理论支撑。
- **联动项目**: claude-mem, agentmemory
- **联动方向**: 论文的内存治理框架 → 开源项目的跨会话记忆安全策略

---

### 2. 4-bit KV-Cache Compression for Context-Heavy Agent Workloads ⭐联动
- **编号**: 2606.20474 | **链接**: https://arxiv.org/abs/2606.20474
- **标签**: #LLM #Efficiency #KVCache #Agent
- **一句话**: 针对多轮 Agent 工作负载的上下文密集型特点，提出 4-bit KV 缓存压缩方案，显著降低推理内存占用。
- **为什么精选**: 与 **headroom**（44k⭐，LLM 输入压缩 60-95%）形成直接互补。headroom 压缩输入端，这篇压缩推理端的 KV 缓存，两者合起来构成 Agent 全链路 token 效率优化。成本敏感时代，这对组合的实际价值极高。
- **联动项目**: headroom
- **联动方向**: 论文 KV 压缩 + headroom 输入压缩 = Agent 端到端上下文优化

---

### 3. DataMagic: Multi-Agent Orchestration for Data Storytelling Videos ⭐联动
- **编号**: 2606.20388 | **链接**: https://arxiv.org/abs/2606.20388
- **标签**: #MultiAgent #DataVisualization #Orchestration
- **一句话**: 采用 Generate-then-Orchestrate 多 Agent 架构，将原始表格数据自动转换为叙事化数据洞察视频。
- **为什么精选**: 与 **OpenMontage**（8.5k⭐，首个开源 Agent 视频制作系统）形成完美对标。DataMagic 是学术界的"数据叙事视频 Agent"，OpenMontage 是工业界的"通用视频制作 Agent"，两者共享"多 Agent 管道编排"的核心架构。可以互相验证技术路线的可行性。
- **联动项目**: OpenMontage
- **联动方向**: 论文的 Generate-then-Orchestrate 架构 ↔ 开源项目的 12 管道 52 工具编排

---

### 4. WorldLines: Benchmarking Long-Horizon Stateful Embodied Agents ⭐联动
- **编号**: 2606.20325 | **链接**: https://arxiv.org/abs/2606.20325
- **标签**: #Agent #EmbodiedAI #LongHorizon #Benchmark
- **一句话**: 构建长时程状态化具身智能体基准测试，评估 Agent 在复杂环境中的长期规划与状态管理能力。
- **为什么精选**: 与 **deer-flow**（72k⭐，字节超级 Agent）的"子代理 + 记忆 + 沙箱"架构深度关联。deer-flow 的 long-horizon 任务执行能力需要类似 WorldLines 的基准来验证。论文中的状态管理评估指标可直接迁移到 deer-flow 的测试套件。
- **联动项目**: deer-flow
- **联动方向**: 论文的 long-horizon 基准 → 开源项目的子代理任务分解与状态持久化测试

---

### 5. Contagion Networks: LLM Evaluator Bias Propagation in Multi-Agent Systems
- **编号**: 2606.20493 | **链接**: https://arxiv.org/abs/2606.20493
- **标签**: #MultiAgent #LLM #Bias #Evaluation
- **一句话**: 揭示当 LLM 作为 multi-agent 系统评估器时，其系统性评估偏差会在 agent 网络中传播并放大。
- **为什么精选**:  multi-agent 系统的"评估偏差传染"是一个被严重低估的风险。deer-flow、OpenMontage 等任何多 Agent 架构都必须面对这个问题。论文提供了量化模型，提醒开源项目在编排层加入评估器轮换或交叉验证机制。
- **联动项目**: deer-flow, OpenMontage（间接）
- **联动方向**: 论文的偏差传播模型 → 多 Agent 系统的评估器健壮性设计

---

### 6. Re-Centering Humans in LLM Personalization
- **编号**: 2606.06614 | **链接**: https://arxiv.org/abs/2606.06614
- **标签**: #LLM #Personalization #HumanEvaluation #Alignment
- **一句话**: 通过 550 段人类对话揭示 LLM 个性化在真实数据上的局限：属性提取、相关性匹配和响应生成三阶段均与人类偏好存在显著差距。
- **为什么精选**: 直接挑战"记忆 = 个性化"的简单假设。claude-mem 和 agentmemory 存储的跨会话记忆，如果无法正确提取和匹配用户属性，反而可能产生错误的个性化。这篇论文提供了诊断框架，帮助记忆类项目避免"有记忆但用不好"的陷阱。
- **联动项目**: claude-mem, agentmemory（间接）
- **联动方向**: 论文的个性化局限诊断 → 记忆项目的用户属性提取与匹配策略优化

---

### 7. IFLLM: Implicit Feedback for LLM Alignment via Mouse Trajectories and Eye Gaze
- **编号**: 2606.20482 | **链接**: https://arxiv.org/abs/2606.20482
- **标签**: #LLM #Alignment #ImplicitFeedback #DPO
- **一句话**: 利用鼠标轨迹和眼动追踪收集隐式用户反馈，通过 DPO 对齐 LLM，无需显式标注即可提升响应质量。
- **为什么精选**: 代表了一种新的交互范式——从"显式反馈"转向"隐式反馈"。对 Agent 系统（尤其是 deer-flow、OpenMontage 这类面向终端用户的项目）来说，这意味着未来可以通过用户的自然操作（而非点击 thumbs up/down）来持续优化 Agent 行为。
- **联动项目**: deer-flow, OpenMontage（间接）
- **联动方向**: 论文的隐式反馈采集 → 开源项目的用户交互层设计

---

### 8. Agentic Symbolic Search (ASYS): PDE Theory Discovery via Differentiable Programs
- **编号**: 2606.20467 | **链接**: https://arxiv.org/abs/2606.20467
- **标签**: #Agent #ScientificDiscovery #Symbolic #PDE
- **一句话**: 构建 Agent 框架将 PDE 理论转化为可微符号程序，实现偏微分方程理论的自动搜索与验证。
- **为什么精选**: 展示了 Agent 在硬核科学发现中的潜力。与本周的"工程 Agent"（deer-flow、PowerAgentBench）形成对照——Agent 不仅是工具编排者，也可以是理论发现者。这种"符号推理 + 可微计算"的混合范式可能影响到 codegraph 这类代码知识图谱的推理方式。
- **联动项目**: codegraph（间接）
- **联动方向**: 论文的符号搜索范式 → 代码知识图谱的推理增强

---

## 未入选论文（3篇）

| 论文 | 原因 |
|------|------|
| PerceptionDLM (2606.20441) | 多模态扩散方向，与本周 Agent/记忆/效率主题关联较弱 |
| PowerAgentBench-Dyn (2606.20401) | 电力系统专用基准，垂直领域较窄，与开源项目无直接映射 |
| Whose Norms? (2606.07877) | 文化对齐研究重要，但与本周项目的技术栈无直接联动点 |

---

## 📊 联动总览

| 论文 | 联动项目 | 联动强度 | 联动主题 |
|------|----------|----------|----------|
| GateMem | claude-mem, agentmemory | ⭐⭐⭐ | 共享内存治理 ↔ 跨会话记忆持久化 |
| 4-bit KV-Cache | headroom | ⭐⭐⭐ | 推理端压缩 ↔ 输入端压缩，端到端优化 |
| DataMagic | OpenMontage | ⭐⭐⭐ | 多 Agent 视频编排 ↔ 12 管道 52 工具 |
| WorldLines | deer-flow | ⭐⭐⭐ | 长时程基准 ↔ 子代理+记忆+沙箱 |
| Contagion Networks | deer-flow, OpenMontage | ⭐⭐ | 评估偏差传染 ↔ 多 Agent 评估健壮性 |
| Re-Centering Humans | claude-mem, agentmemory | ⭐⭐ | 个性化局限 ↔ 记忆正确使用策略 |
| IFLLM | deer-flow, OpenMontage | ⭐⭐ | 隐式反馈 ↔ 用户交互层设计 |
| ASYS | codegraph | ⭐ | 符号搜索 ↔ 代码知识推理增强 |

---

## 🔍 本周主题洞察

**1. Agent 记忆的"治理"缺口**
GateMem + claude-mem + agentmemory 共同指向一个问题：记忆存起来了，但谁来管？权限怎么分？冲突怎么解？开源项目目前聚焦"持久化"，论文提醒"治理"是下一个战场。

**2. Token 效率的全链路化**
headroom（输入压缩）+ 4-bit KV-Cache（推理压缩）+ codegraph（预索引减少 token）= Agent 全链路上下文优化已成共识。成本驱动的工程选择正在重塑架构。

**3. 多 Agent 编排的隐忧**
DataMagic 和 OpenMontage 都依赖多 Agent 管道，但 Contagion Networks 揭示的评估偏差传染意味着：编排层越复杂，评估器越可能成为系统级单点故障。

**4. 视频 Agent 从玩具走向工具**
DataMagic（学术）+ OpenMontage（开源）双双证明：视频制作不再是"演示级"，而是可以通过 Agent 管道工程化。这个品类可能正在从 0 到 1。

---

*Generated by Kimi Claw | 周四论文精选 | W26*
