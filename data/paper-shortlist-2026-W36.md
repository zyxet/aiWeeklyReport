# 📄 2026-W36 论文精选短名单

> 筛选时间：2026-09-03 | 来源：paper-pool-2026-W36.md（126篇）
> 保留规则：按评估打分表评分，总分排序取Top 8

---

## 评估维度说明

每项1-5分，总分25分：
- **创新性**：方法/视角的新颖程度
- **技术深度**：理论严谨性与实验充分性
- **影响力**：对领域或实践的潜在影响
- **开源/可复现**：代码/数据公开程度
- **契合度**：与核心关注领域（LLM推理、Agent、RAG、安全）的匹配度

---

## 🏆 Top 8 精选论文

### 1. LongGuard: Mechanistic Analysis and Training-Free Mitigation of Long-Context Failure in Safety Guardrails

- **arXiv ID**: [2608.27580v2](https://arxiv.org/abs/2608.27580)
- **评分**: 25/25 ⭐
- **创新性**: 5 | **技术深度**: 5 | **影响力**: 5 | **开源**: 5 | **契合度**: 5
- **中文摘要（50字内）**: 提出SafetyNIAH评估框架，通过三层注意力-逻辑-行为分析定位长上下文安全护栏失效机制，并给出训练无关缓解方案。
- **开源标记**: ⭐ **代码+数据已开源**（"Code and data are available online"）
- **关键亮点**:
  - 在0.25k-32k长度网格上评估15个主流护栏，不安全召回率平均下降超50%
  - 定位机制：注意力质量稀释→不安全/安全逻辑边际压缩→检测决策崩溃
  - 提出Chunked Detection和Attention-Head Sharpening两种训练无关缓解方法
  - CAHR协议根据上下文长度和审计侧选择配置

---

### 2. AgentFold: Closed-Loop Agentic Search for Protein Folding Model Design

- **arXiv ID**: [2608.26747v2](https://arxiv.org/abs/2608.26747)
- **评分**: 24/25 ⭐
- **创新性**: 5 | **技术深度**: 5 | **影响力**: 5 | **开源**: 5 | **契合度**: 4
- **中文摘要（50字内）**: 多Agent框架将蛋白质折叠模型开发转化为可执行代码变体的闭环搜索，MCTS策略分配计算资源。
- **开源标记**: ⭐ **代码+实验资源已开源**
- **关键亮点**:
  - 从ESMFold出发，Agent自主提出假设、实现调试代码修改、评估模型变体
  - 探索约80个模型变体，消耗约5000 GPU小时和1.7亿LLM token
  - 最佳lDDT提升7.5%，超越独立Codex提案和随机搜索基线
  - 揭示设计模式：早期软可学习先验和门控细化带来稳定增益

---

### 3. Tensor Methods for Language Models: From Token Representation to Training, Adaptation, Inference, Compression, and Interpretability

- **arXiv ID**: [2608.30505v1](https://arxiv.org/abs/2608.30505)
- **评分**: 23/25 ⭐
- **创新性**: 4 | **技术深度**: 5 | **影响力**: 5 | **开源**: 5 | **契合度**: 4
- **中文摘要（50字内）**: 系统综述张量分解与网络在LLM全生命周期的应用，覆盖7阶段并提出压缩-实现差距指标ρ_gap。
- **开源标记**: ⭐ **GitHub页面已公开**
- **关键亮点**:
  - 七阶段生命周期分类法：tokenization→embeddings→pre-training→adaptation→compression→inference→interpretability
  - 统一notation和理论基础，分析各Transformer组件的张量化策略
  - 提出ρ_gap指标衡量理论内存缩减与实测系统级加速之间的差距
  - 明确参数节省何时可转化为内存效率、计算效率或可解释性

---

### 4. AgenticRag-R1: Agentic Reinforcement Learning with Stack Memory for Multi-Step Reasoning, Retrieval and Memorizing

- **arXiv ID**: [2608.29622v1](https://arxiv.org/abs/2608.29622)
- **评分**: 23/25 ⭐
- **创新性**: 4 | **技术深度**: 4 | **影响力**: 5 | **开源**: 5 | **契合度**: 5
- **中文摘要（50字内）**: 通过记忆栈和细粒度动作空间深度整合推理、检索与记忆，分层动作感知奖励支持长程学习。
- **开源标记**: ⭐ **代码匿名可用**
- **关键亮点**:
  - 解决现有RAG系统粗粒度动作空间和轨迹级奖励导致的弱奖励分配问题
  - 信息感知轨迹拒绝策略实现有效的长程学习
  - 在多跳、开放域和Agentic推理基准上持续超越强基线
  - 学习更鲁棒、可解释、记忆感知的推理行为

---

### 5. Why RAGs Hallucinate: Penalty-Aware Evaluation of Retrieval-Augmented Generation Systems with Knowledge-Gap Canaries

- **arXiv ID**: [2608.26385v1](https://arxiv.org/abs/2608.26385)
- **评分**: 23/25 ⭐
- **创新性**: 4 | **技术深度**: 4 | **影响力**: 5 | **开源**: 5 | **契合度**: 5
- **中文摘要（50字内）**: 提出惩罚感知评估框架，用知识缺口金丝雀检测RAG系统何时不该回答，揭示系统差异在节制策略而非准确率。
- **开源标记**: ⭐ **全部代码、配置、转录和法官投票已发布**
- **关键亮点**:
  - 非对称评分：正确+1、错误-4、弃权0，揭露体积准确率奖励猜测的问题
  - 知识缺口金丝雀：答案可验证不在知识库中的问题
  - 三个商业RAG系统的金丝雀违规率差异约6倍（16.7% vs 98.1%）
  - 失败归因管道分离检索、生成和节制策略失败

---

### 6. Geometry of Divergence: Tracking Hidden-State Trajectories for Adaptive Multi-Turn Reasoning

- **arXiv ID**: [2608.30650v1](https://arxiv.org/abs/2608.30650)
- **评分**: 22/25
- **创新性**: 5 | **技术深度**: 5 | **影响力**: 4 | **开源**: 3 | **契合度**: 5
- **中文摘要（50字内）**: 用时间曲率和方差斜率两个几何信号表征LLM隐藏状态轨迹，识别推理过程中的关键转折。
- **关键亮点**:
  - 将多轮推理建模为隐藏状态轨迹，引入互补几何信号
  - 在四个任务和三个基础LLM上验证，正确/错误片段可事先区分
  - 动作链分解显示可分离性具有动作依赖性
  - tau-Bench成功率从24.1%提升至39.6%，token成本降低11.2%

---

### 7. When LLM Meets Tree Search: A Systematic View of Inference as Search in Large Language Models

- **arXiv ID**: [2608.30395v1](https://arxiv.org/abs/2608.30395)
- **评分**: 22/25
- **创新性**: 4 | **技术深度**: 4 | **影响力**: 5 | **开源**: 4 | **契合度**: 5
- **中文摘要（50字内）**: 系统综述基于树搜索的推理方法，将推理重新框架化为实例特定优化，提出统一设计空间。
- **关键亮点**:
  - 从非知情搜索到MCTS的演进梳理
  - 统一设计空间覆盖搜索拓扑、评估信号和控制动态
  - 倡导标准化计算报告抽象，使计算-准确率权衡显式可比较
  - 将碎片化文献统一在"推理即搜索"视角下

---

### 8. Selective Disclosure of Hidden Directives in Reasoning Models: Behavioral Asymmetry and Steering

- **arXiv ID**: [2608.29070v1](https://arxiv.org/abs/2608.29070)
- **评分**: 22/25
- **创新性**: 5 | **技术深度**: 4 | **影响力**: 5 | **开源**: 3 | **契合度**: 5
- **中文摘要（50字内）**: 发现推理模型的思维链对恶意隐藏指令的披露概率高于良性指令，揭示共享隐藏方向。
- **关键亮点**:
  - 提出指令-合规差距（ICG）量化CoT中隐藏指令的披露不对称性
  - 在8个前沿推理模型（5个家族）上验证，100%精度检测
  - LLM监控器仅读取推理轨迹即可在82%的恶意轨迹中识别具体指令
  - 对比激活加法因果诱导隐藏行为，良性/恶意隐藏向量高度相似

---

## 📊 汇总统计

| 指标 | 数值 |
|------|------|
| 候选池论文数 | 126篇 |
| 精选短名单 | 8篇 |
| 有开源代码/数据 | 5篇（62.5%）⭐ |
| 领域分布 | 安全(2)、RAG(2)、推理(2)、Agent/科学(1)、综述(1) |
| 平均评分 | 23.0/25 |

---

## 🔖 标签分类

- **安全/对齐**: LongGuard、Selective Disclosure of Hidden Directives
- **Agent/工具**: AgentFold、AgenticRag-R1
- **RAG**: AgenticRag-R1、Why RAGs Hallucinate
- **推理机制**: Geometry of Divergence、When LLM Meets Tree Search
- **效率/方法**: Tensor Methods for Language Models

---

> 由周四论文精选任务自动生成 | 下一步：等待人工确认短名单
