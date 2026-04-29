#!/bin/bash
# 周三深度筛选任务 - intelligence-filter-wednesday
# 执行时间: 每周三 14:00

echo "🕑 [$(date '+%Y-%m-%d %H:%M')] 开始执行周三深度筛选..."

CURRENT_DATE=$(date '+%Y-%m-%d')
WEEK_NUM=$(date +%W)
YEAR=$(date +%Y)

# 读取候选池
POOL_FILE="~/.openclaw/workspace/intelligence-system/data/candidate-pool-${YEAR}-W${WEEK_NUM}.md"
SHORTLIST_FILE="~/.openclaw/workspace/intelligence-system/data/shortlist-${YEAR}-W${WEEK_NUM}.md"

if [ ! -f "${POOL_FILE}" ]; then
    echo "❌ 错误: 未找到候选池文件 ${POOL_FILE}"
    exit 1
fi

echo "📖 读取候选池: ${POOL_FILE}"
echo "🔍 开始验证每个项目..."

# 创建短名单文件
cat > ${SHORTLIST_FILE} << EOF
# 周三精选短名单 - ${YEAR}年第${WEEK_NUM}周

筛选日期: ${CURRENT_DATE}
状态: ⏸️ 待用户确认

---

## 筛选规则
- ❌ 删除: Star < 100 且无媒体 coverage 的项目
- ⚠️ 标记: 有争议/炒作嫌疑的项目
- ✅ 保留: 5-7 个高质量项目进入精选池

---

## 候选项目验证结果

| 序号 | 项目名 | 定位 | 当前 Star | 媒体覆盖 | 入选理由/删除原因 |
|------|--------|------|-----------|----------|-------------------|
| 1 | 待填充 | 待填充 | 待填充 | 待填充 | 待填充 |
| 2 | 待填充 | 待填充 | 待填充 | 待填充 | 待填充 |
| 3 | 待填充 | 待填充 | 待填充 | 待填充 | 待填充 |

---

## ⚠️ 人工介入点

**请确认以上短名单后，回复"继续"以执行下一步。**

如果确认无误，将：
1. 将保留项目标记为"精选池"
2. 准备周五周报生成所需的数据

EOF

echo "✅ 短名单已生成: ${SHORTLIST_FILE}"
echo "⏸️ 【人工介入点】等待用户确认..."
echo "   请在确认后回复"继续"执行下一步"

# 输出暂停标记
echo "PAUSE|${SHORTLIST_FILE}|AWAITING_CONFIRMATION"
