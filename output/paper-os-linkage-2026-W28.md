# 论文-开源联动分类分析 — 2026-W28

> 生成时间: 2026-07-10 19:00 CST
> 开源项目: 7个（来自 os-shortlist-2026-W28.md）
> 精选论文: 8篇（来自 paper-shortlist-2026-W28.md）

---

## 主题一：Agent 安全分层体系 🔒

**开源项目**:
- **SkillSpector** — NVIDIA 首个 AI Agent Skill 安全扫描器，68 种攻击模式

**关联论文**:
- **HaloGuard 1.0** (论文7) — 0.8B 宪法分类器，F1 90.9，46 语言覆盖，超越大 30 倍 guard 模型
- **Steerability via Constraints** (论文8) — 4B Gemma 后门检测召回率 90.9%，约束驱动监督
- **LACUNA** (论文5) — 参数级 LLM 遗忘评估平台，揭露现有方法"输出好但参数未擦除"

**联动洞察**:
三个论文 + 一个项目形成了 Agent 安全的四层覆盖：HaloGuard（输入过滤）+ SkillSpector（技能扫描）+ Steerability（编码约束）+ LACUNA（遗忘验证）。HaloGuard 0.8B 打败大 30 倍模型的发现说明**安全是数据工程而非参数量问题**。SkillSpector 的 68 种攻击模式与 Steerability 的约束框架可以组合使用：前者发现漏洞，后者通过编码规范预防。

---

## 主题二：Agent 效率"不修改权重"时代 ⚡

**开源项目**:
- **headroom** — 上下文压缩 60-95%，token 成本直接砍半
- **SkillOpt** — 冻结 LLM 文本空间优化，52/52 基准全胜

**关联论文**:
- **PAW** (论文3) — 4B 编译器→0.6B 解释器，推理内存仅 1/50，匹配 Qwen3-32B 性能
- **CheckRLM** (论文6) — 推理链中及时检查事实一致性，最小成本修正

**联动洞察**:
PAW + SkillOpt + headroom 三个独立工作都走"不修改权重，系统级优化"路线。PAW 用离线编译换取在线效率，SkillOpt 在文本空间做冻结优化，headroom 在上下文侧做压缩。CheckRLM 提供了"优化后如何校验"的闭环——推理链中的事实检查确保压缩/优化不损失准确性。这构成了完整的 Agent 效率三件套：压缩→优化→校验。

---

## 主题三：代码推理与终端 Agent 🛠️

**开源项目**:
- **oh-my-pi** — 终端原生 AI 编码 Agent，LSP/DAP 内置，55K 行 Rust

**关联论文**:
- **DecompRL** (论文2) — GPU token 成本降低 50 倍，组合爆炸从推理转移到评估
- **Steerability via Constraints** (论文8) — 编码 Agent 的约束驱动监督

**联动洞察**:
oh-my-pi 是终端原生编码 Agent，DecompRL 是代码推理的优化方案，Steerability 是编码 Agent 的安全监督。三者覆盖"编码 Agent 的效率+安全"全链路。DecompRL 的 50 倍成本降低可以直接让 oh-my-pi 的推理更快更便宜；Steerability 的约束框架可以为 oh-my-pi 生成的代码提供自动审计。

---

## 主题四：长上下文架构与开源模型 🔬

**开源项目**:
- **GLM-5.2** — 753B MoE，1M 上下文，MIT 许可证

**关联论文**:
- **HOLA** (论文1) — 海马体线性注意力，340M 参数长上下文突破，32k needle recall 大幅优于基线

**联动洞察**:
GLM-5.2 的 1M 上下文是工程实践，HOLA 是架构创新，两者在长上下文需求上共振。HOLA 的双系统架构（有界精确 KV 缓存 + 半参数化测试时记忆）为 GLM-5.2 类模型的长上下文能力提供了理论解释。GLM-5.2 的 MIT 许可证意味着社区可以直接在其上实验 HOLA 架构。

---

## 主题五：自主科研 Agent 与视频 Agent 🎬

**开源项目**:
- **OpenMontage** — 全球首个开源端到端 Agentic 视频制作系统

**关联论文**:
- **Autonomous Research Agents** (论文4) — 端到端自主研究智能体，47 次会话完成从构思到论文

**联动洞察**:
两者共享"端到端自主"的核心范式：Autonomous Research Agents 在凝聚态物理领域实现全流程自动化，OpenMontage 在视频生产领域实现全流程自动化。两者都展示了 Agent 系统"给定目标后自主完成全流程"的能力。OpenMontage 的 12 管道 500+ Skill 可以借鉴 Autonomous Research 的"新鲜上下文隔离+对抗性审查"容错机制。

---

## 主题六：Agent 联网能力与工具调用 🌐

**开源项目**:
- **Agent-Reach** — 让 AI Agent 获得互联网访问能力，13+ 平台零 API 费

**关联论文**:
- **MCP Server Architecture Patterns** (W27 论文，延续影响)
- **PAW** (论文3) — Program-as-Weights 模糊函数编程

**联动洞察**:
Agent-Reach 解决了 Agent"能访问什么"的问题，PAW 解决了 Agent"如何高效调用工具"的问题。Agent-Reach 的智能后端路由与 PAW 的编译器-解释器架构可以结合：将常用工具调用模式编译为轻量权重，通过 Agent-Reach 的路由分发执行。这构成了"工具发现→工具编译→工具执行"的完整链路。

---

## 联动矩阵总览

| 项目 \ 论文 | HOLA | DecompRL | PAW | Auto Research | LACUNA | CheckRLM | HaloGuard | Steerability |
|------------|------|----------|-----|---------------|--------|----------|-----------|--------------|
| SkillSpector | — | — | — | — | 🔗 安全分层 | — | 🔗 输入+技能 | 🔗 约束扫描 |
| headroom | — | — | 🔗 效率 | — | — | 🔗 校验 | — | — |
| SkillOpt | — | — | 🔗 冻结优化 | — | — | — | — | — |
| OpenMontage | — | — | — | 🔗 端到端自主 | — | — | — | — |
| Agent-Reach | — | — | 🔗 工具调用 | — | — | — | — | — |
| oh-my-pi | — | 🔗 代码推理 | — | — | — | — | — | 🔗 编码约束 |
| GLM-5.2 | 🔗 长上下文 | — | — | — | — | — | — | — |

**图例**: 🔗 强关联 | ⭐ 间接关联 | — 弱关联

---

## 核心趋势判断

### 1. 安全正在分层化
HaloGuard（输入）+ SkillSpector（技能）+ Steerability（编码约束）+ LACUNA（遗忘验证）= 覆盖 Agent 全生命周期的安全体系。

### 2. 小模型挑战大模型安全假设
HaloGuard 0.8B 打败大 30 倍 guard 模型；Steerability 用 4B 模型实现 90.9% 后门检测。约束和数据工程 > 纯参数规模。

### 3. Agent 效率进入"不修改权重"时代
PAW + SkillOpt + headroom 三个独立工作都走系统优化路线，企业可在不重新训练模型的情况下获得显著性能/成本提升。

### 4. 从"论文驱动"到"工具驱动"的范式转移
7 个开源项目中 5 个是纯工程驱动。Agent 领域需求已足够具体，工程师可直接构建工具而不等待学术论文。

### 5. 中国开源模型的全球竞争力上升
GLM-5.2 以 MIT 许可证、1M 上下文、SWE-bench Pro 62.1% 的成绩，与 Llama/Qwen 形成三足鼎立。

---

## 强关联组合推荐

| 组合名称 | 组件 | 效果 |
|----------|------|------|
| 安全双层体系 | HaloGuard + SkillSpector | 输入层+执行层全覆盖，0.8B+静态扫描 |
| Agent 效率三件套 | headroom + SkillOpt + CheckRLM | 压缩→优化→校验，不修改权重 |
| 边缘代码部署 | PAW + oh-my-pi | 4B编译→0.6B执行，终端原生低延迟 |
| 长上下文验证 | HOLA + GLM-5.2 | 架构创新+大规模实践互相验证 |

---

> **下一步**: 基于以上分析生成《AI开源情报周报》主文档
