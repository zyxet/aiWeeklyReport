# 📅 2026 W24 论文精选周报

**日期**：2026-06-11 周四
**来源**：arXiv cs.CL / cs.LG / cs.AI recent
**筛选**：从26篇候选池中按5维评分（每项1-5分，总分25分）保留6篇+2备选

---

## 本周主题：推理效率 · Agent安全 · 评估可靠性

---

## 🏆 精选列表（按总分排序）

| 排名 | 论文 | 总分 | 创新 | 实用 | 深度 | 机构 | 代码 | 标签 |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | **Breaking the Ice: Analyzing Cold Start Latency in vLLM** | 20 | 3 | 5 | 4 | 3 | 5 | Evaluation, System |
| 2 | **AI Code Sandboxes: A Comparative Security Study** | 20 | 3 | 5 | 4 | 3 | 5 | Safety, Code Agent |
| 3 | **Multilingual Fact-Checking at Scale** | 19 | 3 | 5 | 3 | 3 | 5 | Code Agent, Hallucination/Factuality |
| 4 | **AgentTrust: A Self-Improving Trust Layer** | 18 | 5 | 5 | 4 | 3 | 1 | Agent, RAG, Safety |
| 5 | **Distilling LLM Reasoning into an Interpretable Policy Tree** | 18 | 4 | 4 | 4 | 3 | 3 | Agent, Multi-Agent, Reasoning |
| 6 | **Do Coding Agents Deceive Us?** | 17 | 4 | 5 | 4 | 3 | 1 | Agent, RAG, Evaluation |
| 备选 | **FlashCP: Context Parallelism for LLM Training** | 17 | 4 | 5 | 4 | 3 | 1 | Memory, Training |
| 备选 | **Chiaroscuro Attention: Spending Compute in the Dark** | 17 | 5 | 4 | 5 | 2 | 1 | Evaluation, Architecture |

---

## 🔑 一句话摘要

**[1] vLLM Cold Start**：分析vLLM推理引擎冷启动延迟，构建预测模型，为大规模推理资源规划提供可操作的性能指导。

**[2] AI Code Sandboxes**：从六个维度比较五种AI代码沙箱产品的安全隔离能力，揭示引擎类型与补丁策略对安全性的决定性影响。

**[3] Multilingual Fact-Checking**：部署于Factiverse的多语言事实核查系统，证明微调紧凑模型在114种语言上可替代昂贵LLM。

**[4] AgentTrust**：为AI Agent动作构建自进化信任层，通过语义威胁的RAG记忆与词法威胁的规则蒸馏实现零误拦安全决策。

**[5] Co-pi-tree**：将LLM推理蒸馏为可解释策略树，在Overcooked-AI中实现35.4%奖励提升，同时减少77.7%的LLM查询。

**[6] CapCode**：设计带随机测试的上限评估框架，检测编码Agent通过捷径欺骗评测的行为，保障评估分数的真实意义。

---

## 📦 开源亮点

- **vLLM Cold Start**：开源数据集+分析工具+预测脚本，可直接用于生产环境优化
- **AI Code Sandboxes**：Apache-2.0 companion repository，提供可复现安全评估框架
- **Multilingual Fact-Checking**：代码和数据公开，含完整多语言事实核查pipeline

---

## 🏷️ 标签分布

- Agent（4篇）：AgentTrust、Co-pi-tree、CapCode、AI Code Sandboxes
- Safety（3篇）：AgentTrust、CapCode、AI Code Sandboxes
- Evaluation（3篇）：vLLM Cold Start、CapCode、Chiaroscuro Attention
- Memory/System（2篇）：FlashCP、vLLM Cold Start
- 多语言/多模态（1篇）：Multilingual Fact-Checking

---

> 筛选完成，等待用户确认。确认后执行git提交。
