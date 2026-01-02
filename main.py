import json
from pathlib import Path

# currenDir = os.getcwd()


def add_task(task: str):
    try:
        with open(file_Name, "a") as file:
            json.dump(task, file)
        print("task added!")
    except Exception as e:
        print(f"Error has occured {e}")


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


def delete_AllTasks(file_Name):
    file_path = file_Name
    try:
        with open(file_path, "w"):
            pass
        print(f"Deleted All task {file_path}")
    except Exception as e:
        print(f"Error has occured {e}")


print("Enter File Name: ")
file_Name = Path(input())

if not file_Name.exists():
    file_Name.touch()
    print(f"File {file_Name} created succefully  ")
else:
    print(f" file {file_Name} exists already ")

while True:
    print("Welcome to Task Tracker CLI")
    print("1. Add Task")
    print("2. Show tasks")
    print("3. Delete All tasks")
    print("4. Exit")
    choice = input("Choose Your choice: ")

    if choice == "1":
        task = input("Enter Your Task -> ")
        add_task(task)
    elif choice == "2":
        show_task(file_Name)

    elif choice == "3":
        delete_AllTasks(file_Name)

    elif choice == "4":
        break

    else:
        break
