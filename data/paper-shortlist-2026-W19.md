# 2026-W19 论文精选短名单

> **周号**: 2026-W19（2026年5月4日–5月10日）  
> **评选日期**: 2026-05-07  
> **候选池规模**: 23篇  
> **入选数量**: 8篇  
> **评选标准**: 创新性(5)、实用性(5)、技术深度(5)、机构背书(5)、代码可得性(5)，总分25分

---

## 🏆 TOP 8 精选论文

### 1. SAGE: Strategy-Aware Optimization Modeling with Reasoning LLMs (★21分)

| 项目 | 内容 |
|------|------|
| **arXiv** | 2605.02545 |
| **标题** | SAGE: Strategy-Aware Optimization Modeling with Reasoning LLMs |
| **作者** | Ruiqing Zhao, Fengzhi Li, Yuan Zuo, Rui Liu, Yansong Liu, Yunfei Ma, et al. |
| **机构** | 南京大学, 华中科技大学 |
| **一句话摘要** | 面向运筹优化建模的策略感知框架，显式建模策略选择提升72.7%→80.3%的pass@1精度，压缩约束规模14.2%。 |
| **代码** | ✅ 官方开源 [github.com/rachhhhing/SAGE](https://github.com/rachhhhing/SAGE) |
| **开源池关联** | ⚡ **双料项目**（论文+代码均在本周候选池） |

**评分详情**:
| 维度 | 得分 | 理由 |
|------|------|------|
| 创新性 | 4 | 首次将"建模策略"显式纳入LLM训练，Segment-Weighted GRPO新奖励设计 |
| 实用性 | 5 | 直接面向生产级优化建模，覆盖合成/真实场景，8个基准测试 |
| 技术深度 | 4 | solver-verified数据构建，多策略对比验证充分 |
| 机构背书 | 4 | 南京大学+华中科技大学，国内运筹优化强校 |
| 代码可得性 | 4 | GitHub已开源，但文档完整度待验证 |

---

### 2. HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness (★20分)

| 项目 | 内容 |
|------|------|
| **arXiv** | 2605.02709 |
| **标题** | HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness |
| **作者** | Jianing Wang, Yunlong Feng, Runnan Fang, Ailing Zhang, Chenxu Wang, Haipeng Luo, et al. |
| **机构** | 南京大学 |
| **一句话摘要** | 测试时扩展新范式：并行推理+自适应融合，以"重思考"内技能驱动智能体推理边界突破。 |
| **代码** | ✅ 官方开源 [github.com/wjn1996/HeavySkill](https://github.com/wjn1996/HeavySkill)（Apache-2.0） |
| **开源池关联** | ⚡ **双料项目**（论文+代码均在本周候选池） |

**评分详情**:
| 维度 | 得分 | 理由 |
|------|------|------|
| 创新性 | 4 | 测试时扩展的分解式新范式，区别于传统CoT/ToT |
| 实用性 | 4 | 可插拔到现有LLM推理流程，但需较多计算资源 |
| 技术深度 | 4 | 并行推理+自适应融合机制，理论框架完整 |
| 机构背书 | 4 | 南京大学，国内NLP强校 |
| 代码可得性 | 4 | Apache-2.0开源，仓库活跃 |

---

### 3. ORPilot: Leveraging LLMs for Generalizable End-to-End Optimization Modeling (★19分)

| 项目 | 内容 |
|------|------|
| **arXiv** | 2605.02751 |
| **标题** | ORPilot: Leveraging LLMs for Generalizable End-to-End Optimization Modeling |
| **作者** | Guangrui Xie, Jianhua Liu, Yankai Wu, Zhi Zheng, Dongdong Wang, Shengsheng Wang, et al. |
| **机构** | 中国科学技术大学, 华为诺亚方舟实验室 |
| **一句话摘要** | 端到端运筹优化建模代理，打通问题描述→数学建模→求解器调用全流程，覆盖6类经典问题。 |
| **代码** | ❌ 未找到官方代码仓库 |

**评分详情**:
| 维度 | 得分 | 理由 |
|------|------|------|
| 创新性 | 4 | 端到端优化建模闭环，6类问题统一框架 |
| 实用性 | 5 | 直接面向OR领域实际建模需求，与华为诺亚合作 |
| 技术深度 | 4 | 覆盖线性/整数/组合优化，实验验证充分 |
| 机构背书 | 5 | 中科大+华为诺亚方舟，产学研结合 |
| 代码可得性 | 1 | 无公开代码 |

---

### 4. CASA: Context-Aware Secure Agentic AI Access Control (★18分)

| 项目 | 内容 |
|------|------|
| **arXiv** | 2605.02682 |
| **标题** | CASA: Context-Aware Secure Agentic AI Access Control |
| **作者** | Christopher Berl, Yi Liu, Jinzhuo Luo, Bang Huang, Leilei Gan, Jing Yu, et al. |
| **机构** | 蚂蚁集团, 新加坡管理大学 |
| **一句话摘要** | 面向智能体AI的上下文感知零信任访问控制框架，为自主智能体系统提供动态安全策略引擎。 |
| **代码** | ❌ 未找到官方代码仓库 |

**评分详情**:
| 维度 | 得分 | 理由 |
|------|------|
| 创新性 | 4 | 首个面向Agentic AI的上下文感知访问控制框架 |
| 实用性 | 5 | 直接面向企业级AI安全部署需求，蚂蚁集团背书 |
| 技术深度 | 4 | 零信任架构+动态策略，理论框架完整 |
| 机构背书 | 4 | 蚂蚁集团+新加坡管理大学 |
| 代码可得性 | 1 | 无公开代码 |

---

### 5. SCHEMA: An Evaluation Benchmark for Avoiding Cognitive Collapse in Frontier Models (★18分)

| 项目 | 内容 |
|------|------|
| **arXiv** | 2605.02411 |
| **标题** | SCHEMA: An Evaluation Benchmark for Avoiding Cognitive Collapse in Frontier Models |
| **作者** | Michael Roman, Nikhil Patel, Marco Gori, Claudio Gentili, Giuseppe Marra, et al. |
| **机构** | 意大利比萨大学, 国际高等研究院(SISSA) |
| **一句话摘要** | 诊断前沿模型"认知塌陷"（过度依赖模式匹配）的基准测试，覆盖6大前沿模型准确率仅19.7%。 |
| **代码** | ❌ 未找到官方代码仓库 |

**评分详情**:
| 维度 | 得分 | 理由 |
|------|------|
| 创新性 | 4 | 提出"认知塌陷"新评估维度，区别于传统benchmark |
| 实用性 | 4 | 对模型安全部署有重要参考价值 |
| 技术深度 | 4 | 多维度评估框架，6模型对比实验 |
| 机构背书 | 4 | 意大利顶尖研究机构 |
| 代码可得性 | 2 | 文中未明确提及代码 |

---

### 6. DataClaw: A Process-Oriented Agent Benchmark for Exploratory Real-World Data Analysis (★18分)

| 项目 | 内容 |
|------|------|
| **arXiv** | 2605.02503 |
| **标题** | DataClaw: A Process-Oriented Agent Benchmark for Exploratory Real-World Data Analysis |
| **作者** | Qiaohong Zhang, Weihao Ye, Jialong Chen, Yi Luo, BoYuan Li, Bowen Deng, et al. |
| **机构** | 浙江大学, 香港科技大学, 南加州大学 |
| **一句话摘要** | 面向探索性真实数据分析的过程导向基准，206万真实记录+492跨域任务，揭示当前智能体准确率不足50%。 |
| **代码** | ❌ 未找到官方代码仓库 |

**评分详情**:
| 维度 | 得分 | 理由 |
|------|------|
| 创新性 | 4 | 过程级评估（中间里程碑），区别于结果导向benchmark |
| 实用性 | 5 | 直接面向企业数据分析需求，数据规模真实 |
| 技术深度 | 4 | 多领域覆盖，任务设计源自智库咨询场景 |
| 机构背书 | 4 | 浙大+港科大+USC |
| 代码可得性 | 1 | 无公开代码 |

---

### 7. AcademiClaw: When Students Set Challenges for AI Agents (★18分)

| 项目 | 内容 |
|------|------|
| **arXiv** | 2605.02669 |
| **标题** | AcademiClaw: When Students Set Challenges for AI Agents |
| **作者** | Yantao Liu, Yijie Liu, Zeyuan Yang, Weiran Wang, Peng Li, Jianing Wang, et al. |
| **机构** | 复旦大学, 香港大学 |
| **一句话摘要** | 由大学生出题的双语学术任务基准，80个真实学术场景检验AI智能体的高等教育辅助能力。 |
| **代码** | ✅ 官方开源 [github.com/GAIR-NLP/AcademiClaw](https://github.com/GAIR-NLP/AcademiClaw) |
| **开源池关联** | ⚡ **双料项目**（论文+代码均在本周候选池） |

**评分详情**:
| 维度 | 得分 | 理由 |
|------|------|
| 创新性 | 3 | 学生出题的众包模式，但方法论创新有限 |
| 实用性 | 4 | 直接面向学术辅助场景，双语支持 |
| 技术深度 | 4 | 80任务覆盖广泛学术场景，评估维度多 |
| 机构背书 | 4 | 复旦+港大 |
| 代码可得性 | 3 | GitHub开源，但Star数较少 |

---

### 8. Position: How can Graphs Help Large Language Models? (★17分)

| 项目 | 内容 |
|------|------|
| **arXiv** | 2605.02452 |
| **标题** | Position: How can Graphs Help Large Language Models? |
| **作者** | Xiyuan Wang, Yi Hu, Yanbo Wang, Chuan Shi, Muhan Zhang |
| **机构** | 北京邮电大学 |
| **一句话摘要** | 从知识更新、推理增强、结构化理解三维度论证图技术对LLM的补充价值，展望稀疏架构与脑启发记忆系统。 |
| **代码** | ❌ 观点/综述论文，无代码 |

**评分详情**:
| 维度 | 得分 | 理由 |
|------|------|
| 创新性 | 4 | 提出图-LLM互补新视角，展望稀疏架构 |
| 实用性 | 3 | 理论框架为主，落地路径需进一步探索 |
| 技术深度 | 4 | 三维度系统论证，引用丰富 |
| 机构背书 | 3 | 北京邮电大学 |
| 代码可得性 | 3 | 综述论文，无代码但提供方向性指引 |

---

## 📊 评分总览

| 排名 | arXiv | 标题 | 总分 | 代码 | 双料 |
|------|-------|------|------|------|------|
| 1 | 2605.02545 | SAGE: Strategy-Aware Optimization Modeling | **21** | ✅ | ⚡ |
| 2 | 2605.02709 | HeavySkill: Heavy Thinking as Inner Skill | **20** | ✅ | ⚡ |
| 3 | 2605.02751 | ORPilot: End-to-End Optimization Modeling | **19** | ❌ | - |
| 4 | 2605.02682 | CASA: Secure Agentic AI Access Control | **18** | ❌ | - |
| 5 | 2605.02411 | SCHEMA: Avoiding Cognitive Collapse | **18** | ❌ | - |
| 6 | 2605.02503 | DataClaw: Exploratory Data Analysis Benchmark | **18** | ❌ | - |
| 7 | 2605.02669 | AcademiClaw: Student Challenges for AI Agents | **18** | ✅ | ⚡ |
| 8 | 2605.02452 | How can Graphs Help LLMs? | **17** | - | - |

---

## 🔗 开源池关联

本周开源候选池中有 **3个** 项目与精选论文形成"论文+代码"双料组合：

| 论文 | 代码仓库 | 匹配度 |
|------|----------|--------|
| SAGE (2605.02545) | [github.com/rachhhhing/SAGE](https://github.com/rachhhhing/SAGE) | 完全匹配 |
| HeavySkill (2605.02709) | [github.com/wjn1996/HeavySkill](https://github.com/wjn1996/HeavySkill) | 完全匹配 |
| AcademiClaw (2605.02669) | [github.com/GAIR-NLP/AcademiClaw](https://github.com/GAIR-NLP/AcademiClaw) | 完全匹配 |

---

## 📝 淘汰论文（15篇）

以下论文因总分较低或主题偏离未入选：

| arXiv | 标题 | 淘汰原因 |
|-------|------|----------|
| 2605.02427 | Graph as a Value-Added Knowledge Interface for LLM-Based Agents | 实用性偏低，框架概念阶段 |
| 2605.02395 | PolicyCast: Fine-Tuning Discrete Action Policies | 评分中等，领域较窄 |
| 2605.02442 | Rethinking Generalization in Reasoning SFT | 实验规模有限，验证不足 |
| 2605.02572 | Test-Time Credit Assignment in LLMs | 理论贡献为主，实用场景不清 |
| 2605.02489 | Ternary Retrieval Distillation | 技术路径较窄，应用范围有限 |
| 2605.02398 | Increasing Robustness of Constraint Solvers | 领域专精，通用性不足 |
| 2605.02832 | Making Large Language Models Better Table Reasoners | 已有类似工作，增量创新 |
| 2605.02661 | KG2Causal: Knowledge-Graph-Conditioned Causal Graphs | 技术组合常规，无突破性 |
| 2605.02728 | Fine-tuning of Causal LLMs via Mutual Information | 理论深度不足，实验规模小 |
| 2605.02765 | Automated Knowledge Extraction for Digital Twins | 应用特定，通用性有限 |
| 2605.02396 | Diffusion Models for Zero-Shot Object Detection | 领域特定，非本周关注重点 |
| 2605.02819 | Neural Space-Time Dilated Extreme Residual Model | 领域偏CV，偏离AI Agent主线 |
| 2605.02860 | Biomedical Knowledge Distillation via Prompt Tuning | 领域特定（生物医学），偏离主线 |
| 2605.02603 | Diffusion Model Based Any-to-Any Infrared-Visible Fusion | CV领域，偏离本周主题 |
| 2605.02592 | Object-Centric Diffusion for Efficient Video Editing | CV领域，偏离本周主题 |

---

## 💡 本周趋势洞察

1. **运筹优化+LLM成为热点**：SAGE、ORPilot、SAGE均聚焦运筹优化建模，LLM+OR交叉领域爆发
2. **Benchmark建设活跃**：DataClaw、SCHEMA、AcademiClaw三个benchmark聚焦不同维度评估智能体
3. **安全与控制受关注**：CASA聚焦Agentic AI安全访问控制，预示智能体安全成为新战场
4. **开源配套率33%**：8篇入选论文中3篇有官方代码，开源生态逐步完善

---

*本文件由 Kimi Claw 自动生成，数据来源：arXiv API + kimi_fetch 混合采集*
