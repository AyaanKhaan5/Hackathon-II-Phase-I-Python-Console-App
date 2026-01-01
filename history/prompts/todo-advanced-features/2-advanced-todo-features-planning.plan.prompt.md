---
id: 2
title: advanced-todo-features-planning
stage: plan
date_iso: 2025-12-30
surface: agent
model: Claude Sonnet 4.5
feature: todo-advanced-features
branch: 1-todo-advanced-features
user: user
command: /sp.plan
labels:
  - planning
  - todo
  - advanced-features
  - recurring-tasks
  - datetime

links:
  spec: specs/1-todo-advanced-features/spec.md
  ticket: null
  adr: null
  pr: null

files_yaml:
  - specs/1-todo-advanced-features/plan.md
  - specs/1-todo-advanced-features/research.md
  - specs/1-todo-advanced-features/data-model.md
  - specs/1-todo-advanced-features/quickstart.md
  - specs/1-todo-advanced-features/contracts/task-contracts.json

tests_yaml:
  - Constitution compliance check
  - Architecture sketch validation
  - Data model validation
  - Contract definition verification

prompt_text: |
  You are now in the planning phase (/sp.plan) for the Advanced Level of "The Evolution of Todo".

  CRITICAL CONTEXT:
  - Basic and Intermediate Levels are already fully implemented and working perfectly in the current codebase.
  - DO NOT rewrite or regenerate the entire project.
  - All changes must be purely additive and preserve 100% backward compatibility.

  This plan is to safely extend the existing working app with ONLY the Advanced Level features, following the constitution (v2.0.0) and the newly generated Advanced specifications.

  The plan must strictly follow Spec-Kit Plus structure:

  1. Architecture Sketch
     - Text-based diagram showing current components + new extensions (e.g., recurrence service, startup reminder logic)
     - Clearly indicate integration points without disrupting existing functionality

  2. Technical Context
     - Language: Python 3.11+
     - Dependencies: Standard library only
     - Storage: JSON files (existing mechanism)
     - Performance: <100ms for task operations, <2s for startup processing

  3. Constitution Check
     - GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.
     - Verify compliance with all constitution principles

  4. Project Structure
     - Organize files according to standard layout
     - Create appropriate modules for separation of concerns

  5. Manual testing plan including:
     - Create recurring task → complete → verify new instance appears with correct next date
     - Set task due yesterday → start app → see overdue banner and highlight
     - Set task due today in 30 mins → start app → see "DUE SOON"
     - Existing non-recurring tasks → complete normally (no auto-generate)
     - Tasks from Basic/Intermediate → display and behave correctly
     - Edge cases: monthly recurrence across year boundary, no time specified

  7. Technical Details
   - Research-concurrent approach
   - Organize implementation in phases:
     - Foundation: Extend Task model safely
     - Core Logic: Recurrence generation and datetime upgrade
     - UI/UX: Startup reminders and enhanced display
     - Polish: Menu updates and user flows
   - Use standard library only (datetime, timedelta)
   - Update README with Advanced features demo

  Additional Guidelines:
  - Extend existing Task dataclass with safe defaults
  - Prefer adding new service module (e.g., services/recurrence.py) over bloating existing ones
  - Startup reminder: execute early in main() before menu loop
  - Menu: Add clear new options for "Create Recurring Task", "Manage Recurrence"
  - Display: Enhance list view with time and recurrence indicator (e.g., 🔁 for recurring)
  - Ensure old tasks (no due_datetime or recurrence) behave exactly as before

  Generate a complete, professional, and safe incremental plan that guarantees clean evolution to Advanced Level without breaking any existing functionality.

  Focus on minimal, targeted, non-disruptive extensions.

  Begin planning now.

response_text: |
  Successfully created the implementation plan for Advanced Todo Features. The plan includes:
  - Architecture sketch showing new components (recurrence service, reminder service)
  - Technical context with Python 3.11+, standard library only
  - Constitution compliance with all v2.0.0 principles
  - Project structure with modular architecture (models, services, cli)
  - Data model extension with safe defaults for backward compatibility
  - Research document with technical decisions
  - Quickstart guide for developers
  - API contracts for new functionality

  The plan maintains 100% backward compatibility with existing Basic/Intermediate features while adding:
  - Recurring tasks with intervals (daily, weekly, monthly, yearly)
  - DateTime due dates with time precision (YYYY-MM-DD HH:MM)
  - Startup reminder processing for overdue and "DUE SOON" tasks
  - New service modules for separation of concerns

outcome: |
  Implementation plan successfully created for Advanced Todo Features.
  All required documentation artifacts generated and validated.
  Plan compliant with constitution v2.0.0 and ready for task generation phase.

evaluation: |
  The plan meets all requirements:
  - Architecture supports new features while preserving existing functionality
  - Backward compatibility maintained through safe defaults
  - Modular design with clear separation of concerns
  - All constitution principles verified and compliant
  - Technical approach aligns with standard library constraint
---
