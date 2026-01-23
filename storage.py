import json

def load_tasks(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def add_task(file_path, task_text: str):
    try:
        tasks = load_tasks(file_path)

        if tasks:
            next_id = str(max(map(int, tasks.keys())) + 1)
        else:
            next_id = "1"

        tasks[next_id] = {"task": task_text, "status": "todo"}

        with open(file_path, "w") as f:
            json.dump(tasks, f, indent=2)
        return next_id
    except Exception as e:
        print(f"Error has occured {e}")
        return None