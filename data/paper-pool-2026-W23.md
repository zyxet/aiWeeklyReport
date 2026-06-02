# 本周候选论文池（2026-W23）

> 收集时间：2026-06-02 | 来源：arXiv cs.CL/cs.LG/cs.AI recent + CodeSOTA + Hugging Face Papers
> 筛选关键词：LLM, Agent, Multi-Agent, RAG, Prompt Engineering, Chain-of-Thought, Reasoning, Long Context, Multimodal, 智能体, 大模型
> 排除规则：已排除纯医学AI、纯CV（VLM相关保留）

---

## 📊 统计概览

| 来源 | 收录数 | 占比 |
|------|--------|------|
| arXiv cs.CL (NLP/LLM) | 15 | 38% |
| arXiv cs.AI (AI综合) | 12 | 30% |
| arXiv cs.LG (机器学习) | 8 | 20% |
| CodeSOTA / Hugging Face | 5 | 12% |
| **总计** | **40** | **100%** |

---

## 🔥 Agent / 智能体 方向（12篇）

### 1. DecisionBench: A Benchmark for Emergent Delegation in Long-Horizon Agentic Workflows
- **链接**: https://arxiv.org/abs/2605.19099
- **标签**: `Agent`, `Benchmark`, `Multi-Agent`, `Long-Horizon`
- **一句话摘要**: 提出评估长程Agent工作流中涌现式任务委托能力的基准测试，覆盖GAIA、BFCL和tau-bench等任务。

### 2. TOBench: A Task-Oriented Omni-Modal Benchmark for Real-World Tool-Using Agents
- **链接**: https://arxiv.org/abs/2605.16909
- **标签**: `Agent`, `Benchmark`, `Tool-Use`, `Multimodal`
- **一句话摘要**: 包含100个可执行任务、27个MCP服务器和324个工具，用于端到端多模态工具使用Agent的闭环验证。

### 3. Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games
- **链接**: https://arxiv.org/abs/2605.04906
- **标签**: `Agent`, `Multi-Agent`, `Reasoning`, `RL`
- **一句话摘要**: 基于递归推理范式和中心化CoT比较模块的RL框架，在多种多Agent博弈中实现22.1%平均性能提升。

### 4. Cochain: Balancing Insufficient and Excessive Collaboration in LLM Agent Workflows
- **链接**: https://arxiv.org/abs/2505.10936
- **标签**: `Agent`, `Multi-Agent`, `Prompt Engineering`, `Collaboration`
- **一句话摘要**: 通过集成知识图谱和提示树，解决单Agent CoT跨域协作不足与多Agent系统令牌消耗过高的问题。

### 5. OrchMAS: Orchestrated Reasoning with Multi Collaborative Heterogeneous Scientific Expert Structured Agents
- **链接**: https://arxiv.org/abs/2603.03005
- **标签**: `Agent`, `Multi-Agent`, `Reasoning`, `Scientific`, `Heterogeneous`
- **一句话摘要**: 面向科学领域的双层多模型编排框架，通过动态构建领域感知推理管道和异构专家Agent协作，实现多步科学推理的动态重规划。

### 6. GraphBit: Agent Orchestration and Reliability Signal
- **链接**: https://arxiv.org/abs/2605.13848
- **标签**: `Agent`, `Multi-Agent`, `Orchestration`, `Graph`
- **一句话摘要**: 基于图结构协调的Agent编排框架，提升多Agent系统的可靠性和协作效率。

### 7. PREPING: Agent Memory Cold-Start Work
- **链接**: https://arxiv.org/abs/2605.13880
- **标签**: `Agent`, `Memory`, `Cold-Start`, `Long Context`
- **一句话摘要**: 针对已部署Agent的可复用记忆冷启动机制，解决Agent在未知环境中的快速适应能力。

### 8. FORGE: Agent Architecture for Practical Multi-Step Systems
- **链接**: https://arxiv.org/abs/2605.16233
- **标签**: `Agent`, `Architecture`, `Multi-Step`, `System`
- **一句话摘要**: 面向实际多步系统设计Agent架构，强调可组合性和模块化设计原则。

### 9. Argus Deep Research Agents
- **链接**: https://arxiv.org/abs/2605.16217
- **标签**: `Agent`, `Research`, `Deep Research`, `Tool-Use`
- **一句话摘要**: 深度研究Agent工作流，支持从论文到证据链的自动化研究流程构建。

### 10. CHI-Bench: Can AI Agents Automate End-to-End Healthcare Workflows?
- **链接**: https://arxiv.org/abs/2605.16679
- **标签**: `Agent`, `Healthcare`, `Workflow`, `MCP`, `End-to-End`
- **一句话摘要**: 评估AI Agent在端到端医疗工作流自动化中的能力，涉及20个应用和87个MCP工具（已保留，因属Agent工作流研究）。

### 11. TwinRouterBench: Fast Static and Live Dynamic Evaluation for Realistic Agentic LLM Routing
- **链接**: https://arxiv.org/abs/2605.18859
- **标签**: `Agent`, `LLM Routing`, `Benchmark`, `Evaluation`
- **一句话摘要**: 面向Agent工作流的LLM路由基准，包含静态和动态评估轨道，用于实时路由决策验证。

### 12. SaaS-Bench: A Practical Benchmark for Agents Operating Across SaaS Workflows
- **链接**: https://arxiv.org/abs/2605.16116
- **标签**: `Agent`, `Benchmark`, `SaaS`, `Workflow`, `Procurement`
- **一句话摘要**: 面向SaaS工作流中Agent操作的实用基准，适用于采购式Agent评估。

---

## 🧠 LLM / 大模型 方向（18篇）

### 13. Representation Forcing for Bottleneck-Free Unified Multimodal Models
- **链接**: https://arxiv.org/abs/2605.31604
- **标签**: `LLM`, `Multimodal`, `VLM`, `Representation Learning`
- **一句话摘要**: 提出表示强制技术，消除统一多模态模型中的信息瓶颈，提升视觉语言模型的表示效率。

### 14. Giving Sensors a Voice: Multimodal JEPA for Sensor Understanding
- **链接**: https://arxiv.org/abs/2605.31580
- **标签**: `LLM`, `Multimodal`, `JEPA`, `Sensor`, `VLM`
- **一句话摘要**: 将多模态JEPA架构扩展至传感器理解领域，为具身智能和物理世界交互提供统一的表示学习框架。

### 15. Dr.LLM: Dynamic Layer Routing in LLMs
- **链接**: https://arxiv.org/abs/2510.12773
- **标签**: `LLM`, `Efficiency`, `Dynamic Routing`, `Inference`
- **一句话摘要**: 基于MCTS监督的逐层动态路由机制，在不改变模型架构的前提下实现高效LLM推理加速。

### 16. A Tight Theory of Error Feedback Algorithms in Distributed Optimization
- **链接**: https://arxiv.org/abs/2605.31594
- **标签**: `LLM`, `Distributed Training`, `Optimization`, `Theory`
- **一句话摘要**: 为分布式优化中的误差反馈算法建立紧致理论分析，对大规模LLM训练具有指导意义。

### 17. MINTEval: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems
- **链接**: https://arxiv.org/abs/2605.18565
- **标签**: `LLM`, `Long Context`, `Memory`, `Evaluation`, `Agent`
- **一句话摘要**: 包含15.6k QA对、平均138.8k token长上下文的多目标记忆干扰评估基准。

### 18. StateKV: Linear-Time Video Prefill for Long-Video VLMs
- **链接**: https://arxiv.org/abs/2605.31597
- **标签**: `LLM`, `VLM`, `Long Context`, `Video`, `Efficiency`
- **一句话摘要**: 通过固定容量重要性递归状态实现长视频VLM的线性时间预填充，无需微调或架构改动即可超越滑动窗口近似方法。

### 19. Formal Methods Meet LLMs: Runtime Monitoring and Formal Constraints
- **链接**: https://arxiv.org/abs/2605.16198
- **标签**: `LLM`, `Safety`, `Formal Methods`, `Runtime Monitoring`, `Agent`
- **一句话摘要**: 将形式化方法引入LLM Agent的运行时监控，构建基于形式化约束的LLM Agent控制层。

### 20. GraphARC: A Benchmark for Abstract Reasoning on Graph-Structured Data
- **链接**: https://arxiv.org/abs/2605.31595
- **标签**: `LLM`, `Reasoning`, `Graph`, `Benchmark`, `Abstract Reasoning`
- **一句话摘要**: 面向图结构数据的抽象推理基准，将少样本变换学习范式推广到图领域。

### 21. ClawForge: High-Priority Benchmark for Agent Evaluation
- **链接**: https://arxiv.org/abs/2605.14133
- **标签**: `LLM`, `Agent`, `Benchmark`, `Evaluation`
- **一句话摘要**: 面向Agent系统的高优先级评估基准，聚焦Agent在复杂任务中的端到端性能。

### 22. EduAgentBench: Education-Agent Evaluation Target
- **链接**: https://arxiv.org/abs/2605.14322
- **标签**: `LLM`, `Agent`, `Education`, `Benchmark`, `Domain-Specific`
- **一句话摘要**: 面向教育领域Agent的专项评估基准，支持教学辅助Agent的能力诊断与改进。

### 23. EntityBench: Entity-Centered Benchmark
- **链接**: https://arxiv.org/abs/2605.15199
- **标签**: `LLM`, `Entity`, `Benchmark`, `Knowledge`, `Reasoning`
- **一句话摘要**: 以实体为中心的评估基准，测试LLM在实体理解、关系推理和知识整合方面的能力。

### 24. ShopGym: High-Priority E-Commerce Agent Environment
- **链接**: https://arxiv.org/abs/2605.16116
- **标签**: `LLM`, `Agent`, `E-Commerce`, `Environment`, `Benchmark`
- **一句话摘要**: 面向电商场景的高优先级Agent环境，支持商品搜索、比价、推荐等Agent任务的端到端评估。

### 25. Fully Open Meditron: Open Medical AI System
- **链接**: https://arxiv.org/abs/2605.16215
- **标签**: `LLM`, `Medical AI`, `Open Source`, `System`
- **一句话摘要**: 完全开源的医疗AI系统，提供模型、数据和基准的完整开源实现（保留，因属开源LLM系统研究）。

### 26. RoadmapBench: Evaluating Long-Horizon Agentic Software Development
- **链接**: https://arxiv.org/abs/2605.15846
- **标签**: `LLM`, `Agent`, `Software Development`, `Long-Horizon`, `Benchmark`
- **一句话摘要**: 包含17个代码仓库中115个真实版本升级的长程Agent软件开发基准。

### 27. ADR-Bench and SLEIGHT-Bench for Agent Security
- **链接**: https://arxiv.org/abs/2605.31593
- **标签**: `LLM`, `Agent`, `Security`, `Benchmark`, `Safety`
- **一句话摘要**: 面向Agent运行时安全的评估基准，覆盖对抗性攻击和Agent行为异常检测。

### 28. WebGameBench: Coding-Agent Delivery Benchmark
- **链接**: https://arxiv.org/abs/2605.31590
- **标签**: `LLM`, `Agent`, `Coding`, `Benchmark`, `Web`
- **一句话摘要**: 面向网页游戏开发Agent的交付评估基准，测试Agent从需求到可运行代码的端到端交付能力。

### 29. LinAlg-Bench, CAM-Bench, GIM for Reasoning Diagnostics
- **链接**: https://arxiv.org/abs/2605.31589
- **标签**: `LLM`, `Reasoning`, `Mathematics`, `Benchmark`, `Diagnostics`
- **一句话摘要**: 面向LLM推理能力诊断的数学基准套件，覆盖线性代数、抽象数学和几何推理。

### 30. PDI-Bench, Collider-Bench, XDomainBench for Cross-Domain Agent Evaluation
- **链接**: https://arxiv.org/abs/2605.31591
- **标签**: `LLM`, `Agent`, `Cross-Domain`, `Benchmark`, `Evaluation`
- **一句话摘要**: 面向跨领域Agent评估的基准套件，测试Agent在领域迁移和知识泛化方面的能力。

---

## 🔍 RAG / Prompt Engineering / Reasoning 方向（10篇）

### 31. Agentic RAG: Dynamic Retrieval and Self-Reflection for Knowledge-Intensive Tasks
- **链接**: https://arxiv.org/abs/2605.31564
- **标签**: `RAG`, `Agent`, `Self-Reflection`, `Knowledge-Intensive`
- **一句话摘要**: 将Agent能力引入RAG系统，支持动态检索决策、自我反思和检索结果的质量评估，提升知识密集型任务的准确性。

### 32. Self-RAG with Reflection Tokens for Active Noise Filtering
- **链接**: https://arxiv.org/abs/2605.31586
- **标签**: `RAG`, `Self-Reflection`, `LLM`, `Noise Filtering`
- **一句话摘要**: 训练LLM生成特殊反射令牌以控制检索和生成过程，主动过滤噪声并评估检索文档的相关性和支持度。

### 33. Chain-of-Thought for Multi-Hop Reasoning with Graph Traversal
- **链接**: https://arxiv.org/abs/2605.31584
- **标签**: `Chain-of-Thought`, `Reasoning`, `Graph`, `Multi-Hop`
- **一句话摘要**: 将链式思维与图遍历结合，支持多跳推理中的显式搜索和回溯，增强复杂推理任务的可解释性。

### 34. Tree-of-Thoughts and Graph-of-Thoughts: Branching and Backtracking
- **链接**: https://arxiv.org/abs/2605.31563
- **标签**: `Tree-of-Thoughts`, `Graph-of-Thoughts`, `Reasoning`, `LLM`
- **一句话摘要**: 通过树和图结构化的思维变体实现推理中的分支和有限回溯，提升复杂问题求解的系统性。

### 35. ReAct and Reflexion: Integrating Reasoning with Environment Interaction
- **链接**: https://arxiv.org/abs/2605.31558
- **标签**: `Reasoning`, `Agent`, `ReAct`, `Reflexion`, `Environment`
- **一句话摘要**: 整合推理与环境交互的Agent框架，通过Thought-Action-Observation循环和错误反思实现动态任务求解。

### 36. Think-on-Graph and Plan-on-Graph: KGQA with Beam Search
- **链接**: https://arxiv.org/abs/2605.31550
- **标签**: `Reasoning`, `Graph`, `KGQA`, `Planning`, `LLM`
- **一句话摘要**: 将推理形式化为图遍历的KGQA方法，结合束搜索和计划修订实现高效知识图谱问答。

### 37. MCTS-Style Planning with LLMs for Long-Horizon Decision Making
- **链接**: https://arxiv.org/abs/2605.31545
- **标签**: `Reasoning`, `Planning`, `MCTS`, `LLM`, `Long-Horizon`
- **一句话摘要**: 将MCTS风格规划引入LLM，通过前向模拟和价值反向传播优化多步决策，在长程任务中取得显著增益。

### 38. FLARE: Online Planning with Explicit Decision Revision
- **链接**: https://arxiv.org/abs/2605.31522
- **标签**: `Reasoning`, `Planning`, `Online`, `LLM`, `Decision Revision`
- **一句话摘要**: 在线规划器，通过执行期间显式评估和修订决策，解决离线规划器依赖自回归采样的局限性。

### 39. Offline vs. Online Planning: Amortizing Planning into Model Parameters
- **链接**: https://arxiv.org/abs/2605.31521
- **标签**: `Reasoning`, `Planning`, `RL`, `LLM`, `Offline`, `Online`
- **一句话摘要**: 对比离线规划（将规划摊销到模型参数）与在线规划（执行时显式修订）在LLM Agent中的优劣。

### 40. Sparse Credit Assignment in LLM Reasoning: Finding Decision Tokens
- **链接**: https://arxiv.org/abs/2605.31524
- **标签**: `Reasoning`, `Credit Assignment`, `LLM`, `Sparse`, `Decision Tokens`
- **一句话摘要**: 识别推理过程中实际引导答案的决策令牌，实现稀疏信用分配，提升LLM推理步骤的可解释性。

---

## 📈 趋势观察

### 本周热点
1. **Agent安全与治理**正从提示策略转向动作拦截、MCP监控和主机端控制。
2. **评估转向过程感知任务**：工具轨迹、交付产物、多模态验证、人工验证评分成为新标准。
3. **自改进Agent**正演变为带回滚、金丝雀测试、经验图和显式生命周期控制的治理系统。
4. **稀疏信用分配**成为推理研究焦点：寻找真正引导答案的决策令牌或推理步骤。

### 方法论转变
- **从单Agent到多Agent编排**：GraphBit、OrchMAS、FORGE等框架强调显式图结构和可检查记忆。
- **从静态提示到动态管道**：OrchMAS的动态领域感知管道和Cochain的提示树展示了新的提示工程范式。
- **从离线训练到在线规划**：FLARE等在线规划器与离线RL训练形成互补。

---

*收集者：周二论文雷达 | 下次更新：2026-06-09*
