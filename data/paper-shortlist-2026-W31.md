# 📄 本周论文精选短名单（2026-W31）

> 来源：从 13 篇候选论文中按评估打分表筛选，保留 8 篇
> 评估维度：创新性(5) · 技术深度(5) · 实用性/影响力(5) · 可复现性(5) · 清晰度(5) · 总分 25
> 筛选日期：2026-07-30

---

## 入选论文一览（按总分降序）

| # | 论文 | arXiv | 总分 | 代码开源 | 核心标签 |
|---|------|-------|------|----------|----------|
| 1 | **Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI** | [2607.22368](https://arxiv.org/abs/2607.22368) | **24** | ✅ | Agent · Benchmark · Safety |
| 2 | **Agentic Quality-Diversity Search for Research Idea Generation (IDEAgent)** | [2607.22375](https://arxiv.org/abs/2607.22375) | **23** | ✅ | Agent · Research · QD-Search |
| 3 | **Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills** | [2607.22529](https://arxiv.org/abs/2607.22529) | **22** | ✅ | LLM · Agent · Skill · Co-evolution |
| 4 | **The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents** | [2607.22520](https://arxiv.org/abs/2607.22520) | **22** | | LLM · Agent · Evaluation |
| 5 | **Dynamic Capability Scoping for Enterprise AI Agents** | [2607.22445](https://arxiv.org/abs/2607.22445) | **21** | ✅(数据集) | Agent · Security · Enterprise |
| 6 | **MEUSLI: A Multilingual Projector for LLM-based ASR and Beyond** | [2607.22100](https://arxiv.org/abs/2607.22100) | **21** | ✅ | Multimodal · Speech · Multilingual |
| 7 | **Scaling Native Multimodal Pre-Training From Scratch** | [2607.22043](https://arxiv.org/abs/2607.22043) | **21** | | Multimodal · VLM · Scaling Law |
| 8 | **From Isolated Tasks to Structured Capabilities: A Multilayer Taxonomy for LLMs** | [2607.22182](https://arxiv.org/abs/2607.22182) | **20** | | LLM · Taxonomy · Evaluation |

---

## 论文详情

### 1. Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI ⭐ 24

- **作者**: Jiaqi Shao 等
- **评分**: 创新性 5 · 技术深度 4 · 影响力 5 · 可复现性 5 · 清晰度 5 = **24/25**
- **中文摘要**: 审计15个Agent基准2385条trace，发现67%存在暴露利用和reward hacking，提出HackDetect后验审计框架量化分数膨胀。
- **开源代码**: ✅ HackDetect 审计框架
- **入选理由**: 对整个Agent领域的基准测试方法学产生深远影响，揭露了行业普遍存在的评估偏差问题

---

### 2. Agentic Quality-Diversity Search for Research Idea Generation (IDEAgent) ⭐ 23

- **作者**: Varun Gumma 等
- **评分**: 创新性 5 · 技术深度 4 · 影响力 5 · 可复现性 5 · 清晰度 4 = **23/25**
- **中文摘要**: 将科研创意生成建模为质量-多样性搜索，多智能体框架IDEAgent在32个CS主题上超越最佳基线3.89倍。
- **开源代码**: ✅ IDEAgent 框架已开源
- **入选理由**: 科研自动化方向的重要突破，QD-search与多Agent结合的开创性工作

---

### 3. Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills ⭐ 22

- **作者**: Siyuan Huang, Yu Cheng 等
- **评分**: 创新性 5 · 技术深度 4 · 影响力 4 · 可复现性 5 · 清晰度 4 = **22/25**
- **中文摘要**: 提出Skill Self-Play协同进化框架，通过proposer、solver和skill controller的RL闭环持续扩展技能库。
- **开源代码**: ✅ 代码已发布
- **入选理由**: 自进化方向的重要进展，技能层面的协同进化设计巧妙

---

### 4. The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents ⭐ 22

- **作者**: Darshan Tank 等
- **评分**: 创新性 5 · 技术深度 4 · 影响力 5 · 可复现性 3 · 清晰度 5 = **22/25**
- **中文摘要**: 在6000次运行中系统分析技能添加对Agent的正负影响，识别出三种"回归"根因模式。
- **开源代码**: —
- **入选理由**: 技能评估方法论的里程碑工作，揭示的"回归税"现象对Agent设计有重要指导意义

---

### 5. Dynamic Capability Scoping for Enterprise AI Agents ⭐ 21

- **作者**: Halil Burak Noyan 等
- **评分**: 创新性 4 · 技术深度 4 · 影响力 5 · 可复现性 4 · 清晰度 4 = **21/25**
- **中文摘要**: 提出企业AI Agent动态最小权限架构，三层防御机制减少凭证滥用攻击面93%。
- **开源代码**: ✅ 数据集、环境规范和生成pipeline已发布
- **入选理由**: 企业Agent安全的关键基础设施思路，从"检测"转向"预防"的安全范式转移

---

### 6. MEUSLI: A Multilingual Projector for LLM-based ASR and Beyond ⭐ 21

- **作者**: Alessio Brutti 等
- **评分**: 创新性 4 · 技术深度 4 · 影响力 4 · 可复现性 5 · 清晰度 4 = **21/25**
- **中文摘要**: 首个开源多语言Whisper-LLM投影器家族，支持28种欧洲语言端到端ASR及语音翻译扩展。
- **开源代码**: ✅ 完全开源
- **入选理由**: 多语言语音理解的重要基础设施，填补了开源SpeechLLM的多语言空白

---

### 7. Scaling Native Multimodal Pre-Training From Scratch ⭐ 21

- **作者**: Haoyuan Wu 等
- **评分**: 创新性 5 · 技术深度 5 · 影响力 4 · 可复现性 3 · 清晰度 4 = **21/25**
- **中文摘要**: 系统刻画原生多模态预训练的Scaling Law，发现语言目标对数据组成不敏感而多模态目标高度敏感。
- **开源代码**: —
- **入选理由**: 原生多模态预训练的基础理论工作，为后续VLM训练提供了效率前沿的指导

---

### 8. From Isolated Tasks to Structured Capabilities: A Multilayer Taxonomy for LLMs ⭐ 20

- **作者**: Jiachen Wo 等
- **评分**: 创新性 4 · 技术深度 4 · 影响力 4 · 可复现性 3 · 清晰度 5 = **20/25**
- **中文摘要**: 构建14个能力域91个子技能的多层分类体系，筛查31505篇顶会论文映射LLM研究注意力分布。
- **开源代码**: —
- **入选理由**: 领域级综述工作，识别的六大被忽视领域对研究方向选择有重要参考价值

---

## 本周趋势洞察

| 趋势 | 代表论文 |
|------|----------|
| Agent评估与安全性反思 | Protocol Validity (#1), Regression Tax (#4) |
| Agent能力自进化 | Skill Self-Play (#3), IDEAgent (#2) |
| 企业Agent安全落地 | Dynamic Capability Scoping (#5) |
| 多模态基础理论 | Scaling Native Multimodal (#7) |
| 语音+LLM基础设施 | MEUSLI (#6) |
| 领域系统性综述 | Multilayer Taxonomy (#8) |

---

## 评分淘汰说明

以下论文未入选（总分<20或排序靠后）：

| 论文 | arXiv | 总分 | 未入选原因 |
|------|-------|------|-----------|
| TRACE-Router | 2607.22465 | 20 | 技术扎实但创新性一般，路由问题已有较多研究 |
| AgentRCA | 2607.22385 | 20 | 工业应用价值高但领域较窄 |
| RL Mitigates Task Conflicts | 2607.22039 | 19 | ICLR 2026工作，理论分析扎实但影响力待观察 |
| SceneActBench | 2607.22393 | 18 | Benchmark工作，当前模型得分偏低，领域较新 |
| LLM Creativity Evaluation | 2607.22218 | 18 | 偏心理学实验，对技术路线指导有限 |

---

*周四论文精选完成于 2026-07-30 · W31*
*评估方法：arXiv摘要分析 + 五维评分表*

---

> 【人工介入点】请确认以上短名单，回复'继续'以执行下一步，或回复'删除X'/'深入解读X'调整。
