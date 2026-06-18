# 📚 本周精选论文（2026-W25，8篇）

> 筛选时间：2026-06-18 14:00 (Asia/Shanghai)
> 来源：42篇候选池 → 8篇精选
> 评估标准：创新性、实用性、技术深度、机构背书、代码可得性（每项1-5分，总分25分）

---

## 🏆 本周重磅推荐

### 1. Gaze Heads in VLMs: Mechanistic Analysis and Steering
- **arXiv**: https://arxiv.org/abs/2606.14703
- **一句话摘要**: 在VLM中发现控制视觉描述的"凝视头"，仅修改5-20个注意力头即可定向操控模型回答，无需重训练。
- **评分**: 创新性5 | 实用性4 | 技术深度5 | 机构背书3 | 代码可得性5 → **总分22/25**
- **代码状态**: ✅ **开源** — 代码、交互式Demo、数据集全公开
- **关键词**: VLM, Mechanistic Analysis, Attention Steering, Interpretability

---

### 2. Every Eval Ever: A Unifying Schema and Community Repository for AI Evaluation Results
- **arXiv**: https://arxiv.org/abs/2606.14516
- **一句话摘要**: 首个AI评估结果统一JSON模式与社区仓库，收录22,235个模型、2,273个基准，支持跨框架比较。
- **评分**: 创新性4 | 实用性5 | 技术深度4 | 机构背书4 | 代码可得性5 → **总分22/25**
- **代码状态**: ✅ **开源** — Hugging Face社区数据库，自动格式转换器
- **关键词**: Evaluation, Benchmark, Standardization, Community

---

### 3. AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition
- **arXiv**: https://arxiv.org/abs/2606.14674
- **一句话摘要**: 模块化框架将具身智能体表示为可重用策略组件的受控组合，揭示性能由支架兼容性和交互效应决定。
- **评分**: 创新性4 | 实用性5 | 技术深度4 | 机构背书3 | 代码可得性5 → **总分21/25**
- **代码状态**: ✅ **开源** — 代码、基线、交互式Playground全公开
- **关键词**: Agent, Multi-Agent, Embodied, Composition, Scaffold

---

### 4. LLMs Contain Multitudes: How Deployment Context Reshapes Model-Level Preferences and Values
- **arXiv**: https://arxiv.org/abs/2606.13944
- **一句话摘要**: 发现LLM偏好高度依赖部署上下文，1.2M配对决策显示上下文变化导致3.2倍偏好差异，颠覆模型级别属性假设。
- **评分**: 创新性5 | 实用性5 | 技术深度5 | 机构背书3 | 代码可得性3 → **总分21/25**
- **代码状态**: ⚠️ 研究数据集规模大（12MB），代码状态未明确标注
- **关键词**: LLM, Alignment, Safety, Evaluation, Context Dependency

---

## 🔥 技术突破

### 5. Parallel-Synthesis: Direct Cache-Based Synthesis for Parallel Agent Branches
- **arXiv**: https://arxiv.org/abs/2606.14672
- **一句话摘要**: 让合成器直接消费并行Agent分支的KV缓存，减少首token时间2.5-11倍，无需重新计算冗余前缀。
- **评分**: 创新性5 | 实用性5 | 技术深度4 | 机构背书3 | 代码可得性3 → **总分20/25**
- **代码状态**: ⚠️ 论文未明确标注代码链接
- **关键词**: Agent, Cache, Efficiency, KV Cache, Parallel Computing

---

### 6. AdaSR: Adaptive Streaming Reasoning with Hierarchical Relative Policy Optimization
- **arXiv**: https://arxiv.org/abs/2606.14694
- **一句话摘要**: 自适应流式推理框架，让模型在输入流式传输中推理，通过HRPO学习何时思考及分配计算量。
- **评分**: 创新性4 | 实用性4 | 技术深度4 | 机构背书3 | 代码可得性4 → **总分19/25**
- **代码状态**: ✅ **开源** — 代码已释放
- **关键词**: LLM, Reasoning, Streaming, RL, HRPO

---

## 🚀 智能体进化

### 7. HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry
- **arXiv**: https://arxiv.org/abs/2606.14249
- **一句话摘要**: 可组合自适应智能体接口铸造厂，通过轨迹驱动多智能体进化引擎AEGIS，在5个基准上平均提升+14.5%。
- **评分**: 创新性5 | 实用性4 | 技术深度4 | 机构背书3 | 代码可得性2 → **总分18/25**
- **代码状态**: ⏳ **即将开源** — 作者承诺未来完整开源
- **关键词**: Agent, Harness, Multi-Agent, Evolution, AEGIS

---

## 🌍 文化对齐

### 8. Cultural Data Funnel: A Declining Explicit Cultural Signal in Modern LLM Pipelines
- **arXiv**: https://arxiv.org/abs/2606.13808
- **一句话摘要**: 文化信号在LLM后训练阶段急剧下降，RL中下降97%，释放5.6M文化标注数据集推动研究。
- **评分**: 创新性4 | 实用性4 | 技术深度4 | 机构背书3 | 代码可得性4 → **总分19/25**
- **代码状态**: ✅ **数据集开源** — 5.6M文化标注样本已发布
- **关键词**: LLM, Cultural Alignment, Data Pipeline, Multilingual

---

## 📊 评分汇总

| 排名 | 论文 | 总分 | 创新 | 实用 | 深度 | 背书 | 代码 | 开源 |
|-----|------|------|------|------|------|------|------|------|
| 1 | Gaze Heads in VLMs | 22 | 5 | 4 | 5 | 3 | 5 | ✅ |
| 2 | Every Eval Ever | 22 | 4 | 5 | 4 | 4 | 5 | ✅ |
| 3 | AgentSpec | 21 | 4 | 5 | 4 | 3 | 5 | ✅ |
| 4 | LLMs Contain Multitudes | 21 | 5 | 5 | 5 | 3 | 3 | ⚠️ |
| 5 | Parallel-Synthesis | 20 | 5 | 5 | 4 | 3 | 3 | ⚠️ |
| 6 | AdaSR | 19 | 4 | 4 | 4 | 3 | 4 | ✅ |
| 7 | Cultural Data Funnel | 19 | 4 | 4 | 4 | 3 | 4 | ✅ |
| 8 | HarnessX | 18 | 5 | 4 | 4 | 3 | 2 | ⏳ |

---

## 🔍 本周趋势观察

### 关键发现
1. **VLM可解释性突破**: Gaze Heads首次实现无需重训练的VLM定向操控，为安全审计和可控生成开辟新路
2. **评估基础设施成熟**: Every Eval Ever推动AI评估标准化，22K+模型数据支持跨社区比较
3. **智能体架构范式转移**: 从模型训练转向运行时接口/支架优化（AgentSpec + HarnessX）
4. **对齐安全新挑战**: LLM偏好高度依赖部署上下文，安全保证在一种场景下获得，在另一场景可能失效
5. **文化对齐被忽视**: 后训练阶段文化信号急剧衰减，多语言增强地理多样性但不确保文化平衡

### 论文+代码双料项目（A类）
- ✅ Gaze Heads in VLMs — 代码+Demo+数据集
- ✅ Every Eval Ever — Hugging Face社区数据库
- ✅ AgentSpec — 代码+基线+Playground
- ✅ AdaSR — 代码已释放
- ✅ Cultural Data Funnel — 5.6M数据集

---

*本短名单由AI Agent自动筛选生成，【人工介入点】请确认以上短名单，回复'继续'以执行下一步，或回复'删除X'/'深入解读X'调整。*
