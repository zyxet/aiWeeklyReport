# 论文-开源联动周报 — 2026-W28

> 生成时间: 2026-07-10 19:00 CST
> 来源: os-shortlist-2026-W28.md × paper-shortlist-2026-W28.md

---

## 联动主题分类

### 主题一：Agent 安全分层体系
- **开源**: SkillSpector (NVIDIA, 68种攻击模式)
- **论文**: HaloGuard 1.0 (输入过滤), Steerability (编码约束), LACUNA (遗忘验证)
- **洞察**: 四层覆盖（输入→技能→编码→遗忘），安全是数据工程而非参数量问题

### 主题二：Agent 效率"不修改权重"时代
- **开源**: headroom (60-95%压缩), SkillOpt (52/52全胜)
- **论文**: PAW (4B→0.6B, 内存1/50), CheckRLM (推理链校验)
- **洞察**: 压缩→优化→校验完整链路，企业无需重新训练即可获得提升

### 主题三：代码推理与终端 Agent
- **开源**: oh-my-pi (终端原生AI编码)
- **论文**: DecompRL (50倍成本降低), Steerability (编码约束监督)
- **洞察**: 效率+安全覆盖编码Agent全链路

### 主题四：长上下文架构与开源模型
- **开源**: GLM-5.2 (753B MoE, 1M上下文, MIT)
- **论文**: HOLA (340M参数长上下文突破)
- **洞察**: 架构创新与大规模实践互相验证

### 主题五：自主科研 Agent 与视频 Agent
- **开源**: OpenMontage (端到端视频Agent)
- **论文**: Autonomous Research Agents (47次会话完成全流程)
- **洞察**: 端到端自主范式在科研和视频两个领域同步验证

### 主题六：Agent 联网能力与工具调用
- **开源**: Agent-Reach (13+平台零API费)
- **论文**: PAW (Program-as-Weights工具编译)
- **洞察**: 工具发现→编译→执行的完整链路

---

## 联动矩阵

| 项目 \ 论文 | HOLA | DecompRL | PAW | Auto Research | LACUNA | CheckRLM | HaloGuard | Steerability |
|------------|------|----------|-----|---------------|--------|----------|-----------|--------------|
| SkillSpector | — | — | — | — | 🔗 | — | 🔗 | 🔗 |
| headroom | — | — | 🔗 | — | — | 🔗 | — | — |
| SkillOpt | — | — | 🔗 | — | — | — | — | — |
| OpenMontage | — | — | — | 🔗 | — | — | — | — |
| Agent-Reach | — | — | 🔗 | — | — | — | — | — |
| oh-my-pi | — | 🔗 | — | — | — | — | — | 🔗 |
| GLM-5.2 | 🔗 | — | — | — | — | — | — | — |

🔗 强关联 | ⭐ 间接关联 | — 弱关联

---

*本报告由 AI Agent 自动生成*
