# 📄 本周候选论文池（24篇）

> 📅 收集时间：2026-08-04 | 📊 来源：arXiv + Hugging Face + PaperWeekly

---

## 🔍 LLM 推理与对齐

1. **TokTier: Stateful Tokenization at 94% Cache Hit Rate for Agent Serving** | [arXiv:2607.29678](https://arxiv.org/abs/2607.29678) | `LLM`, `Agent`, `Inference Optimization` | 提出有状态token化服务，针对Agent场景的长上下文增量更新优化，在94.1%缓存命中率下将首token时间降低16-34%。

2. **ResKV: Residual-Cache KV Compression for Long-Context Inference** | [arXiv:2607.29591](https://arxiv.org/abs/2607.29591) | `LLM`, `Long Context`, `KV Cache` | 通过主缓存+残差缓存的分层设计，在相同KV预算下实现更优的长上下文推理压缩效果。

3. **CaRL: Capability-Aligned Reinforcement Learning for Reducing Futile Reasoning** | [arXiv:2607.29211](https://arxiv.org/abs/2607.29211) | `LLM`, `Reasoning`, `RLHF` | 通过能力对齐的奖励塑形和事后拒绝增强，减少LLM在超能力任务上的无效推理。

4. **TwT: Translation with Thought - A Resource-Rational Framework for Chain-of-Thought** | [arXiv:2607.29287](https://arxiv.org/abs/2607.29287) | `LLM`, `Chain-of-Thought`, `Translation` | 基于DeepSeek-R1蒸馏的CoT翻译框架，在15个基准上实现32-60%的token使用量减少。

5. **CalibratedRubric: Bayesian Measurability Filtering for Open-Ended LLM Evaluation** | [arXiv:2607.29252](https://arxiv.org/abs/2607.29252) | `LLM`, `Evaluation`, `Prompt Engineering` | 结合类型特定评分、贝叶斯可测量性过滤和IRT的评估框架，将人工一致性从κ=0.604提升至0.743。

---

## 🤖 Agent 与多智能体

6. **Zero-Mem: Zero-Token Memory Operations for LLM Agents** | [arXiv:2607.29377](https://arxiv.org/abs/2607.29377) | `Agent`, `Memory`, `Long Context` | 提出零token记忆操作，通过实体-上下文图和时间层次结构消除记忆操作的LLM调用开销，减少57.6%时间成本。

7. **SESA: Self-Evolving Skill-Augmented Agent** | [arXiv:2607.29468](https://arxiv.org/abs/2607.29468) | `Agent`, `Multi-Agent`, `Self-Play` | 自进化技能增强Agent，使程序性记忆成为自对弈的动态状态，在7个QA基准上提升1.2-3.2个百分点。

8. **Data Turnstile: Synthetic Training Data for Small Language Model Tool Use** | [arXiv:2607.29250](https://arxiv.org/abs/2607.29250) | `Agent`, `Tool Use`, `SLM` | 面向小模型工具调用的开源合成数据框架，Qwen3-0.6B在BFCL上达到75.9%准确率，超越思维链开启的1.7B模型。

9. **AgentHPOBench: Sequential Benchmark for Scientific Experimental Agents** | [arXiv:2607.29626](https://arxiv.org/abs/2607.29626) | `Agent`, `Scientific Agent`, `HPO` | 面向科学实验Agent的序列优化基准，评估12个Agent在30个ML任务上的实验优化能力。

10. **ExtractBench: Schema-Guided Extraction Benchmark for Enterprise Agents** | [arXiv:2607.29677](https://arxiv.org/abs/2607.29677) | `Agent`, `Document Understanding`, `VLM` | 企业级文档提取基准，覆盖370个文档、8个业务领域，LlamaExtract Agentic Plus在成本和准确率上均表现最优。

11. **AMTFV: Agentic Mathematical Tool-Flow Verification** | [arXiv:2607.29549](https://arxiv.org/abs/2607.29549) | `Agent`, `Reasoning`, `Tool Use` | 通过数学工具流(MTF)接口解耦验证建模与具体执行，在5个数学推理数据集上最高提升8.3个百分点。

---

## 🧠 记忆与上下文

12. **LLM Agents Know but Cannot Act: Decoupled Memory Evaluation** | [arXiv:2607.29433](https://arxiv.org/abs/2607.29433) | `LLM`, `Memory`, `Agent` | 发现LLM Agent存在记忆与行为利用的解耦问题，揭示健康和治疗相关偏好的利用尤其薄弱。

13. **AdaMM: Retrieval and Analytic Memory for Long-Term Multimodal Interactions** | [arXiv:2607.29440](https://arxiv.org/abs/2607.29440) | `Multimodal`, `Memory`, `Agent` | 统一检索记忆和分析记忆的框架，支持对多模态观测的过滤、聚合、排序和时间比较。

14. **Epistemic Vigilance of Vision-Language Models in Cooperative Dialog** | [arXiv:2607.29585](https://arxiv.org/abs/2607.29585) | `VLM`, `Multi-Agent`, `Cooperation` | 发现VLM在合作对话中过度迎合对话伙伴，提出通过减少谄媚行为的向量引导来改善认知警觉性。

---

## 📊 基准测试与评估

15. **Hy-MultiTurn: Chinese Benchmark for Deep Multi-Turn Dialogue Understanding** | [arXiv:2607.29196](https://arxiv.org/abs/2607.29196) | `LLM`, `Evaluation`, `Chinese` | 中文深度多轮对话理解基准，覆盖6种失败机制，209个控制任务，GPT-5.5仅满足41.1%的要求。

16. **DungeonBench: Tactical Reasoning in D&D Combat** | [arXiv:2607.29577](https://arxiv.org/abs/2607.29577) | `LLM`, `Reasoning`, `Benchmark` | D&D战斗战术推理基准，评估LLM在几何、时机、资源、规则交互中的综合决策能力。

17. **FriendBench: Inferring Familiarity from Dyadic Interactions** | [arXiv:2607.29602](https://arxiv.org/abs/2607.29602) | `Multimodal`, `Benchmark`, `VLM` | 从20秒双人对话中推断熟悉度的基准，26个模型在文本/音频/视频模态上与人类表现相当。

18. **ModelEquivBench: Certifying Multi-Relational Equivalence for Generated Optimization Models** | [arXiv:2607.29431](https://arxiv.org/abs/2607.29431) | `LLM`, `Evaluation`, `Code Generation` | 针对自然语言生成优化模型的多关系等价性评估系统，暴露粗粒度评估无法区分的模型差异。

19. **ARB: Authorship-Rewriting Benchmark for AI-Text Detection** | [arXiv:2607.29539](https://arxiv.org/abs/2607.29539) | `LLM`, `Detection`, `Evaluation` | 发现现有AI文本检测器在LLM改写的人类文本上性能暴跌60-78个百分点。

---

## 🔄 强化学习与对齐

20. **LEMUR: Multi-Objective RL with Preference Feedback** | [arXiv:2607.29559](https://arxiv.org/abs/2607.29559) | `RL`, `Multi-Agent`, `Alignment` | 通过人类偏好反馈学习多目标策略的框架，联合学习策略和多个目标特定的奖励模型。

21. **LatentRM: Latent Reasoning Reward Modeling** | [arXiv:2607.29185](https://arxiv.org/abs/2607.29185) | `RLHF`, `Reasoning`, `Reward Model` | 将中间推理痕迹学习为离散潜在变量以最大化下游标量奖励，在分布内和分布外任务上均优于标量和生成式奖励模型。

22. **Causal Reasoning in LLMs: Context Switches Overrule Training Mixture** | [arXiv:2607.29484](https://arxiv.org/abs/2607.29484) | `LLM`, `Reasoning`, `Causal` | 发现干预证据的使用取决于推理时的上下文而非训练混合比例，揭示LLM因果推理中的上下文介导开关。

---

## 🛠️ 其他

23. **InMyStyle: Privacy-First Style Adaptation for Small Language Models** | [arXiv:2607.29238](https://arxiv.org/abs/2607.29238) | `LLM`, `Personalization`, `Privacy` | 本地化的个人写作风格适应系统，0.5B-7B参数模型即可实现有效的AI文本风格转换。

24. **LLM Inversion: Functional Prompt Recovery in Black-Box Settings** | [arXiv:2607.29378](https://arxiv.org/abs/2607.29378) | `LLM`, `Security`, `Prompt Engineering` | 黑盒场景下的功能性提示恢复方法，通过逆向语言模型实现从输出重建输入提示。

---

> 📌 **筛选说明**：本周从 arXiv cs.CL/cs.LG/cs.AI recent 页面（~350篇）中筛选出24篇核心论文，排除纯医学AI、纯CV（非VLM）及纯物理/数学论文。
