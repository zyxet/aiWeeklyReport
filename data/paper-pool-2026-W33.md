# 📄 本周候选论文池（2026-W33）

> 收集时间：2026-08-11  
> 来源：arXiv cs.CL / cs.LG / cs.AI + RSS Feed  
> 筛选关键词：LLM, Agent, Multi-Agent, RAG, CoT, Reasoning, Long Context, Multimodal, VLM, MoE, Prompt Engineering, 智能体, 大模型  
> 排除：纯医学AI、纯CV（非VLM相关）

---

## 🔬 LLM 架构与效率

### 1. EntropyMoE: Entropy-Aware Sparse Expert Routing for Tokenizer-Free LLMs
- **链接**: https://arxiv.org/abs/2608.06398
- **标签**: `LLM` `MoE` `Tokenizer-Free` `Efficiency`
- **一句话**: 为动态字节补丁设计的MoE架构，用补丁熵直接路由专家，在保持下游精度的同时实现最低bits-per-byte。

### 2. TEXAS: Task-Expert-Aware Supervision for Downstream Mixture-of-Experts LLM Adaptation
- **链接**: https://arxiv.org/abs/2608.06396
- **标签**: `LLM` `MoE` `Fine-tuning` `Task Adaptation`
- **一句话**: 通过正确性条件任务专家发现+令牌级监督分配，在18个设置中的17个达到最佳性能。

### 3. Autonomy-of-Heads (AoH): Data-Free Attention Head Diagnosis via Spectral Geometry
- **链接**: https://arxiv.org/abs/2608.06849
- **标签**: `LLM` `Long Context` `Attention` `Efficiency`
- **一句话**: 通过查询-键投影的谱几何无数据识别检索头和流式头，50%稀疏度下保留96.5%性能。

### 4. Learning to Predict Middle-Layer Attention in MLLMs for Visual Token Pruning
- **链接**: https://arxiv.org/abs/2608.06411
- **标签**: `MLLM` `VLM` `Efficiency` `Token Pruning`
- **一句话**: 用轻量级预测器蒸馏中间层注意力，仅保留5.56%视觉令牌即达97.5%性能，实现3.09x端到端加速。

### 5. Sharding Prevents LLM Oversight Failures and Adversarial Exploitation
- **链接**: https://arxiv.org/abs/2608.06422
- **标签**: `LLM` `Safety` `Oversight` `Adversarial`
- **一句话**: 发现单次调用返回多个verdict时LLM judge性能下降，提出分片（sharding）策略将要求分组并行判断，弱judge可胜强judge。

---

## 🤖 Agent 与多智能体系统

### 6. ADIAS: Automated Design of Interactive Agentic Systems
- **链接**: https://arxiv.org/abs/2608.06410
- **标签**: `Agent` `AutoML` `System Design` `Code Agent`
- **一句话**: 以问题为中心的自动化Agent设计框架，用持久化问题状态替代候选中心策略，在5个交互基准上平均提升25.2%。

### 7. PHASE-Tree: Multi-Timescale Character State Tree for Long-Horizon Role-Playing
- **链接**: https://arxiv.org/abs/2608.06975
- **标签**: `Agent` `Role-Playing` `Memory` `Long Context`
- **一句话**: 多时间尺度角色状态树（身份根→人格层→会话层→时刻层），支持局部更新而不破坏未改变特质。

### 8. Do AI Personas Grow? Analyzing Personality Evolution in LLM Agents After Life Events
- **链接**: https://arxiv.org/abs/2608.06485
- **标签**: `Agent` `Personality` `Lifelong` `Psychology`
- **一句话**: 系统评估11种重大生活事件后LLM Agent的人格演变，发现当前模型模拟了人格动态的均值而非形状。

### 9. LLM Knowledge Graph Generation for HR Expertise Declarations
- **链接**: https://arxiv.org/abs/2608.07023
- **标签**: `LLM` `Agent` `Knowledge Graph` `HR`
- **一句话**: 混合KG生成管道，将LLM锚定在Wikidata多语言KG中，用agentic reflexion模式合成新兴概念。

---

## 🔍 RAG 与检索增强

### 10. CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context RAG
- **链接**: https://arxiv.org/abs/2608.07458
- **标签**: `RAG` `Long Context` `KV Cache` `Efficiency`
- **一句话**: 通过细粒度信息块缓存重用，优化长上下文RAG的Pareto前沿（速度vs精度）。

### 11. LitTraceQA: Scientific Literature Grounded QA Benchmark
- **链接**: https://arxiv.org/abs/2608.07370
- **标签**: `RAG` `QA` `Scientific Literature` `Benchmark`
- **一句话**: 科学文献grounded QA基准，要求系统返回论文标识符、证据位置和答案，严格评估检索能力。

### 12. Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Document-Search (READ)
- **链接**: https://arxiv.org/abs/2608.06305
- **标签**: `RAG` `Agent` `Document Search` `Financial`
- **一句话**: 在780页政府财报上，传统稠密检索仅15.7%准确率，READ通过MCP暴露的确定性操作达58.8%。

### 13. Visual RAG for Diffusion Language Models: The Entropy-Based Candidate Filter
- **链接**: https://arxiv.org/abs/2608.07006
- **标签**: `RAG` `Multimodal` `Diffusion LM` `VLM`
- **一句话**: 发现扩散语言模型中无条件传递所有检索页面反而降低准确率，提出熵基候选过滤器ECF解决语义冲突。

---

## 🧠 推理与思维链

### 14. Two-Hop Generalization in Transformers: A Mechanistic Analysis
- **链接**: https://arxiv.org/abs/2608.07261
- **标签**: `LLM` `Reasoning` `Mechanistic Analysis` `CoT`
- **一句话**: 在可控符号环境中训练transformer，揭示两跳泛化完整机制：第二跳遵循训练分布时可靠泛化，偏离时必然失败。

### 15. Simple-OPD: Demystifying Warm-Up for On-Policy Distillation
- **链接**: https://arxiv.org/abs/2608.06802
- **标签**: `LLM` `Distillation` `CoT` `Training`
- **一句话**: 发现OPD预热的核心在于传递教师兼容的思维链模式而非正确答案，甚至错误rollout也能提供相当收益。

### 16. FutureBridge: Token-Level LLM-SLM Collaboration
- **链接**: https://arxiv.org/abs/2608.06819
- **标签**: `LLM` `SLM` `Collaboration` `Reasoning`
- **一句话**: 不依赖LLM局部偏好，而是评估候选令牌对SLM后续推理的支持程度来进行联合排名。

### 17. Test-Time Scaling for Text-to-SQL: The Crystallization Problem
- **链接**: https://arxiv.org/abs/2608.07213
- **标签**: `LLM` `Test-Time Scaling` `SQL` `Memory`
- **一句话**: 提出"结晶化问题"框架，区分test-time scaling中记忆回放的复现价值与对新问题的帮助价值。

### 18. NTDH: Complex Reasoning for Comprehensive Affective Analysis
- **链接**: https://arxiv.org/abs/2608.06425
- **标签**: `LLM` `Reasoning` `GRPO` `SFT`
- **一句话**: 将情感分析重构为复杂推理问题，用SFT+GRPO训练Qwen3-8B，仅用14x更少数据达最强EI-reg结果(Pearson 0.862)。

---

## 🎯 知识、评估与基准

### 19. GPTKB 2.0: Large-Scale Disambiguated Knowledge Base from LLM
- **链接**: https://arxiv.org/abs/2608.06992
- **标签**: `LLM` `Knowledge Graph` `KB` `Disambiguation`
- **一句话**: 3800万三元组覆盖160万实体，支持上下文引导的实体消歧，同义词合并，提供可检查的Web演示。

### 20. Concept Understanding in LLMs: A Concept-Centric Benchmark
- **链接**: https://arxiv.org/abs/2608.07353
- **标签**: `LLM` `Concept Understanding` `Benchmark` `Cognition`
- **一句话**: 设计概念中心基准测试LLM在空间概念上的抽象、组合和基础性理解能力。

### 21. xRouteBench: A Unified Benchmark for LLM Routing
- **链接**: https://arxiv.org/abs/2608.06867
- **标签**: `LLM` `Routing` `Cost-Effective` `Benchmark`
- **一句话**: 统一LLM路由形式化为序贯决策过程，覆盖多种路由任务的自动化评估管道。

### 22. Ekphrasis: Visual Creative Ideation Benchmark for Language Models
- **链接**: https://arxiv.org/abs/2608.06967
- **标签**: `LLM` `Multimodal` `Creativity` `Benchmark`
- **一句话**: 400任务基准评估语言模型产生文本视觉计划的能力，覆盖抽象、组合、变换和适应四种创造性模式。

### 23. GEB-Bench: Abstract Structures Told in Many Voices
- **链接**: https://arxiv.org/abs/2608.04111
- **标签**: `Multimodal` `Reasoning` `Benchmark` `Abstraction`
- **一句话**: 以Gödel-Escher-Bach精神设计的跨模态抽象结构基准，发现模型在单一模态内识别结构远强于跨模态映射。

---

## 🎨 多模态与创造力

### 24. CreativeInstruct: Scalably Teaching LLMs to Balance Quality, Creativity, and Diversity
- **链接**: https://arxiv.org/abs/2608.07460
- **标签**: `LLM` `Creativity` `Instruction Tuning` `RL`
- **一句话**: 通过注入[StartCreativity]跨度，在训练时显式标注创造性区域，平衡质量、创造性和多样性。

### 25. Predicting Gaze in Visual World Studies via Multimodal Attribution
- **链接**: https://arxiv.org/abs/2608.07282
- **标签**: `Multimodal` `VLM` `Psycholinguistics` `Attention`
- **一句话**: 结合CLIP编码器和双模态归因方法，预测视觉世界研究中的凝视行为，融合语言学与视觉输入。

---

## 🔐 安全、偏见与可解释性

### 26. LLM Susceptibility to Prompt Framing and Suggestive Prompting
- **链接**: https://arxiv.org/abs/2608.06977
- **标签**: `LLM` `Prompt Engineering` `Safety` `Bias`
- **一句话**: 评估6个LLM对160种提示框的敏感性，发现模型在事实语境中也会适应提示框架，揭示隐含框架效应与显式操纵的边界。

### 27. Latent Fact-Checking: Detecting Misinformation through Activation Engineering
- **链接**: https://arxiv.org/abs/2608.06417
- **标签**: `LLM` `Interpretability` `Safety` `Misinformation`
- **一句话**: 通过对比激活工程在残差流中提取虚假方向，无需微调或外部检索即可检测错误信息。

### 28. Extracting Internal LLM Knowledge for Concept Content Measurement
- **链接**: https://arxiv.org/abs/2608.07208
- **标签**: `LLM` `Knowledge Extraction` `Interpretability` `ESG`
- **一句话**: 通过监控冻结LLM的激活来替代任务特定微调，测量文本的概念内容。

### 29. Beyond Routing Weights: Faithful Interpretation of MoE Reward Models
- **链接**: https://arxiv.org/abs/2608.06400
- **标签**: `MoE` `Reward Model` `Interpretability` `RLHF`
- **一句话**: 提出CoCo贡献对比方法，用选择-拒绝响应对中贡献差异最大的样本来忠实刻画MoE奖励模型专家的角色。

---

## 📊 扩展与训练

### 30. Skaling Law: Generalized Neural Scaling Law with Interaction Exponent
- **链接**: https://arxiv.org/abs/2608.07222
- **标签**: `LLM` `Scaling Law` `Training`
- **一句话**: 通过单一交互指数耦合模型容量和数据，将MAPE降低1.5-3x，更准确预测数据稀缺和过训练极端情况。

### 31. WebGrader: Training LLMs for Web Development with Self-Evolving Programmatic Grader
- **链接**: https://arxiv.org/abs/2608.06474
- **标签**: `LLM` `Training` `Web Development` `Self-Evolving`
- **一句话**: 用自演化程序化评分器训练LLM进行Web开发，自动评估和反馈循环驱动能力迭代。

---

## 📈 本周趋势洞察

**强信号：**
- **MoE架构**持续热门（3篇）：EntropyMoE、TEXAS、CoCo，专家路由与可解释性成为焦点
- **Agent系统设计**走向自动化（ADIAS）：从候选中心转向问题中心的优化范式
- **RAG与长上下文**仍是核心战场：CoinRAG的KV缓存重用、READ的确定性文档搜索
- **推理机制**深入研究：两跳推理的完整机制揭示、test-time scaling的结晶化问题

**值得关注：**
- 分片（Sharding）策略对LLM judge安全性的提升（安全方向新思路）
- 扩散语言模型在视觉RAG中的独特行为（语义冲突问题）
- 人格化Agent的长期一致性（PHASE-Tree + AI Personas Grow）

---

*共收录 31 篇候选论文 | 生成时间: 2026-08-11 10:00 CST*
