# 📄 本周候选论文池（18篇）

> **收集时间**: 2026-06-30（周二）  
> **收集范围**: 2026-06-23 至 2026-06-30（过去7天）  
> **来源**: arXiv (cs.CL / cs.LG / cs.AI)  
> **筛选关键词**: LLM, Agent, Multi-Agent, RAG, Reasoning, Multimodal, Chain-of-Thought, Prompt Engineering, Long Context, 智能体, 大模型  
> **排除项**: 纯医学AI、纯CV（非VLM相关）

---

## 1. MCP Server Architecture Patterns for LLM-Integrated Applications
- **链接**: https://arxiv.org/abs/2606.30317
- **标签**: `Agent` `MCP` `Architecture` `Tool Use`
- **一句话摘要**: 总结了5种生产级MCP服务器架构模式（Resource Gateway、Tool Orchestrator、Stateful Session Server、Proxy Aggregator、Domain-Specific Adapter）和4种反模式，量化评估显示工具选择准确率在10-15个工具时下降至90%以下。

## 2. Always-On Agents: A Survey of Persistent Memory, State, and Governance in LLM Agents
- **链接**: https://arxiv.org/abs/2606.30306
- **标签**: `Agent` `Survey` `Memory` `Governance` `Long Context`
- **一句话摘要**: 对435篇文献的综述，从6个诊断轴分析持久状态agent的治理问题，提出AOEP-v0评估协议，发现文献偏重状态积累而轻治理恢复。

## 3. ManimAgent: Self-Evolving Multimodal Agents for Visual Education
- **链接**: https://arxiv.org/abs/2606.30296
- **标签**: `Agent` `Multimodal` `Self-Evolution` `Memory`
- **一句话摘要**: 自进化多模态agent通过双通道Episodic Memory Bank跨任务传递反思经验，无需权重更新和人类种子，在科学动画生成任务上验证。

## 4. Rehearsed Multi-Agent Live Product Demonstrations with Real-Time Voice Question Answering
- **链接**: https://arxiv.org/abs/2606.30294
- **标签**: `Multi-Agent` `Voice` `Real-time` `Demonstration`
- **一句话摘要**: Rhetor多agent系统实现实时产品演示和语音问答，在4个部署应用（含Excalidraw）上验证，locator收敛率达1.00。

## 5. Grounding LLM Reasoning under Incomplete Graph Evidence
- **链接**: https://arxiv.org/abs/2606.30247
- **标签**: `Reasoning` `GraphRAG` `KG` `LLM`
- **一句话摘要**: 从不完整图证据下对LLM推理进行理论分析，提出soft grounding框架（KL正则化变形），应用于GraphRAG、KGQA和graph agents。

## 6. Clarus: Coordinating Autonomous Research Agents toward Web-Scale Scientific Collaboration
- **链接**: https://arxiv.org/abs/2606.30246
- **标签**: `Multi-Agent` `Research` `Collaboration` `Agent`
- **一句话摘要**: Clarus协作基础设施协调自主研究agent实现网络级科学协作，定义四层模型（Research Application / Digital Collaboration / Physical Substrate / Physical World）。

## 7. EvalSafetyGap: A Hybrid Survey and Conceptual Framework for LLM Evaluation-Safety Failures
- **链接**: https://arxiv.org/abs/2606.30219
- **标签**: `LLM` `Safety` `Survey` `Evaluation`
- **一句话摘要**: 混合综述分析LLM评估与安全的测量问题，发现能力与对抗鲁棒性关联不显著（r=+0.232, p=0.520），开放-封闭安全差距主要来自治理披露。

## 8. Before Thinking, Learn to Decide: Proactive Routing for Efficient Visual Reasoning
- **链接**: https://arxiv.org/abs/2606.30217
- **标签**: `Multimodal` `Reasoning` `Routing` `Efficiency`
- **一句话摘要**: PRP主动路由范式通过联合评估draft和target模型能力实现早期决策，加速多模态推理而不损失性能。

## 9. Multi-Agentic System Leveraging Open-Source LLMs to Mitigate Disinformation Threats
- **链接**: https://arxiv.org/abs/2606.30259
- **标签**: `Multi-Agent` `LLM` `Open Source` `Disinformation`
- **一句话摘要**: 多agent系统利用开源LLM（LLaMA、Kimi、Qwen、Deepseek等）通过共识机制检测虚假信息，在英语/波兰语/斯洛伐克语/保加利亚语上验证。

## 10. PromptGNN-sim: Deep Fusion and Alignment of GNN and LLMs for Text-Attributed Graph Learning
- **链接**: https://arxiv.org/abs/2606.30291
- **标签**: `LLM` `GNN` `RAG` `Fusion`
- **一句话摘要**: 双向结构-语义融合框架结合GNN和LLM用于文本属性图学习，通过交叉模态对比学习联合优化，优于经典GNN和LLM基线。

## 11. Towards Continual Motion-Language Agents: LoRA Variants for Incremental Motion Understanding and Generation
- **链接**: https://arxiv.org/abs/2606.30266
- **标签**: `Agent` `Continual Learning` `Multimodal` `LoRA`
- **一句话摘要**: 持续运动-语言agent使用MoE-LoRA变体（自编码器路由选择任务专家）实现增量运动理解和生成，近零遗忘。

## 12. When Is a Draft Accepted? A Theory of Acceptance in Speculative Decoding
- **链接**: https://arxiv.org/abs/2606.30265
- **标签**: `LLM` `Decoding` `Efficiency` `Theory`
- **一句话摘要**: 对speculative decoding的接受理论分析，扩展到greedy/tree decoding并在Qwen3上验证，证明 relaxed/tree-based 标准显著扩大认证接受区域。

## 13. EMPATH: A Multilingual Auditor-Judge Benchmark for Safety Evaluation of Emotional-Support Chatbots
- **链接**: https://arxiv.org/abs/2606.30256
- **标签**: `LLM` `Safety` `Benchmark` `Multilingual`
- **一句话摘要**: 多语言审计-法官基准评估情感支持聊天机器人安全性，发现19项指标中10项存在分数膨胀，运行间可靠性是每模型的安全属性而非噪声。

## 14. Inoculation Adapters: Improved Selective Generalization with Fewer Surprising Backdoors
- **链接**: https://arxiv.org/abs/2606.30252
- **标签**: `LLM` `Safety` `Adapter` `Fine-tuning`
- **一句话摘要**: Inoculation Adapters（三步LoRA训练：不良特征训练→冻结附加→部署丢弃）抑制不良特征并减少意外后门，优于inoculation prompting。

## 15. Defending Against Harmful Supervision Hidden in Benign Samples
- **链接**: https://arxiv.org/abs/2606.30263
- **标签**: `LLM` `Safety` `Training` `Defense`
- **一句话摘要**: 提出Embedded Attack（有害QA嵌入良性样本）和DR-SFT防御方法，通过token级正则化缓解有害微调。

## 16. DialogPII: A Multilingual Dataset of Synthetic Dialog Transcripts to Detect Personal Information
- **链接**: https://arxiv.org/abs/2606.30312
- **标签**: `LLM` `Privacy` `Dataset` `Multilingual`
- **一句话摘要**: 多语言合成对话数据集用于检测对话中的个人信息，评估对话AI的隐私保护能力。

## 17. KnowsTFM: Knowledge-Informed Fine-Tuning of Small Tabular Foundation Models
- **链接**: https://arxiv.org/abs/2606.30258
- **标签**: `Foundation Model` `Fine-tuning` `Knowledge Graph`
- **一句话摘要**: 知识引导的小表格基础模型微调，结合知识图谱结构注意力和LoRA在专家领域获得显著提升。

## 18. BrainJanus: A Unified Model for Understanding and Generation across Brain, Vision, and Language
- **链接**: https://arxiv.org/abs/2606.30319
- **标签**: `Multimodal` `VLM` `Brain` `Unified Model`
- **一句话摘要**: 统一模型实现脑信号、视觉和语言的理解与生成，神经科学与VLM的交叉，支持fMRI解码和视觉描述。

---

## 本周研究趋势观察

1. **Agent基础设施与架构**: MCP架构模式、Clarus科研协作基础设施、Always-On Agent综述——Agent方向正从概念验证走向系统级工程化。
2. **安全与评估**: EvalSafetyGap、EMPATH、Inoculation Adapters、DR-SFT——安全评估和防御机制成为高频主题。
3. **多模态与推理**: PRP主动路由、ManimAgent自进化、BrainJanus——多模态推理和高效推理持续活跃。
4. **多Agent协作**: Rhetor演示系统、Clarus科研协作、虚假信息检测多Agent——Multi-Agent系统从简单协作走向复杂任务编排。

---

*本文件由 Kimi Claw 自动生成于 2026-06-30*
