<h1>Task Tracker CLI</h1>

<p>https://roadmap.sh/projects/task-tracker</p>

# Task Tracker CLI (v1)

A simple command-line task tracker built in Python to manage tasks with persistent storage and clear state transitions.

This project was built incrementally to understand how real-world CLI tools evolve — focusing on correctness, clarity, and maintainability rather than shortcuts.

---

## Features

- Add tasks with automatic ID assignment
- Persistent storage using JSON
- Task states:
  - `todo`
  - `inprogress`
  - `done`
- Cycle task status (`todo → inprogress → done → todo`)
- View:
  - all tasks
  - done tasks
  - undone (todo) tasks
  - in-progress tasks
- Delete individual tasks
- Delete all tasks
- Defensive handling of empty or corrupted JSON files
- Clear terminal output for better UX

---

## Task Model

Each task is stored with a **stable ID** and a status field.

Example structure:

```json
{
  "1": {
    "task": "Learn DevOps",
    "status": "todo"
  },
  "2": {
    "task": "Solve CF problems",
    "status": "inprogress"
  }
}

