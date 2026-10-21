# 周三精选短名单 — 2026-W43

> 筛选时间：2026-10-21 14:00 CST
> 来源候选池：`data/os-pool-2026-W43.md`（12 个项目全部完成联网验证）
> 筛选规则：删除 Star < 100 且无 coverage 的项目；主名单保留 5-7 个

## 主名单（7 个）

| # | 项目 | 实时 Star | 语言/许可 | 一句话 | 本周验证要点 |
|---|------|-----------|-----------|--------|--------------|
| 1 | [stablyai/orca](https://github.com/stablyai/orca) | ~96K（10/18 GitHub Trending #8） | Electron/Rust | Agent 舰队编排器：桌面、移动端、远程 runtime 统一跑编码 agent | 10/17 与 ai-memory 同上 Trending，被定性为「agent 时代缺的操作系统级基础设施」；fleet 并行 + 多 runtime 是当前最完整的多 agent 形态 |
| 2 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | ~11.9K（10/20，本周 +208/日） | Rust / MIT | 跨厂商编码 agent 的长期记忆与 handoff 层 | 10/17-20 连续 Trending（#6）；git 版本化 Markdown wiki + SQLite FTS5，零 LLM 默认路径；与 orca 构成「记忆 + 编排」双主线，是本周最值得写的技术故事 |
| 3 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | ~77K（10/20 trendshift，周增 17.1K） | Python+Electron / AGPL-3.0 | 全本地 ElevenLabs 替代品：克隆/设计/配音/听写/有声书，646 语言 | 10/18 起稳居 Trending #10；bicarait 10/11 发了架构拆解（Local API + MCP 暴露给 agent 工作流）；默认引擎 k2-fsa/OmniVoice，隐私优先 |
| 4 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | ~74K | TypeScript+Rust/WASM / MIT | Claude Code/Codex 的多 agent 编排 meta-harness（原 claude-flow） | 生态累计 22M+ 下载；98 个专职 agent + HNSW 向量记忆 + 314 个 MCP 工具；v3.x 持续月更，是编排赛道事实标准，可作 orca 的对照组写 |
| 5 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | ~54.2K（10/18 Trending #4） | — | 给任意命令行软件包一层 agent-native 外壳 | HKUDS 出品（港大数据智能实验室），「agent 原生封装存量 CLI」的思路与 MCP 互补；连续多日 Trending 前四 |
| 6 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | ~51K（10/18 Trending #2） | TypeScript+Python+LaTeX / MIT | 跑在本地、基于 Claude Code 的求职流水线：评估 JD、定制 CV、求职信、面试准备 | 9 个 slash 命令 + drafter-reviewer 双 agent；带 PDF 布局校验和 robots.txt 合规爬虫；「个人工作流 fork 即拥有」的范式样本 |
| 7 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | ~42.1K（10/18 Trending #1，单日 +1,146） | — | Anthropic 官方 Claude Code 插件目录 | 官方下场做插件市场，单日增速本周第一；标志着技能生态从社区散装走向官方托管 |

## 备选（验证通过，主名单满额未入，留作下周观察）

| 项目 | Star | 未入主名单原因 |
|------|------|----------------|
| [elstongun/leviathan](https://github.com/elstongun/leviathan) | ~833 | 技术故事极锋利（~450 token/回答 vs grep 107K token，33ms 延迟，TLDR Data 10/12 报道），但体量最小，适合作为「小体量深技术」彩蛋位 |
| [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html) | ~4K（18 天） | agent skill 让模型只写 Markdown 草稿、CLI 出单页 HTML（token 降到 1/8）；有 HN 帖但互动尚浅 |
| [facebookincubator/muse-gadget-sdk](https://github.com/facebookincubator/muse-gadget-sdk) | ~1.8K | Meta 开源 ESP32/Pi 的 Muse 硬件 SDK（The Verge 报道 + HN 250 分）；硬件向，与本期软件主线偏离 |

## 已剔除

| 项目 | 原因 |
|------|------|
| Meta Muse Wonder | 闭源 API 产品，非开源项目；故事已由 muse-gadget-sdk 覆盖 |
| Kimi-Linear-48B-A3B | MIT 模型发布（HF），属模型动态非工具，建议进「大模型」板块单独跟踪 |
| Qwen3.6 GGUF 视频版 | 模型量化资源，同上 |

## 本期主线判断

**「Agent 需要操作系统」是 W43 的唯一主线。** orca（编排）+ ai-memory（记忆）在 10/17 同日上 Trending 不是巧合——社区正在用脚投票补齐 agent OS 的两个核心原语。Ruflo 是同赛道的在位者，正好构成「新贵 vs 标准」的对照结构。VoiceStudio 则代表另一条线：本地化的垂直能力栈（语音）正在吃掉 SaaS。三幕结构清晰，周五成稿建议按此组织。
