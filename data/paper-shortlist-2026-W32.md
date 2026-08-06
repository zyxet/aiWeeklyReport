# 📄 本周论文精选短名单（W32）

> 📅 筛选时间：2026-08-06 | 🔢 来源：24篇候选池 | ⭐ 入选：8篇

---

## 入选论文（按总分降序）

### 1. Data Turnstile: Synthetic Training Data for Small Language Model Tool Use
- **arXiv**: [2607.29250](https://arxiv.org/abs/2607.29250)
- **标签**: `Agent`, `Tool Use`, `SLM`
- **一句话摘要**: 开源合成数据框架，让0.6B小模型工具调用能力超越1.7B大模型。
- **评分**: 创新4 | 深度4 | 实用5 | 复现5 | 影响4 = **22分**
- **代码**: ⭐ **已开源**（含1000+ APIs、100K+多轮交互数据集）

### 2. TokTier: Stateful Tokenization at 94% Cache Hit Rate for Agent Serving
- **arXiv**: [2607.29678](https://arxiv.org/abs/2607.29678)
- **标签**: `LLM`, `Agent`, `Inference Optimization`
- **一句话摘要**: 有状态token化服务，在94%缓存命中率下将Agent首token时间降低16-34%。
- **评分**: 创新4 | 深度5 | 实用5 | 复现3 | 影响4 = **21分**
- **代码**: ❌ 未开源（大规模生产验证，$1.5×10^{10}$ split checks）

### 3. Zero-Mem: Zero-Token Memory Operations for LLM Agents
- **arXiv**: [2607.29377](https://arxiv.org/abs/2607.29377)
- **标签**: `Agent`, `Memory`, `Long Context`
- **一句话摘要**: 零token记忆操作框架，通过结构化检索替代LLM调用，降低57.6%记忆开销。
- **评分**: 创新5 | 深度4 | 实用5 | 复现3 | 影响4 = **21分**
- **代码**: ⏳ 承诺开源（"After peer review"后发布）

### 4. SESA: Self-Evolving Skill-Augmented Agent
- **arXiv**: [2607.29468](https://arxiv.org/abs/2607.29468)
- **标签**: `Agent`, `Multi-Agent`, `Self-Play`
- **一句话摘要**: 自进化技能增强Agent，使程序性记忆成为自对弈动态状态，持续提升推理能力。
- **评分**: 创新5 | 深度4 | 实用4 | 复现4 | 影响4 = **21分**
- **代码**: ⭐ **已开源**

### 5. ResKV: Residual-Cache KV Compression for Long-Context Inference
- **arXiv**: [2607.29591](https://arxiv.org/abs/2607.29591)
- **标签**: `LLM`, `Long Context`, `KV Cache`
- **一句话摘要**: 残差缓存KV压缩，主缓存+残差缓存分层设计，实现更优长上下文推理。
- **评分**: 创新4 | 深度5 | 实用4 | 复现3 | 影响4 = **20分**
- **代码**: ❌ 未开源

### 6. CaRL: Capability-Aligned Reinforcement Learning for Reducing Futile Reasoning
- **arXiv**: [2607.29211](https://arxiv.org/abs/2607.29211)
- **标签**: `LLM`, `Reasoning`, `RLHF`
- **一句话摘要**: 能力对齐强化学习，通过奖励塑形减少LLM在超能力任务上的无效推理。
- **评分**: 创新5 | 深度4 | 实用4 | 复现3 | 影响4 = **20分**
- **代码**: ⭐ **已开源**

### 7. Hy-MultiTurn: Chinese Benchmark for Deep Multi-Turn Dialogue Understanding
- **arXiv**: [2607.29196](https://arxiv.org/abs/2607.29196)
- **标签**: `LLM`, `Evaluation`, `Chinese`
- **一句话摘要**: 中文深度多轮对话基准，覆盖6种失败机制，GPT-5.5仅满足41.1%。
- **评分**: 创新4 | 深度4 | 实用4 | 复现4 | 影响4 = **20分**
- **代码**: ⏳ 基准数据集（通常开源，待确认）

### 8. LLM Agents Know but Cannot Act: Decoupled Memory Evaluation
- **arXiv**: [2607.29433](https://arxiv.org/abs/2607.29433)
- **标签**: `LLM`, `Memory`, `Agent`
- **一句话摘要**: 揭示Agent记忆与行为利用的解耦问题，健康偏好利用尤其薄弱。
- **评分**: 创新5 | 深度4 | 实用3 | 复现3 | 影响4 = **19分**
- **代码**: ❌ 未开源

---

## 筛选说明

**评分维度**（每项1-5分，总分25分）：
- 创新性/原创性：是否提出新颖思路或方法
- 技术深度：技术方案的严谨性和深度
- 实用价值：对实际应用或后续研究的直接帮助
- 可复现性：是否有代码/数据，实验是否充分
- 领域影响力：在领域内的潜在影响力

**入选理由**：
- 8篇论文覆盖Agent、推理优化、数据合成、评估基准、RLHF对齐等核心方向
- 3篇已开源（Data Turnstile、SESA、CaRL），2篇承诺开源
- 工程价值突出的TokTier和Zero-Mem虽未开源，但生产验证数据详实
- 领域分布均衡，避免单一方向过度集中

**未入选但值得关注的论文**：
- **AMTFV** (2607.29549): 数学工具流验证，最高提升8.3%，适合数学推理方向跟进
- **LatentRM** (2607.29185): 潜在推理奖励模型，奖励建模新范式
- **CalibratedRubric** (2607.29252): 评估框架，人工一致性κ从0.604提升至0.743

---

> 📌 **人工介入点**：请确认以上短名单，回复'继续'以执行下一步，或回复'删除X'/'深入解读X'调整。
