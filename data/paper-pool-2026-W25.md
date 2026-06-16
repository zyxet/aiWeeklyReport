# 📄 本周候选论文池（2026-W25，42篇）

> 收集时间：2026-06-16 10:00 AM (Asia/Shanghai)  
> 来源：arXiv cs.CL/cs.LG/cs.AI recent、Hugging Face Papers trending、PaperWeekly  
> 筛选关键词：LLM, Agent, Multi-Agent, RAG, Reasoning, CoT, Multimodal, VLM, Alignment, Memory, Safety  
> 排除：纯医学AI、纯CV（除非VLM相关）、纯理论数学

---

## 1. AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition
- **链接**: https://arxiv.org/abs/2606.14674
- **标签**: Agent, Multi-Agent, Embodied, Composition
- **一句话摘要**: 模块化框架将具身智能体表示为可重用策略组件的受控组合，标准化感知、记忆、推理、反思、动作接口，揭示性能由支架兼容性和交互效应而非孤立模块强度决定。

## 2. HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry
- **链接**: https://arxiv.org/abs/2606.14249
- **标签**: Agent, Harness, Multi-Agent, Evolution
- **一句话摘要**: 可组合、自适应、可进化的智能体接口铸造厂，通过轨迹驱动的多智能体进化引擎AEGIS，在5个基准上平均提升+14.5%（最高+44.0%），证明智能体进步不必仅靠模型缩放。

## 3. Parallel-Synthesis: Direct Cache-Based Synthesis for Parallel Agent Branches
- **链接**: https://arxiv.org/abs/2606.14672
- **标签**: Agent, Multi-Agent, Cache, Efficiency
- **一句话摘要**: 让合成器直接消费并行工作智能体的KV缓存，减少首token时间2.5x-11x，无需重新计算冗余前缀。

## 4. Communication Policy Evolution for Proactive LLM Agents
- **链接**: https://arxiv.org/abs/2606.14314
- **标签**: Agent, Multi-Agent, Communication, Evolution
- **一句话摘要**: 通过通信策略演化(CPE)让LLM智能体主动优化与用户的文本和UI交互，无需修改模型即可实现最佳任务成功率。

## 5. GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge
- **链接**: https://arxiv.org/abs/2606.14470
- **标签**: Agent, Reasoning, Memory, Version Control
- **一句话摘要**: 将智能体推理树存储为git仓库，每个评分的思想是一个commit，使推理可回放、可审计、可跨智能体合并。

## 6. SkillAudit: Ground-Truth-Free Skill Evolution via Paired Trajectory Auditing
- **链接**: https://arxiv.org/abs/2606.14239
- **标签**: Agent, Skill, Evolution, Self-Improvement
- **一句话摘要**: 无需真值反馈的智能体技能进化框架，通过配对轨迹审计隔离技能变化，在89个容器化任务上达到73.9%平均奖励。

## 7. Closing the Reflection Gap: A Free Calibration Bonus for Agentic RL
- **链接**: https://arxiv.org/abs/2606.14211
- **标签**: Agent, RL, Reflection, Calibration
- **一句话摘要**: 通过RefGRPO关闭智能体反射差距，将智能体变为基于环境反馈的自身验证器，文本到SQL任务中不确定率从44.4%降至7.7%。

## 8. When Should Agent Trust Be Conditional? Skill-Conditional Reputation in Agent Swarms
- **链接**: https://arxiv.org/abs/2606.14200
- **标签**: Agent, Multi-Agent, Trust, Safety
- **一句话摘要**: 研究异构智能体集群中技能条件信任，发现条件信任仅在特定机制（高异质性、稀疏证据、相关技能）下获胜，并量化跨技能借用作为攻击通道。

## 9. SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model
- **链接**: https://arxiv.org/abs/2606.14574
- **标签**: LLM, Agent, Planning, Benchmark
- **一句话摘要**: 通过符号世界模型评估LLM规划中的潜在失败，发现高达56%的计划包含潜在失败，显式状态推理可减少72%的潜在失败。

## 10. When the Tool Decides: LLM Agents Defer Blindly to GNN Tools
- **链接**: https://arxiv.org/abs/2606.14476
- **标签**: Agent, LLM, Tool, Reasoning
- **一句话摘要**: LLM智能体盲目服从GNN工具（97.6-99.2%一致），更强的模型服从率更高，选择性调用必须显式设计而非自然涌现。

## 11. WebDecept: Deceptive Interface Safety of Web Agents
- **链接**: https://arxiv.org/abs/2606.13686
- **标签**: Agent, Web, Safety, Multimodal
- **一句话摘要**: 评估多模态Web智能体在7种欺骗性电商界面下的安全性，发现所有模型在强注意力操纵下几乎都会误购。

## 12. StreamMemBench: Streaming Evaluation of Agent Memory for Future-Oriented Assistance
- **链接**: https://arxiv.org/abs/2606.14571
- **标签**: Agent, Memory, Benchmark
- **一句话摘要**: 流式评估智能体记忆，测试从观察到未来辅助的信息传递能力，发现当前系统常无法利用观察证据或反馈。

## 13. SANA: What Matters for QA Agents over Massive Data Lakes?
- **链接**: https://arxiv.org/abs/2606.13904
- **标签**: Agent, RAG, QA, Reasoning
- **一句话摘要**: 诊断框架分析数据湖上QA Agent的搜索、规划、数据分析瓶颈，发现复杂检索和系统级问题超越单纯的长上下文扩展。

## 14. OCC-RAG: OOD-Capable, Controlled-Cache Retrieval-Augmented Generation
- **链接**: https://arxiv.org/abs/2606.00683
- **标签**: RAG, OOD, Cache, LLM
- **一句话摘要**: 缓存推理与单次检索交替迭代，解决OOD查询在RAG中的性能下降，避免复杂的缓存更新机制。

## 15. From Chatbot to Digital Colleague: The Paradigm Shift Toward Persistent Autonomous AI
- **链接**: https://arxiv.org/abs/2606.14502
- **标签**: LLM, Agent, Reasoning, CoT, Memory
- **一句话摘要**: 从聊天机器人到数字同事的转变，涵盖推理时计算、CoT推理、反射、过程监督和RL，提出Workspace+Skill范式实现同事级状态持久化。

## 16. TwinBI: An Agentic Digital Twin for Efficient Augmented Interactions with BI Dashboards
- **链接**: https://arxiv.org/abs/2606.13731
- **标签**: Agent, BI, Multi-Agent, UI
- **一句话摘要**: 智能体数字孪生框架统一仪表板操作和自然语言查询，将精确匹配准确率从43.3%提升至63.3%。

## 17. YeasierAgent: Agentic Social Sandbox for Symbiotic Agent-Native Applications
- **链接**: https://arxiv.org/abs/2606.13722
- **标签**: Agent, Multi-Agent, Social, Sandbox
- **一句话摘要**: 共生智能体原生应用构建范式，通过平台无关的交互单元实现跨平台智能体协作空间，统一情感陪伴和工具执行。

## 18. A Lightweight Parallel of Decoupled Training and Online Interaction for LLM Agents
- **链接**: https://arxiv.org/abs/2606.01686
- **标签**: Agent, Training, Decoupling
- **一句话摘要**: 解耦LLM Agent的训练和在线交互，内存占用仅3.7%，实现持续更新而不影响服务稳定性。

## 19. Adaptive Auto-Harness: A Real-Time Inference Adapter for LLM Agents (LIFE-HARNESS)
- **链接**: https://arxiv.org/abs/2606.01770
- **标签**: Agent, Harness, Runtime, Multi-Agent
- **一句话摘要**: 引入四层实时推理接口适配器，不改变模型权重提升确定性LLM Agent性能，在WebArena和OSWorld上表现优异。

## 20. Minim: Privacy-Aware Minimal View for Agents via Trusted Local Sanitization
- **链接**: https://arxiv.org/abs/2606.13949
- **标签**: Agent, Privacy, UI, Safety
- **一句话摘要**: 本地隐私感知最小化，在UI状态传输前过滤敏感信息，基于上下文完整性框架保留任务关键信息。

## 21. Capability Minimization as a Safety Primitive: Risk-Aware Causal Gating for LLM Agents
- **链接**: https://arxiv.org/abs/2606.13884
- **标签**: Agent, Safety, Causal, Risk
- **一句话摘要**: 通过因果风险门控实现最小权限LLM智能体，显式分离因果风险与预测不确定性，在高风险决策中减少高成本错误。

## 22. AdaSR: Adaptive Streaming Reasoning with Hierarchical Relative Policy Optimization
- **链接**: https://arxiv.org/abs/2606.14694
- **标签**: LLM, Reasoning, Streaming, RL
- **一句话摘要**: 自适应流式推理框架，让模型在输入流式传输过程中进行推理，通过分层相对策略优化(HRPO)学习何时思考及分配计算量。

## 23. CORA: Consistency-Oriented Reasoning Alignment in Multimodal RLVR
- **链接**: https://arxiv.org/abs/2606.14691
- **标签**: VLM, Multimodal, RL, Reasoning, Alignment
- **一句话摘要**: 解决多模态RLVR中思维与答案不一致的问题，通过一致性奖励模型和混合奖励优势分割(HRAS)提升推理可信度。

## 24. Gaze Heads in VLMs: Mechanistic Analysis and Steering
- **链接**: https://arxiv.org/abs/2606.14703
- **标签**: VLM, Multimodal, Mechanistic Analysis, Steering
- **一句话摘要**: 在VLM中发现控制视觉描述的注意力头（gaze heads），可定向操控模型回答，仅修改5-20个头即可改变描述对象。

## 25. VISTA: Cross-View Reinforcement Learning for GUI Grounding
- **链接**: https://arxiv.org/abs/2606.14512
- **标签**: VLM, Agent, RL, GUI, Multimodal
- **一句话摘要**: 跨视图强化学习提升GUI定位精度，通过多视角比较和自我验证锚点，将Qwen3-VL 30B在ScreenSpot-Pro上从53.7提升至67.0。

## 26. PF-OPSD: Prompt-Free Open-Point-of-Scene Disentanglement for Object-Attribute Compositional Learning
- **链接**: https://arxiv.org/abs/2606.03603
- **标签**: VLM, Compositional, Disentanglement
- **一句话摘要**: 无需提示的开放场景点解耦，实现对象-属性组合学习，提升VLM对未见对象-属性组合的推理能力。

## 27. BayLing-Duplex: Native Full-Duplex Speech Dialogue with a Single Autoregressive LLM
- **链接**: https://arxiv.org/abs/2606.14528
- **标签**: LLM, Speech, Dialogue, Multimodal
- **一句话摘要**: 原生全双工语音对话，单自回归LLM实现实时双向语音交互，突破传统轮流对话的延迟限制。

## 28. LoSoNA: A Benchmark for Local Social Norm Adaptation in Group Conversations
- **链接**: https://arxiv.org/abs/2606.14600
- **标签**: LLM, Agent, Social, Benchmark
- **一句话摘要**: 评估LLM智能体在群聊中推断和适应本地社交规范的能力，Gemini 3.1 Pro达到84.2%，Claude Fable 5达到81.6%。

## 29. Validating LLM-Based Urban Simulators: Mobility Realism in Generative Agents
- **链接**: https://arxiv.org/abs/2606.13835
- **标签**: Agent, Simulation, LLM, Evaluation
- **一句话摘要**: 验证LLM城市模拟器中生成智能体的移动模式真实性，发现模型遵循真实空间约束但偏离时间规律性和语义活动多样性。

## 30. Cultural Data Funnel: A Declining Explicit Cultural Signal in Modern LLM Pipelines
- **链接**: https://arxiv.org/abs/2606.13808
- **标签**: LLM, Alignment, Cultural, Data
- **一句话摘要**: 文化信号在LLM后训练阶段急剧下降，显式文化信号在SFT中下降41%，在RL中下降97%，多语言增强地理多样性但不确保文化平衡。

## 31. Characterizing Cultural Localization in AI-Generated Stories
- **链接**: https://arxiv.org/abs/2606.14626
- **标签**: LLM, Cultural, Localization, Generation
- **一句话摘要**: 衡量AI生成故事中模板化文化本地化的程度，发现仅9-17%的词汇跨国籍变化，剩余叙事共享文化无关的模板。

## 32. LLMs Contain Multitudes: How Deployment Context Reshapes Model-Level Preferences and Values
- **链接**: https://arxiv.org/abs/2606.13944
- **标签**: LLM, Evaluation, Alignment
- **一句话摘要**: LLM的偏好和价值观高度依赖部署上下文（系统提示、对话历史、角色），并非模型级别的固定属性，上下文变化导致3.2x的偏好分布差异。

## 33. LLM-as-a-Judge Reliability Under Repeated Evaluation
- **链接**: https://arxiv.org/abs/2606.13685
- **标签**: LLM, Evaluation, Judge, Reliability
- **一句话摘要**: LLM-as-a-Judge在重复评估中稳定性不足，成对偏好翻转平均13.6%，28%的问题超过20%翻转率，需要报告多次试验的聚合结果。

## 34. Every Eval Ever: A Unifying Schema and Community Repository for AI Evaluation Results
- **链接**: https://arxiv.org/abs/2606.14516
- **标签**: Evaluation, LLM, Benchmark
- **一句话摘要**: 标准化AI评估结果的统一JSON模式和社区仓库，收录22,235个模型、2,273个基准和31种评估格式，支持跨框架比较。

## 35. Poker Arena: Multi-Axis Profiling of Strategic Reasoning and Memory in LLMs
- **链接**: https://arxiv.org/abs/2606.13815
- **标签**: LLM, Reasoning, Memory, Benchmark
- **一句话摘要**: 通过德州扑克多轴评估LLM战略推理和记忆能力，发现标量排行榜系统性地误排名，跨维度一致性超过单轴峰值性能。

## 36. DLawBench: Evaluating LLMs Through Multi-Turn Legal Consultation
- **链接**: https://arxiv.org/abs/2606.13931
- **标签**: LLM, Evaluation, Multi-Turn, Reasoning
- **一句话摘要**: 通过多轮法律咨询评估LLM的交互式法律推理能力，发现模型在多轮对话中保持法律一致性方面存在显著差距。

## 37. Ψ-Bench: A Benchmark for Psychological Profiling of LLMs
- **链接**: https://arxiv.org/abs/2606.02754
- **标签**: LLM, Benchmark, Psychology
- **一句话摘要**: 通过心理测量手段评估LLM在理解性、记忆性、自我概念和认知偏差方面的表现，发现模型存在系统性心理偏差。

## 38. Adversarial Concept Search: Predicting Compositional Errors From Feature Geometry
- **链接**: https://arxiv.org/abs/2606.13934
- **标签**: LLM, Reasoning, Safety, Analysis
- **一句话摘要**: 通过表示几何预测LLM在概念组合上的失败，当概念编码正交时可靠组合，编码接近时产生干扰失败，无需评估具体输入。

## 39. Persona-Pruner: Sculpting Lightweight Role-Playing Models
- **链接**: https://arxiv.org/abs/2606.14695
- **标签**: LLM, Pruning, Persona, Role-Playing
- **一句话摘要**: 从LLM中剪枝出特定角色的人格子网络，保留角色扮演能力，实现轻量级角色扮演模型，无需重新训练。

## 40. PI-Hunter: In-Context Persona Inference
- **链接**: https://arxiv.org/abs/2606.12737
- **标签**: LLM, Persona, Inference, Safety
- **一句话摘要**: 推断聊天模型中内置的角色人格，仅通过文本对话揭示隐藏特征，评估10个前沿模型的隐私泄露风险。

## 41. Multi-Task Learning Based On Improving Accuracy of Sparse Mixture of Experts
- **链接**: https://arxiv.org/abs/2606.12703
- **标签**: LLM, MoE, Multi-Task
- **一句话摘要**: 通过路由多任务损失和多采样过程提升稀疏MoE专家选择准确性，增强多任务学习能力。

## 42. Efficient On-Device Diffusion LLM Inference
- **链接**: https://arxiv.org/abs/2606.13740
- **标签**: LLM, Diffusion, On-Device, Efficiency
- **一句话摘要**: 通过GPU并行采样实现扩散LLM的高效设备端推理，突破扩散模型在边缘设备上的计算瓶颈。

---

## 本周亮点

### 🔥 重点关注
1. **AgentSpec + HarnessX**: 智能体支架/接口的系统性研究成为本周热点，两篇论文从模块化组合和进化角度探索智能体架构。
2. **Parallel-Synthesis**: 工程突破——直接消费并行Agent分支的KV缓存，实现2.5x-11x加速。
3. **LLM偏好部署依赖性**: 2606.13944揭示LLM偏好并非模型级别属性，而是高度依赖部署上下文，对AI安全评估有重大影响。
4. **Cultural Data Funnel**: 文化信号在LLM后训练阶段急剧下降（RL中下降97%），对全球部署的AI系统有重要启示。

### 📊 趋势观察
- **智能体架构**: 从模型训练转向运行时接口/支架优化（HarnessX、LIFE-HARNESS、AgentSpec）
- **评估可靠性**: LLM-as-a-Judge的稳定性问题被量化（13.6%翻转率），Every Eval Ever推动评估标准化
- **多模态推理**: CORA解决VLM思维-答案不一致，Gaze Heads实现VLM可解释性操控
- **隐私安全**: Minim实现本地隐私最小化，WebDecept评估欺骗性界面对Agent的影响

---

*本报告由AI Agent自动收集生成，如有遗漏或错误请指正。*
