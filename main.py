import json
from pathlib import Path
import os
import sys
from storage import load_tasks, add_task
from core import clear_screen, show_all_tasks, show_done_tasks, show_undone_tasks, show_inprogress_tasks, delete_task, mark_task, delete_all_tasks




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

clear_screen()
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
        new_id = add_task(file_Name, task)
        if new_id:
            clear_screen()
            print(f"task added with id {new_id}")
    elif choice == "2":
        show_all_tasks(file_Name)
    elif choice == "3":
        show_done_tasks(file_Name)
    elif choice == "4":
        show_undone_tasks(file_Name)
    elif choice == "5":
        show_inprogress_tasks(file_Name)
    elif choice == "6":
        show_all_tasks(file_Name)
        task_id = input("Enter ID: ")
        mark_task(file_Name, task_id)
    elif choice == "7":
        show_all_tasks(file_Name)
        task_id = input("Enter ID: ")
        delete_task(file_Name, task_id)
    elif choice == "8":
        delete_all_tasks(file_Name)
    elif choice == "9":
        break

    else:
        print("Input Error Exiting")
        break
