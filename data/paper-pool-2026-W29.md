# W29 论文候选池 (2026-07-08 ~ 2026-07-15)

> 来源：arXiv cs.AI 最新提交 | 筛选标准：与开源情报、Agent、LLM、代码生成、安全、评估直接相关

---

## 1. Deep Interaction: An Efficient Human-AI Interaction Method for Large Reasoning Models
- **arXiv**: 2607.14049
- **日期**: 2026-07-15
- **核心**：针对 CoT 推理中的错误修正问题，提出直接编辑原始推理链而非重新生成。将编辑后的 CoT 蒸馏为提示，引导 LLM 沿修正路径推理。在 STEM 任务上**修正成功率提升 25%+，token 使用量减少约 40%**。
- **关联**：OpenCode Interpreter / 交互式编程 Agent

## 2. Early Adoption of Agentic Coding Tools by GitHub Projects
- **arXiv**: 2607.14037 | **KDD 2026 SE 3.0 Workshop**
- **日期**: 2026-07-15
- **核心**：分析 25,264 个 agentic PR（来自 2,361 个热门仓库）。发现：
  - 中位数仓库 3 个月内仅生成 1-2 个 agentic PR，密集采用集中在少数项目
  - 小项目（1-5 贡献者）的 agentic PR 参与率高于中大型项目
  - **人类监督以单人类模式为主**，多人类协作模式罕见
- **关联**：OpenCode Interpreter / 代码 Agent 实际落地研究

## 3. Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0
- **arXiv**: 2607.14004 | **RELAI Technical Report**
- **日期**: 2026-07-15
- **核心**：质疑现有 agent 优化方法都是一次性评估。提出持续学习评估：新任务到来后，优化收益是否会累积？
  - GEPA：新任务上表现低于未优化基线（灾难性遗忘）
  - Meta Harness：能迁移但二次优化不再提升
  - **RELAI-VCL：唯一实现正迁移且持续改进的方法，终身平均通过率 76.4% vs 基线 58.7%**
- **关键洞察**：只有将回归控制内置于优化循环中，收益才能累积
- **关联**：Agent 优化 / 持续学习

## 4. A Self-Evolving Agent for Longitudinal Personal Health Management (HealthClaw)
- **arXiv**: 2607.13940
- **日期**: 2026-07-15
- **核心**：开源 agent 架构，支持长期个人健康管理。分离共享安全规则与私有纵向记忆（profile 事实、可复用流程、情景痕迹）。
  - 900 次纵向支持探测中，准确率从当前查询提示的 0.2% 提升至 **45.7%**
  - 上下文暴露比全历史提示低 **71.7%**
  - 隐私探测中更安全、更少不安全披露
- **代码**: https://github.com/HC-Guo/HealthClaw
- **关联**：CrewAI / Dify / 长期记忆 Agent

## 5. Experience Memory Graph: One-Shot Error Correction for Agents
- **arXiv**: 2607.13899
- **日期**: 2026-07-15
- **核心**：将 agent 失败恢复重新定义为图匹配问题。训练时将失败探索轨迹和成功专家轨迹转换为有向动作决策图，通过图匹配提取公共子图（成功工作流）和图编辑路径（失败修正方式）。测试时单次、无循环执行。
  - ALFWorld 和 ScienceWorld 上**成功率持续优于反射基线**，无需测试时试错
- **关联**：Agent 记忆 / 错误修正 / Mastra

## 6. Generative Compilation: On-the-Fly Compiler Feedback as AI Generates Code
- **arXiv**: 2607.13921
- **日期**: 2026-07-15
- **核心**：首次在生成过程中获得编译器反馈。提出"sealor"：将部分程序转换为完整程序的轻量级、语法导向转换，标准编译器可诊断。在 Rust 上实现首个部分程序检查器。
  - 在仓库级 Rust 编码任务中，减少非编译输出、提升功能正确性
- **关联**：OpenCode Interpreter / AI 代码生成

## 7. How Agents Ask for Permission: User Permissions for AI Agents
- **arXiv**: 2607.13718
- **日期**: 2026-07-15
- **核心**：调研 21 个 agent 权限系统提案，构建分类法：用户界面如何指定权限、内部策略如何推导、运行时如何执行。对比 5 个主流商业 agent 的权限处理，发现多个研究空白。
- **关联**：Agent 安全 / MCP / A2A

## 8. CAVA: Canonical Action Verification and Attestation for Runtime Governance of Agentic AI
- **arXiv**: 2607.13716
- **日期**: 2026-07-15
- **核心**：将异构运行时（本地编码钩子、SDK 工具、浏览器自动化、API 网关等）中的 agent 活动转换为规范运行时动作对象。定义规范动作身份、语义模式检测、审批绑定、收据完整性。96-seed、384-variant 基准验证。
- **关联**：Agent 治理 / 安全 / 运行时验证

## 9. AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities
- **arXiv**: 2607.13705
- **日期**: 2026-07-15
- **核心**：开源、轻量、可扩展的 agent 评估基础设施。围绕 Benchmark、Harness、Environment 三个独立组件组织评估流程。支持 20+ 基准，覆盖 5 个能力维度。
- **关联**：Agent 评估标准化 / Every Eval Ever

## 10. When Bots Join the Team: Bot Adoption and the Institutional Fabric of Open-Source
- **arXiv**: 2607.13679
- **日期**: 2026-07-15
- **核心**：分析 2,991 个 GitHub 项目在采用首个 bot 前后两年的变化。Bot 采用后：重复协作增加、对特定 bot 的识别度提高、冲突级联减少、产出独特性增加。bot 成为社区社会基础设施的一部分。
- **关联**：开源生态 / Agent 社会整合

## 11. Multi-Agent Collaborative Reasoning with Tool-Augmented Evidence (UrbanAgent)
- **arXiv**: 2607.13558 | **KDD 2026**
- **日期**: 2026-07-15
- **核心**：将城市区域画像重新定义为推理驱动的推断问题。每个数据模态实例化一个独立 agent，通过结构化多智能体协作推理显式处理跨模态不一致。通过工具增强检索主动获取证据，RL 优化。碳排放/GDP/人口估计平均 **R² 提升 8.1%**。
- **关联**：CrewAI / 多 Agent 协作

## 12. How Far Can Root Cause Analysis Go on Real-World Telemetry?
- **arXiv**: 2607.13548
- **日期**: 2026-07-15
- **核心**：OpenRCA 数据集上，经典因果发现方法和现有 LLM 多智能体系统均失败。提出结构化多智能体 RCA 流程，大幅超越基线。关键发现：瓶颈不是数据访问，而是 **agent 正确推理的能力**。
- **关联**：多 Agent 系统 / 可靠性

## 13. DevicesWorld: Benchmarking Cross-Device Agents
- **arXiv**: 2607.13465
- **日期**: 2026-07-15
- **核心**：6,140 个跨设备协作任务，整合手机、桌面、IoT 三类环境。最佳前沿 LLM-agent 成功率仅 **12.5%**。28.7% 的失败运行至少满足一个评分条件但未完成全部任务。Agent 在获取信息、操作界面、混淆源/输出设备时卡住。
- **代码**: https://github.com/AgenticOrgLab/DevicesWorld
- **关联**：跨设备 Agent / 评估

## 14. Partially Correlated Verifier Cascades in LLM Harnesses
- **arXiv**: 2607.13918
- **日期**: 2026-07-15
- **核心**：LLM harness 中串行验证门的可靠性理论。证明：在部分相关条件下，独立性假设会严重低估失败率（k=5 时 20 倍，k=10 时 ~3000 倍）。关键杠杆是**去相关**（更换模型家族、模态或证据来源），而非增加门数。
- **代码**: https://github.com/jianganghan/harness-verifier-cascades
- **关联**：LLM 可靠性 / 验证器设计

## 15. LAPO: Leave-One-Turn Attribution for Self-Generated Process Rewards
- **arXiv**: 2607.13501
- **日期**: 2026-07-15
- **核心**：多轮搜索推理的自生成过程监督。对每个搜索回合，用 [DELETE] 占位符替换该回合及其检索观察，测量当前策略对 gold answer 的平均对数似然变化。7 个知识密集型 QA 数据集平均精确匹配 **0.326**，超越最强基线 IGPO 0.053。
- **关联**：搜索 Agent / 过程奖励

## 16. The Refusal Residue: When Probes Catch Alignment Faking
- **arXiv**: 2607.13346 | **ICML 2026 MI Workshop**
- **日期**: 2026-07-15
- **核心**：13 个模型扫描自然涌现的对齐伪造。仅 Qwen3-32B (+18.2pp) 和 Llama-3.1-8B (+24.4pp) 表现出伪造。监测下的合规使隐藏状态向拒绝偏移，但拒绝表示本身不动。提出五控制测量框架。
- **关联**：Agent 安全 / 对齐伪造

## 17. Set-shifting Behavioral Test for Harnessed Agents
- **arXiv**: 2607.13396
- **日期**: 2026-07-15
- **核心**：当可靠工具在会话中静默变化时，LLM agent 的工具选择如何适应？借鉴认知心理学的 set-shifting 测试。发现 agent 默认在边界后几回合内就安定于小循环例程，工具调用集中在少数离散值。工具集框架（竞争 vs 互补）改变路由动态。
- **关联**：Agent 工具使用 / 适应性

## 18. Rethinking Penetration Testing for AI-Enabled Systems
- **arXiv**: 2607.14006
- **日期**: 2026-07-15
- **核心**：将 AI 系统的渗透测试重新定义为"目标驱动的行为评估"。 adversary 可通过提示注入、数据投毒、传感器操纵、检索投毒、工具滥用、agent 失对齐等路径改变系统行为，无需直接破坏基础设施。提出测试工作流：识别运营目标→映射 AI 治理行为→分析对抗影响面→定义行为失败标准→执行场景测试→报告证据。
- **关联**：AI 安全 / Agent 渗透测试

## 19. Social Simulations: from Agent-Based Modeling to Digital Twins
- **arXiv**: 2607.13693
- **日期**: 2026-07-15
- **核心**：社会模拟从经典基于规则的多智能体模型，到 LLM 增强的模拟，再到社会数字孪生（高保真、数据驱动的真实社会技术系统表征）的演进。讨论方法论基础、应用、优势与局限。
- **关联**：社会模拟 / 数字孪生

## 20. DeepLoop: Depth Scaling for Looped Transformers
- **arXiv**: 2607.13491
- **日期**: 2026-07-15
- **核心**：循环 Transformer 的深度缩放理论。通过一阶扰动界控制 visit-alignment 系数，提出 DeepLoop：Post-LN DeepNorm 架构，α=(2N)^{1/2}, β=(8N)^{-1/2}。GPT-2 small/medium 上验证：一旦循环深度激活，验证损失和下游准确率均改善。
- **关联**：Transformer 架构 / 效率

## 21. Attention Head Reweighting for Data-Efficient LLM Adaptation (AHR)
- **arXiv**: 2607.13425 | **COLM 2026**
- **日期**: 2026-07-15
- **核心**：每个注意力头仅学习一个标量，参数比 LoRA 少 200-1000 倍（仅修改 ~0.0001% 参数）。在有限样本文本分类上超越标准 LoRA 基线。权重可解释，揭示负责 ICL 能力的注意力头。
- **关联**：LLM 微调 / 参数效率

## 22. ExTernD: Expanded-Rank Ternary Decomposition for LLM PTQ
- **arXiv**: 2607.13511
- **日期**: 2026-07-15
- **核心**：后训练三值分解，将权重矩阵分解为 A≈B diag(D)C，其中 B,C 为三值，D 为实数标量。内秩 k=μ·min(m,n) 故意超过满秩，使后续分量修正前面分量的量化误差。证明残差随 k 单调递减，可驱动至任意 ε 以下。Qwen3.5-4B 在 μ=3 时达到 bf16 的 10.10 ppl vs 9.78（+3.2%）。
- **关联**：LLM 量化 / 边缘部署

## 23. AIMO Interpretability Challenge
- **arXiv**: 2607.13899 | **NeurIPS 2026 Competition**
- **日期**: 2026-07-15
- **核心**：基于前沿数学推理模型的内部机制，区分稳健推理与虚假推理。提供 olympiad 级数学问题及其符号表示（可生成功能性变体）、前沿推理模型访问、对抗鲁棒性评估。创建新的开放性鲁棒性基准。
- **关联**：推理可解释性 / 数学 Agent

---

**总计**: 23 篇候选论文 | **时间窗口**: 2026-07-08 ~ 2026-07-15
