# AI 开源周报（2026 年第 W48 周）

> 生成时间：2026-11-27（周五）
> 覆盖周期：2026-11-23 ~ 2026-11-27
> 数据来源：周三开源短名单（7 项目）+ 周四论文短名单（8 篇）
> 本周主题：**PyPI 供应链投毒** · **Agent 记忆内化竞赛** · **AI 优化 AI 推理**

---

## 本周概览

| # | 项目 | 分类 | 一句话 | 本周最大变化 |
|---|------|------|--------|-------------|
| 1 | **Microsoft Agent Framework** | Agent 框架 | 企业级 Agent SDK（.NET/Python 双语言），本周遭遇 PyPI 供应链投毒 | 11/12 发布 1.26.0 → 11/17 1.26.1/1.26.2 被注入凭据窃取器，~190K 月下载用户面临风险 |
| 2 | **Kimi K3.1 Pro** | 开源模型 | 2.8T MoE + 104B active + 1M context，当前最强开源权重 | API 10/23 上线后持续放量，Morph 平台 $2.50/$14.00 定价引发"自托管 vs API"新一轮成本核算 |
| 3 | **caveman** | Skill 生态 | Token 压缩规则引擎，~1,160 tokens 撬动 78% 压缩率 | Skill Leaderboard 11/1 居首后持续霸榜，"给 AI 做减法"方法论成为 Skill 设计范式 |
| 4 | **claude-mem** | Agent 记忆层 | Claude Code 原生记忆层事实标准，Obsidian 集成 | 11/14 发布 L0 防护机制，独立审计（Issue #5910）确认 v15.16.1 无 Claude Agent SDK 集成 |
| 5 | **OpenHands v1.40.0** | Agent 框架 | 自托管开发者控制中心（Agent Canvas），多 Agent 编排平台 | 11/12 发布 v1.40.0，已迭代至 v1.45.0；93.5K ⭐ 稳居 GitHub 最高星开源 AI SWE 框架 |
| 6 | **Sim (simstudioai/sim)** | Agent 工作区 | 可视化 Agent 构建 + 270+ 集成 + MCP 协议支持 | 突破 30K ⭐，v9.63 发布（11/19），新增"工作流即代码"（workflows as code）能力 |
| 7 | **SpecPilot** | 推理加速 | 用 Agentic Loop 自主发现推理优化策略 | arXiv 11/4 + GitHub 开源；RTX PRO 6000 上投机解码加速 10.87×，"AI 优化 AI 推理"新范式 |

**本周趋势一句话**：W47 的叙事是"中间层协议化与工具化"，本周画风突变——**安全成为主角**。Microsoft Agent Framework 在 PyPI 上遭遇供应链投毒（1.26.1/1.26.2 两个版本被注入凭据窃取器），~190K 月下载量的企业级 Agent SDK 成为攻击目标，而周四论文短名单恰好有 ROGUE-AI（89% 的 Agent 安全事件无需攻击者在场即可复现）和辩论系统内部人攻击——**学术预警和真实攻击在同一周交汇，Agent 安全从"可选"变为"必选"**。与此同时，记忆赛道上 MemOnce（1313× 缓存削减的原生记忆架构）和 claude-mem（116K ⭐ 工程事实标准）形成学术-工程双轨推进；SpecPilot 则用 Agentic Loop 自动发现推理优化，在 RTX PRO 6000 上实现 10.87× 加速——**"AI 优化 AI"从口号变成可复现的代码**。

---

## 论文-开源映射表（A-D 分类）

> 本周结构：**A类 5 · B类 0 · C类 3 · D类 6 · 跨界 1**

**A类：论文 + 官方代码（5 篇）— 可立即复现**

| 论文 | 分数 | 官方代码 | 联动开源项目 | 联动方式 |
|------|------|---------|-------------|---------|
| MemOnce 🏆 | 24 | ✅ clare-nie.github.io/MemOnce | claude-mem | 原生记忆架构（末层隐状态缓存，1313× 削减）↔ 工程侧记忆层——学术从架构层突破，工程从系统集成层落地 |
| MASSys 🏆 | 23 | ✅ github.com/MAS-Sys-Bench/MAS-Sys | OpenHands / Sim | "同一 workflow 换 serving 环境排名翻转"直接警示 Agent 编排平台——评测结果不可跨环境迁移 |
| LongCat LRSA 🏆 | 23 | ✅ 已合并入 SGLang | SpecPilot | 稀疏注意力（1024K 实测）↔ Agentic Loop 推理优化——推理加速的架构派与自搜索派殊途同归 |
| VeriLadder | 22 | ✅ 数据集+模型公开 | — | EDA 工具链自动验证 716K 数据质量，RTLLM 31.7→50.0——数据管线 > 模型规模 |
| RI-Bench | 20 | ✅ 代码+数据公开 | claude-mem / OpenHands | 12,000 episode 角色完整性基准——测试 Agent 在权威压力下是否越权，是 Agent 平台的"出厂安全检测" |

**C类：论文先行（3 篇）— 代码未随论文发布**

| 论文 | 分数 | 对应方向 | 跟进建议 |
|------|------|---------|---------|
| ROGUE-AI 🏆 | 21 | Agent 安全事件复现审计 | **本周最重要论文**——89% 安全事件无需攻击者在场即可复现，直接对标 MS Agent Framework 投毒事件；代码释放后应作为 CI/CD 安全审计工具 |
| S-Mind | 21 | 空间智能内化 | 4B 模型打平 GPT-6-Astra，比工具型 Agent 快 100 倍——关注代码释放和空间 token 的训练方案 |
| Insider Attack | 20 | 多智能体辩论内部人攻击 | 无需提示注入即可操纵辩论结论——对一票否决式决策系统威胁直接，关注防御方案 |

**D类：项目先行（6 个）— 暂无对应论文**：Kimi K3.1 Pro、caveman、claude-mem、OpenHands v1.40.0、Microsoft Agent Framework、Sim

**跨界（1 个）**：**SpecPilot**——同时出现在开源短名单（GitHub 仓库 StargazerX0/SpecPilot）和 arXiv 论文（2611.02501），是罕见的"论文+代码"同步交付的推理优化项目。Agent 是 Claude Opus 5.5 in Claude Code，三轮自主迭代将 Qwen3.8-27B 的 DFlash2 投机解码从 184 tok/s 提升至 416 tok/s。

**B类（社区复现）连续第五周空缺**（W44-W48 均为 0）——放码策略两极分化固化。

**本周最强联动**：**ROGUE-AI（学术预警 Agent 安全风险）× Microsoft Agent Framework 供应链投毒（真实攻击事件）**——论文 11/4 发表（108 起安全事件审计，89% 可自主复现），攻击 11/17 发生（PyPI 包被注入凭据窃取器），同一周内学术诊断被现实验证。论文的核心发现"多数危害 Agent 自己就能造成，不需要攻击者"在投毒事件中精确兑现：恶意 .pth 文件在每次 Python 启动时自动执行，无需任何用户交互。**这不是巧合，是 Agent 生态成熟度到达临界点后的必然**——当 ~190K 月下载量的包成为攻击目标时，安全审计必须成为发布流程的内建环节而非事后补救。

---

## 🔥 重磅推荐

### Microsoft Agent Framework PyPI 供应链投毒 — 2026 年 AI 工具链最严重安全事件

**来源**: [Orca Security](https://orca.security/resources/research/microsoft-agent-framework-pypi-supply-chain-attack-versions-1-26-1-and-1-26-2-steal-cloud-credentials/) · [Chainguard](https://www.chainguard.dev/unchained/microsoft-agent-framework-compromised-on-pypi-november-2026) · [Aikido](https://www.aikido.dev/blog/two-malicious-agent-framework-releases-hit-pypi-in-33-minutes) · [StepSecurity](https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised) · 攻击日期 2026-11-17
**License**: MIT（框架本体）| **Stars**: ~14.6K ⭐ | **包**: `agent-framework` on PyPI（~190K 月下载）

这是本周最重要的事件，也是 2026 年 AI 工具链上最严重的供应链安全事件。

**时间线**：

| 时间 (UTC) | 事件 |
|-----------|------|
| 11/12 | 1.26.0 正常发布（最后一个干净版本，支持 Python 3.14） |
| 11/17 20:35 | **1.26.1 上传 PyPI**——内含凭据窃取器 |
| 11/17 20:36 | Chainguard 扫描器 48 秒内自动阻断（无需外部信号） |
| 11/17 21:06 | PyPI 隔离 1.26.1 |
| 11/17 21:08 | **1.26.2 上传**——攻击者在隔离后 2 分钟再次发布，载荷升级 |
| 11/17 21:16 | PyPI 隔离 1.26.2 |
| 11/17 ~21:20 | 暴露窗口关闭，总时长约 45 分钟 |

**攻击手法**——.pth 启动钩子：

- 恶意代码藏在 `.pth` 文件中（1.26.1 为 `agent_framework_meta.pth`，1.26.2 为 `af_runtime_diag.pth`）
- **Python 在解释器启动时自动处理 .pth 文件**——无论你是否 import agent_framework，只要这个包装了，每次启动 Python 窃取器都会运行
- 这是继 10 月 LiteLLM 1.107.0 之后第二次 .pth 攻击，手法相同

**窃取目标**——直指 AI 开发链：

- 环境变量：TOKEN / SECRET / PASSWORD / KEY / AZURE / AWS / GITHUB / OPENAI / PIP / NPM / NUGET
- 凭据文件：Azure CLI JSON、pip.conf、.npmrc、.netrc、Git credential stores、Docker config.json、**Hugging Face tokens**、Azure Pipelines .credentials、.env files、GitHub Actions runner temp files
- 进程内存：`/proc/<pid>/environ` 读取其他进程环境变量
- 云身份：GitHub Actions OIDC tokens、Azure DevOps OIDC tokens、Azure managed identity tokens（覆盖 9 种 Azure 资源类型）、Azure Instance Metadata Service

**外渗方式**：zlib 压缩 + base64 编码的 JSON，通过 HTTPS POST 发送到 webhook.site 端点，User-Agent 伪装为 `runtime-diagnostics/1`。

**影响范围**：agent-framework 是 umbrella meta-package（依赖 agent-framework-core 等 22+ 子包）。**子包未受影响**——恶意代码只注入 meta-package。但该包 ~190K 月下载量意味着大量开发者的 CI/CD 流水线、云构建环境和本地工作站可能在暴露窗口内安装了恶意版本。

**缓解措施**：PyPI 已隔离两个恶意版本，1.26.0 恢复为最新稳定版。如果在此期间安装了 1.26.1 或 1.26.2：
1. **不要启动 Python**——用 shell 工具（非 Python）删除 .pth 文件和载荷
2. 隔离主机
3. 轮换所有凭据（Azure、GitHub、AWS、HF、OpenAI 等）
4. 撤销 GitHub Actions 和 Azure DevOps 运行时凭据

**为什么重要**：三个层面的警示——

1. **可信发布者 ≠ 可信发布**。两个恶意版本均通过 Microsoft 关联的 PyPI 可信发布者账号上传，说明是账号被盗而非仿冒包。Provenance 只能告诉你谁按的按钮，不能告诉你按钮按下时账号是否还是本人。
2. **.pth 手法持续有效**。它在任何应用代码运行之前执行，甚至对"装了但从未 import"的包也生效——lockfile 中一个未使用的依赖就是一个活的窃取器。
3. **AI 构建链成为靶心**。窃取目标清单直捣模型访问权限（HF tokens、OpenAI keys）和云消费额度（Azure identities）——攻击者知道钱和算力在哪里。

**与本周论文的呼应**：ROGUE-AI（周四短名单 #5）对 108 起 Agent 安全事件做系统化复现审计，发现 89% 无需攻击者在场即可重现危害。11/4 的学术警告，11/17 就成为现实。**Agent 生态的安全成熟度远远落后于功能迭代速度**——我们在造更快的 Agent，但没有给它们配刹车。

**风险**：1.26.1/1.26.2 的具体安装量未公开；攻击者可能通过 webhook.site 日志获取了大量凭据，后续可能有关联攻击；框架的声誉受损可能影响企业采纳节奏；Microsoft 需要重建对 PyPI 发布管线的信任（2FA、签名校验、发布冷却期）。

---

## 工具框架类

### OpenHands v1.40.0 — 从编码 Agent 到开发者控制中心

**仓库**: [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) · **License**: MIT · **Stars**: ~93.5K ⭐
**发布**: v1.40.0（2026-11-12），截至本周已迭代至 v1.45.0

OpenHands（原名 OpenDevin）是目前 GitHub 上 Star 数最高的开源 AI 软件工程代理框架。v1.40.0 的核心变化是**重新定位**：从"让模型帮你写代码的工具"进化为**自托管开发者控制中心（Agent Canvas）**。

**核心能力**：

- **多 Agent 编排**：同一个 Canvas 可统一调度 OpenHands 原生 Agent、Claude Code、Codex、Gemini CLI、Pi、OpenCode 等任意 ACP 兼容 Agent
- **Docker 沙箱执行**：Agent 在容器内动手，你在容器外看结果——Agent 对沙箱内一切有完整权限，宿主机访问由你控制挂载
- **多后端并行**：可同时连接本地 Docker、远端 VM、OpenHands Cloud 多个后端，不同任务分配给不同后端
- **Automations**：可视化配置定时任务（Cron）和 Webhook 事件触发——GitHub 新 Issue → 自动分析 → 拆解任务 → 创建 PR 草稿 → Slack 通知

**迭代节奏**：平均每周一个版本。v1.38.0（11/10）加入对话预算计量器；v1.41.0（11/16）新增自动化设置向导和实验性功能页面；v1.42.0（11/18）支持多 Git 连接选择；v1.44.0-1.45.0（本周）持续打磨 UI 和性能。

**集成面**：支持任意 LLM（通过 LLM Profiles 配置 API Base URL + Model + API Key）；接入 Slack、GitHub、Linear、Notion 完成自动化工作流。

**为什么重要**：93.5K ⭐ + MIT + 每周迭代，OpenHands 是开源 Agent 框架中生态最活跃的选择。它的"控制中心"定位变化反映了市场演化的方向：**单个 Agent 的能力已被充分探索，下一个战场是"如何管理多个 Agent"**——这与本周 Sim 的"工作区"定位、claude-mem 的"记忆层"定位形成互补：OpenHands 管执行，Sim 管编排，claude-mem 管记忆。三个项目共同勾勒出 Agent 基础设施的三层分工。

**风险**：迭代极快（两月内 v1.36→v1.45），API 和配置可能频繁变化；macOS 应用未签名（Gatekeeper 隔离，需手动 `xattr -dr com.apple.quarantine`）；生产环境使用 `latest` 标签的 Docker 镜像有版本漂移风险；多 Agent 编排的权限边界和安全隔离需要额外审查——尤其在本周 MS Agent Framework 投毒事件的背景下。

### Sim (simstudioai/sim) — 30K 星的 Agent 协作工作区

**仓库**: [simstudioai/sim](https://github.com/simstudioai/sim) · **License**: Apache 2.0 · **Stars**: ~30.1K ⭐（11/20 数据）
**版本**: v9.63（2026-11-19）

Sim 是协作式 AI Agent 工作区——构建、部署、监控 Agent 和 Workflow 的一体化平台，自称被 100,000+ builder 使用。

**核心能力**：

- **可视化 Agent 构建**：拖拽式工作流编辑器，270+ 集成（Twilio、monday、asana、clickup、airtable、notion、supabase、amplitude、box、docusign、dropbox 等）
- **MCP 协议支持**：`https://mcp.sim.ai/mcp` 端点，Claude Code、Codex 等 MCP 客户端可直接连接，管理 workspace、运行 workflow、操作表格/知识库/文件/日志
- **工作流即代码**（Workflows as Code）：v9.63 新增能力，workflow 和 workspace 可以代码形式定义和版本管理
- **多模态工作区**：Chat、Workflow、Tables（内置数据库）、Files、Knowledge（Agent 记忆）、Desktop（Mac 应用）统一在一个 workspace
- **Computer Use**：编辑日历事件、管理联系人、查找提醒——通过 app commands 操控桌面应用

**迭代节奏**：极其激进——11/19 一天内发布 9.63，此前四天发了五个版本。最近重点：MCP code mode 全量开放、PII 服务 NetworkPolicy 隔离、CSP 策略收紧、SSO 回调域名验证。

**为什么重要**：30K ⭐ + Apache 2.0 + 100K+ 用户，Sim 在"Agent 工作区"赛道与 Dify（161K ⭐）形成差异化竞争：Dify 偏开发者/API 优先，Sim 偏可视化/协作优先。v9.63 的"工作流即代码"是重要信号——**可视化编排和代码定义正在融合**，而非对立。本周发布还包含从 OpenAI Agent Builder 迁移的指南（后者将于 11/30 关停）——平台洗牌期，Sim 在积极吸收流离用户。

**风险**：版本号跳跃极快（9.63），API 稳定性需要验证；computer-use 功能涉及桌面操控，安全边界需要审查；自托管 Helm chart 的默认配置需要加强（近期修复了 placeholder secrets 和 CSP 问题）；与 Dify/n8n 等竞品的功能同质化压力。

### caveman — 119K 星的 Skill 生态标杆：给 AI 做减法

**仓库**: [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) · **License**: MIT · **Stars**: ~119K ⭐
**排名**: Skill Leaderboard 11/1 居首

Caveman 是一个极致精简的编码 Agent 规则引擎——核心理念是"给 AI 工具做减法"。安装仅需 `npx skills add JuliusBrussee/caveman -g`。

**核心机制**：

- **Rules 仅 ~1,160 tokens**：对比动辄上万 token 的 system prompt，caveman 的规则集精巧到可以全文阅读
- **双模式**：`/caveman` 在基线规则上再减 3% token；`/ultracave` 直接砍 35% token——激进的压缩模式
- **78% Token 压缩率**：实际使用中大幅降低 Agent 的上下文消耗

**为什么重要**：119K ⭐ 的 Skill 项目，在 Skill Leaderboard 上压过众多大厂出品居首——这说明社区对"轻量级 Skill"有真实需求。caveman 的崛起与 W47 的 stitch-skills（Google 官方 Skills 库）形成有趣对照：**一个是大厂精心设计的 15 技能套件，一个是个人开发者 1,160 tokens 的规则集，星数却是后者的 18 倍**。原因可能很简单：多数开发者不需要 15 个技能，他们需要的是一个"装了就能用、不占上下文"的默认配置。在 Skill 生态膨胀期，caveman 的"减法哲学"是对过度工程化的一记耳光。

**风险**：Token 压缩率与输出质量的 trade-off 需要实测验证——/ultracave 模式砍掉 35% token 是否影响代码质量，尚无独立基准；规则集过于精简可能遗漏边缘场景；作为个人项目，长期维护承诺不确定。

---

## Agent 记忆与基础设施

### claude-mem — 116K 星记忆层的事实标准与它的 L0 防护

**仓库**: [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) · **License**: MIT · **Stars**: ~116K ⭐
**版本**: v15.16.1 · **最近更新**: 2026-11-14（L0 防护机制）

claude-mem 是 Claude Code 的原生记忆层——Obsidian 集成 + 结构化日志 + 跨会话持久记忆，是该赛道星数最高的项目。

**本周关键动态**：

- **L0 防护机制（11/14）**：引入分级防护方案，修复成本据报 $1.9M。L0 是最低防护级别，提供基础的记忆完整性和安全保证
- **独立审计（Issue #5910，11/10）**：社区对 v15.16.1 进行了安全审计，确认**无 Claude Agent SDK 集成**——这意味着 claude-mem 目前通过非官方方式与 Claude Code 交互，存在被官方更新打破的兼容性风险
- **版本节奏**：v15.9.0（11/3）→ v15.16.1（11/14），十天七个补丁版本，迭代极快

**与本周论文的联动**：MemOnce（24/25，本周论文最高分）提出了"只缓存末层隐状态"的原生记忆架构，在 1M 上下文下实现 1313× 缓存削减。claude-mem 走的是另一条路——在应用层用结构化的 Markdown + Obsidian 知识图谱模拟记忆。两条路线的对比：MemOnce 从模型架构层面解决记忆问题（需要重新训练），claude-mem 从系统集成层面解决（即插即用）。**短期内 claude-mem 的路线更实用，长期 MemOnce 的路线更根本**——但当 LongCat LRSA（稀疏注意力，1024K 实测）这样的推理层优化普及时，应用层记忆工具的价值命题可能需要重新校准。

**风险**：Issue #5910 揭示的"无 Claude Agent SDK 集成"是实质性风险——意味着依赖非公开 API 或 hook 机制，Claude Code 任何更新都可能破坏兼容性；$1.9M 修复成本的 L0 防护暗示此前存在严重安全漏洞，具体细节未完全公开；116K ⭐ 的项目由个人开发者维护，巴士因子极低。

---

## 模型与算法类

### Kimi K3.1 Pro — 最强开源权重的"API 经济学"

**来源**: [Hugging Face](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) · [Morph 实测](https://www.morphllm.com/kimi-k3-1) · 权重 11/2 上架
**License**: Kimi K3.1 Pro License（MIT 风格主体 + 附加条款：年营收 $20M 或月活 100M 以上需额外授权）
**架构**: 2.8T MoE（896 experts，top-16）· 104B active · 1M token 上下文 · 原生 MXFP4

K3.1 Pro 连续第三周入选短名单（W46 现实检验 → W47 社区量化 → W48 API 经济学）。本周的新增信息是 Morph 平台的第三方评测和 API 定价对比。

**关键数据**（Morph 评测，2026-11-09）：

- **API 定价**：$2.00 input / $10.00 output per 1M tokens；cached input 仅 $0.20
- **Morph 平台定价**：morph-kimik31 $2.50 / $14.00（比官方 API 略高）
- **Terminal-Bench 4.0**：65.7 vs Claude Opus 5.5 的 66.4——差距不到 1 个百分点
- **Artificial Analysis Intelligence Index v5**：46 分，登顶 open-weight 榜首
- **API 上线时间**：2026-10-23

**成本数学**（更新版）：W46 的结论（"自托管没有经济性"）在 API 正式定价后更加清晰。以一个月 10 亿 token 的调用量估算，API 成本约 $12,000-60,000（取决于 input/output 比例和缓存命中率）。而自托管需要至少 8×H100（或等效 GPU）运行 104B active MoE，月成本远超 $50,000。**API 是唯一经济选择**，除非有数据主权或合规需求。

**但社区量化仍在推进**：llama.cpp `kimi_k31` 架构 PR 待合并，Unsloth GGUF（Q4_K_XL 1,509 GB）已发布。W47 的判断在 W48 依然成立：GGUF 的意义不是"让桌面用户能跑"，而是**打开 llama.cpp 生态的适配通道**——Ollama、LM Studio、llama-server 的跟进只是时间问题。

**为什么持续重要**：K3.1 Pro 的三周叙事（落地→检验→接力→经济学）是 2026 年"开放权重"故事最完整的切片。本周的新增维度是**API 定价的竞争力**——$2/$10 的定价低于 Claude Opus 5.5（~$15/$75）和 GPT-6（~$10/$30），而 Terminal-Bench 差距不到 1 分。**"接近前沿性能 + 1/7 价格"的组合在推理密集型场景（代码生成、长文档分析）中具有碾压性优势**。

**风险**：License 附加条款（$20M 营收/100M MAU）对大企业的法律合规团队是审查障碍；1M context 的实际延迟和成本需要场景化评估；社区量化在 MXFP4 原生权重上的信息损失尚缺独立基准；API 服务的稳定性和速率限制在生产负载下未经验证。

### SpecPilot — AI 优化 AI 推理：Agentic Loop 自主发现 10.87× 加速

**仓库**: [StargazerX0/SpecPilot](https://github.com/StargazerX0/SpecPilot) · **论文**: [arXiv 2611.02501](https://arxiv.org/abs/2611.02501)（2026-11-02/04）
**Stars**: < 100（新项目）· **硬件**: H100 SXM5 / RTX PRO 6000 Blackwell Server Edition

SpecPilot 是本周最有趣的技术项目——用 Claude Opus 5.5 in Claude Code 作为 Agent，**自主发现**投机解码（Speculative Decoding）的最优系统配置，而非人工调优。

**工作原理**：

1. **多轮自主迭代**：Agent 分析当前系统的性能瓶颈（cost model 重新测量每轮的上限），提出优化方向，实现补丁，用配对运行（paired runs）验证，提升则晋级（promote）
2. **Token Forcing 验证**：每个"密封终版"（sealed final）都需通过在未见请求上的计时测试和 token 强制一致性检查——防止 reward hacking
3. **W12 无损 12-bit 权重格式**：四轮部署中最大单一贡献——在 GEMM 寄存器内逐位精确解码 BF16 权重，使纯 BF16 推理在 8-30B 模型上加速 1.15-1.26×（batch 1-32），在最多 64 行的 GEMM 上击败 cuBLAS BF16

**关键数据**：

| 部署 | 加速比 | Tokens/step | 解码速度 |
|------|--------|-------------|---------|
| Qwen3.8-27B + DFlash2, H100（单请求） | **2.13×** | 4.65→13.08 | 184→416 tok/s |
| Qwen3.8-27B + DSpark, H100 | **2.38×** | 4.42→12.85 | 173→435 tok/s |
| Qwen3.8-27B + DFlash2, RTX PRO 6000 | **2.44×** | 5.23→12.80 | 108→272 tok/s |
| Muse-Glimmer-30B + DFlash2, RTX PRO 6000 | **2.21×** | 5.16→12.64 | 111→256 tok/s |
| **RTX PRO 6000 综合（跨 5 项基准）** | **10.87×** | — | — |
| Gemma-4-12B + EAGLE-3, H100（单请求） | **3.11×** | 2.04→2.54 | — |

实际场景演示：PEAR 机器人推理系统（Qwen3.8-27B + DFlash2），同一 LIBERO 任务，SpecPilot + efficient reasoning 在 49.2 秒完成，而基线（vLLM + DFlash2）需要 188.7 秒——**3.84× 端到端加速**。

**为什么重要**：三个层面——

1. **方法论**：传统推理优化依赖人类专家逐层调优，SpecPilot 证明 Agentic Loop 可以在 7-27 小时 GPU 时间内自主发现等效甚至更优的配置。三轮迭代中每轮瓶颈不同（第一轮 token 数、第二轮权重字节、第三轮 kernel 效率），Agent 每次都正确识别并转向。
2. **W12 格式**：12-bit 无损权重编码是独立贡献——比特精确还原 BF16 权重，同时在 GEMM 中直接解码，减少 25% 权重读取量。这个格式对纯 AR 推理也有效（不依赖投机解码）。
3. **与本周论文的呼应**：LongCat LRSA（稀疏注意力）代表"人类架构创新"路线，SpecPilot 代表"AI 自主搜索"路线——两条路线在同一周推进，且都作用于 SGLang 推理栈。**当 AI 开始优化 AI 的基础设施时，优化循环本身就在加速**——第一轮 11.7 小时，第二轮 19.3 小时，但第二轮有 103 个变更（vs 第一轮 26 个），Agent 的学习曲线在陡峭上升。

**风险**：< 100 ⭐ 的新项目，代码质量和可维护性未经社区检验；H100/RTX PRO 6000 的 kernel 优化绑定特定 GPU 架构（sm_120a），不具可移植性；Agent 自主优化的可解释性有限——知道"什么有效"但"为什么有效"可能需要逆向工程；依赖 Claude Opus 5.5 in Claude Code 作为 Agent，优化成本本身不低（单部署 20-86 GPU-hours）。

---

## 数据观察

### 本周安全事件：MS Agent Framework 投毒——AI 工具链的"心脏出血时刻"？

| 维度 | 数据 |
|------|------|
| 受影响包 | `agent-framework` on PyPI（meta-package） |
| 恶意版本 | 1.26.1、1.26.2 |
| 最后一个干净版本 | 1.26.0（11/12） |
| 暴露窗口 | ~45 分钟（11/17 20:35–21:20 UTC） |
| 月下载量 | ~190K |
| 未受影响 | agent-framework-core + 22 个子包 |
| 攻击手法 | .pth 启动钩子（第二次，第一次是 LiteLLM 1.107.0） |
| 窃取目标 | Azure/GitHub/AWS/HF/OpenAI 凭据 + 云身份 token |

这次事件可能成为 AI 工具链安全的转折点。三个结构性问题暴露无遗：.pth 手法的持续有效性（Python 生态的已知弱点）、可信发布者机制的单点失效（账号被盗即可发布恶意版本）、以及 AI 构建链作为高价值目标的现实（模型访问权限 + 云消费额度 = 攻击者的双重动机）。

### 论文代码开放率：5/8（62.5%），连续两周稳定

| 周 | A类 | C类 | 开放率 |
|---|-----|-----|--------|
| W46 | 3 | 5 | 37.5% |
| W47 | 5 | 3 | 62.5% |
| W48 | 5 | 3 | 62.5% |

NeurIPS 2026 截稿季后的代码释放窗口持续。C 类 3 篇（ROGUE-AI / S-Mind / Insider Attack）均涉及安全方向——安全论文的代码释放通常更谨慎（防止攻击手法被滥用），这是合理的不释放理由。

### Agent 安全研究占比：3/8（37.5%），创历史新高

周四短名单 8 篇论文中 3 篇聚焦 Agent 安全：ROGUE-AI（安全事件复现审计）、Insider Attack（辩论系统内部人攻击）、RI-Bench（角色完整性基准）。加上开源侧的 MS Agent Framework 投毒事件，**"Agent 安全"首次同时占据开源和学术两个维度的最大权重**——这不是偶然，是 Agent 部署量达到临界点后的必然。

### Kimi K3.1 Pro 四周叙事弧

| 周 | 叙事 | 关键事件 |
|---|------|---------|
| W45 | 权重落地 | 11/2 权重上架 HF，1.56TB，MXFP4 |
| W46 | 现实检验 | 无 GGUF、无 llama.cpp、门槛 610GB 起 |
| W47 | 社区接力 | Unsloth GGUF 落地（1,509 GB Q4_XL），llama.cpp PR 待合并 |
| W48 | API 经济学 | API 定价 $2/$10 公布，Terminal-Bench 65.7 vs Opus 66.4，性价比优势确立 |

四周完成"落地→检验→接力→经济学"的完整叙事弧。K3.1 Pro 正在从"技术奇迹"变成"经济选择"——这是开源模型生命周期中最关键的转变。

---

## 推荐阅读

1. **[Microsoft agent-framework compromised on PyPI（Chainguard, 2026-11-17）](https://www.chainguard.dev/unchained/microsoft-agent-framework-compromised-on-pypi-november-2026)** — 最完整的技术分析：.pth 手法、窃取目标清单、Chainguard 48 秒自动阻断的决策逻辑、以及"可信发布者 ≠ 可信发布"的深层洞察
2. **[Two malicious agent-framework releases hit PyPI in 33 minutes（Aikido, 2026-11-17）](https://www.aikido.dev/blog/two-malicious-agent-framework-releases-hit-pypi-in-33-minutes)** — 攻击时间线的逐分钟还原，含两轮载荷的差异分析
3. **[Microsoft agent-framework PyPI Supply-Chain Attack（Orca Security）](https://orca.security/resources/research/microsoft-agent-framework-pypi-supply-chain-attack-versions-1-26-1-and-1-26-2-steal-cloud-credentials/)** — 影响面评估和 IOC（入侵指标）清单
4. **[SpecPilot 论文（arXiv 2611.02501）](https://arxiv.org/abs/2611.02501)** — Agentic Loop 自主推理优化的完整方法论，含 W12 无损权重格式细节和三轮迭代的瓶颈转移分析
5. **[OpenHands 完整教程：v1.40.0 从安装到自动化（腾讯云开发者社区, 2026-11-16）](https://cloud.tencent.com/developer/article/2785331)** — Agent Canvas 四种安装方式的场景化选择指南 + 生产环境配置建议
6. **[Sim: open-source workspace for AI agent workflows（Rank Agents, 2026-11-20）](https://rankagents.app/blog/sim-review)** — Sim 平台能力评测，含 v9.63 新特性分析

---

*由 friday-report 任务生成 | intelligence-system*
*数据源：data/os-shortlist-2026-W48.md + data/paper-shortlist-2026-W48.md*
*联动分析：output/weekly-report-paper-os-2026-W48.md（待 friday-paper-merge 生成）*
