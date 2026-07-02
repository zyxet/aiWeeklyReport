# 📋 本周论文精选短名单（W27）

> **生成时间**: 2026-07-02（周四）
> **来源**: paper-pool-2026-W27.md（18篇候选）
> **筛选标准**: 5维度评分（创新/实用/方法/契合/开放），总分25分
> **保留数量**: 8篇（保留率 44%）

---

## 1. Grounding LLM Reasoning under Incomplete Graph Evidence
- **链接**: https://arxiv.org/abs/2606.30247
- **标签**: `Reasoning` `GraphRAG` `KG` `LLM`
- **中文摘要**: 从不完整图证据下对LLM推理进行理论分析，提出soft grounding框架（KL正则化变形），应用于GraphRAG、KGQA和graph agents。
- **评分**: 创新5/实用4/方法5/契合5/开放3 = **22分**
- **开源代码**: 未明确标注
- **入选理由**: 理论深度与GraphRAG实用场景结合，填补图推理的理论空白

---

## 2. Clarus: Coordinating Autonomous Research Agents toward Web-Scale Scientific Collaboration
- **链接**: https://arxiv.org/abs/2606.30246
- **标签**: `Multi-Agent` `Research` `Collaboration` `Agent`
- **中文摘要**: 四层协作模型协调自主研究agent实现网络级科学协作，定义Research Application/Digital Collaboration/Physical Substrate/Physical World层级。
- **评分**: 创新5/实用4/方法4/契合5/开放4 = **22分**
- **开源代码**: ⭐ 基础设施型项目，预期开源
- **入选理由**: Multi-Agent从简单编排走向科研基础设施，工程化意义重大

---

## 3. Before Thinking, Learn to Decide: Proactive Routing for Efficient Visual Reasoning
- **链接**: https://arxiv.org/abs/2606.30217
- **标签**: `Multimodal` `Reasoning` `Routing` `Efficiency`
- **中文摘要**: PRP主动路由范式通过联合评估draft和target模型能力实现早期决策，加速多模态推理而不损失性能。
- **评分**: 创新5/实用5/方法4/契合5/开放3 = **22分**
- **开源代码**: 未明确标注
- **入选理由**: 多模态推理效率关键问题，零性能损失的加速方案

---

## 4. MCP Server Architecture Patterns for LLM-Integrated Applications
- **链接**: https://arxiv.org/abs/2606.30317
- **标签**: `Agent` `MCP` `Architecture` `Tool Use`
- **中文摘要**: 总结5种生产级MCP服务器架构模式与4种反模式，量化评估显示工具选择准确率在10-15个工具时下降至90%以下。
- **评分**: 创新4/实用5/方法4/契合5/开放3 = **21分**
- **开源代码**: 未明确标注
- **入选理由**: MCP生态当前最热工程话题，5种架构模式可直接指导生产

---

## 5. Always-On Agents: A Survey of Persistent Memory, State, and Governance in LLM Agents
- **链接**: https://arxiv.org/abs/2606.30306
- **标签**: `Agent` `Survey` `Memory` `Governance` `Long Context`
- **中文摘要**: 对435篇文献的综述，从6个诊断轴分析持久状态agent的治理问题，提出AOEP-v0评估协议。
- **评分**: 创新4/实用4/方法4/契合5/开放4 = **21分**
- **开源代码**: 综述类，提供评估协议
- **入选理由**: Agent领域最全面的综述，AOEP协议可能成为行业标准

---

## 6. BrainJanus: A Unified Model for Understanding and Generation across Brain, Vision, and Language
- **链接**: https://arxiv.org/abs/2606.30319
- **标签**: `Multimodal` `VLM` `Brain` `Unified Model`
- **中文摘要**: 统一模型实现脑信号、视觉和语言的理解与生成，支持fMRI解码和视觉描述，神经科学与VLM交叉。
- **评分**: 创新5/实用4/方法5/契合4/开放3 = **21分**
- **开源代码**: 未明确标注
- **入选理由**: 脑-VLM交叉前沿，fMRI解码精度代表多模态理解新高度

---

## 7. ManimAgent: Self-Evolving Multimodal Agents for Visual Education
- **链接**: https://arxiv.org/abs/2606.30296
- **标签**: `Agent` `Multimodal` `Self-Evolution` `Memory`
- **中文摘要**: 自进化多模态agent通过双通道Episodic Memory Bank跨任务传递反思经验，无需权重更新和人类种子，在科学动画生成任务上验证。
- **评分**: 创新5/实用4/方法4/契合4/开放3 = **20分**
- **开源代码**: 未明确标注
- **入选理由**: 自进化机制+跨任务记忆传递，Agent能力自主增长的关键方向

---

## 8. Multi-Agentic System Leveraging Open-Source LLMs to Mitigate Disinformation Threats
- **链接**: https://arxiv.org/abs/2606.30259
- **标签**: `Multi-Agent` `LLM` `Open Source` `Disinformation`
- **中文摘要**: 多agent系统利用开源LLM（LLaMA、Kimi、Qwen、Deepseek等）通过共识机制检测虚假信息，在英语/波兰语/斯洛伐克语/保加利亚语上验证。
- **评分**: 创新4/实用4/方法3/契合4/开放5 = **20分**
- **开源代码**: ⭐ 论文+代码双料项目（明确使用开源LLM，多语言验证）
- **入选理由**: 开源LLM多Agent共识机制，多语言覆盖，有明确应用价值

---

## 筛选说明

| 维度 | 说明 |
|------|------|
| 创新 | 方法新颖度、理论贡献 |
| 实用 | 工程落地价值、场景明确度 |
| 方法 | 实验设计、评估充分性 |
| 契合 | 与AI Agent/LLM/RAG/Reasoning等核心方向匹配度 |
| 开放 | 代码/数据/协议开源程度 |

## 本周主题聚焦

- **Agent基础设施**（2篇）：MCP架构、Clarus协作基础设施
- **多模态推理**（2篇）：PRP高效路由、BrainJanus脑-VLM统一
- **Agent认知能力**（2篇）：Always-On记忆综述、ManimAgent自进化
- **图/推理**（1篇）：不完整图证据下的LLM推理
- **多Agent应用**（1篇）：开源LLM虚假信息检测

---

*由 Kimi Claw 自动筛选于 2026-07-02*
