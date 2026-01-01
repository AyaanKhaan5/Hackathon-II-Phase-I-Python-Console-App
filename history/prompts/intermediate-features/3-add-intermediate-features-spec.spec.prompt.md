---
id: 3
title: Add Intermediate Features Spec
stage: spec
date: 2025-12-30
surface: agent
model: claude-sonnet-4-5-20250929
feature: intermediate-features
branch: 1-intermediate-features
user: user
command: /sp.specify
labels: [specification, intermediate, todo-app, features]
links:
  spec: specs/1-intermediate-features/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/1-intermediate-features/spec.md
 - specs/1-intermediate-features/checklists/requirements.md
tests:
 - none
---

## Prompt

You are now in the specification phase (/sp.specify) for the Intermediate Level of "The Evolution of Todo".

CRITICAL RULE: The Basic Level functionality (already implemented) MUST NOT BREAK under any circumstances. All existing behaviors from Basic Level must work exactly as before – adding Intermediate features is purely additive and evolutionary.

This specification covers ONLY the new Intermediate Level features. Basic Level is complete and must remain fully functional and unchanged in behavior.

Strictly follow the current constitution (version 2.0.0).

Intermediate Level Features to Add (Purely Additive):

1. Due Dates
   - Optional due date (YYYY-MM-DD) assignable during add or update
   - If no due date set, behave exactly as  Tasks created in Basic Level must load and function perfectly with new features (missing fields treated as defaults)
- Menu must include all old options with same numbers/behavior if possible, or clearly separate new ones
- No changes to core task ID, title, description, completed status behavior
-in Basic Level
   - Display due date in list view only if present
   - Show "OVERDUE" label or symbol if due date is past today's date

2. Priorities & Tags/Categories
   - Priority: High, Medium (default), Low – added as new optional field
   - Tags: List of free-text tags (empty by default)
   - If not set, task behaves exactly as Basic Level task
   - Users can set/change them during add or update

3. Search & Filter
   - New menu option: "Search & Filter Tasks"
   - Search by keyword (title, description, tags) – case insensitive
   - Filters: status, priority, due date range, specific tag
   - Can combine multiple filters
   - After viewing filtered results, return to main menu normally
   - Regular "List All Tasks" remains unchanged and shows everything

4. Sort Tasks
   - New menu option or setting: choose sort order for list display
   - Options: Due date (earliest first), Priority (H>M>L), Creation time, Title
   - Default sort: Due date (earliest first), then priority
   - If no due dates, fall b List view enhances display (adds priority, due, tags) but core info remains visible

Technical Requirements:
- Extend Task dataclass with new optional fields (due_date: date | None = None, priority: str = "Medium", tags: list[str] = field(default_factory=list))
- Storage layer must handle old and new task formats seamlessly
- CLI: Add new menu options clearly labeled as "Intermediate Features"
- All input optional – user can skip new fields and get pure Basic behavior
- Standard library only, full type hints, clean separation of concerns

Generate detailed, actionable specifications in Spec-Kit Plus format that:
- Clearly mark what is new vs what must remain unchanged
- Define safe extension points (model, display, menu)
- Include user flows showing both old and new paths
- Cover migration/compatibility scenarios
- Handle defaults and missing data gracefully

Produce specifications focused on safe, non-breaking evolution from Basic to Intermediate Level.

Start generating now.

## Response snapshot

# Feature Specification: Intermediate Features - Due Dates, Priorities, Tags, Search, Filter, Sort

**Feature Branch**: `1-intermediate-features`
**Created**: 2025-12-30
**Status**: Draft
**Input**: User description: "You are now in the specification phase (/sp.specify) for the Intermediate Level of \"The Evolution of Todo\".

CRITICAL RULE: The Basic Level functionality (already implemented) MUST NOT BREAK under any circumstances. All existing behaviors from Basic Level must work exactly as before – adding Intermediate features is purely additive and evolutionary.

This specification covers ONLY the new Intermediate Level features. Basic Level is complete and must remain fully functional and unchanged in behavior.

Strictly follow the current constitution (version 2.0.0).

Intermediate Level Features to Add (Purely Additive):

1. Due Dates
   - Optional due date (YYYY-MM-DD) assignable during add or update
   - If no due date set, behave exactly as in Basic Level
   - Display due date in list view only if present
   - Show \"OVERDUE\" label or symbol if due date is past today's date

2. Priorities & Tags/Categories
   - Priority: High, Medium (default), Low – added as new optional field
   - Tags: List of free-text tags (empty by default)
   - If not set, task behaves exactly as Basic Level task
   - Users can set/change them during add or update

3. Search & Filter
   - New menu option: \"Search & Filter Tasks\"
   - Search by keyword (title, description, tags) – case insensitive
   - Filters: status, priority, due date range, specific tag
   - Can combine multiple filters
   - After viewing filtered results, return to main menu normally
   - Regular \"List All Tasks\" remains unchanged and shows everything

4. Sort Tasks
   - New menu option or setting: choose sort order for list display
   - Options: Due date (earliest first), Priority (H>M>L), Creation time, Title
   - Default sort: Due date (earliest first), then priority
   - If no due dates, fall back to other criteria

Technical Requirements:
- Extend Task dataclass with new optional fields (due_date: date | None = None, priority: str = \"Medium\", tags: list[str] = field(default_factory=list))
- Storage layer must handle old and new task formats seamlessly
- CLI: Add new menu options clearly labeled as \"Intermediate Features\"
- All input optional – user can skip new fields and get pure Basic behavior
- Standard library only, full type hints, clean separation of concerns

Generate detailed, actionable specifications in Spec-Kit Plus format that:
- Clearly mark what is new vs what must remain unchanged
- Define safe extension points (model, display, menu)
- Include user flows showing both old and new paths
- Cover migration/compatibility scenarios
- Handle defaults and missing data gracefully

Produce specifications focused on safe, non-breaking evolution from Basic to Intermediate Level.

Start generating now."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add Due Dates to Tasks (Priority: P1)

As a user, I want to assign due dates to my tasks so I can track deadlines and manage my time more effectively. I can add a due date when creating a new task or update an existing task to include a due date. If I don't add a due date, the task behaves exactly as it did in Basic Level.

**Why this priority**: Due dates are fundamental for task organization and time management, providing immediate value for users who need to track deadlines.

**Independent Test**: Can be fully tested by adding tasks with due dates and verifying they display correctly in the list view. Users can see which tasks have due dates and which don't, without affecting Basic Level functionality.

**Acceptance Scenarios**:

1. **Given** I am on the add task screen, **When** I enter a valid due date in YYYY-MM-DD format, **Then** the task is created with the due date and displays in the task list
2. **Given** I have an existing task without a due date, **When** I update the task and add a due date, **Then** the task is updated with the due date and displays correctly in the list
3. **Given** I have tasks with due dates, **When** I view the task list, **Then** tasks with due dates show the date and overdue tasks are marked as such
4. **Given** I have tasks without due dates, **When** I view the task list, **Then** tasks display exactly as they did in Basic Level (no due date shown)

---

### User Story 2 - Set Task Priorities and Tags (Priority: P2)

As a user, I want to assign priorities (High, Medium, Low) and tags to my tasks so I can categorize and prioritize them effectively. I can set these when creating or updating tasks, and if I don't set them, the task behaves exactly as it did in Basic Level.

**Why this priority**: Priorities and tags provide essential organization capabilities that help users focus on important tasks and categorize their work.

**Independent Test**: Can be fully tested by creating tasks with different priorities and tags, and verifying they display correctly in the list view. Basic Level tasks continue to work unchanged.

**Acceptance Scenarios**:

1. **Given** I am adding a new task, **When** I select a priority level (High/Medium/Low) and add tags, **Then** the task is created with these attributes and displays in the list
2. **Given** I have an existing task, **When** I update it to add priority and tags, **Then** the task is updated and displays correctly
3. **Given** I have tasks with priorities and tags, **When** I view the list, **Then** the priority and tags are visible in the display
4. **Given** I have tasks without priorities or tags, **When** I view the list, **Then** they display as Basic Level tasks

---

### User Story 3 - Search Tasks by Content (Priority: P3)

As a user, I want to search for tasks by keyword in the title, description, or tags so I can quickly find specific tasks among many. This feature should not affect the basic functionality of the application.

**Why this priority**: Search capability becomes valuable as users accumulate more tasks, but is less critical than due dates and priorities.

**Independent Test**: Can be fully tested by searching for tasks with specific keywords and verifying that matching tasks are returned. The search functionality can be accessed separately from basic task operations.

**Acceptance Scenarios**:

1. **Given** I have multiple tasks with different content, **When** I enter a search keyword, **Then** all tasks containing that keyword in title, description, or tags are displayed
2. **Given** I perform a search, **When** no tasks match the keyword, **Then** I see a clear message that no results were found
3. **Given** I perform a search, **When** I want to return to all tasks, **Then** I can easily clear the search and return to the full list

---

### User Story 4 - Filter Tasks by Criteria (Priority: P4)

As a user, I want to filter my tasks by status, priority, due date range, or specific tags so I can focus on the tasks that matter most to me right now.

**Why this priority**: Filtering provides more advanced organization capabilities beyond search, allowing users to view specific subsets of tasks.

**Independent Test**: Can be fully tested by applying different filters and verifying that only matching tasks are displayed. The filtering functionality is separate from basic task operations.

**Acceptance Scenarios**:

1. **Given** I have tasks with different statuses, priorities, and due dates, **When** I apply a status filter, **Then** only tasks with that status are displayed
2. **Given** I have applied multiple filters, **When** I clear a filter, **Then** the remaining filters continue to apply
3. **Given** I am viewing filtered results, **When** I want to see all tasks again, **Then** I can clear all filters and return to the full list

---

### User Story 5 - Sort Tasks by Different Criteria (Priority: P5)

As a user, I want to sort my tasks by due date, priority, creation time, or title so I can view them in the order that makes the most sense for my current needs.

**Why this priority**: Sorting provides additional organization capabilities that complement filtering and search, but is less critical than the other features.

**Independent Test**: Can be fully tested by selecting different sort orders and verifying that tasks are displayed in the correct sequence.

**Acceptance Scenarios**:

1. **Given** I have tasks with various due dates, **When** I sort by due date, **Then** tasks are ordered from earliest to latest due date
2. **Given** I have tasks with different priorities, **When** I sort by priority, **Then** tasks are ordered High to Low priority
3. **Given** I have multiple sort options, **When** I select a sort method, **Then** tasks are consistently ordered according to that method

---

### Edge Cases

- What happens when a user enters an invalid date format? The system should reject the input and provide a clear error message with the expected format (YYYY-MM-DD)
- How does the system handle tasks with the same due date when sorting? They should be sorted by priority, then by creation time, then by title
- What happens when a user searches for a term that matches both title and description? The task should appear in results only once
- How does the system handle tasks with multiple tags during filtering? A task should match if it has ANY of the specified tags when using OR logic, or ALL when using AND logic
- What happens when a task has both a due date and priority for sorting? The default should be due date first, then priority
- How does the system handle empty tags or tags with special characters? Empty tags should be ignored, special characters should be handled safely

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST extend the Task data model with optional due_date (date type, default None), priority (string, default "Medium"), and tags (list of strings, default empty)
- **FR-002**: System MUST allow users to add due dates in YYYY-MM-DD format when creating or updating tasks
- **FR-003**: System MUST validate due date format and reject invalid formats with clear error messages
- **FR-004**: System MUST display due dates in the task list only for tasks that have them set
- **FR-005**: System MUST mark tasks as "OVERDUE" in the display if their due date is past today's date
- **FR-006**: System MUST allow users to set priority levels as "High", "Medium", or "Low" with "Medium" as default
- **FR-007**: System MUST display priority indicators in the task list for tasks that have them set
- **FR-008**: System MUST allow users to add multiple tags to tasks as free-text labels
- **FR-009**: System MUST display tags in the task list for tasks that have them set
- **FR-010**: System MUST provide a "Search & Filter Tasks" menu option that allows keyword search across title, description, and tags
- **FR-011**: System MUST support case-insensitive search across all searchable fields
- **FR-012**: System MUST provide filtering options for status, priority, due date range, and specific tags
- **FR-013**: System MUST allow combining multiple filters simultaneously
- **FR-014**: System MUST provide sorting options: due date (earliest first), priority (H>M>L), creation time, and title
- **FR-015**: System MUST default to sorting by due date (earliest first) then priority when displaying tasks
- **FR-016**: System MUST maintain backward compatibility with Basic Level tasks that lack new fields
- **FR-017**: System MUST handle old task formats seamlessly when loading existing Basic Level tasks
- **FR-018**: System MUST provide clear menu options for new Intermediate Level features while preserving all Basic Level functionality
- **FR-019**: System MUST allow users to skip new fields and get pure Basic Level behavior when adding or updating tasks
- **FR-020**: System MUST preserve all existing Basic Level functionality without any changes in behavior

### Key Entities *(include if feature involves data)*

- **Task**: Extended entity with optional due_date (date | None), priority (str with values "High"/"Medium"/"Low"), and tags (list[str]). Maintains all original Basic Level attributes (id, title, description, completed status)
- **Search Result**: A subset of tasks matching search criteria, containing the same attributes as the original Task entity
- **Filter Criteria**: A set of conditions (status, priority, due date range, specific tags) used to narrow down the task list
- **Sort Criteria**: A specification for ordering tasks (due date, priority, creation time, title) with direction (ascending/descending)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can successfully add due dates to new and existing tasks with 95% success rate (measured by successful task creation/update without errors)
- **SC-002**: Users can search for tasks by keyword and find relevant results within 2 seconds for task lists up to 1000 tasks
- **SC-003**: Users can filter tasks by at least 4 different criteria (status, priority, due date, tags) and see filtered results within 1 second
- **SC-004**: Users can sort tasks by at least 4 different criteria (due date, priority, creation time, title) with consistent and predictable ordering
- **SC-005**: 90% of users can successfully use new Intermediate Level features without breaking existing Basic Level functionality
- **SC-006**: Users can identify overdue tasks visually in the task list with 100% accuracy
- **SC-007**: All existing Basic Level functionality continues to work exactly as before with no regression in performance or behavior
- **SC-008**: Users can add, modify, and view tasks with priorities and tags with the same ease as Basic Level tasks

## Outcome

- ✅ Impact: Created comprehensive specification for intermediate features (due dates, priorities, tags, search, filter, sort) while maintaining backward compatibility
- 🧪 Tests: none
- 📁 Files: Created specs/1-intermediate-features/spec.md and specs/1-intermediate-features/checklists/requirements.md
- 🔁 Next prompts: Continue with planning phase using /sp.plan
- 🧠 Reflection: Specification clearly defines additive features that enhance the basic todo app without breaking existing functionality

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin planning for intermediate features implementation