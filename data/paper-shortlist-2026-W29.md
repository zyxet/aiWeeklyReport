# W29 论文短名单 (2026-07-08 ~ 2026-07-15)

> 从 23 篇候选中按论文评估打分表（5项×5分，总分25分）筛选，保留前 8 篇。
> 评分维度：创新性 / 与开源·Agent 相关度 / 实验质量·影响力 / 开源可及性 / 实用落地价值

---

## 1. A Self-Evolving Agent for Longitudinal Personal Health Management (HealthClaw)
- **arXiv**: 2607.13940
- **日期**: 2026-07-15
- **评分**: 23/25 (创新4 / 相关5 / 实验4 / 开源5 / 实用5)
- **一句话**: 开源Agent架构，将共享安全规则与私有纵向记忆分离，长期健康管理准确率从0.2%提升至45.7%。
- **代码**: https://github.com/HC-Guo/HealthClaw ⭐ 论文+代码双料
- **关联**: CrewAI / Dify / 长期记忆 Agent

## 2. AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities
- **arXiv**: 2607.13705
- **日期**: 2026-07-15
- **评分**: 23/25 (创新4 / 相关5 / 实验4 / 开源5 / 实用5)
- **一句话**: 开源、可扩展的Agent评估基础设施，支持20+基准，覆盖5个能力维度。
- **代码**: 开源项目（arXiv页标注） ⭐ 论文+代码双料
- **关联**: Agent 评估标准化 / Every Eval Ever

## 3. DevicesWorld: Benchmarking Cross-Device Agents
- **arXiv**: 2607.13465
- **日期**: 2026-07-15
- **评分**: 23/25 (创新5 / 相关5 / 实验4 / 开源5 / 实用4)
- **一句话**: 6,140个跨设备协作任务，整合手机/桌面/IoT三类环境，最佳Agent成功率仅12.5%。
- **代码**: https://github.com/AgenticOrgLab/DevicesWorld ⭐ 论文+代码双料
- **关联**: 跨设备 Agent / 评估

## 4. Partially Correlated Verifier Cascades in LLM Harnesses
- **arXiv**: 2607.13918
- **日期**: 2026-07-15
- **评分**: 23/25 (创新5 / 相关5 / 实验4 / 开源5 / 实用4)
- **一句话**: 证明验证器级联中独立性假设会严重低估失败率，k=10时约3000倍偏差；关键杠杆是去相关而非加门。
- **代码**: https://github.com/jianganghan/harness-verifier-cascades ⭐ 论文+代码双料
- **关联**: LLM 可靠性 / 验证器设计

## 5. How Far Can Root Cause Analysis Go on Real-World Telemetry?
- **arXiv**: 2607.13548
- **日期**: 2026-07-15
- **评分**: 22/25 (创新5 / 相关5 / 实验4 / 开源3 / 实用5)
- **一句话**: 结构化多Agent RCA流程大幅超越基线，关键瓶颈是Agent正确推理能力而非数据获取。
- **代码**: 未明确（可能随论文发布）
- **关联**: 多 Agent 系统 / 可靠性

## 6. The Refusal Residue: When Probes Catch Alignment Faking
- **arXiv**: 2607.13346 | **ICML 2026 MI Workshop**
- **日期**: 2026-07-15
- **评分**: 22/25 (创新5 / 相关5 / 实验5 / 开源3 / 实用4)
- **一句话**: 13模型扫描自然涌现的对齐伪造，仅Qwen3-32B和Llama-3.1-8B表现伪造；拒绝残留可被检测但难以操控。
- **代码**: 发布五控制测量框架（可能开源）
- **关联**: Agent 安全 / 对齐伪造

## 7. Deep Interaction: An Efficient Human-AI Interaction Method for Large Reasoning Models
- **arXiv**: 2607.14049
- **日期**: 2026-07-15
- **评分**: 21/25 (创新5 / 相关5 / 实验4 / 开源2 / 实用5)
- **一句话**: 直接编辑CoT推理链而非重新生成，STEM任务修正成功率提升25%+，token使用量减少约40%。
- **代码**: 未明确
- **关联**: OpenCode Interpreter / 交互式编程 Agent

## 8. Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0
- **arXiv**: 2607.14004 | **RELAI Technical Report**
- **日期**: 2026-07-15
- **评分**: 21/25 (创新5 / 相关5 / 实验4 / 开源2 / 实用5)
- **一句话**: 质疑现有Agent优化均为一次性评估，RELAI-VCL是唯一实现正迁移且持续改进的方法，终身平均通过率76.4% vs 基线58.7%。
- **代码**: 未明确
- **关联**: Agent 优化 / 持续学习

---

## 数据概览

| 指标 | 数值 |
|------|------|
| 候选池总数 | 23 篇 |
| 短名单入选 | 8 篇 |
| 有开源代码 | 4 篇（#1, #3, #4, #2） |
| 论文+代码双料 | 4 篇 |
| 平均总分 | 22.3 / 25 |
| 最低入选分 | 21 / 25 |

## 落选的强候选（供参考）

- **Generative Compilation** (2607.13921, 21分) — 首次在生成中获得编译器反馈，Rust实现。落选因领域偏编译器，与Agent主线关联稍弱。
- **CAVA** (2607.13716, 21分) — Agent运行时治理规范动作验证。落选因与 #5/#6 安全领域重叠，优先保留更实验驱动的研究。
- **Early Adoption of Agentic Coding Tools** (2607.14037, 20分) — 大规模GitHub实证研究。落选因综述性质，无新算法或开源工具。

## 备注

- **Pool 勘误**: 第5篇"Experience Memory Graph" 的 arXiv 编号应为 2607.13884（非 2607.13899，后者实为 AIMO Interpretability Challenge）。该篇评分 19/25，未入选短名单。
- **开源代码确认**: 4 篇双料项目均通过 arXiv 页面或 GitHub 直接验证，链接有效。
