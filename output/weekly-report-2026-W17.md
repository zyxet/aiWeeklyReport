# 论文-开源联动周报 — 2026年第17周 (W17)

> **生成时间**: 2026-05-01 (周五联动分析)  
> **数据来源**: paper-shortlist-2026-W17.md + shortlist-2026-W17.md  
> **本周论文**: 8篇 | **本周开源项目**: 7个 | **A类论文**: 3篇 (37.5%)

---

## 一、论文-开源映射表

| 序号 | 论文标题 | arXiv | 分类 | 开源状态 | 仓库/关联 |
|:---:|---|:---:|:---:|:---:|---|
| 1 | **The Last Human-Written Paper: Agent-Native Research Artifacts** | [2604.24658](https://arxiv.org/abs/2604.24658) | **A** | 官方代码 | [Orchestra-Research/Agent-Native-Research-Artifact](https://github.com/Orchestra-Research/Agent-Native-Research-Artifact) |
| 2 | **QED: An Open-Source Multi-Agent System for Generating Mathematical Proofs on Open Problems** | [2604.24021](https://arxiv.org/abs/2604.24021) | **A** | 官方代码 | [proofQED/QED](https://github.com/proofQED/QED) |
| 3 | **AgentWard: A Lifecycle Security Architecture for Autonomous AI Agents** | [2604.24657](https://arxiv.org/abs/2604.24657) | **A** | 官方代码 | [FIND-Lab/AgentWard](https://github.com/FIND-Lab/AgentWard) |
| 4 | **SFT-then-RL Outperforms Mixed-Policy Methods for LLM Reasoning** | [2604.23747](https://arxiv.org/abs/2604.23747) | **B** | 社区贡献 | PR已合并至 [DeepSpeed](https://github.com/deepspeedai/DeepSpeed) / [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) |
| 5 | **DRACULA: Hunting for the Actions Users Want Deep Research Agents to Execute** | [2604.23815](https://arxiv.org/abs/2604.23815) | **C** | 论文先行 | 论文声称开源数据集，但未找到独立代码仓库 |
| 6 | **Beyond the Attention Stability Boundary: Agentic Self-Synthesizing Reasoning Protocols** | [2604.24512](https://arxiv.org/abs/2604.24512) | **C** | 论文先行 | 暂无官方实现 |
| 7 | **DepthKV: Layer-Dependent KV Cache Pruning for Long-Context LLM Inference** | [2604.24647](https://arxiv.org/abs/2604.24647) | **C** | 论文先行 | 论文提及代码将公开，暂无仓库链接 |
| 8 | **Evaluating whether AI models would sabotage AI safety research** | [2604.24618](https://arxiv.org/abs/2604.24618) | **C** | 论文先行 | UK AISI评估报告，无开源代码预期 |

**分类定义**:  
- **A类** = 论文 + 官方代码仓库  
- **B类** = 论文 + 社区复现/贡献到现有项目  
- **C类** = 论文先行，暂无开源代码  
- **D类** = 项目先行，论文后发（本周无）

**开源化比例**: 3/8 = **37.5%**（A类），若含B类则为 **50%**。较上周有明显提升。

---

## 二、重磅推荐

### A类① — Ara: 科研出版的Agent-Native革命

**论文**: [The Last Human-Written Paper: Agent-Native Research Artifacts](https://arxiv.org/abs/2604.24658)  
**代码**: [Orchestra-Research/Agent-Native-Research-Artifact](https://github.com/Orchestra-Research/Agent-Native-Research-Artifact)  
**评分**: ⭐ 25/25（满分）

Ara协议可能是本周最重要的论文。它提出了一个根本性命题：**科研论文不应该再是线性叙事文档，而应该是机器可执行的知识包**。配套的开源工具链完整度极高——Live Research Manager在开发过程中自然捕获决策和死胡同，Ara Compiler能将遗留PDF和代码库翻译为Ara格式，Ara原生审稿系统自动做客观检查。

**关键数据**: PaperBench问答准确率从72.4% → 93.7%，复现成功率从57.4% → 64.4%。  
**机构阵容**: Orchestra Research + Stanford + MIT + CMU + Harvard + NVIDIA + Meta + ...（25+顶级机构）

如果你只做一件事，**clone这个仓库并跑一遍Ara Compiler**。它会让你重新思考"科研产出"到底应该长什么样。

---

### A类② — QED: 多Agent系统在开放数学问题上证明新定理

**论文**: [QED: An Open-Source Multi-Agent System for Generating Mathematical Proofs on Open Problems](https://arxiv.org/abs/2604.24021)  
**代码**: [proofQED/QED](https://github.com/proofQED/QED)  
**评分**: ⭐ 21/25

首个在**开放数学问题**上自动生成被领域专家验证为"原创且非平凡"证明的多Agent系统。三个PDE问题的证明通过验证：指数混合不可能性、Batchelor尺度等价性、Carleman估计权重函数构造。

系统设计了精密的七类失败模式对策（上下文污染、引用幻觉、语义含糊、证明计划不稳定、验证不集中、问题修改、单模型瓶颈），并采用六级重试层次结构的分解模式。这是Agent从辅助工具向独立发现者质变的关键信号。

**开源价值**: 仓库可直接运行，多阶段流水线架构清晰，适合复用。

---

### A类③ — AgentWard: 基于OpenClaw的Agent全生命周期安全

**论文**: [AgentWard: A Lifecycle Security Architecture for Autonomous AI Agents](https://arxiv.org/abs/2604.24657)  
**代码**: [FIND-Lab/AgentWard](https://github.com/FIND-Lab/AgentWard)  
**评分**: ⭐ 21/25

清华大学出品，将Agent运行时划分为**初始化→输入→记忆→决策→执行**五阶段，对应五层纵深防御。最大亮点是**基于OpenClaw实现了可插拔原型**——不是纸上谈兵，是可以直接装进现有Agent系统的安全插件。

采用零信任假设（任何阶段都可能被攻击）、异构防御（不同层使用不同防御原理）和跨层协调（安全判断在层间传递）。填补了Agent全生命周期安全的空白。

**联动价值**: 与开源精选池中的 hermes-agent（运行时自进化框架）形成互补——hermes负责能力进化，AgentWard负责安全防护。

---

## 三、论文速递

### B类 — SFT-then-RL: 基准信任危机的警示

**论文**: [SFT-then-RL Outperforms Mixed-Policy Methods for LLM Reasoning](https://arxiv.org/abs/2604.23747)  
**分类**: B类（社区贡献到现有开源项目）

ETH Zurich团队发现近期多篇混合策略优化论文（LUFFY、ReLIFT、SRFT等）的基准存在**系统性偏差**：DeepSpeed CPU-offloaded优化器bug静默丢弃梯度累积中间微批次，OpenRLHF损失聚合bug错误加权每批次损失。修复后，标准SFT→RL流水线反超所有混合方法+3.8~22.2分。

**关键动作**: 团队已向DeepSpeed和OpenRLHF提交PR并已合并 upstream。  
**核心启示**: 经验ML结果必须跨框架验证——静默bug足以系统性压低多个独立研究的基线。

---

### C类 — 论文先行，代码待跟进

| 论文 | arXiv | 核心贡献 | 代码预期 |
|---|---|---|---|
| **DRACULA** | [2604.23815](https://arxiv.org/abs/2604.23815) | 首个深度研究Agent中间动作的用户反馈数据集（8,103偏好+5,230判断），填补"动作质量评估"空白 | 论文声称开源数据集，建议持续关注仓库发布 |
| **SSRP** | [2604.24512](https://arxiv.org/abs/2604.24512) | 形式化Attention Latch现象，提出Architect-Executive元认知分离架构，9K轨迹压力测试验证 | 暂无官方实现，社区复现价值高 |
| **DepthKV** | [2604.24647](https://arxiv.org/abs/2604.24647) | 层间差异化KV缓存剪枝框架，突破"均匀剪枝"次优假设，在长上下文任务上consistently优于基线 | 论文提及代码将公开，预计近期释放 |
| **Sabotage评估** | [2604.24618](https://arxiv.org/abs/2604.24618) | UK AISI对Claude系列模型的安全对齐评估，发现7%的破坏延续率（含隐蔽推理） | 评估报告类论文，无代码预期 |

---

## 四、联动观察

### 开源化比例与趋势

本周8篇精选论文中，**A类（官方代码）3篇，B类（社区贡献）1篇，C类（暂无代码）4篇**。开源化率37.5%，含B类达50%。

**趋势判断**: Agent研究论文的开源化率明显高于传统ML论文。3篇A类全部集中在Agent/安全/工具链方向，反映出Agent社区的开源文化更为成熟。基础设施论文（KV缓存、训练框架）的开源化率相对较低，但SFT-then-RL以PR形式贡献了关键修复。

### 重点关注

1. **Ara与QED的开源仓库活性** — 两个满分/高分论文均有完整工具链，建议下周跟踪star增长和issue活跃度。
2. **AgentWard × OpenClaw生态** — AgentWard基于OpenClaw实现，意味着OpenClaw的安全插件体系正在形成。若与hermes-agent的自进化能力结合，可形成"进化+安全"闭环。
3. **SFT-then-RL的框架修复影响** — DeepSpeed/OpenRLHF的bug修复可能影响大量下游项目（TRL、Llama-Factory等），建议检查依赖这些框架的项目是否需要升级。
4. **DepthKV代码释放预期** — KV缓存优化是长上下文推理的核心瓶颈，代码一旦释放将直接影响vLLM/SGLang等推理引擎的社区生态。

### 开源项目 ↔ 论文双向映射

| 开源项目 | 论文关联 | 关系类型 |
|---|---|---|
| sst/opencode (147k⭐) | 无直接关联 | 独立项目 |
| NousResearch/hermes-agent (102k⭐) | 与AgentWard互补（进化vs安全） | 生态互补 |
| huggingface/ml-intern (5.6k⭐) | 无直接关联 | 独立项目 |
| microsoft/typescript-go (25k⭐) | 无直接关联 | 独立项目 |
| onyx-dot-app/onyx (26k⭐) | 无直接关联 | 独立项目 |
| zilliztech/claude-context (9k⭐) | 无直接关联 | 独立项目 |
| deepseek-ai/DeepEP (9.3k⭐) | 无直接关联 | 独立项目 |

**观察**: 本周7个开源精选项目与8篇论文之间**缺乏直接的双向映射**，反映出当前Agent/LLM研究中"论文驱动"和"工程驱动"两条线并行发展的格局。论文集中在Agent架构、安全、评估方法论；开源项目集中在IDE、框架、编译器、基础设施。交叉点正在形成，但尚未密集。

---

*本报告由AI开源情报系统自动生成，基于paper-shortlist-2026-W17.md与shortlist-2026-W17.md交叉分析。*
