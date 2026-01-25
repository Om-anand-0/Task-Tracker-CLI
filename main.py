import json
from pathlib import Path
from storage import add_task
from core import (
    clear_screen,
    show_all_tasks,
    show_done_tasks,
    show_undone_tasks,
    show_inprogress_tasks,
    delete_task,
    mark_task,
    delete_all_tasks,
)
from args import args
import sys

# Handle file path - check if .json extension already exists
file_path = Path(args.file if args.file.endswith(".json") else args.file + ".json")

if not file_path.exists() or file_path.stat().st_size == 0:
    file_path.touch()
    with open(file_path, "w") as f:
        json.dump({}, f)
        print(f"File {file_path} created successfully")
else:
    print(f"{file_path} exists already, using {file_path}")

# Validate that actions requiring a value have one
if args.action in ["add", "delete", "mark"] and not args.value:
    print(f"{args.action} requires a value")
    sys.exit(1)

# Handle actions
if args.action == "add":
    task_id = add_task(file_path, args.value)
    if task_id:
        print(f"Task added with ID {task_id}")
elif args.action == "list":
    show_all_tasks(file_path)
elif args.action == "delete":
    delete_task(file_path, args.value)
elif args.action == "mark":
    mark_task(file_path, args.value)
elif args.action == "done":
    show_done_tasks(file_path)
elif args.action == "undone":
    show_undone_tasks(file_path)
elif args.action == "inprogress":
    show_inprogress_tasks(file_path)
elif args.action == "clear":
    delete_all_tasks(file_path)
