# The Evolution of Todo - Phase I

A simple in-memory command-line Todo application in Python.

## Features

This application supports the 5 core features:
1. Add a new task with a title and description
2. Delete a task by its ID (with confirmation)
3. Update an existing task's title or description by ID
4. View/list all tasks with ID, title, description, and completion status
5. Mark a task as complete or incomplete (toggle) by ID

## Project Setup with UV

This project uses UV for Python package management. UV is a fast Python package installer and resolver.

### Installation

To install UV, run:

```bash
# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Project Setup

1. Clone the repository
2. Navigate to the project directory
3. Install dependencies (though this project uses only Python standard library):

```bash
uv sync
```

### Running the Application

```bash
uv run python src/todo/main.py
```

## Usage

The application runs in a continuous command-loop with a clear numbered text menu:
- 1: Add Task
- 2: List Tasks
- 3: Update Task
- 4: Mark Complete/Incomplete
- 5: Delete Task (with confirmation)
- 6: Exit

Tasks are stored in-memory only and will be lost upon exit (Phase I constraint).