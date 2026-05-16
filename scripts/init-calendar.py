#!/usr/bin/env python3
"""
初始化年度执行日历
生成: config/calendar-YYYY.yaml + logs/execution-log-YYYY.md

用法:
    python3 scripts/init-calendar.py [year]
    
默认生成当前年份的全年计划。
"""

import datetime
import sys
import os

# 任务定义 - 单点配置，改这里就够了
# weekday 用 isoweekday: 1=Monday, 7=Sunday
TASK_DEFINITIONS = {
    "monday-collect": {
        "name": "周一情报收集",
        "weekday": 1,
        "hour": 9,
        "output_template": "data/os-pool-{year}-W{week}.md",
        "description": "搜索 GitHub Trending、HuggingFace Papers、中文技术媒体，收集本周 LLM/AI Agent 开源项目候选池"
    },
    "tuesday-paper-collect": {
        "name": "周二论文雷达",
        "weekday": 2,
        "hour": 9,
        "output_template": "data/paper-pool-{year}-W{week}.md",
        "description": "访问 arXiv cs.CL/cs.LG/cs.AI，搜索 HuggingFace Papers，收集过去7天 LLM 与 Agent 相关论文"
    },
    "wednesday-filter": {
        "name": "周三深度筛选",
        "weekday": 3,
        "hour": 14,
        "output_template": "data/os-shortlist-{year}-W{week}.md",
        "description": "从候选池筛选高质量项目，验证 Star 数、技术测评、媒体 coverage，生成短名单",
        "depends_on": ["monday-collect"]
    },
    "thursday-paper-filter": {
        "name": "周四论文精选",
        "weekday": 4,
        "hour": 14,
        "output_template": "data/paper-shortlist-{year}-W{week}.md",
        "description": "对候选论文评分（创新性/实用性/技术深度/机构背书/代码可得性），保留6-8篇，标记论文+开源关联",
        "depends_on": ["tuesday-paper-collect"]
    },
    "friday-report": {
        "name": "周五周报生成",
        "weekday": 5,
        "hour": 17,
        "output_template": "data/weekly-report-{year}-W{week}.md",
        "description": "深度扫描精选项目，生成结构化《AI开源周报》",
        "depends_on": ["wednesday-filter"]
    },
    "friday-paper-merge": {
        "name": "周五论文-开源联动",
        "weekday": 5,
        "hour": 19,
        "output_template": "data/weekly-report-{year}-W{week}.md",
        "description": "生成论文-开源映射表（A/B/C/D类），合并生成联动版周报",
        "depends_on": ["friday-report", "thursday-paper-filter"]
    }
}


def iso_week(date_obj):
    """返回 ISO 周次字符串，如 W20"""
    _, week, _ = date_obj.isocalendar()
    return f"W{week:02d}"


def generate_calendar(year):
    """生成全年执行计划"""
    schedule = {}
    
    start = datetime.date(year, 1, 1)
    end = datetime.date(year, 12, 31)
    
    current = start
    while current <= end:
        weekday = current.isoweekday()  # 1=Monday, 7=Sunday
        week = iso_week(current)
        date_str = current.strftime("%Y-%m-%d")
        
        # 查找今天所有计划任务（支持同一天多个任务，如周五有两个）
        tasks_today = []
        for tid, tdef in TASK_DEFINITIONS.items():
            if tdef["weekday"] == weekday:
                tasks_today.append({
                    "task_id": tid,
                    "name": tdef["name"],
                    "hour": tdef["hour"],
                    "output_template": tdef["output_template"],
                    "planned_status": "scheduled",
                    "actual_status": "pending",
                    "output_file": None,
                    "completed_at": None,
                    "notes": None
                })
        
        if tasks_today:
            schedule[date_str] = {
                "week": week,
                "tasks": tasks_today
            }
        else:
            schedule[date_str] = {
                "week": week,
                "tasks": []
            }
        
        current += datetime.timedelta(days=1)
    
    return schedule


def write_calendar_yaml(year, schedule, base_dir):
    """写入 calendar YAML"""
    yaml_path = os.path.join(base_dir, f"config/calendar-{year}.yaml")
    os.makedirs(os.path.dirname(yaml_path), exist_ok=True)
    
    lines = [
        f"# AI 开源情报系统 - {year}年执行日历",
        f"# 生成时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"# 修改规则: 只改 task_definitions 里的模板和描述，不要改 schedule 部分",
        f"# 复核脚本读取此文件判断计划 vs 实际",
        f"",
        f"year: {year}",
        f"version: 1",
        f"",
        f"task_definitions:",
    ]
    
    for tid, tdef in TASK_DEFINITIONS.items():
        lines.append(f"  {tid}:")
        lines.append(f"    name: {tdef['name']}")
        lines.append(f"    weekday: {tdef['weekday']}")
        lines.append(f"    hour: {tdef['hour']}")
        lines.append(f"    output_template: \"{tdef['output_template']}\"")
        lines.append(f"    description: \"{tdef['description']}\"")
        if "depends_on" in tdef:
            deps = ", ".join([f'\"{d}\"' for d in tdef["depends_on"]])
            lines.append(f"    depends_on: [{deps}]")
    
    lines.extend([
        "",
        "schedule:",
    ])
    
    for date_str in sorted(schedule.keys()):
        day = schedule[date_str]
        lines.append(f"  \"{date_str}\":")
        lines.append(f"    week: \"{day['week']}\"")
        lines.append(f"    tasks:")
        if day["tasks"]:
            for task in day["tasks"]:
                lines.append(f"      - task_id: \"{task['task_id']}\"")
                lines.append(f"        planned_status: \"{task['planned_status']}\"")
                lines.append(f"        actual_status: \"{task['actual_status']}\"")
                lines.append(f"        output_file: null")
                lines.append(f"        completed_at: null")
                lines.append(f"        notes: null")
        else:
            lines.append(f"      []  # rest day")
    
    with open(yaml_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines) + "\n")
    
    print(f"✅ Calendar YAML 已生成: {yaml_path}")
    return yaml_path


def write_execution_log(year, schedule, base_dir):
    """写入执行日志 Markdown（每天一行，同一天多任务则多行）"""
    log_path = os.path.join(base_dir, f"logs/execution-log-{year}.md")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    lines = [
        f"# {year}年执行日志",
        f"",
        f"> 由 cron 任务自动更新。每天任务完成后追加/修改对应行。",
        f"> 复核时请查看此表格，而非扫描文件名。",
        f"",
        f"## 执行概览",
        f"",
        f"| 日期 | 星期 | 周次 | 任务ID | 任务名称 | 计划 | 实际 | 产出文件 | 完成时间 | 备注 |",
        f"|------|------|------|--------|----------|------|------|----------|----------|------|",
    ]
    
    weekday_names = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    
    for date_str in sorted(schedule.keys()):
        day = schedule[date_str]
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        wday_name = weekday_names[date_obj.weekday()]
        
        if day["tasks"]:
            for task in day["tasks"]:
                lines.append(
                    f"| {date_str} | {wday_name} | {day['week']} | {task['task_id']} | {task['name']} | scheduled | ⏳ pending | - | - | - |"
                )
        else:
            lines.append(
                f"| {date_str} | {wday_name} | {day['week']} | - | - | rest | ⏸ rest | - | - | - |"
            )
    
    # 统计
    total_tasks = sum(len(d["tasks"]) for d in schedule.values())
    rest_days = sum(1 for d in schedule.values() if not d["tasks"])
    
    lines.extend([
        "",
        "## 统计",
        "",
        f"- 总任务数: {total_tasks}",
        f"- 执行日: {sum(1 for d in schedule.values() if d['tasks'])}",
        f"- 休息日: {rest_days}",
        f"",
        "---",
        f"最后更新: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
    ])
    
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines) + "\n")
    
    print(f"✅ Execution Log Markdown 已生成: {log_path}")
    return log_path


def main():
    year = int(sys.argv[1]) if len(sys.argv) > 1 else datetime.datetime.now().year
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)
    
    print(f"🗓️  正在生成 {year} 年执行日历...")
    print(f"📁 项目目录: {base_dir}")
    
    schedule = generate_calendar(year)
    
    yaml_path = write_calendar_yaml(year, schedule, base_dir)
    log_path = write_execution_log(year, schedule, base_dir)
    
    print(f"\n✅ 完成!")
    print(f"   Calendar: {yaml_path}")
    print(f"   Log:      {log_path}")
    print(f"\n下一步:")
    print(f"   1. 检查 task_definitions 里的 output_template 是否符合当前命名规则")
    print(f"   2. 用 scripts/check-status.py 查看执行概览")
    print(f"   3. 更新 cron systemPrompt，让任务从 calendar 读取配置、完成后更新 log")


if __name__ == "__main__":
    main()
