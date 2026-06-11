# 论文精选 — 2026-W24

> 周期：2026-06-08 ~ 2026-06-14
> 筛选时间：2026-06-11（周四）
> 来源：arXiv cs.AI 等，26篇候选池 → 6+2篇精选

---

## 🏆 本周精选（按总分排序）

| 排名 | 论文 | 总分 | 标签 | 代码 |
|:---|:---|:---:|:---|:---:|
| 1 | **Breaking the Ice: Analyzing Cold Start Latency in vLLM** | 20 | 系统/评估 | ✅ |
| 2 | **AI Code Sandboxes: A Comparative Security Study** | 20 | 安全/代码Agent | ✅ |
| 3 | **Multilingual Fact-Checking at Scale** | 19 | 事实核查/多语言 | ✅ |
| 4 | **AgentTrust: A Self-Improving Trust Layer** | 18 | Agent/安全/RAG | ❌ |
| 5 | **Distilling LLM Reasoning into an Interpretable Policy Tree** | 18 | Agent/推理/多Agent | 项目页 |
| 6 | **Do Coding Agents Deceive Us?** | 17 | Agent/评估/RAG | ❌ |

**备选**：FlashCP（训练优化）、Chiaroscuro Attention（架构创新）

---

## 🔑 一句话摘要

**vLLM Cold Start** — 分析vLLM推理引擎冷启动延迟，构建预测模型，为大规模推理资源规划提供可操作的性能指导。

**AI Code Sandboxes** — 从六个维度比较五种AI代码沙箱产品的安全隔离能力，揭示引擎类型与补丁策略对安全性的决定性影响。

**Multilingual Fact-Checking** — 部署于Factiverse的多语言事实核查系统，证明微调紧凑模型在114种语言上可替代昂贵LLM。

**AgentTrust** — 为AI Agent动作构建自进化信任层，通过语义威胁的RAG记忆与词法威胁的规则蒸馏实现零误拦安全决策。

**Co-pi-tree** — 将LLM推理蒸馏为可解释策略树，在Overcooked-AI中实现35.4%奖励提升，同时减少77.7%的LLM查询。

**CapCode** — 设计带随机测试的上限评估框架，检测编码Agent通过捷径欺骗评测的行为，保障评估分数的真实意义。

---

## 📦 开源亮点

- **vLLM Cold Start**：开源数据集+分析工具+预测脚本
- **AI Code Sandboxes**：Apache-2.0 companion repository
- **Multilingual Fact-Checking**：代码和数据公开

---

## 评估维度

| 论文 | 实用价值 | 技术新颖 | 开源质量 | 社区契合 | 时效热度 |
|:---|:---:|:---:|:---:|:---:|:---:|
| vLLM Cold Start | 5 | 4 | 5 | 3 | 3 | 20 |
| AI Code Sandboxes | 5 | 4 | 5 | 3 | 3 | 20 |
| Multilingual Fact-Checking | 5 | 4 | 4 | 3 | 3 | 19 |
| AgentTrust | 4 | 4 | 3 | 4 | 3 | 18 |
| Co-pi-tree | 4 | 4 | 3 | 4 | 3 | 18 |
| CapCode | 4 | 4 | 2 | 4 | 3 | 17 |

---

## 🏷️ 本周标签云

Agent（3篇）、安全（3篇）、评估（3篇）、RAG（2篇）、系统、代码Agent、事实核查、多语言、推理、多Agent、训练优化、架构创新

---

*W24 论文精选完成。周五 17:00 生成《AI开源情报周报》主报告。*
