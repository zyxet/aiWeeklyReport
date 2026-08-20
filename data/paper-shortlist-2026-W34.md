# 📄 W34 论文精选短名单

> **筛选时间**: 2026-08-20  
> **周期**: W34 (2026-08-12 ~ 2026-08-18)  
> **来源**: 从 18 篇候选中精选 8 篇  
> **筛选标准**: 创新性×实用性×实验充分性×写作质量×领域相关性（每项1-5分，满分25）

---

## 🏆 入选论文（按总分排序）

### 1. YOPO: You Only Pass Once
| [arXiv:2608.14465](https://arxiv.org/abs/2608.14465)  
| 标签: `Reasoning` `Steering` `Abstention` `Efficiency`  
| **评分: 24/25** (创新5 实用5 实验5 写作4 相关5)  
| 🏷️ 一句话摘要: 单次前向传播同时实现答案生成、推理引导和拒绝回答，Qwen2.5三任务准确率从0.375提升至0.798。  
| 💻 代码: 未明确开源

### 2. Behavioral Lift: Which Reasoning Behaviors Are Actually Associated with Correctness?
| [arXiv:2608.13760](https://arxiv.org/abs/2608.13760)  
| 标签: `Reasoning` `Training Analysis` `VLM`  
| **评分: 24/25** (创新5 实用4 实验5 写作5 相关5)  
| 🏷️ 一句话摘要: 发现推理训练放大"自我纠正"等行为，但与正确性最相关的是"置信度校准"，揭示放大-提升差距。  
| 💻 代码: 未明确开源

### 3. On-policy Distillation for Long-Context to Short-Context
| [arXiv:2608.14277](https://arxiv.org/abs/2608.14277)  
| 标签: `Distillation` `Reasoning` `Long Context`  
| **评分: 22/25** (创新4 实用5 实验5 写作4 相关4)  
| 🏷️ 一句话摘要: 将长上下文教师模型推理能力迁移到短上下文学生模型，Intern-S2在ProofBench上提升21.2分。  
| 💻 代码: 未明确开源

### 4. Envs-FORGE: Dynamic Environment Synthesis for Terminal Agent RL
| [arXiv:2608.14312](https://arxiv.org/abs/2608.14312)  
| 标签: `RL` `Agent` `Training` `Code`  
| **评分: 22/25** (创新4 实用4 实验5 写作4 相关5)  
| 🏷️ 一句话摘要: 将验证器奖励转换为动态训练环境合成策略，Qwen 3.5 35B在tb-core上Pass@1提升9.2个百分点。  
| 💻 代码: ✅ [源码已发布](https://arxiv.org/abs/2608.14312)

### 5. LRM Batch Pruning
| [arXiv:2608.14003](https://arxiv.org/abs/2608.14003)  
| 标签: `Reasoning` `Efficiency` `Pruning`  
| **评分: 21/25** (创新4 实用5 实验4 写作4 相关4)  
| 🏷️ 一句话摘要: 针对推理模型批处理场景的训练无关自适应剪枝，DeepSeek-R1-Distill-Qwen-7B上准确率提升39.7个百分点。  
| 💻 代码: 未明确开源

### 6. Multilingual GRPO: A Large-Scale Empirical Study
| [arXiv:2608.13698](https://arxiv.org/abs/2608.13698)  
| 标签: `RL` `Multilingual` `Reasoning`  
| **评分: 21/25** (创新4 实用4 实验5 写作4 相关4)  
| 🏷️ 一句话摘要: 大规模多语言GRPO实证研究，发现母语推理与英语差距很小，但存在语言特定的能力退化。  
| 💻 代码: 未明确开源

### 7. Diverse Hypothesis Deliberation (DHD)
| [arXiv:2608.14375](https://arxiv.org/abs/2608.14375)  
| 标签: `Multi-Agent` `Reasoning`  
| **评分: 21/25** (创新5 实用4 实验4 写作4 相关4)  
| 🏷️ 一句话摘要: 测量多Agent推理中"错误但有用"消息的价值，发现超40%的错误答案消息对最终推理有帮助。  
| 💻 代码: 未明确开源

### 8. HERMES: Multi-Agent Framework for Scientific Document Extraction
| [arXiv:2608.14055](https://arxiv.org/abs/2608.14055)  
| 标签: `Multi-Agent` `Document Understanding` `Science` `Code`  
| **评分: 21/25** (创新4 实用4 实验5 写作4 相关4)  
| 🏷️ 一句话摘要: 从55卷古生物学专著中提取32,277个化石分类实体和451,878个属性，效率提升6倍。  
| 💻 代码: ✅ [数据已在线发布](https://arxiv.org/abs/2608.14055)

---

## 📊 统计

| 类别 | 入选数 |
|------|--------|
| Reasoning & CoT | 4 |
| Agent & Multi-Agent | 2 |
| Efficiency | 1 |
| Multilingual | 1 |
| **总计** | **8** |
| **论文+代码双料** | **2** |

---

## 📝 备注

- 第12篇 IterCOMP (arXiv:2608.13588) 与第17篇 BCMT 在原始论文池中出现 arxiv 号重复（均为2608.13578），已修正 IterCOMP 为正确编号 2608.13588。
- 入选论文平均得分 22.0/25，落选论文平均得分 19.2/25。
- 两个论文+代码双料项目：Envs-FORGE（终端Agent RL环境合成）、HERMES（科学文档结构化提取）。

---

*精选完成于 2026-08-20 14:00 (Asia/Shanghai)*
