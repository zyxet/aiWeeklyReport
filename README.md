# AI 开源情报周报 | AI Open Source Intelligence Weekly

> **自动追踪 LLM 与 AI Agent 领域的开源动态与前沿论文，每周五生成结构化情报报告。**
>
> **Automated tracking of open-source dynamics and frontier papers in LLM & AI Agent, generating structured intelligence reports every Friday.**

---

## 简介 | Overview

本项目是一个自动化情报收集系统，每周执行六轮定时任务，从 GitHub、arXiv、Hugging Face 等渠道抓取 AI 开源项目与学术论文，经过多轮筛选、验证和联动分析，最终生成中文周报。

This project is an automated intelligence collection system that executes six scheduled tasks weekly, crawling AI open-source projects and academic papers from GitHub, arXiv, Hugging Face, etc. After multi-round filtering, verification, and linkage analysis, it generates Chinese weekly reports.

**覆盖领域 | Coverage:**
- LLM (Large Language Models)
- AI Agent / Multi-Agent Systems
- RAG (Retrieval-Augmented Generation)
- Prompt Engineering & Chain-of-Thought
- Multimodal Models
- MoE (Mixture of Experts)
- AI-Native Developer Tools

---

## 工作流程 | Workflow

| 星期 | 任务 | 输出文件 | 说明 |
|------|------|----------|------|
| **周一** | 情报收集 | `candidate-pool-YYYY-WW.md` | 从 GitHub Trending、HackerNews 等抓取 10-15 个候选项目 |
| **周二** | 论文雷达 | `paper-pool-YYYY-WW.md` | 从 arXiv cs.CL/cs.LG/cs.AI、Hugging Face Papers 收集 15-20 篇论文 |
| **周三** | 深度筛选 | `shortlist-YYYY-WW.md` | 验证网络数据、打分排序，保留 6-8 个精选项目 |
| **周四** | 论文精选 | `paper-shortlist-YYYY-WW.md` + `weekly-paper-selection-YYYY-WW.md` | 论文评分、摘要生成、标记与开源项目的关联 |
| **周五** | 周报生成 | `weekly-report-YYYY-WW.md` | 汇总开源情报，生成完整周报 |
| **周五** | 论文-开源联动 | `paper-os-linkage-YYYY-WW.md` | 论文与开源项目的映射分析（A/B/C/D 分类） |

---

## 目录结构 | Directory Structure

```
aiWeeklyReport/
├── data/                          # 原始数据与中间产物
│   ├── candidate-pool-YYYY-WW.md      # 周一：开源候选池
│   ├── shortlist-YYYY-WW.md           # 周三：开源短名单
│   ├── paper-pool-YYYY-WW.md         # 周二：论文候选池
│   ├── paper-shortlist-YYYY-WW.md    # 周四：论文短名单
│   ├── weekly-report-YYYY-WW.md      # 周五：AI 开源周报
│   └── weekly-paper-selection-YYYY-WW.md  # 周四：论文精选周报
├── output/                        # 深度分析产出
│   └── paper-os-linkage-YYYY-WW.md   # 周五：论文-开源联动分析
├── scripts/                       # 自动化脚本（可选）
└── README.md                      # 本文件
```

> **命名规则 | Naming Convention:** `filename-YYYY-WW.md`，其中 `YYYY` 为年份，`WW` 为 ISO 周数（如 `2026-W17`）。
>
> **Naming Rule:** `filename-YYYY-WW.md`, where `YYYY` is the year and `WW` is the ISO week number (e.g., `2026-W17`).

---

## 筛选标准 | Selection Criteria

### 开源项目 | Open Source Projects

| 维度 | 权重 | 说明 |
|------|------|------|
| 创新性 | 20% | 全新架构/范式 vs 微创新 |
| 实用性 | 20% | 生产可用 vs 纯理论研究 |
| 技术深度 | 20% | 理论扎实、工程完善 |
| 机构背书 | 20% | OpenAI/DeepMind/微软等 vs 独立开发者 |
| 社区热度 | 20% | Stars 增长趋势、Issue 活跃度 |

**排除项 | Exclusions:**
- 绕过付费的代理工具（合规风险）
- 纯合集类仓库（Awesome-list 等）
- 非 AI 领域（如纯安全工具、纯金融项目）
- 数据不足或影响力有限的项目

### 学术论文 | Academic Papers

| 维度 | 权重 | 说明 |
|------|------|------|
| 创新性 | 20% | 全新架构 5 分 / 微创新 3 分 |
| 实用性 | 20% | 生产可用 5 分 / 理论研究 1 分 |
| 技术深度 | 20% | 理论扎实 5 分 / 缺乏验证 1 分 |
| 机构背书 | 20% | OpenAI/DeepMind 等 5 分 / 独立研究者 1 分 |
| 代码可得性 | 20% | 官方开源 5 分 / 无代码 1 分 |

---

## 论文-开源联动分类 | Paper-OS Linkage Categories

每份联动分析报告将项目/论文分为四类：

| 分类 | 定义 | 优先级 |
|------|------|--------|
| **A 类** | 论文 + 官方代码 | ⭐⭐⭐⭐⭐ |
| **B 类** | 论文 + 社区复现 | ⭐⭐⭐⭐ |
| **C 类** | 论文先行，暂无代码 | ⭐⭐⭐ |
| **D 类** | 项目先行，论文后发 | ⭐⭐⭐ |

---

## 使用方式 | How to Use

1. **阅读周报 | Read Reports:** 直接打开 `data/weekly-report-YYYY-WW.md` 查看当周精选项目与趋势分析
2. **深挖项目 | Deep Dive:** 查看 `data/shortlist-YYYY-WW.md` 了解每个项目的详细评分与排除原因
3. **追踪论文 | Track Papers:** 查看 `data/paper-shortlist-YYYY-WW.md` 获取带评分的论文列表
4. **联动洞察 | Linkage Insights:** 查看 `output/paper-os-linkage-YYYY-WW.md` 了解论文与开源项目的映射关系

---

## 自动化 | Automation

本项目完全自动化运行，由 [OpenClaw](https://github.com/openclaw/openclaw) + Kimi AI 驱动：

- **定时任务 | Scheduled Tasks:** 周一到周五自动执行
- **数据持久化 | Data Persistence:** 所有产出自动提交到本仓库
- **通知渠道 | Notification:** 周报完成后推送到飞书私聊

---

## 许可 | License

本项目中的报告内容基于公开数据源（GitHub、arXiv 等）生成，仅供学习与研究使用。各项目与论文的版权归原作者所有。

The report content in this project is generated from public data sources (GitHub, arXiv, etc.) and is intended for learning and research purposes only. The copyright of each project and paper belongs to its respective author.

---

> **"追踪开源，记录未来。"**
>
> **"Tracking open source, recording the future."**
