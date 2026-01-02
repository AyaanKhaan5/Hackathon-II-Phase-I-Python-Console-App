# The Evolution of Todo - Phase I

A simple in-memory command-line Todo application in Python with both **core and advanced task management features**.

## Features

This application supports the core and advanced features:

### Core Features:
1. Add a new task with a title and description
2. Delete a task by its ID (with confirmation)
3. Update an existing task's title or description by ID
4. View/list all tasks with ID, title, description, and completion status
5. Mark a task as complete or incomplete (toggle) by ID

### Advanced / Planned Features:
6. Search & filter tasks by keyword, status, priority, or date
7. Assign priorities and categories (e.g., high/medium/low or work/home)
8. Sort tasks by due date, priority, or alphabetically
9. Add recurring tasks (e.g., weekly meetings)
10. Manage task recurrence and due dates with optional reminders

## Youtube Video 
```bash
# https://www.youtube.com/watch?v=coi-1NX0X3A
```


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
uv run python -m todo.main
```

## Usage

The application runs in a **continuous command-loop** with a clear numbered text menu:

- 1: Add Task
- 2: List Tasks
- 3: Update Task
- 4: Toggle Task Completion
- 5: Delete Task (with confirmation)
- 6: Search & Filter Tasks
- 7: Add Recurring Task
- 8: Manage Recurrence
- 9: Exit

**Notes:**
- Tasks are stored **in-memory** only and will be lost upon exit (Phase I limitation).  
- Advanced features like recurring tasks, priorities, and search/filter are included in the menu for progression.
