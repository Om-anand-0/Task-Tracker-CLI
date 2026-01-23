import sys
import json
import os
from pathlib import Path
from storage import load_tasks

def clear_screen():
    if sys.platform.startswith("linux"):
        os.system("clear")
    elif sys.platform == "win32":
        os.system("cls")

def show_all_tasks(file_path):
    try:
        clear_screen()
        tasks = load_tasks(file_path)
        if tasks:
            for task_id, inner_dict in tasks.items():
                task_name = inner_dict["task"]
                current_status = inner_dict.get("status", "todo")
                if current_status == "done":
                    status_icon = "✅"
                elif current_status == "inprogress":
                    status_icon = "⏳"
                else:
                    status_icon = "❌"

                print(f" ID: {task_id}: {task_name} | Status: {status_icon}")
        else:
            print("No tasks found.")
    except Exception as e:
        print(f"ERROR: {e} has occured !")


def show_done_tasks(file_path):
    try:
        clear_screen()
        tasks = load_tasks(file_path)
        if tasks:
            found = False
            for task_id, inner_dict in tasks.items():
                task_name = inner_dict["task"]
                if inner_dict.get("status") == "done":
                    print(f"ID {task_id}: {task_name} | Status : ✅")
                    found = True
            if not found:
                print("No done tasks found.")
        else:
            print("No tasks found.")

    except Exception as e:
        print(f"ERROR: {e} has occured")


def show_undone_tasks(file_path):
    try:
        clear_screen()
        tasks = load_tasks(file_path)
        if tasks:
            found = False
            for task_id, inner_dict in tasks.items():
                task_name = inner_dict["task"]
                if inner_dict.get("status") == "todo":
                    print(f"ID {task_id}: {task_name} | Status : ❌")
                    found = True
            if not found:
                print("No undone tasks found.")
        else:
            print("No tasks found.")

    except Exception as e:
        print(f"ERROR: {e} has occured")


def show_inprogress_tasks(file_path):
    try:
        clear_screen()
        tasks = load_tasks(file_path)
        found = False
        for task_id, inner_dict in tasks.items():
            if inner_dict.get("status") == "inprogress":
                print(f"ID {task_id}: {inner_dict['task']} | Status : ⏳")
                found = True
        if not found:
            print("No tasks are currently in progress.")
    except Exception as e:
        print(f"ERROR: {e} has occured")


def delete_task(file_path, task_id):
    try:
        tasks = load_tasks(file_path)
        removed_task = tasks.pop(task_id, None)
        if removed_task:
            clear_screen()
            print(f"Deleted Task: {removed_task['task']}")
            with open(file_path, "w") as f:
                json.dump(tasks, f, indent=2)
        else:
            print(f"ID {task_id} not found.")

    except Exception as e:
        print(f"ERROR: {e} has occured !")


def mark_task(file_path, task_id):
    try:
        tasks = load_tasks(file_path)
        if task_id in tasks:
            current_status = tasks[task_id].get("status", "todo")
            if current_status == "todo":
                tasks[task_id]["status"] = "inprogress"
            elif current_status == "inprogress":
                tasks[task_id]["status"] = "done"
            else:
                tasks[task_id]["status"] = "todo"
            
            with open(file_path, "w") as f:
                json.dump(tasks, f, indent=2)
            clear_screen()
            print(f"Task {task_id} is now: {tasks[task_id]['status']}")

        else:
            print(f"ID {task_id} not found.")

    except Exception as e:
        print(f"ERROR: {e} has occured !")


def delete_all_tasks(file_path):
    try:
        with open(file_path, "w") as f:
            json.dump({}, f)
        clear_screen()
        print(f"Deleted All task from {file_path}")
    except Exception as e:
        print(f"Error has occured {e}")