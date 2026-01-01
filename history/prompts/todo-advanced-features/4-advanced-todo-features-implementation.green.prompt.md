---
id: 4
title: advanced-todo-features-implementation
stage: green
date_iso: 2025-12-30
surface: agent
model: Claude Sonnet 4.5
feature: todo-advanced-features
branch: 1-todo-advanced-features
user: user
command: /sp.implement
labels:
  - implementation
  - todo
  - advanced-features
  - recurring-tasks
  - datetime
  - reminders

links:
  spec: specs/1-todo-advanced-features/spec.md
  plan: specs/1-todo-advanced-features/plan.md
  tasks: specs/1-todo-advanced-features/tasks.md
  ticket: null
  adr: null
  pr: null

files_yaml:
  - src/todo/models.py
  - src/todo/utils.py
  - src/todo/storage.py
  - src/todo/cli.py
  - src/todo/main.py
  - src/todo/services/reminders_service.py
  - src/todo/services/recurrence_service.py
  - src/todo/services/__init__.py
  - src/todo/__init__.py

tests_yaml:
  - Task model extension with new fields
  - DateTime parsing and validation
  - Recurrence service functionality
  - Reminders service functionality
  - Storage layer updates
  - CLI interface updates
  - Main application integration

prompt_text: |
  You are now in the implementation phase (/sp.implement) for the Advanced Level of "The Evolution of Todo".

  IMPORTANT:
  - Basic + Intermediate Levels are already fully working.
  - This is a CONSOLE-ONLY app – no browser, no GUI.
  - DO NOT rewrite the entire project – only extend existing code safely.

  Add ONLY these Advanced features on top of current working app:

  1. Recurring Tasks
     - In Add/Edit Task: ask for recurrence (None/Daily/Weekly/Monthly)
     - When user marks a recurring task complete:
       - Automatically create a new identical task
       - Shift due_datetime forward (daily +1 day, weekly +7 days, monthly +approx 30 days)
       - Keep title, description, priority, tags, recurrence setting
     - Show 🔁 symbol in list for recurring tasks

  2. Full DateTime + Intelligent Console Reminders
     - Upgrade due to due_datetime (YYYY-MM-DD [HH:MM] – time optional)
     - If no time given → assume 23:59
     - On app startup (before menu):
       - Check all tasks against current time
       - Print big reminder banner with counts of:
         - Overdue tasks
         - Due today
         - Due soon (next 2 hours)
       - Example:
         "⚠️ REMINDERS: 1 OVERDUE | 2 DUE TODAY | 1 DUE SOON"
     - In list view: show time, [OVERDUE], [DUE SOON] labels

  Rules:
  - Extend Task model with safe defaults (old tasks must work)
  - Use datetime and timedelta only
  - Keep all existing menu options and behavior intact
  - Only add optional prompts – skipping gives old behavior
  - Generate ONLY incremental changes (show what to add/modify in existing files)

  Begin safe incremental implementation now.

response_text: |
  Successfully implemented Advanced Todo Features with:

  1. Recurring Tasks functionality:
     - Extended Task model with recurrence, is_template, and parent_id fields
     - Created RecurrenceService for managing recurring task lifecycle
     - Added recurring task creation and management to CLI
     - Implemented automatic instance generation when recurring tasks are completed
     - Added 🔁 symbol display for recurring tasks in list view

  2. DateTime and Reminders functionality:
     - Extended Task model with due_datetime field
     - Created comprehensive datetime utility functions for parsing/validation
     - Created RemindersService for detecting overdue/due-soon tasks
     - Added startup reminder banner showing counts of overdue, due today, and due soon tasks
     - Enhanced task display to show time and status indicators

  3. Backward compatibility maintained:
     - All existing Basic/Intermediate features continue to work unchanged
     - New fields have safe defaults (None, False) for existing tasks
     - Existing task workflows remain identical when not using advanced features

  4. User interface updates:
     - Updated main menu with new options for recurring tasks
     - Enhanced task display with datetime and recurrence information
     - Added new prompts for datetime and recurrence input
     - Maintained all existing functionality and behavior

outcome: |
  Advanced Todo Features successfully implemented with full backward compatibility.
  All core functionality working: recurring tasks with automatic instance generation,
  datetime due dates with time precision, and intelligent startup reminders.
  Existing Basic/Intermediate features remain unchanged and fully functional.

evaluation: |
  The implementation meets all requirements:
  - Recurring tasks with daily, weekly, monthly intervals working correctly
  - DateTime due dates with optional time precision implemented
  - Startup reminders showing overdue/due today/due soon counts
  - Backward compatibility with existing tasks maintained
  - All new features integrated seamlessly with existing codebase
  - Safe defaults ensure no disruption to existing functionality
---
