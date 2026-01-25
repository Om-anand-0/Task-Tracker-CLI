# Task Tracker CLI

<p>https://roadmap.sh/projects/task-tracker</p>

A simple command-line task tracker built in Python to manage tasks with persistent storage and clear state transitions.

This project was built incrementally to understand how real-world CLI tools evolve — focusing on correctness, clarity, and maintainability rather than shortcuts.

---

## Features

- ✅ Add tasks with automatic ID assignment
- ✅ Persistent storage using JSON with custom file support
- ✅ Task states: `todo`, `inprogress`, `done`
- ✅ Cycle task status (`todo → inprogress → done → todo`)
- ✅ Filter tasks by status (done, undone, in-progress)
- ✅ Delete individual or all tasks
- ✅ Defensive handling of empty or corrupted JSON files
- ✅ Clean terminal output with status icons (✅ ⏳ ❌)

---

## Usage

### Basic Commands

```bash
# Add a new task
python main.py add "Your task description"

# List all tasks
python main.py list

# Mark task status (cycles: todo → inprogress → done → todo)
python main.py mark <task_id>

# Delete a task
python main.py delete <task_id>

# Clear all tasks
python main.py clear
```

### Filter Tasks by Status

```bash
# Show only completed tasks
python main.py done

# Show only todo tasks
python main.py undone

# Show only in-progress tasks
python main.py inprogress
```

### Custom File Storage

```bash
# Use a custom file (default: tasks.json)
python main.py add "Task" --file myproject
python main.py list --file myproject
```

---

## Task Model

Each task is stored with a **stable ID** and a status field.

Example structure (`tasks.json`):

```json
{
  "1": {
    "task": "Learn DevOps",
    "status": "todo"
  },
  "2": {
    "task": "Solve CF problems",
    "status": "inprogress"
  },
  "3": {
    "task": "Build CLI tools",
    "status": "done"
  }
}
```

---

## Project Structure

```
.
├── main.py       # Entry point and CLI argument handling
├── args.py       # Argument parser configuration
├── core.py       # Core task operations (display, mark, delete)
├── storage.py    # JSON file I/O operations
└── tasks.json    # Default task storage file
```

---

## Available Actions

| Action | Description | Requires Value |
|--------|-------------|----------------|
| `add` | Add a new task | ✅ Task text |
| `list` | Show all tasks | ❌ |
| `mark` | Toggle task status | ✅ Task ID |
| `delete` | Delete a task | ✅ Task ID |
| `done` | Show completed tasks | ❌ |
| `undone` | Show todo tasks | ❌ |
| `inprogress` | Show in-progress tasks | ❌ |
| `clear` | Delete all tasks | ❌ |
| `exit` | Exit the CLI | ❌ |
