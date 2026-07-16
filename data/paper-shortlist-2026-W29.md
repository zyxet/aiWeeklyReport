# W29 论文精选短名单 (2026-07-15)

> 从 23 篇候选论文中精选 8 篇，优先：①与本周开源短名单（OpenCode Interpreter / n8n / Dify / Browser Use / MCP / CrewAI / Mastra）有直接关联；②代表新方向或重要突破；③有开源代码或重要会议接受。

---

## 1. Early Adoption of Agentic Coding Tools by GitHub Projects
- **arXiv**: 2607.14037 | **KDD 2026 Workshop SE 3.0**
- **关联开源**: OpenCode Interpreter, n8n
- **核心**：25,264 个 agentic PR（2,361 仓库）的实证分析。小项目参与率高于大项目；单人类监督占主导；密集采用仍集中在少数项目。**Agent 编码工具的实际落地图景，比 Star 数更能说明问题。**

## 2. Do Agent Optimizers Compound? (Terminal-Bench 2.0)
- **arXiv**: 2607.14004 | **RELAI Technical Report**
- **关联开源**: Mastra, CrewAI
- **核心**：首次持续学习评估 Agent 优化器。GEPA 灾难性遗忘，Meta Harness 停滞，**RELAI-VCL 唯一实现正迁移 + 持续改进（76.4% vs 基线 58.7%）**。**关键洞察**：只有回归控制内置在优化循环中，收益才能累积。

## 3. Experience Memory Graph: One-Shot Error Correction for Agents
- **arXiv**: 2607.13899
- **关联开源**: CrewAI, Mastra
- **核心**：将 Agent 失败恢复重新定义为图匹配问题。提取成功工作流和失败修正路径存入记忆图，测试时**单次、无循环执行**。ALFWorld/ScienceWorld 上持续优于反射基线，无需测试时试错。**Agent 记忆从"反思"走向"图结构化经验复用"的关键一步。**

## 4. CAVA: Canonical Action Verification for Runtime Governance
- **arXiv**: 2607.13716
- **关联开源**: MCP, A2A, Browser Use
- **核心**：Agent 运行时治理的语义层。将异构运行时（SDK 工具、浏览器自动化、API 网关、工作流引擎）的活动统一转换为规范动作对象，定义审批绑定、收据完整性、语义模式检测。384-variant 基准验证。**Agent 行动可审计性的基础设施级框架。**

## 5. AgentCompass: A Unified Evaluation Infrastructure
- **arXiv**: 2607.13705
- **关联开源**: 通用
- **核心**：开源、轻量、可扩展的 Agent 评估基础设施。Benchmark + Harness + Environment 三组件解耦，支持 20+ 基准覆盖 5 个能力维度。异步容错运行时 + 轨迹分析工具。**Agent 评估碎片化问题的工程化解决方案。**

## 6. DevicesWorld: Benchmarking Cross-Device Agents
- **arXiv**: 2607.13465 | 代码开源
- **关联开源**: Browser Use, MCP
- **核心**：6,140 个跨设备协作任务（手机+桌面+IoT），最佳前沿 LLM-Agent **成功率仅 12.5%**。28.7% 的失败至少满足一个条件但未完成全部任务。Agent 在信息获取、设备混淆、界面操作上系统性失败。**跨设备是下一个 Agent 能力边界，而非当前强项。**
- **代码**: https://github.com/AgenticOrgLab/DevicesWorld

## 7. How Agents Ask for Permission: User Permissions for AI Agents
- **arXiv**: 2607.13718
- **关联开源**: MCP, CrewAI, Dify
- **核心**：调研 21 个权限系统提案，构建分类法（界面指定→内部推导→运行时执行）。对比 5 个商业 Agent 发现：**产品级统一策略无法满足用户级差异化需求**。识别多个研究空白，包括用户偏好动态更新、权限冲突解决、跨平台一致性。

## 8. Generative Compilation: Compiler Feedback During AI Code Generation
- **arXiv**: 2607.13921
- **关联开源**: OpenCode Interpreter, Dify
- **核心**：首次在**生成过程中**获得编译器反馈。提出"sealor"将部分程序转换为完整程序供标准编译器诊断。在 Rust 仓库级任务上减少非编译输出、提升功能正确性。**将编译器从"事后检查"变为"生成中的副驾驶"，对强类型语言代码 Agent 意义重大。**

---

## 双料关联（论文 ↔ 开源）

| 论文 | 关联开源项目 | 关联维度 |
|------|-------------|----------|
| Early Adoption of Agentic Coding Tools | OpenCode Interpreter | 实际落地图景 |
| Do Agent Optimizers Compound? | Mastra, CrewAI | Agent 优化与持续学习 |
| Experience Memory Graph | CrewAI, Mastra | 记忆组件化 |
| CAVA | MCP, A2A, Browser Use | 运行时治理与可审计性 |
| AgentCompass | 通用 | 评估标准化 |
| DevicesWorld | Browser Use, MCP | 跨设备能力边界 |
| How Agents Ask for Permission | MCP, CrewAI, Dify | 权限安全 |
| Generative Compilation | OpenCode Interpreter | 代码生成质量 |

---

**W29 论文核心判断**:
1. **Agent 评估从"跑分"走向"基础设施"**：AgentCompass + DevicesWorld 表明社区意识到评估工具本身需要工程化
2. **Agent 优化进入"持续学习"阶段**：一次性调优不够，RELAI-VCL 证明回归控制是累积收益的关键
3. **Agent 安全从"边界防御"走向"运行时治理"**：CAVA + Permissions 论文关注行动审计和权限粒度，而非单纯的对齐训练
4. **代码 Agent 的瓶颈在"编译反馈时机"**：Generative Compilation 将编译器从后验变为生成中，可能是强类型语言 Agent 的质量拐点
