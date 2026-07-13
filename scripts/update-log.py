#!/usr/bin/env python3
"""Update execution log for intelligence system tasks.

Supports both JSON (execution-log.json) and Markdown (logs/execution-log-YYYY.md) formats.
Also updates the in-memory Markdown table if the date row already exists.
"""
import argparse
import json
import os
import re
from datetime import datetime

BASE_DIR = os.path.expanduser("~/.openclaw/workspace/intelligence-system")
JSON_LOG = os.path.join(BASE_DIR, "execution-log.json")


def iso_week(dt: datetime) -> int:
    return dt.isocalendar()[1]


def get_markdown_log_path(year: int) -> str:
    return os.path.join(BASE_DIR, f"logs/execution-log-{year}.md")


def ensure_markdown_log(year: int) -> str:
    """Return the Markdown log path, creating the file with header if absent."""
    path = get_markdown_log_path(year)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        header = f"""# {year}年执行日志

> 由 cron 任务自动更新。每天任务完成后追加/修改对应行。\n> 复核时请查看此表格，而非扫描文件名。\n\n## 执行概览\n\n| 日期 | 星期 | 周次 | 任务ID | 任务名称 | 计划 | 实际 | 产出文件 | 完成时间 | 备注 |\n|------|------|------|--------|----------|------|------|----------|----------|------|\n"""
        with open(path, "w") as f:
            f.write(header)
    return path


def weekday_cn(dt: datetime) -> str:
    mapping = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    return mapping[dt.weekday()]


def update_json_log(date: str, task_id: str, status: str, output_file: str, year: str, note: str = ""):
    log_entry = {
        "date": date,
        "task_id": task_id,
        "status": status,
        "output_file": output_file,
        "year": year,
        "note": note,
        "timestamp": datetime.now().isoformat(),
    }
    logs = []
    if os.path.exists(JSON_LOG):
        try:
            with open(JSON_LOG, "r") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []
    logs.append(log_entry)
    os.makedirs(os.path.dirname(JSON_LOG), exist_ok=True)
    with open(JSON_LOG, "w") as f:
        json.dump(logs, f, indent=2)


def update_markdown_log(
    date: str,
    task_id: str,
    task_name: str,
    status: str,
    output_file: str,
    year: str,
    note: str = "",
):
    """Insert or update a row in the Markdown table log."""
    path = ensure_markdown_log(int(year))
    with open(path, "r") as f:
        content = f.read()

    dt = datetime.strptime(date, "%Y-%m-%d")
    week = f"W{iso_week(dt):02d}"
    weekday = weekday_cn(dt)
    time_str = datetime.now().strftime("%H:%M")

    # Determine status symbol
    status_symbol = {
        "completed": "✅ completed",
        "error": "❌ error",
        "pending": "⏳ pending",
        "running": "🔄 running",
    }.get(status, status)

    # Build the new row
    new_row = f"| {date} | {weekday} | {week} | {task_id} | {task_name} | scheduled | {status_symbol} | {output_file} | {time_str} | {note} |"

    # Try to find and replace an existing row for the same date + task_id
    lines = content.split("\n")
    pattern = re.compile(
        rf"^\| {re.escape(date)} \| .*? \| .*? \| {re.escape(task_id)} \| .*? \| .*? \| .*? \| .*? \| .*? \| .*? \|$"
    )

    replaced = False
    for i, line in enumerate(lines):
        if pattern.match(line):
            lines[i] = new_row
            replaced = True
            break

    if not replaced:
        # Append after the header separator line (the line with all dashes)
        # Find the last header separator and insert after it
        insert_idx = None
        for i in range(len(lines) - 1, -1, -1):
            if re.match(r"^\|[-:\s|]+\|$", lines[i]):
                insert_idx = i + 1
                break
        if insert_idx is None:
            insert_idx = len(lines)
        lines.insert(insert_idx, new_row)

    with open(path, "w") as f:
        f.write("\n".join(lines))
        if not content.endswith("\n"):
            f.write("\n")

    print(f"Log updated: {date} {task_id} -> {status}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True)
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--task-name", required=True)
    parser.add_argument("--status", required=True, choices=["completed", "error", "pending", "running"])
    parser.add_argument("--output-file", required=True)
    parser.add_argument("--year", required=True)
    parser.add_argument("--note", default="", help="Optional note (e.g. error reason)")
    args = parser.parse_args()

    update_json_log(args.date, args.task_id, args.status, args.output_file, args.year, args.note)
    update_markdown_log(
        args.date,
        args.task_id,
        args.task_name,
        args.status,
        args.output_file,
        args.year,
        args.note,
    )


if __name__ == "__main__":
    main()
