import json
from pathlib import Path
import os
import sys
# currenDir = os.getcwd()


def clearscr():
    if sys.platform.startswith("linux"):
        os.system("clear")
    elif sys.platform == "win32":
        os.system("cls")


def load_tasks():
    try:
        with open(file_Name, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


def add_task(task_text: str):
    try:
        tasks = load_tasks()

        if tasks:
            next_id = str(max(map(int, tasks.keys())) + 1)
        else:
            next_id = "1"

        tasks[next_id] = {"task": task_text, "status": "todo"}

        with open(file_Name, "w") as f:
            json.dump(tasks, f, indent=2)
        clearscr()
        print(f"task added with id {next_id}")
    except Exception as e:
        print(f"Error has occured {e}")


def show_allTask():
    try:
        clearscr()
        tasks = load_tasks()
        for task_id, inner_dict in tasks.items():
            task_name = inner_dict["task"]
            current_status = inner_dict.get("status", "todo")
            if current_status == "done":
                status_icon = "✅"
            elif current_status == "inprogress":
                status_icon = "⏳"
            else:
                # This covers "todo" and any unexpected values
                status_icon = "❌"

            print(f" ID: {task_id}: {task_name} | Status: {status_icon}")
    except Exception as e:
        print(f"ERROR: {e} has occured !")


def showDoneTask():
    try:
        clearscr()
        tasks = load_tasks()
        for task_id, inner_dict in tasks.items():
            task_name = inner_dict["task"]
            if inner_dict.get("status") == "done":
                print(f"ID {task_id}: {task_name} | Status : ✅")

    except Exception as e:
        print(f"ERROR: {e} has occured")


def showUndoneTask():
    try:
        clearscr()
        tasks = load_tasks()
        for task_id, inner_dict in tasks.items():
            task_name = inner_dict["task"]
            if inner_dict.get("status") == "todo":
                print(f"ID {task_id}: {task_name} | Status : ❌")

    except Exception as e:
        print(f"ERROR: {e} has occured")


def showInprogressTask():
    try:
        clearscr()
        tasks = load_tasks()
        found = False
        for task_id, inner_dict in tasks.items():
            if inner_dict.get("status") == "inprogress":
                print(f"ID {task_id}: {inner_dict['task']} | Status : ⏳")
                found = True
        if not found:
            print("No tasks are currently in progress.")
    except Exception as e:
        print(f"ERROR: {e} has occured")


def delete_task(id: str):
    try:
        tasks = load_tasks()
        # show_allTask()
        removed_task = tasks.pop(id, None)
        if removed_task:
            clearscr()
            print(f"Deleted Task: {removed_task['task']}")
        with open(file_Name, "w") as f:
            json.dump(tasks, f, indent=2)
        # clearscr()

    except Exception as e:
        print(f"ERROR: {e} has occured !")


def mark_task(task_id: str):
    try:
        # 1 load task
        # 2 update task
        # 3 save task
        # here i am loading task then doing idk what but we can use not operator like a toggle to invert it
        # then save

        tasks = load_tasks()
        if task_id in tasks:
            current_status = tasks[task_id].get("status", "todo")
            if current_status == "todo":
                tasks[task_id]["status"] = "inprogress"
            elif current_status == "inprogress":
                tasks[task_id]["status"] = "done"
            else:
                tasks[task_id]["status"] = "todo"
            # saving file
            with open(file_Name, "w") as f:
                json.dump(tasks, f, indent=2)
                clearscr()
            print(f"Task {task_id} is now: {tasks[task_id]['status']}")

        else:
            print(f"ID {task_id} not found.")

    except Exception as e:
        print(f"ERROR: {e} has occured !")


def delete_AllTasks(file_Name):
    file_path = file_Name
    try:
        with open(file_path, "w") as f:
            json.dump({}, f)
            clearscr()
        print(f"Deleted All task from {file_path}")
    except Exception as e:
        print(f"Error has occured {e}")


print("Enter File Name: ")
file_Name = Path(input() + ".json")
# file_Name+="json"

if not file_Name.exists() or file_Name.stat().st_size == 0:
    file_Name.touch()
    with open(file_Name, "w") as f:
        json.dump({}, f)

    print(f"File {file_Name} created succefully  ")
else:
    print(f" {file_Name} exists already so using {file_Name} ")
    # print(f" Using {file_Name}")
clearscr()
while True:
    print("Welcome to Task Tracker CLI")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Show Done Tasks")
    print("4. Show Undone Tasks")
    print("5. Show Inprogres Tasks")
    print("6. Mark Task")
    print("7. Delete Task")
    print("8. Delete All Task")
    print("9. Exit")
    choice = input("Choose Your choice: ")

    if choice == "1":
        task = input("Enter Your Task -> ")
        add_task(task)
    elif choice == "2":
        # show_task(file_Name)
        show_allTask()
    elif choice == "3":
        showDoneTask()
    elif choice == "4":
        showUndoneTask()
    elif choice == "5":
        showInprogressTask()
    elif choice == "6":
        show_allTask()
        id = input("Enter ID: ")
        mark_task(id)
        # show_allTask()
    elif choice == "7":
        show_allTask()
        id = input("Enter ID: ")
        delete_task(id)
        # show_allTask()
    elif choice == "8":
        delete_AllTasks(file_Name)

    elif choice == "9":
        break

    else:
        print("Input Error Exiting")
        break
