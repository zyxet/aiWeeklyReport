# 🎯 论文精选短名单（2026-W38）

> 精选日期：2026-09-17 周四
> 来源：paper-pool-2026-W38.md（49篇候选）
> 筛选标准：创新性、实用性、技术深度、机构背书、代码可得性（每项1-5分，总分25分）
> 结果：保留8篇

---

## 🏆 精选论文（按总分排序）

### 1. AMDKernelVault: Open HIP and Triton Kernel Corpus and Training Framework for AMD CDNA GPUs
- **arXiv**: https://arxiv.org/abs/2609.12471
- **标签**: `GPU Kernel` `Code Generation` `AMD` `Open Source`
- **中文摘要（50字内）**: 首个AMD GPU开源算子语料库，含6.2万HIP与4万Triton内核，训练Qwen3-8B达最优正确率。
- **评分**: 创新性4 | 实用性4 | 技术深度4 | 机构背书4 | 代码可得性5 = **21/25**
- **代码**: ⭐ **论文+代码双料**（语料库+训练代码+生成管线均开源）
- **推荐理由**: 填补AMD GPU生态空白——现有内核生成智能体以CUDA/NVIDIA为中心，本文构建6.2万执行验证HIP内核语料库，SFT+执行感知RL训练后在PyTorch-to-HIP和TritonBench-G上取得最高正确率。开源力度大，实用价值极高。

---

### 2. ZipBench: Simple, Low-Cost, and Theoretically Grounded Benchmark Compression
- **arXiv**: https://arxiv.org/abs/2609.12475
- **标签**: `Benchmark` `Evaluation Efficiency` `LLM Evaluation` `Open Source`
- **中文摘要（50字内）**: 低成本基准压缩框架，仅用少量锚点LLM构建100+紧凑基准，Spearman相关达0.98且代码开源。
- **评分**: 创新性4 | 实用性5 | 技术深度4 | 机构背书4 | 代码可得性4 = **21/25**
- **代码**: ⭐ **论文+代码双料**（ZipBench Zoo已发布，含100+压缩基准）
- **推荐理由**: 解决评估成本痛点——传统基准冗余导致评估浪费，ZipBench仅用少量锚点LLM+伪评估合成即实现MAE 0.002-0.02、Spearman ~0.98的压缩效果，附带理论误差和排名一致性保证，对算力受限研究者极其友好。

---

### 3. SoK: Jailbreaking Attacks and Defenses in the Era of Modern LLMs and Agentic AI
- **arXiv**: https://arxiv.org/abs/2609.12413
- **标签**: `AI Safety` `Jailbreak` `Agentic Security` `SoK`
- **中文摘要（50字内）**: 系统化综述Agent时代越狱安全，发现最终响应过滤无法阻止中间层泄露，提出跨层执行感知防御框架。
- **评分**: 创新性4 | 实用性5 | 技术深度4 | 机构背书3 | 代码可得性3 = **20/25**
- **代码**: 🔍 待确认（统一Agent框架下实证，预计可复现）
- **推荐理由**: Agent安全必读——覆盖用户交互、规划推理、记忆、工具调用、Agent间通信全链路攻击防御分类，三大关键发现：强原生对齐≠抗越狱、防御效果高度依赖模型/攻击/组件、低最终响应攻击成功率可掩盖严重中间层沦陷。推动从响应中心防御转向跨层执行感知安全。

---

### 4. BlueLM-GUI: A Real-Device-Centric Flywheel for Building Mobile GUI Agents
- **arXiv**: https://arxiv.org/abs/2609.12394
- **标签**: `GUI Agent` `Mobile` `Reinforcement Learning` `VLM`
- **中文摘要（50字内）**: 35B-A3B移动端GUI智能体，真机训练飞轮闭环，MobileGUI-VBench达87.4分超越最强闭源模型5.1分。
- **评分**: 创新性4 | 实用性5 | 技术深度4 | 机构背书4 | 代码可得性3 = **20/25**
- **代码**: 🔍 待确认（模型在开源模型中最佳，预计模型权重开源）
- **推荐理由**: 工业级GUI智能体训练范式——"Every Sample Matters + Every Rollout Is Real + Every Query Evolves"三原则解决沙箱训练与生产环境分布不匹配、真机失败样本利用不足、基准饱和三大痛点。在数百台真机上进行Agentic RL训练，效果直接可迁移到部署。

---

### 5. K-Bench: Scoring LLM Unlearning under Agentic Deployment
- **arXiv**: https://arxiv.org/abs/2609.12808
- **标签**: `Unlearning` `Privacy` `Agent Evaluation` `Benchmark`
- **中文摘要（50字内）**: 首个Agent部署下遗忘评测基准，6通道检测秘密泄露，发现权重中秘密无法被现有20种方法真正移除。
- **评分**: 创新性5 | 实用性4 | 技术深度4 | 机构背书3 | 代码可得性3 = **19/25**
- **代码**: 🔍 待确认（基准框架，预计开源）
- **推荐理由**: 视角独到——现有遗忘基准（TOFU/MUSE）仅在模型层面验证遗忘，部署为Agent后证书不再适用。K-Bench检查ReAct Agent全部6个通道（CoT、工具调用、观察、摘要等），发现秘密在Prompt/检索库中时泄露率仍达22-86%，权重中的秘密20种已发表方法均无法真正移除。

---

### 6. TAM: Tasks over Application Manuals for Evaluating Long-Horizon Procedural Reasoning
- **arXiv**: https://arxiv.org/abs/2609.13005
- **标签**: `Benchmark` `Long-horizon Reasoning` `Procedural QA` `Open Source`
- **中文摘要（50字内）**: 评估LLM遵循数百页规则手册的多步程序推理，GPT-5精确匹配仅1-15%，揭示当前基准高估推理能力。
- **评分**: 创新性4 | 实用性4 | 技术深度4 | 机构背书3 | 代码可得性4 = **19/25**
- **代码**: ⭐ **论文+代码双料**（数据和代码公开发布）
- **推荐理由**: 诊断精准——从ICD-10-CM临床编码和美国联邦量刑的真实手册构建任务，需执行跨章节依赖的多步推理才能得到精确答案。GPT-5最佳精确匹配仅1%（ICD-10）和15.5%（量刑），RAG/ReAct/Agent框架均无法有效解决，暴露LLM推理能力的真实边界。

---

### 7. CoG: Cognition on Graph — Training-Free Adaptive Knowledge Exploration for Multi-Hop QA
- **arXiv**: https://arxiv.org/abs/2609.12791
- **标签**: `RAG` `Knowledge Graph` `Multi-hop QA` `Open Source`
- **中文摘要（50字内）**: 免训练认知启发知识探索框架，图-文双向深度协同，7个多跳QA基准显著超越现有方法。
- **评分**: 创新性4 | 实用性4 | 技术深度4 | 机构背书3 | 代码可得性4 = **19/25**
- **代码**: ⭐ **论文+代码双料**（代码和数据集已开源）
- **推荐理由**: 受人类问题解决的plan-explore-reflect认知循环启发，实现结构化图与非结构化文本的深度双向协同——文本中抽取的实体动态引导图探索弥合知识缺口。免训练、探索效率高，7个多跳QA基准全面超越SOTA，是Graph RAG方向的高质量工作。

---

### 8. SAS: Simple Attention Sparsification via Gated Sparse Attention
- **arXiv**: https://arxiv.org/abs/2609.13141
- **标签**: `Attention` `Long Context` `Efficiency` `Triton Kernel`
- **中文摘要（50字内）**: 门控稀疏注意力端到端优化上下文排序，紧预算下优势显著，实现FlashAttention风格高效Triton内核。
- **评分**: 创新性4 | 实用性4 | 技术深度5 | 机构背书3 | 代码可得性3 = **19/25**
- **代码**: 🔍 待确认（Triton内核提及，预计开源）
- **推荐理由**: 解决可训练稀疏注意力核心痛点——现有方法蒸馏密集注意力分布导致排序与预测影响不对齐。SAS通过将连续选择器分数注入注意力logits实现端到端优化，对数空间门控+归一化softmax门控+连续分数保留三个设计选择关键，紧预算下收益尤为显著。

---

## 📊 评选统计

| 维度 | 平均得分 |
|------|---------|
| 创新性 | 4.1/5 |
| 实用性 | 4.4/5 |
| 技术深度 | 4.3/5 |
| 机构背书 | 3.4/5 |
| 代码可得性 | 3.6/5 |

**入选率**: 8/49 (16.3%)
**双料项目（论文+代码）**: 4个（AMDKernelVault, ZipBench, TAM, CoG）

---

## 🗑️ 高分未入选论文（Top Excluded）

| # | 论文 | 总分 | 未入选原因 |
|---|------|------|-----------|
| 9 | GAUGE: Evaluating LLM-as-Judge Gates for Agent Selection | 18 | 分析型论文，发现重要但缺乏方法论贡献 |
| 10 | CCPS: Chopthin-Consensus Power Sampling for LLM Reasoning | 19 | SMC推理方法较niche，与SAS同分但适用面窄 |
| 11 | SynthSentry: Corpus-Level Synthetic Contamination Detection | 19 | 实用但实验规模偏小，结论外推性待验证 |
| 12 | Long-Context Recall via FFN Residual Vectors | 19 | 创新性极高但实用性依赖进一步工程验证 |
| 13 | RunningTensor: Higher-Order Recurrent Memory | 18 | 概念优雅但仅概念验证阶段 |

---

*Generated by thursday-paper-filter | Week 38, 2026*
