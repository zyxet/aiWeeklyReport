#!/usr/bin/env python3
"""
更新执行日志
由 cron 任务完成后调用，标记任务状态。

用法:
    python3 scripts/update-log.py --date 2026-05-15 --task-id friday-report --status completed --output-file data/weekly-report-2026-W20.md [--notes "xxx"]

状态值:
    completed | failed | pending | skipped
"""

import argparse
import os
import datetime
import re
import sys

def update_log(year, date_str, task_id, status, output_file=None, notes=None, completed_at=None):
    log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                            f"logs/execution-log-{year}.md")
    
    if not os.path.exists(log_path):
        print(f"❌ 日志文件不存在: {log_path}")
        sys.exit(1)
    
    with open(log_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 状态图标映射
    status_icon = {
        'completed': '✅ completed',
        'failed': '❌ failed',
        'pending': '⏳ pending',
        'skipped': '⏭ skipped',
        'error': '❌ error'
    }.get(status, status)
    
    if not completed_at:
        completed_at = datetime.datetime.now().strftime('%H:%M')
    
    if not output_file:
        output_file = '-'
    
    if not notes:
        notes = '-'
    
    # 找到匹配的行并替换
    found = False
    new_lines = []
    
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith('|') or '日期' in stripped or '---' in stripped:
            new_lines.append(line)
            continue
        
        parts = [p.strip() for p in stripped.split('|')]
        if len(parts) >= 10:
            line_date = parts[1]
            line_task = parts[4] if parts[4] != '-' else None
            
            if line_date == date_str and line_task == task_id:
                # 重建这一行
                # parts: ['', date, weekday, week, task_id, task_name, planned, actual, output_file, completed_at, notes, '']
                new_line = f"| {parts[1]} | {parts[2]} | {parts[3]} | {parts[4]} | {parts[5]} | {parts[6]} | {status_icon} | {output_file} | {completed_at} | {notes} |\n"
                new_lines.append(new_line)
                found = True
                continue
        
        new_lines.append(line)
    
    if not found:
        print(f"⚠️  未找到匹配行: date={date_str}, task_id={task_id}")
        print(f"   日志中可能还没有这一天的记录，或者 task_id 不匹配")
        sys.exit(1)
    
    with open(log_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"✅ 已更新日志: {date_str} {task_id} → {status_icon}")
    print(f"   产出: {output_file}")
    print(f"   时间: {completed_at}")

def main():
    parser = argparse.ArgumentParser(description='更新周报系统执行日志')
    parser.add_argument('--date', required=True, help='日期，格式 YYYY-MM-DD')
    parser.add_argument('--task-id', required=True, help='任务ID，如 monday-collect')
    parser.add_argument('--status', required=True, choices=['completed', 'failed', 'pending', 'skipped', 'error'], 
                        help='执行状态')
    parser.add_argument('--output-file', help='产出文件路径（相对项目根目录）')
    parser.add_argument('--notes', help='备注')
    parser.add_argument('--completed-at', help='完成时间，格式 HH:MM（默认当前时间）')
    parser.add_argument('--year', type=int, default=datetime.date.today().year, help='年份')
    
    args = parser.parse_args()
    
    update_log(
        year=args.year,
        date_str=args.date,
        task_id=args.task_id,
        status=args.status,
        output_file=args.output_file,
        notes=args.notes,
        completed_at=args.completed_at
    )

if __name__ == '__main__':
    main()
