# 📄 本周候选论文池（12篇）

> 收集时间：2026-10-20（周二）｜覆盖周期：2026-10-13 ~ 2026-10-19
> 来源：arXiv cs.CL / cs.LG / cs.AI、Hugging Face Papers Trending、PaperWeekly
> 筛选关键词：LLM, Agent, Multi-Agent, RAG, Reasoning, Long Context, Multimodal, 智能体, 大模型

---

| # | 标题 | 链接 | 标签 | 一句话摘要 |
|---|------|------|------|-----------|
| 1 | OS-Helix: Unifying GUI Interaction and Code Execution in Native Computer-Using Agents | https://arxiv.org/abs/2610.22234 | Agent, Computer Use, GUI+Code, RL | 端到端强化学习训练的原生计算机使用智能体，将 GUI 操作与代码执行统一在同一动作空间中。 |
| 2 | OpenGCUA: Toward a Fully Open Stack for Generalist Computer Use | https://arxiv.org/abs/2610.22200 | Agent, Computer Use, Open Source | 阿里 MAI 团队开源的通用计算机使用智能体全栈——视觉定位、文本定位、奖励建模全部开放权重与数据。 |
| 3 | DLite: History-free Speculative Decoding for Agentic AI | https://arxiv.org/abs/2610.23787 | Agent, Inference Acceleration, Speculative Decoding | 面向智能体负载的免历史投机解码框架，草稿模型无需维护完整上下文历史，显著降低长会话推理延迟。 |
| 4 | Pack Light, CarryOn: Building Object-Oriented Context for Long-Horizon Agents | https://arxiv.org/abs/2610.18784 | Agent, Long Context, Context Management | 借鉴编程语言对象模型，将智能体上下文封装为可复用对象，实现长程任务中的高效状态管理。 |
| 5 | Into the Unknown: Benchmarking AI Agents on Open Scientific Research Problems | https://arxiv.org/abs/2610.19159 | Agent, Benchmark, Science | DOE 实验室联合 benchmark：9 个前沿 agent 对开放科学问题写出 135 篇跟进论文，0 篇通过全部评审条件。 |
| 6 | LiveMACE: Process-Aware Evaluation of LLM Agent Capabilities in Evolving Markets | https://arxiv.org/abs/2610.09872 | Agent, Evaluation, Benchmark, Multi-Agent | 用真实金融市场作为天然演进环境，评估 5 个前沿 LLM 的工具使用、持久记忆、规则遵循与多智能体协作，揭示"结果-能力鸿沟"。 |
| 7 | Learning to Think and Explore in 3D World (ACT3D) | https://arxiv.org/abs/2610.21783 | VLM, 3D, RL, Multimodal | 让 VLM 像人一样在 3D 空间中主动移动视角获取证据，RL 训练后平均准确率 53.2%，超 Gemini 3.6 Flash。 |
| 8 | TreeOPSD: Tree-Aware Posterior Distillation for Long-Horizon Agentic Reinforcement Learning | https://arxiv.org/abs/2610.23181 | Agent, RL, Long-Horizon | 无 critic、无外部教师的树感知后验自蒸馏框架，通过共享前缀分支树实现回合级信用分配。 |
| 9 | OpenMobile-2: Building Versatile Mobile Agents with Scalable Environments and App-Native Tools | https://huggingface.co/papers | Mobile Agent, Benchmark, Open Source | 全开源移动智能体——环境、数据、benchmark、模型一体开放，支持应用原生工具调用。 |
| 10 | DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses | https://huggingface.co/papers | Agent, Scientific Discovery, Self-Improvement | 递归自我改进框架，让 LLM agent 自主发现有价值的科学假设。 |
| 11 | AgentGarten: Massively Concurrent Real-Time Trial Environment for Agents | https://www.iyiou.com/data/202610121143036 | Agent, Multi-Agent, Environment | 大规模并发实时试炼场，为智能体提供真实世界并行任务环境。 |
| 12 | MoHGE: Fine-grained Agentic Reasoning via Mixture of Heterogeneous Grouped Experts | https://www.iyiou.com/data/202610121143036 | Reasoning, MoE, Agent | ACL 2026 杰出论文——异构分组混合专家架构实现细粒度智能体推理。 |

---

## 🏷️ 标签分布

- **Agent / 智能体**: #1 #2 #3 #4 #5 #6 #8 #10 #11 #12（10篇）
- **Computer Use**: #1 #2（2篇）
- **RL / 强化学习**: #1 #7 #8（3篇）
- **Benchmark / 评估**: #5 #6 #9（3篇）
- **VLM / Multimodal**: #7（1篇）
- **Long Context / Long-Horizon**: #4 #8（2篇）
- **Science / 科学发现**: #5 #10（2篇）
- **推理优化**: #3 #12（2篇）

## 📝 本周观察

1. **Computer Use 赛道爆发**：OS-Helix 和 OpenGCUA 几乎同周发布，一个走端到端 RL 训练路线，一个走全栈开源路线，GUI+Code 混合动作空间已成为共识。
2. **长上下文与长程推理分化**：Pack Light CarryOn 从软件工程借对象模型管上下文，TreeOPSD 从 RL 信用分配入手，两条路线各自推进。
3. **Agent 评测走向"过程感知"**：LiveMACE 和 Into the Unknown 都不满足于看结果，而是深入决策过程——前者用 trace 诊断能力，后者用 135 篇论文揭示 agent 科研能力的天花板还很低。
4. **VLM 主动探索**：ACT3D 让视觉语言模型学会"走过去看看"，而不是被动接受给定视角，RL 驱动下超过 Gemini 3.6 Flash。
