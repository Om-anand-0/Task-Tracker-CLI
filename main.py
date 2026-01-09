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
    with open(file_Name, "r") as f:
        return json.load(f)


def add_task(task_text: str):
    try:
        tasks = load_tasks()

        if tasks:
            next_id = str(max(map(int, tasks.keys())) + 1)
        else:
            next_id = "1"

        tasks[next_id] = {"task": task_text, "done": False}

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
            is_done = inner_dict["done"]
            status = "✅" if is_done else "❌"
            print(f" ID: {task_id}: {task_name} | Status: {status}")
    except Exception as e:
        print(f"ERROR: {e} has occured !")


def show_task(file_Name):
    file_path = file_Name
    try:
        with open(file_path, "r") as file:
            tasks = file.readlines()
            print(tasks)
    except FileNotFoundError as e:
        print(f"Error {e} has occured")
    except Exception as e:
        print(f"{e} has occured")


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
            tasks[task_id]["done"] = not tasks[task_id]["done"]
        # saving file
        with open(file_Name, "w") as f:
            json.dump(tasks, f, indent=2)
            clearscr()
        print(f"Task {task_id} updated succefully")

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
    print("3. Mark Task")
    print("4. Delete Task")
    print("5. Delete All Task")
    print("6. Exit")
    choice = input("Choose Your choice: ")

    if choice == "1":
        task = input("Enter Your Task -> ")
        add_task(task)
    elif choice == "2":
        # show_task(file_Name)
        show_allTask()
    elif choice == "3":
        show_allTask()
        id = input("Enter ID: ")
        mark_task(id)
        # show_allTask()
    elif choice == "4":
        show_allTask()
        id = input("Enter ID: ")
        delete_task(id)
        # show_allTask()
    elif choice == "5":
        delete_AllTasks(file_Name)

    elif choice == "6":
        break

    else:
        print("Input Error Exiting")
        break
