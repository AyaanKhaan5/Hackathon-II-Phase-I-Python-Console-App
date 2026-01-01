---
id: 5
title: Generate Tasks
stage: tasks
date: 2025-12-30
surface: agent
model: claude-sonnet-4-5-20250929
feature: intermediate-features
branch: 1-intermediate-features
user: user
command: /sp.tasks
labels: [tasks, implementation, todo-app]
links:
  spec: specs/1-intermediate-features/spec.md
  plan: specs/1-intermediate-features/plan.md
  tasks: specs/1-intermediate-features/tasks.md
  adr: null
  pr: null
files:
 - specs/1-intermediate-features/tasks.md
tests:
 - none
---

## Prompt

Generate implementation tasks for the Intermediate Level features of "The Evolution of Todo".

CRITICAL: The Basic Level functionality (already implemented) MUST NOT BREAK under any circumstances. All changes are purely additive and evolutionary.

Strictly follow the current constitution (version 2.0.0) and the existing specification and plan.

Create a comprehensive, actionable task list that safely implements Intermediate features on top of the existing Basic Level code.

The tasks must follow Spec-Kit Plus structure exactly:

1. Implementation Strategy
   - MVP scope definition (User Story 1)
   - Phased approach with priority order

2. Dependencies
   - Clear dependency relationships between user stories

3. Parallel Execution Opportunities
   - Identify tasks that can be done in parallel

4. Phase Structure:
   - Phase 1: Setup (project initialization)
   - Phase 2: Foundational (blocking prerequisites for all user stories)
   - Phase 3+: One phase per user story (in priority order from spec.md)
   - Final Phase: Polish & cross-cutting concerns

5. Each task must follow checklist format:
   - Checkbox: - [ ]
   - Task ID: Sequential number (T001, T002, etc.)
   - Parallel marker: [P] if task can be done in parallel
   - Story label: [US1], [US2], etc. for user story tasks
   - Description: Clear action with file path

Generate complete, professional tasks ready for immediate implementation.

## Response snapshot

# Implementation Tasks: Intermediate Features - Due Dates, Priorities, Tags, Search, Filter, Sort

**Feature**: Intermediate Features for "The Evolution of Todo"
**Branch**: 1-intermediate-features
**Created**: 2025-12-30
**Status**: Draft

## Implementation Strategy

This implementation follows a phased approach with user stories in priority order (P1 through P5). Each user story represents a complete, independently testable increment that adds value while maintaining backward compatibility with Basic Level functionality.

**MVP Scope**: User Story 1 (Due Dates) provides immediate value and establishes the foundation for other Intermediate Level features.

## Dependencies

- User Story 1 (Due Dates) must be completed before User Story 2 (Priorities & Tags) since both modify the Task model
- User Story 2 must be completed before User Story 3 (Search) since search needs to include tags
- User Story 2 must be completed before User Story 4 (Filter) since filtering needs priority and tags
- User Story 2 must be completed before User Story 5 (Sort) since sorting needs due dates and priority

## Parallel Execution Opportunities

- Within each user story, model, service, and CLI changes can often be done in parallel
- Search, filter, and sort services can be developed in parallel after foundational changes are complete

## Phase 1: Setup

- [ ] T001 Create services directory structure in src/todo/
- [ ] T002 Set up git branch 1-intermediate-features

## Phase 2: Foundational Changes

- [ ] T003 [P] Extend Task dataclass with new optional fields in src/todo/models.py
- [ ] T004 [P] Update TaskStorage to handle new fields in src/todo/storage.py
- [ ] T005 [P] Update display_tasks function to show new fields in src/todo/cli.py
- [ ] T006 [P] Add date utility functions for due date validation in src/todo/utils.py

## Phase 3: User Story 1 - Add Due Dates to Tasks (Priority: P1)

**Goal**: Enable users to assign due dates to tasks and display overdue status

**Independent Test**: Users can add tasks with due dates and verify they display correctly in the list view, with overdue tasks marked appropriately.

**Tasks**:

- [ ] T007 [US1] Add due date validation function in src/todo/utils.py
- [ ] T008 [US1] Update add_task CLI function to accept optional due date in src/todo/cli.py
- [ ] T009 [US1] Update update_task CLI function to accept optional due date in src/todo/cli.py
- [ ] T010 [US1] Modify display_tasks to show due dates and overdue status in src/todo/cli.py
- [ ] T011 [US1] Test that Basic Level tasks still work unchanged with due date feature

## Phase 4: User Story 2 - Set Task Priorities and Tags (Priority: P2)

**Goal**: Allow users to assign priority levels and tags to tasks

**Independent Test**: Users can create tasks with different priorities and tags, verifying they display correctly while Basic Level tasks continue to work unchanged.

**Tasks**:

- [ ] T012 [US2] Add priority validation function in src/todo/utils.py
- [ ] T013 [US2] Add tag processing function in src/todo/utils.py
- [ ] T014 [US2] Update add_task CLI function to accept optional priority and tags in src/todo/cli.py
- [ ] T015 [US2] Update update_task CLI function to accept optional priority and tags in src/todo/cli.py
- [ ] T016 [US2] Modify display_tasks to show priority and tags in src/todo/cli.py
- [ ] T017 [US2] Test that Basic Level tasks still work unchanged with priority and tags features

## Phase 5: User Story 3 - Search Tasks by Content (Priority: P3)

**Goal**: Enable users to search for tasks by keyword across title, description, and tags

**Independent Test**: Users can search for tasks with specific keywords and verify that matching tasks are returned separately from basic task operations.

**Tasks**:

- [ ] T018 [US3] Create TaskSearchService in src/todo/services/search_service.py
- [ ] T019 [US3] Implement keyword search functionality in search_service.py
- [ ] T020 [US3] Add search menu option and CLI interface in src/todo/cli.py
- [ ] T021 [US3] Integrate search functionality with main application loop in src/todo/main.py
- [ ] T022 [US3] Test search functionality with various keyword combinations

## Phase 6: User Story 4 - Filter Tasks by Criteria (Priority: P4)

**Goal**: Allow users to filter tasks by status, priority, due date range, or specific tags

**Independent Test**: Users can apply different filters and verify that only matching tasks are displayed separately from basic task operations.

**Tasks**:

- [ ] T023 [US4] Create TaskFilterService in src/todo/services/filter_service.py
- [ ] T024 [US4] Implement filtering by status, priority, due date range, and tags in filter_service.py
- [ ] T025 [US4] Add filter menu option and CLI interface in src/todo/cli.py
- [ ] T026 [US4] Integrate filtering functionality with main application loop in src/todo/main.py
- [ ] T027 [US4] Test filtering with various criteria combinations

## Phase 7: User Story 5 - Sort Tasks by Different Criteria (Priority: P5)

**Goal**: Enable users to sort tasks by due date, priority, creation time, or title

**Independent Test**: Users can select different sort orders and verify that tasks are displayed in the correct sequence.

**Tasks**:

- [ ] T028 [US5] Create TaskSortService in src/todo/services/sort_service.py
- [ ] T029 [US5] Implement sorting by due date, priority, creation time, and title in sort_service.py
- [ ] T030 [US5] Add sort menu option and CLI interface in src/todo/cli.py
- [ ] T031 [US5] Integrate sorting functionality with main application loop in src/todo/main.py
- [ ] T032 [US5] Test sorting with various criteria and verify default sort behavior

## Phase 8: Polish & Cross-Cutting Concerns

- [ ] T033 Update main menu to include all new Intermediate Level features while preserving Basic Level options
- [ ] T034 Implement combined search, filter, and sort functionality
- [ ] T035 Add comprehensive error handling for all new features
- [ ] T036 Test complete backward compatibility with Basic Level functionality
- [ ] T037 Update documentation and user help messages
- [ ] T038 Perform integration testing of all features working together
- [ ] T039 Run full regression test to ensure no Basic Level functionality was broken

## Outcome

- ✅ Impact: Created comprehensive task list for implementing intermediate features with clear phase structure and dependencies
- 🧪 Tests: none
- 📁 Files: Created tasks.md with 39 implementation tasks
- 🔁 Next prompts: Begin implementation with first tasks
- 🧠 Reflection: Tasks follow proper checklist format and maintain backward compatibility requirements
- 📋 ADRs: None needed for task generation

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Start implementation with foundational tasks