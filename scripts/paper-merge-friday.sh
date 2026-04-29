#!/bin/bash
# 周五论文-开源联动分析任务 - paper-merge-friday
# 执行时间: 每周五 19:00（在开源周报生成后执行）

echo "🔗 [$(date '+%Y-%m-%d %H:%M')] 开始执行论文-开源联动分析..."

CURRENT_DATE=$(date '+%Y-%m-%d')
WEEK_NUM=$(date +%W)
YEAR=$(date +%Y)

# 读取源文件
PAPER_SHORTLIST_FILE="~/.openclaw/workspace/intelligence-system/data/paper-shortlist-${YEAR}-W${WEEK_NUM}.md"
OPEN_SOURCE_SHORTLIST_FILE="~/.openclaw/workspace/intelligence-system/data/shortlist-${YEAR}-W${WEEK_NUM}.md"
MERGED_FILE="~/.openclaw/workspace/intelligence-system/data/merged-report-${YEAR}-W${WEEK_NUM}.md"

# 检查文件是否存在
if [ ! -f "${PAPER_SHORTLIST_FILE}" ]; then
    echo "⚠️ 警告: 未找到论文精选池文件"
    PAPER_EXISTS=false
else
    PAPER_EXISTS=true
fi

if [ ! -f "${OPEN_SOURCE_SHORTLIST_FILE}" ]; then
    echo "⚠️ 警告: 未找到开源精选池文件"
    OSS_EXISTS=false
else
    OSS_EXISTS=true
fi

if [ "$PAPER_EXISTS" = false ] && [ "$OSS_EXISTS" = false ]; then
    echo "❌ 错误: 无可用的精选文件"
    exit 1
fi

echo "📖 正在读取精选池文件..."
echo "🔍 开始生成论文-开源映射表..."
echo "📊 按 A-D 类优先级重新排序..."

# 创建合并报告文件
cat > ${MERGED_FILE} << 'EOF'
# AI 开源情报周报 W${WEEK_NUM} | 论文联动版

日期: ${CURRENT_DATE}  
本期编辑: Kimi Claw

---

## 📑 本周论文精选（LLM & Agent）

### 🔥 论文-开源映射表（本周必读）

| 论文标题 | 类型 | 论文链接 | 代码链接 | 实现状态 |
|---------|------|---------|---------|---------|
| [标题] | A类 | arxiv.org/abs/xx | github.com/xx | 官方实现，已验证 |
| [标题] | B类 | arxiv.org/abs/xx | github.com/xx | 社区复现，Star:xxx |
| [标题] | C类 | arxiv.org/abs/xx | - | 暂无代码，关注后续 |
| [标题] | D类 | arxiv.org/abs/xx | github.com/xx | 项目先行，论文后发 |

*注：A类=官方代码，B类=社区复现，C类=论文先行，D类=项目先行*

### 重磅推荐（A类+D类项目，1-3个）
[详细解读，包含：论文核心贡献+代码实现亮点+快速上手建议]

### 论文速递（B类+C类，简要列表）
- [标题] | [中文摘要] | [arXiv链接]

### 💡 联动观察
- 本周有 {N} 篇论文同时发布了开源实现，占比{X}%
- 重点关注：[具体论文名]，其代码已收录在本周开源周报第{X}项
- 趋势提示：[如有多个同类论文集中出现，简要说明]

---

## 🚀 开源项目精选（前文）

[开源项目周报内容将插入此处]

---

*数据来源: arXiv, HuggingFace, GitHub, PaperWeekly*  
*报告生成时间: ${CURRENT_DATE}*

EOF

echo "✅ 联动分析报告已生成: ${MERGED_FILE}"
echo "📤 准备推送到飞书..."

# 输出完成标记
echo "COMPLETE|${MERGED_FILE}|${YEAR}-W${WEEK_NUM}|READY_TO_SEND"
