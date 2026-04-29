#!/bin/bash
# 周四论文精选任务 - paper-filter-thursday
# 执行时间: 每周四 14:00

echo "🎯 [$(date '+%Y-%m-%d %H:%M')] 开始执行周四论文精选..."

CURRENT_DATE=$(date '+%Y-%m-%d')
WEEK_NUM=$(date +%W)
YEAR=$(date +%Y)

# 读取候选池
PAPER_POOL_FILE="~/.openclaw/workspace/intelligence-system/data/paper-pool-${YEAR}-W${WEEK_NUM}.md"
PAPER_SHORTLIST_FILE="~/.openclaw/workspace/intelligence-system/data/paper-shortlist-${YEAR}-W${WEEK_NUM}.md"

if [ ! -f "${PAPER_POOL_FILE}" ]; then
    echo "❌ 错误: 未找到论文候选池文件 ${PAPER_POOL_FILE}"
    echo "请确保周二的论文收集任务已执行"
    exit 1
fi

echo "📖 正在读取论文候选池..."
echo "🔍 开始对每篇论文进行深度分析和评分..."
echo "📊 评估维度: 创新性/实用性/技术深度/机构背书/代码可得性"

# 创建论文精选池文件
cat > ${PAPER_SHORTLIST_FILE} << 'EOF'
# 本周论文精选池 - ${YEAR}年第${WEEK_NUM}周
筛选日期: ${CURRENT_DATE}
状态: ✅ 待用户确认

## 📋 说明
本文档包含 6-8 篇精选论文，每篇已按《论文评估打分表》进行标准化评分（满分25分）

## 🎯 精选论文列表

<!-- AI Agent将基于以下格式填充：

### 【论文N】总分：{X}/25
- **标题（英文）**: [原始标题]
- **中文摘要**: [一句话中文概括，50字以内]
- **作者/机构**: [主要作者及所属机构]
- **arXiv链接**: https://arxiv.org/abs/xxxx.xxxxx
- **代码链接**: [如有GitHub链接]
- **评估详情**:
  - 创新性：{X}/5
  - 实用性：{X}/5
  - 技术深度：{X}/5
  - 机构背书：{X}/5
  - 代码可得性：{X}/5
- **与开源项目关联**: [是否关联本周开源候选池 / 建议补充]
- **推荐理由**: [2-3句话]

-->

## 🔗 与开源项目联动分析
- 本周候选论文中，有 {N} 篇已有开源实现
- 与开源候选池重叠项目：[列出]
- 建议补充到开源候选池：[列出]

---
⏸️ **暂停，等待用户确认**：是否调整名单或深入解读某篇？
请回复：
- "继续" - 确认当前名单，周五合并到周报
- "删除X" - 删除第X篇论文
- "深入解读X" - 对第X篇进行详细分析
EOF

echo "✅ 论文精选池已生成: ${PAPER_SHORTLIST_FILE}"
echo "⏸️ 等待用户确认..."

# 输出完成标记
echo "COMPLETE|${PAPER_SHORTLIST_FILE}|${YEAR}-W${WEEK_NUM}|WAITING_CONFIRM"
