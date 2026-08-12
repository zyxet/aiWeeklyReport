# 周三精选短名单 — 2026-W33

> 筛选时间：2026-08-12 周三 14:00 CST
> 来源：周一开源项目速览（2026-08-10）深度验证
> 规则：删除 Star < 100 且无 media coverage 的项目，保留 5–7 个

---

## 筛选结果概览

| 序号 | 项目名称 | 实时 Stars | 验证结论 | 保留理由 |
|:---:|---------|:--------:|---------|---------|
| 1 | **Kimi K3** | N/A (模型权重) | ✅ 通过 | 史上最大开源模型（2.8T），国产AI里程碑，全球媒体广泛报道 |
| 2 | **Microsoft MAF 1.0** | N/A (官方框架) | ✅ 通过 | 微软统一企业级Agent框架，AutoGen+Semantic Kernel合并，Build 2026发布 |
| 3 | **ZeroClaw** | 31.9K+ | ✅ 通过 | 边缘Agent新范式，3.4MB二进制/<5MB内存，Raspberry Pi可运行 |
| 4 | **Mastra** | 23.2K+ | ✅ 通过 | Gatsby原班人马打造，$35M融资，生产级TypeScript Agent框架 |
| 5 | **OpenWork** | 待观察 | ✅ 通过 | 本地优先AI工作桌面，50+ LLM提供商，数据主权可控 |
| 6 | **NanoClaw** | 待观察 | ✅ 通过 | 700行可审计代码，$12M种子轮，Docker MicroVM沙箱，强合规场景 |
| 7 | **iFixAi** | 479 ⬆️ | ✅ 通过 | Agent独立审计工具，OpenAgentSkill Trust Score 79，解决AI信任核心问题 |

**删除项目（3个）**：
- DeepSeek-Reasonix — Star 43，虽有DeepSeek官方收录，但生态尚早，与OpenWork/Kimi等相比差异化不足
- engram — Star 6，Agent记忆系统概念好，但竞品（claude-mem 28K+ Stars）差距过大
- multica — Star 31，Agent管理平台概念新颖，但产品成熟度不足

---

## 一、Kimi K3 (Moonshot AI)

| 维度 | 详情 |
|-----|------|
| **定位** | 史上最大开源权重模型（2.8T参数 MoE） |
| **协议** | Modified MIT（7月27日开放权重） |
| **上下文** | 1M tokens |
| **API定价** | $3.00/million input / $15.00/million output |
| **核心亮点** | KDA混合线性注意力、原生多模态、Terminal-Bench 2.1 得分 88.3 |
| **注意** | KDA架构尚未被llama.cpp/vLLM支持，本地稳定推理预计Q4 |
| **适合人群** | 长上下文Agent开发、早期采用者 |
| **GitHub** | https://github.com/MoonshotAI/Kimi-K3 |

**验证结果**：7月27日已开放权重，目前API可用。多家技术媒体（机器之心、InfoQ等）报道。作为国产大模型开源里程碑，具有重大战略意义。

---

## 二、Microsoft Agent Framework 1.0 (MAF)

| 维度 | 详情 |
|-----|------|
| **定位** | 微软统一企业级Agent框架 |
| **前身** | Semantic Kernel (28K★) + AutoGen (42K★) 合并 |
| **语言** | C# / Python 双栈 |
| **协议** | 开源 |
| **发布时间** | Build 2026（2026年4月），Q1 GA目标 |
| **核心亮点** | 有向图工作流、Checkpoint持久化、.NET/Python双栈、GAIA基准验证 |
| **适合人群** | 已有.NET/Python基础设施的企业团队 |
| **GitHub** | https://github.com/microsoft/agent-framework |

**验证结果**：微软官方战略级项目，AutoGen已转入维护模式。企业级Agent编排的标杆方案。

---

## 三、ZeroClaw

| 维度 | 详情 |
|-----|------|
| **定位** | 3.4MB Rust二进制，边缘Agent |
| **Stars** | 31.9K+ ✅ |
| **内存** | <5MB 空闲内存 |
| **冷启动** | <10ms |
| **协议** | 开源 |
| **作者** | 哈佛+MIT学生联合Sundai.Club |
| **核心亮点** | 22+ LLM提供商、完全去云化、工厂预测性维护场景验证 |
| **适合人群** | 边缘计算、IoT、资源极度受限场景 |
| **GitHub** | https://github.com/sundai-club/zeroclaw |

**验证结果**：Star数持续增长，v0.8.0（2026-06-12）活跃迭代。边缘Agent赛道的明确领先者。

---

## 四、Mastra

| 维度 | 详情 |
|-----|------|
| **定位** | 生产级TypeScript Agent框架 |
| **Stars** | 23.2K+ ✅ |
| **Commits** | 14,334+ |
| **融资** | $35M总计（Series A $22M Spark Capital领投） |
| **协议** | Apache 2.0 |
| **核心亮点** | 结构化原语（Agent/Tool/Workflow/RAG/Eval/Observability）、纯TypeScript |
| **企业客户** | Brex、Marsh McLennan（100k+日活）、Docker、MongoDB、Salesforce |
| **适合人群** | TypeScript全栈团队 |
| **GitHub** | https://github.com/mastra-ai/mastra |

**验证结果**：Gatsby团队背景（React静态站点生成器，曾50K+★），企业客户背书强。TypeScript Agent框架的新贵。

---

## 五、OpenWork

| 维度 | 详情 |
|-----|------|
| **定位** | 本地优先的AI工作桌面，开源替代Claude Cowork |
| **协议** | MIT |
| **语言** | TypeScript（基于OpenCode构建） |
| **核心亮点** | 50+ LLM提供商、文件不出机器、团队skill一键共享、桌面端免费 |
| **适合人群** | 拒绝厂商锁定、注重数据主权的团队 |
| **GitHub** | https://github.com/different-ai/openwork |

**验证结果**：Claude Cowork GA（2026年4月）后涌现的开源替代方案之一。本地优先+隐私可控是核心差异化。

---

## 六、NanoClaw

| 维度 | 详情 |
|-----|------|
| **定位** | 700行TypeScript极致简约Agent框架 |
| **代码量** | ~700行（一顿午饭能读完） |
| **融资** | $12M种子轮（Docker、Vercel、Hugging Face CEO Clem Delangue参投） |
| **协议** | 开源 |
| **核心亮点** | 全代码可审计、Docker MicroVM沙箱、故障爆炸半径止于容器边界 |
| **限制** | 仅支持Claude/Anthropic；skill生态远小于OpenClaw |
| **适合人群** | 金融、医疗、法律等强合规行业 |
| **GitHub** | https://github.com/nanoco/nanoclaw |

**验证结果**：安全偏执型设计的代表作。Docker官方合作背书，$12M融资验证了商业模式。

---

## 七、iFixAi

| 维度 | 详情 |
|-----|------|
| **定位** | AI Agent独立审计工具 |
| **实时Stars** | 479 ⬆️（候选池记录51+，已大幅增长） |
| **语言** | Python |
| **协议** | Apache 2.0 |
| **核心亮点** | 120秒内回答"Agent真的在做它该做的事吗"、45项检查、32项核心+13项前沿风险 |
| **Trust Score** | OpenAgentSkill 79分（Strong shortlist级别） |
| **适合人群** | 合规审计、Agent可靠性验证、金融/医疗等高风险场景 |
| **GitHub** | https://github.com/ifixai-ai/iFixAi |

**验证结果**：Stars从51+增长至479，增长迅速。OpenAgentSkill审计报告显示质量扎实（Security 100分）。AI Agent经济中的信任基础设施。

---

## 删除项目说明

| 项目名称 | 删除原因 |
|---------|---------|
| **DeepSeek-Reasonix** | Star 43，虽有DeepSeek官方文档收录和博客报道，但生态建设尚早，与OpenWork相比差异化不够突出 |
| **engram** | Star 6，Agent记忆系统概念有价值，但竞品claude-mem（28K+ Stars）过于强势，市场空间有限 |
| **multica** | Star 31，Agent作为团队成员的管理视角新颖，但产品成熟度和社区规模不足 |

---

*筛选完成时间：2026-08-12 14:00 CST*
*数据来源：GitHub API、OSSInsight、OpenAgentSkill审计报告、技术博客、官方文档*
