# 周三精选短名单 · W38 / 2026-09-16

> 筛选来源：`data/os-pool-2026-W38.md`（17 个候选）
> 筛选规则：Star < 100 且无媒体 coverage → 淘汰；最终保留 7 个
> 数据验证时间：2026-09-16 14:00 CST（GitHub API 实时 star / 媒体检索）

---

## 一、本周短名单（7 个）

### AI Agent 基础设施层（6）

| 项目 | 定位 | 实时 Star | 技术测评要点 | 媒体 Coverage | 风险/备注 |
|------|------|-----------|--------------|---------------|-----------|
| **OpenClaw** | 个人 AI 助手网关（IM 渠道接入） | **389,816** | 渠道生态最完整（Telegram/Discord/Slack/飞书/钉钉/企微）；v2026.9.4 支持 ACP 协议接入 Codex/Claude Code | 持续高热度，中文社区覆盖密集 | 本体代码未开源（仅 runtime），周报长期跟踪项 |
| **DeepSeek Harness** | Agent harness / 沙箱执行环境 | **225,726** | 与 DeepSeek-V4 同步发布；执行层标准化方向明确 | 发布即登顶 GitHub Trending | ⚠️ **CVE-2026-82533 沙箱逃逸漏洞**（2026-09-08 披露），生产部署需等补丁或加隔离 |
| **MCP reference servers** | MCP 协议官方参考实现 | **90,368** | MCP 已成事实标准；数据库类 server 进入 GA 阶段 | 协议层持续被引用 | 注意许可证为自定义（NOASSERTION），非标准 OSI |
| **Mem0** | Agent 记忆层 | **65,372** | 记忆检索仍是 agent 产品化最大痛点； Mem0 为默认方案之一 | 配套评测文持续产出 | 赛道竞品多（Zep 等），护城河一般 |
| **Mastra** | TypeScript Agent 框架 | **28,090** | TS 生态 agent 框架头部；工作流编排 + 记忆 + 工具链一体化 | 海外 JS 社区覆盖稳定 | Python 生态分流（LangGraph），增长趋缓 |
| **TrueForge** ⭐新锐 | 声明式 Agent 运行时 | **5,669** | 配置文件定义 agent 行为，vibe coding 友好；8 月发布，增长曲线陡（48h 内 2,100→5,669） | 发布初期海外技术圈有讨论 | 项目极年轻（<30 天），生产案例少，观察期 |

### 开源语音合成（TTS）（1）

| 项目 | 定位 | 实时 Star | 技术测评要点 | 媒体 Coverage | 风险/备注 |
|------|------|-----------|--------------|---------------|-----------|
| **MOSS-TTS** | 语音/音效生成模型家族 | **4,109** | Apache-2.0；覆盖长文 narration、多说话人对话、语音设计、音效、实时流式全场景；MOSS-TTSD v1.0 主观评测超 Doubao 与 Gemini 2.5-pro；支持 vLLM-Omni 推理；last push 2026-09-06，维护活跃 | CSDN/掘金教程、hysenlabs 深度评测（2026-09-09）、Pinokio 收录 | 推理需较新依赖栈（Transformers 5.0）；GPU 门槛仍在 |

---

## 二、淘汰清单（10 个）及理由

| 项目 | 淘汰理由 |
|------|----------|
| Chatterbox (Resemble AI) | 26,442★ 但 repo 自 2026-07-21 无更新，近 2 个月无新 release，社区活跃度下降 |
| Qwen3-TTS | 13,406★ 但 last push 2026-03-17，维护停滞半年，issue 响应慢 |
| Orpheus-TTS | 6,339★ 但 last push 2025-12-05，近 9 个月无更新，实质停更 |
| NeuTTS | 6,281★，但许可证为自定义（NOASSERTION），商用合规需逐条确认；产品化程度低 |
| Bonsai 8B (PrismML) | 1-bit 量化技术突破（1.15GB / iPhone 44 tok/s），媒体 coverage 强（Forbes/ArsTechnica），但发布于 2026-03-31，非本周活跃事件；且主流推理引擎（LM Studio/Ollama）尚不支持 1-bit，落地受阻——移入观察池 |
| Kimi K3（Moonshot） | HF 权重发布（2.8T MoE），coverage 充足；非代码仓库项目，无 GitHub star 轨迹，本榜单不覆盖模型权重类 |
| Muse Glimmer（Meta） | 同上，30B 权重发布，非代码仓库生态项目 |
| Apertus 1.5 | 同上，8B/70B 开放权重 |
| Hy3（腾讯） | 同上，295B MoE 权重发布 |
| FLUX.2-dev / Z-Image / ERNIE-Image-Turbo | 同上，图像生成权重发布，模型类项目不在本周代码生态榜单范围 |

---

## 三、本周核心判断

1. **基础设施层"执行环境"成新战场**：DeepSeek Harness 以 225k star 证明 harness/沙箱层已是 agent 生态最大公约数，但 CVE-2026-82533 同时敲响警钟——执行层安全审计将成企业 adoption 前置条件。
2. **TrueForge 是本周最值得跟踪的新锐**：<30 天 5.7k star，声明式范式对非专业开发者友好。若下周 star 增速保持，升级为重点评测对象。
3. **TTS 赛道进入"全家族"竞争**：MOSS-TTS 一个 repo 覆盖 narration/对话/音效/流式/语音设计五个场景，且有主观评测对标闭源模型的数据。单独的 TTS 模型 repo（Chatterbox/Orpheus）在活跃度上已掉队。
4. **协议层固化**：MCP 参考实现 star 突破 9 万，"agent 怎么连工具"这个问题正在被 MCP 终结，差异化竞争上移至编排层与记忆层。

---

*筛选：Kimi Claw · 2026-09-16 14:00 CST*
*下一步：thursday-deep-dive（短名单深度评测）*
