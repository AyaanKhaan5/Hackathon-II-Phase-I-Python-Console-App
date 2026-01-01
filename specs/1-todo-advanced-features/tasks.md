# Tasks: Advanced Todo Features - Recurring Tasks and DateTime Reminders

## Feature Overview

Implementation of Advanced Todo Features including recurring tasks with configurable intervals (daily, weekly, monthly, yearly) and enhanced datetime due dates with time precision (YYYY-MM-DD HH:MM). The system will automatically generate new task instances when recurring tasks are completed and provide simulated reminders at app startup for overdue and "DUE SOON" tasks. All changes maintain 100% backward compatibility with existing Basic and Intermediate level tasks.

## Dependencies

- User Story 2 (DateTime Due Dates) must be completed before User Story 1 (Recurring Tasks) can be fully tested
- Foundational task T003 (Extend Task model) is required by all other user stories

## Parallel Execution Examples

- T004 [P] [US2] and T005 [P] [US2] can run in parallel (different files: datetime_utils.py and reminders.py)
- T007 [P] [US1] and T008 [P] [US1] can run in parallel (different files: recurrence.py and menu.py)

## Implementation Strategy

MVP scope includes User Story 2 (DateTime reminders) and basic User Story 1 (recurring tasks) functionality. Additional features like recurrence management and edge case handling will be implemented in subsequent iterations.

---

## Phase 1: Setup

### Goal
Initialize project structure and dependencies for Advanced features implementation.

### Independent Test
Project structure matches implementation plan with all required directories and files created.

- [ ] T001 Create src/models directory if it doesn't exist
- [ ] T002 Create src/services directory if it doesn't exist
- [ ] T003 Create src/cli directory if it doesn't exist
- [ ] T004 Create src/lib directory if it doesn't exist
- [ ] T005 Create tests/unit directory if it doesn't exist

---

## Phase 2: Foundation

### Goal
Extend the existing Task model with new fields for datetime and recurrence functionality while maintaining backward compatibility.

### Independent Test
Extended Task model supports all new fields with safe defaults and maintains existing functionality.

- [ ] T006 Extend Task dataclass in src/models/task.py with due_datetime field (datetime | None, default None)
- [ ] T007 Extend Task dataclass in src/models/task.py with recurrence field (str | None, default None)
- [ ] T008 Extend Task dataclass in src/models/task.py with is_template field (bool, default False)
- [ ] T009 Extend Task dataclass in src/models/task.py with parent_id field (int | None, default None)
- [ ] T010 Update Task model validation to handle new fields with proper defaults
- [ ] T011 Update existing task storage to handle new fields with safe migration

---

## Phase 3: User Story 2 - DateTime Due Dates and Reminders (Priority: P1)

### Goal
As a user, I want to set due dates with time precision (YYYY-MM-DD HH:MM) and receive simulated reminders at app startup so that I can better manage time-sensitive tasks.

### Independent Test
User can set a datetime for a task and see overdue/due soon alerts when starting the application.

- [ ] T012 [P] [US2] Create datetime utility functions in src/lib/datetime_utils.py for parsing and validation
- [ ] T013 [P] [US2] Implement datetime parsing with format validation (YYYY-MM-DD HH:MM) in datetime_utils.py
- [ ] T014 [P] [US2] Create reminders service in src/services/reminders.py for overdue and due-soon detection
- [ ] T015 [P] [US2] Implement get_overdue_tasks function in reminders.py that returns tasks past due datetime
- [ ] T016 [P] [US2] Implement get_due_soon_tasks function in reminders.py that returns tasks due within next hour
- [ ] T017 [P] [US2] Implement get_startup_reminders function in reminders.py that returns summary counts and task lists
- [ ] T018 [P] [US2] Update task display in existing menu to show time if present and "OVERDUE"/"DUE SOON" indicators
- [ ] T019 [US2] Integrate startup reminder processing into main application startup sequence
- [ ] T020 [US2] Display summary banner "You have X overdue tasks and Y due today!" at app startup
- [ ] T021 [US2] Update task creation/editing to accept datetime input in YYYY-MM-DD HH:MM format
- [ ] T022 [US2] Add datetime validation to prevent invalid date/time entries
- [ ] T023 [US2] Test acceptance scenario: task with due datetime in past shows as overdue at startup
- [ ] T024 [US2] Test acceptance scenario: task due within next hour shows "DUE SOON" at startup
- [ ] T025 [US2] Test acceptance scenario: startup summary banner shows correct counts

---

## Phase 4: User Story 1 - Create Recurring Tasks (Priority: P1)

### Goal
As a user, I want to mark an existing task as recurring with a repeat interval (daily, weekly, monthly, yearly) so that I don't have to manually recreate routine tasks.

### Independent Test
User can select an existing task and configure it to repeat at specified intervals, with the system maintaining the original as a template.

- [ ] T026 [P] [US1] Create recurrence service in src/services/recurrence.py for task generation logic
- [ ] T027 [P] [US1] Implement calculate_next_due_date function in recurrence.py for all intervals (daily, weekly, monthly, yearly)
- [ ] T028 [P] [US1] Implement generate_next_instance function in recurrence.py that creates new task from template
- [ ] T029 [P] [US1] Implement handle_task_completion function in recurrence.py that creates new instance if recurring
- [ ] T030 [P] [US1] Add recurrence validation to ensure only valid intervals (daily, weekly, monthly, yearly) are accepted
- [ ] T031 [US1] Update task completion logic to check for recurrence and generate new instances
- [ ] T032 [US1] Create recurring task creation interface in menu system
- [ ] T033 [US1] Add "Create Recurring Task" option to main menu in cli/menu.py
- [ ] T034 [US1] Implement recurring task creation workflow with interval selection
- [ ] T035 [US1] Set is_template=True for recurring tasks and preserve as template
- [ ] T036 [US1] Generate first instance for new recurring task with appropriate due date
- [ ] T037 [US1] Test acceptance scenario: existing task made recurring with daily interval creates template and tomorrow's instance
- [ ] T038 [US1] Test acceptance scenario: marking recurring task complete generates new instance with next due date

---

## Phase 5: User Story 3 - View Recurring Task Lifecycle (Priority: P2)

### Goal
As a user, I want to view both recurring task templates and their generated instances so that I can understand the relationship between templates and active tasks.

### Independent Test
User can see which tasks are templates vs. instances and understand the relationship between them.

- [ ] T039 [P] [US3] Update task display format to distinguish between templates and instances
- [ ] T040 [P] [US3] Add visual indicator (e.g., 🔁) to recurring tasks in task list display
- [ ] T041 [US3] Show recurrence interval in task display for template tasks
- [ ] T042 [US3] Show parent template relationship for instance tasks
- [ ] T043 [US3] Update list view to clearly mark templates vs. instances
- [ ] T044 [US3] Test acceptance scenario: recurring task templates are clearly marked with recurrence rules visible
- [ ] T045 [US3] Test acceptance scenario: generated instances are linked to parent templates in display

---

## Phase 6: User Story 4 - Edit/Disable Recurrence (Priority: P2)

### Goal
As a user, I want to edit or delete the recurrence rule of a task so that I can modify or stop recurring tasks as needed.

### Independent Test
User can modify the recurrence interval or completely disable recurrence for a template.

- [ ] T046 [P] [US4] Add "Manage Recurrence" option to main menu
- [ ] T047 [P] [US4] Implement recurrence management interface in cli/menu.py
- [ ] T048 [US4] Create function to update recurrence rule for template tasks
- [ ] T049 [US4] Create function to disable recurrence (set to None) for template tasks
- [ ] T050 [US4] Ensure template tasks cannot be marked complete directly
- [ ] T051 [US4] Update recurrence rule to affect future instances only (not past ones)
- [ ] T052 [US4] Test acceptance scenario: editing recurrence rule causes future instances to follow new rule
- [ ] T053 [US4] Test acceptance scenario: disabling recurrence prevents new instances after current one completes

---

## Phase 7: User Story 5 - Handle DateTime Edge Cases (Priority: P3)

### Goal
As a user, I want the system to handle datetime edge cases gracefully (month boundaries, leap years, etc.) so that recurring tasks continue to work correctly across all date/time scenarios.

### Independent Test
System correctly handles month boundaries, leap years, and other datetime edge cases when generating recurring tasks.

- [ ] T054 [P] [US5] Implement edge case handling for monthly recurrence across month boundaries
- [ ] T055 [P] [US5] Handle February 31st case by adjusting to last valid day of month
- [ ] T056 [P] [US5] Handle leap year cases (February 29th) in recurrence calculations
- [ ] T057 [US5] Test acceptance scenario: monthly recurring task from January 31st adjusts correctly for February
- [ ] T058 [US5] Test acceptance scenario: recurring task crossing year boundaries handles correctly

---

## Phase 8: Polish & Cross-Cutting Concerns

### Goal
Final integration, testing, and polish to ensure all features work together seamlessly.

### Independent Test
All advanced features work together and maintain backward compatibility with existing functionality.

- [ ] T059 Update README with documentation for Advanced features
- [ ] T060 Create user guide for recurring tasks and datetime features
- [ ] T061 Add error handling for edge cases in recurrence and datetime functionality
- [ ] T062 Verify backward compatibility with existing Basic/Intermediate tasks
- [ ] T063 Performance test: ensure startup reminder processing completes within 2 seconds
- [ ] T064 Run all existing tests to confirm no regression in Basic/Intermediate functionality
- [ ] T065 User acceptance testing for all implemented features
- [ ] T066 Code review and documentation completion
- [ ] T067 Final integration testing with all features enabled