# 周三精选短名单 - Week 36 (2026-09-02)

> 本周主题：Agent Coding Intelligence
> 筛选规则：删除 Star < 100 且无 coverage 的项目
> 最终保留：6 个项目

---

| # | 项目名称 | 类型 | 一句话定位 | Star/Coverage | 验证来源 | 入选理由 |
|---|---------|------|-----------|---------------|---------|---------|
| 1 | **NeMo Switchyard** | 开源框架 | NVIDIA 开源 Agent 动态路由框架，Rust 代理 + 可组合路由算法 | ⭐ ~2.1k | NVIDIA Developer Blog (2026-08-11), blockchain.news, GitHub PR 活跃 | NVIDIA 官方开源，Cognition（Devin）已实际采用验证，支持 OpenAI/Anthropic API 互转，是 Agent 基础设施层的关键拼图 |
| 2 | **Memmy** | 开源工具 | 跨 Agent 共享记忆层，支持 Claude Code / Codex / Cursor 等 6 种工具 | ⭐ ~943 | byteiota.com (2026-08-06), h89.cn 源码拆解, stork.ai 评测, SkillsLLM 收录 | 解决真实痛点——多 AI 工具间记忆不互通。Star 持续快速增长（7月底 342 → 9月初 943），四层记忆 + 六路混合召回架构完整 |
| 3 | **DeepSeek V4-Flash** | 开源模型 | 284B MoE（13B 激活），100万上下文，MIT License | 月下载 310 万次 | VentureBeat (2026-08-13), modemguides 本地部署指南, DeepSeek 官方 | 可本地部署的前沿开源模型，1台 128GB 电脑即可运行。Agent 自托管推理的最优解之一，生态支持 vLLM / SGLang / llama.cpp |
| 4 | **OpenAI Agent Sandbox Breach** | 安全事件 | Prompt 注入绕过限制，泄露系统提示词 | N/A | Wired, 404 Media, Bloomberg - Tier1 媒体全覆盖 | 8月重大安全事件，直接影响 Agent 开发实践。暴露沙箱隔离不足，推动行业重新审视 Agent 安全边界 |
| 5 | **Meta Muse Code** | 闭源 Beta | Meta 终端原生编码 Agent，对标 Claude Code | N/A | buildfastwithai.com, mindstudio.ai, codersera.com, digitalapplied.com 多家评测 | Meta 正式进入编码 Agent 市场，$1.25/$4.25 每百万 token 的定价是行业价格颠覆者。contributor tier 10 倍折扣引发数据隐私讨论 |
| 6 | **BNB Agent Studio v2** | 开发平台 | 一键部署链上 AI Agent，v2 完成赚钱闭环 | SDK 活跃 | CryptoBriefing (2026-08-18), BNB Chain 官方博客, Yahoo Finance | 8 月 18 日发布 v2，Agent 从「能花钱」到「能赚钱」——ERC-8183 商业流完整闭环。Altana 自托管钱包引入链上权限边界，区块链+Agent 经济模型创新 |

---

## 淘汰项目

| 项目名称 | 淘汰原因 |
|---------|---------|
| River AI | 候选池标注"液态AI架构"和"Star: ~1.2k"无法验证；搜索结果显示 River AI 为 Igor Babuschkin 创办的融资公司（$1.1B），与"开源液态架构"描述不匹配 |
| Salesforce "Claudeforce" | 纯商业收购动向，技术信息量有限 |
| OpenAI Agent Plugins 标准 | 标准提案阶段，缺乏实质性代码或产品 |
| DevAgentRadar | 情报聚合工具本身，非本期分析对象 |

---

## 本周亮点

1. **NeMo Switchyard + Memmy 组合**：Agent 基础设施正在补齐——路由（Switchyard）+ 记忆（Memmy）+ 模型（V4-Flash）形成自托管 Agent 的完整技术栈
2. **安全事件倒逼规范**：OpenAI 沙箱绕过事件后，SAFE 框架已获 120+ 组织支持，Agent 安全将从"事后修补"转向"前置设计"
3. **Meta 价格武器**：Muse Code 的 $1.25/$4.25 定价可能迫使 Anthropic 和 OpenAI 调整策略，终端 Agent 市场进入价格战阶段
4. **Agent 经济化落地**：BNB Agent Studio v2 的 ERC-8183 闭环意味着 Agent 可以真正"自食其力"——接任务、交付、收款，无需人工干预

---

*短名单生成时间：2026-09-02 14:00 CST*
*数据源：GitHub API、NVIDIA Developer Blog、VentureBeat、CryptoBriefing 等*
