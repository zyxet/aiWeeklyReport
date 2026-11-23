# 周一开源项目速览 · 2026 W48（11.17–11.23）

## 一、本周热点项目

**1. Kimi K3.1 Pro（Moonshot AI）**
本周开源权重圈最硬的发布。Hugging Face 仓库 11 月 2 日创建，延续 K3 的 MoE 架构并在 agentic 基准上继续刷榜。在 11 月更新的 Open-Weight Benchmark Leaderboard 上处于第一梯队，是当前自部署场景下综合能力最强的开放权重模型之一。值得关注其与 DeepSeek-V4.1-Flash、GLM-5.3 的横向对比。

**2. Microsoft Agent Framework · python-1.26.0（11/13）**
AutoGen 与 Semantic Kernel 合并后的统一框架持续高频迭代。会话管理、工作流检查点（checkpointing + time travel）、内置 OpenTelemetry，MCP client 开箱即用。14.6k stars，MIT 协议，.NET 与 Go 在预览中。生产级多智能体编排的微软系标准答案。

**3. OpenHands v1.40.0（11/12）**
开源编程智能体平台的标杆更新，93.4k stars，MIT。本期看点是沙箱执行与多模型接入的进一步成熟，配合 SWE-bench Pro 类 agentic 评测已经成为 coding agent 基础设施的默认参照物之一。

**4. claude-mem（116k stars）**
跨会话持久记忆层——捕获 agent 会话中的一切行为，用 AI 压缩后在未来会话中按需回注。支持 Claude Code、OpenClaw、Codex、Gemini 等多种 agent。本周在 memory/context 赛道热度极高，代表了"agent 长期记忆"从玩具走向基础设施的节点。

**5. caveman（119k stars）**
病毒式传播的 skill：用"穴居人语"给编码 agent 写 prompt，宣称砍掉 65% token。Go 实现，本质是极致的 prompt 压缩代理。数字惊人，争议也真实——但它把"上下文工程的成本意识"这个议题推到了台前。

## 二、领域趋势观察

**1. 评测基准全面 agentic 化。** MMLU-Pro、SWE-bench Verified 这些老牌基准正在从前沿模型卡片上消失，取而代之的是 Terminal-Bench 2.1→4.0、DeepSWE v1.1、SWE-bench Pro、Toolathlon 以及 Artificial Analysis 综合指数（5.0.1）。模型竞争的战场从"知识问答"彻底转向"能不能干活"，而且对 scaffolding 极其敏感——评测本身的工程含量在快速上升。

**2. 记忆与上下文成为基础设施级赛道。** claude-mem、OpenViking（自进化上下文数据库）、TencentDB-Agent-Memory（四层本地记忆管线）这类项目密集出现，且增长迅猛。共识正在形成：长期运行的 agent 比拼的不只是推理能力，而是"记住了什么、记忆如何治理、上下文如何跨工具跨会话流动"。

**3. 消费级硬件跑前沿模型成为显学。** Qwen3.8-Flash-Next（125B MoE）在 1-2 张 RTX 显卡上跑到 1M 上下文；GLM-5.3-Flash 在 DGX Spark 和双 RTX PRO 6000 上各有调优分支；DeepSeek-V4.1-Flash 在 4x DGX Spark 上做到 438 tok/s。推理优化的战场已经从"能不能跑"转向"跑得好不好、调优过程是否可复现"。

**4. Agent 网关层快速收敛。** LiteLLM（64k）、New API（52k）、agentgateway（6.3k，Rust，MCP+A2A）、Respan Gateway（单 binary 全模型路由）等本周均有活跃更新。模型路由、预算控制、429 故障转移正在从应用层配置下沉为独立基础设施层。

## 三、值得关注的信号

- **SpecPilot**：自动化的投机解码算法发现与系统优化工具——推理加速开始朝"自动调优"方向演进，值得跟踪其对 vLLM/SGLang 生态的渗透。
- **Sim（30k stars, Apache 2.0）**：可视化 AI 工作空间本周发布 v0.9.56，节点式 agent 编排的 UI 层选手，与 Dify（161k，修改版 Apache）形成两条路线之争。
- **AG2 v1.3.1（11/10）**：AutoGen 进入维护模式后，AG2 作为其社区继承者持续迭代，多智能体对话框架的权力交接基本完成。
- **TradingAgents（122k stars）**：多智能体金融交易框架继续疯涨，垂直领域的 multi-agent 协作是当前 star 增长最快的品类之一。
- **Hermes Agent / Prime Agent**：持久化通用 agent 架构与自我改进型长任务 coding agent，8 月以来的增长惯性延续至今，代表"agent 长跑"方向的早期形态。

---
*收集时间：2026-11-23 10:00 CST · 来源：GitHub Trending、Kimi Search、TrendShift、社区评测文章*
