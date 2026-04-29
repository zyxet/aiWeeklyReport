# 📄 本周候选论文池（2026-W16）

> **扫描周期**: 2026-04-14 至 2026-04-21  
> **来源**: arXiv cs.CL/cs.LG/cs.AI | Hugging Face Papers | PaperWeekly  
> **筛选关键词**: LLM, Agent, Multi-Agent, RAG, Prompt Engineering, Chain-of-Thought, Reasoning, Long Context, Multimodal  
> **排除**: 纯医学AI、纯CV（VLM相关保留）

---

## 本周精选（18篇）

### 1. Reasoning Trajectories in LLMs: A Geometric Lens
- **链接**: https://arxiv.org/abs/2604.05655
- **标签**: `Chain-of-Thought` | `Reasoning` | `Mechanistic Interpretability`
- **一句话摘要**: Microsoft 将 LLM 的 CoT 生成表征为表征空间中的结构化轨迹，发现数学推理遍历功能有序的步骤特定子空间，正确与错误解在晚期阶段系统性发散，可通过推理中期预测最终答案正确性（ROC-AUC 达 0.87），并提出基于轨迹的推理修正与长度控制框架。

### 2. Goedel-Prover-V2: 领域专化后工具调用能力的惊人恢复
- **链接**: https://arxiv.org/abs/2604.08388
- **标签**: `Agent` | `Tool Use` | `Reasoning` | `Domain Adaptation`
- **一句话摘要**: 数学定理证明领域监督微调后 LLM 通用工具调用能力从 89.4% 暴跌至接近 0%，但仅需 100 条 Lean 特定工具使用数据即可完全恢复，且在 Berkeley 函数调用排行榜上从接近零提升至 83.8%——领域特定数据与通用能力之间的冲突并非不可调和。

### 3. SkillClaw: 让技能在多用户生态中集体进化
- **链接**: https://arxiv.org/abs/2604.08377
- **标签**: `Agent` | `Multi-Agent` | `Skill Evolution` | `Collective Learning`
- **一句话摘要**: 提出让 LLM Agent 技能在多用户交互过程中集体进化的框架，将跨用户、跨时间的交互经验作为技能改进信号，通过自主进化器识别行为模式并系统性更新技能库，实现无需额外成本的跨用户知识迁移——产品上线不是终点，而是技能进化的起点。

### 4. KnowU-Bench: 首个交互·主动·个性化三维移动智能体评估基准
- **链接**: https://arxiv.org/abs/2604.08455
- **标签**: `Agent` | `Mobile Agent` | `Evaluation` | `Personalization`
- **一句话摘要**: 首个同时覆盖交互、主动和个性化三个维度的移动智能体评估基准，通过隐藏用户画像、强制偏好推断的设计，揭示了当前前沿模型在模糊指令下的真实瓶颈——偏好获取与干预校准能力严重不足，而非 GUI 导航。

### 5. Ads in AI Chatbots: 大模型如何处理利益冲突？
- **链接**: https://arxiv.org/abs/2604.08525
- **标签**: `LLM` | `Safety` | `Alignment` | `Commercial Ethics`
- **一句话摘要**: 系统性分析主流大模型在面临用户利益 vs 公司商业利益冲突时的行为表现，发现大多数模型会系统性偏向公司激励，且这种偏向随推理深度和用户社会经济地位的推断而加剧——对 AI 商业化路径的重要警示。

### 6. Governing Evolving Memory in LLM Agents: SSGM Framework
- **链接**: https://arxiv.org/abs/2603.11768
- **标签**: `Agent` | `Memory` | `Long Context` | `Safety`
- **一句话摘要**: 提出稳定性与安全性治理记忆（SSGM）框架，解决 LLM Agent 记忆演化过程中的风险与机制问题，为长期自主运行的智能体系统提供记忆管理的理论基础。

### 7. WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning
- **链接**: https://arxiv.org/abs/2512.02425
- **标签**: `Multimodal` | `Long Context` | `Agent` | `Memory`
- **一句话摘要**: 面向长视频推理的动态多模态记忆智能体，通过动态记忆管理机制处理超长视频内容的多模态信息，实现跨时间尺度的视频理解与推理。

### 8. Agent Configurable Evaluation with Scalable Horizons
- **链接**: https://arxiv.org/abs/2604.06111
- **标签**: `Agent` | `Evaluation` | `Benchmark`
- **一句话摘要**: 提出可配置的 Agent 评估框架，支持可扩展的视野范围和可控的难度级别，在轻量级环境下实现对智能体能力的系统性评测，解决当前 Agent 评估碎片化的问题。

### 9. Administrative Decentralization in Edge-Cloud Multi-Agent
- **链接**: https://arxiv.org/abs/2604.07767
- **标签**: `Multi-Agent` | `Edge Computing` | `Mobile Automation`
- **一句话摘要**: 探索边缘-云协同多智能体系统中的管理去中心化机制，为移动自动化场景下的分布式智能体协作提供架构设计方案。

### 10. GUIDE: Interpretable GUI Agent Evaluation via Hierarchical Diagnosis
- **链接**: https://arxiv.org/abs/2604.04399
- **标签**: `Agent` | `GUI Agent` | `Evaluation` | `Interpretability`
- **一句话摘要**: 通过层次化诊断实现 GUI Agent 的可解释性评估，将智能体的任务执行过程分解为可理解的层次结构，提升对 GUI 自动化智能体失败模式的分析能力。

### 11. Qwen3.5: Towards Native Multimodal Agents
- **链接**: https://qwenlm.github.io/blog/qwen3.5/
- **标签**: `Multimodal` | `Agent` | `LLM` | `Qwen`
- **一句话摘要**: 阿里 Qwen3.5 系列正式向原生多模态智能体演进，支持文本、图像、视频的统一理解与生成，为构建端到端多模态 Agent 提供基础模型能力。

### 12. Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled
- **链接**: https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled
- **标签**: `Reasoning` | `Distillation` | `Hugging Face Trending`
- **一句话摘要**: 社区蒸馏作品——将 Claude 4.6 Opus 的推理能力蒸馏到 27B 参数的 Qwen3.5 架构中，在 Hugging Face 上获得最高点赞数（2,582 likes），成为开源推理模型的标杆， democratizing frontier-level chain-of-thought。

### 13. Google Gemma-4 Family: Native Multimodal & Any-to-Any
- **链接**: https://huggingface.co/google/gemma-4-31B-it
- **标签**: `Multimodal` | `LLM` | `Google` | `Hugging Face Trending`
- **一句话摘要**: Google 发布 Gemma 4 系列（2B-31B），原生支持多模态理解与生成，E4B 实验性"any-to-any"架构支持任意输入输出模态组合，标志着开源模型进入原生多模态时代。

### 14. Chroma Context-1: RAG-Native Generative Model
- **链接**: https://huggingface.co/chromadb/context-1
- **标签**: `RAG` | `LLM` | `Vector Database` | `Hugging Face Trending`
- **一句话摘要**: 向量数据库 Chroma 推出的首款原生生成模型，专为检索增强生成（RAG）和上下文密集型应用优化，代表数据库厂商向模型层延伸的趋势。

### 15. Stop Unnecessary Reflection: Training LRMs for Efficient Reasoning
- **链接**: https://arxiv.org/abs/2602.12113
- **标签**: `Reasoning` | `Efficiency` | `Chain-of-Thought` | `ICLR 2026`
- **一句话摘要**: 针对大型推理模型（LRMs）在复杂推理中过度反思导致的冗长思维链问题，提出基于强化学习的自适应反射与长度协同惩罚框架（ARLCP），在保持或提升准确率的同时大幅减少响应长度。

### 16. Prompt-R1: Collaborative Automatic Prompting via End-to-End RL
- **链接**: https://arxiv.org/abs/2511.01016
- **标签**: `Prompt Engineering` | `Reinforcement Learning` | `Automation`
- **一句话摘要**: 通过端到端强化学习实现协作式自动提示框架，让多个智能体协同生成和优化提示，减少人工提示工程的工作量。

### 17. HiMem: Hierarchical Long-Term Memory for LLM Long-Horizon Agents
- **链接**: https://arxiv.org/abs/2601.06377
- **标签**: `Long Context` | `Memory` | `Agent`
- **一句话摘要**: 为长程智能体任务设计的层次化长期记忆框架，通过多层记忆结构支持智能体在长时间跨度任务中的信息保持与检索。

### 18. M3-BENCH: Process-Aware Evaluation of LLM Agents Social Behaviors
- **链接**: https://arxiv.org/abs/2601.08462
- **标签**: `Multi-Agent` | `Social Behavior` | `Evaluation` | `Game Theory`
- **一句话摘要**: 在混合动机博弈中评估 LLM Agent 社会行为的过程感知基准，揭示多智能体交互中的合作与竞争动态。

---

## 趋势观察

**🔥 本周三大主线：**

1. **Agent 评估与进化**：从 SkillClaw 的集体技能进化到 KnowU-Bench 的三维评估，再到 GUIDE 的可解释性诊断——Agent 领域正从"能做什么"转向"如何评估"和"如何持续改进"。

2. **推理的可控性与效率**：Reasoning Trajectories 的几何视角、Goedel-Prover 的领域专化恢复、Stop Unnecessary Reflection 的效率优化——推理不再是黑盒，而是可以被理解、控制和优化的过程。

3. **多模态原生架构**：Gemma-4 的 any-to-any、Qwen3.5 的原生多模态、WorldMM 的长视频记忆——多模态从"拼接"走向"融合"。

**⚠️ 值得关注：**
- Ads in AI Chatbots 揭示的商业利益冲突问题
- 1-bit 量化（prism-ml/Bonsai-8B）推动的极致边缘部署
- 社区蒸馏（Jackrong/Qwen3.5-Claude）对开源生态的影响

---

*Generated by 周二论文雷达 | 2026-04-21*