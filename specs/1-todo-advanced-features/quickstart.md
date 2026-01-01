# Quickstart: Advanced Todo Features

## Setting up Recurring Tasks

### Creating a Recurring Task
1. Launch the todo application
2. Select "Create Recurring Task" from the main menu
3. Enter task description
4. Choose recurrence interval (daily/weekly/monthly/yearly)
5. Optionally set due date and time in YYYY-MM-DD HH:MM format
6. The task is saved as a template and the first instance is generated

### Managing Recurring Tasks
1. View recurring tasks in the task list (marked with 🔁 indicator)
2. Complete recurring task instances to automatically generate the next occurrence
3. Edit recurrence rules through "Manage Recurrence" menu option
4. Disable recurrence by removing the recurrence interval

## Using DateTime Due Dates

### Setting Due Dates with Time
1. When creating or editing a task, enter due date in format: YYYY-MM-DD HH:MM
2. Example: "2025-12-31 14:30" for December 31, 2025 at 2:30 PM
3. Due dates remain optional - leave blank for no due date

### Viewing Reminders
1. On application startup, overdue tasks are prominently displayed
2. Tasks due within the next hour show "DUE SOON" indicator
3. Summary banner shows count of overdue and due-today tasks

## Menu Navigation Changes

### New Menu Options
- "Create Recurring Task" - Create tasks with recurrence rules
- "Manage Recurrence" - Edit or disable recurrence for existing tasks
- Enhanced task list with time and recurrence indicators

### Backward Compatibility
- All existing menu options continue to work identically
- Existing tasks without datetime or recurrence display unchanged
- No disruption to existing task workflows

## Development Setup

### Required Dependencies
- Python 3.11+
- Standard library only (no external packages required)

### Testing New Features
1. Create recurring task → complete → verify new instance appears with correct next date
2. Set task due yesterday → start app → see overdue banner and highlight
3. Set task due today in 30 mins → start app → see "DUE SOON"
4. Verify existing non-recurring tasks behave normally
5. Test edge cases: monthly recurrence across year boundary