---
id: 1
title: Create Constitution
stage: constitution
date: 2025-12-29
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: user
command: /sp.constitution
labels: [constitution, setup, governance]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

You are building Phase I of "The Evolution of Todo": a simple in-memory command-line Todo application in Python.

This is a hackathon project using Spec-Kit Plus for strict spec-driven development.

Project Goal for Phase I:
Create a basic console-based Todo app that stores tasks only in memory (no files, no database). It must support exactly these 5 core features:
1. Add a new task with a title and description.
2. Delete a task by its ID.
3. Update an existing task's title or description by ID.
4. View/list all tasks, showing ID, title, description, and completion status (with clear indicators like [ ] for incomplete and [x] for complete).
5. Mark a task as complete or incomplete (toggle) by ID.

The app should run in a loop, presenting a simple text menu for commands (e.g., 1: Add, 2: List, 3: Update, etc.), and exit gracefully.

Technology Constraints:
- Use Python 3.13+.
- Managed with UV (so setup instructions must include UV usage).
- No external libraries – only Python standard library.
- In-memory storage only (e.g., a list of dicts or a simple Task class).

Development Principles (these must be in the constitution as immutable rules):
- Follow clean code: readable variable/function names, small functions, separation of concerns (e.g., separate modules for models, storage, UI/cli).
- Proper project structure: src/ folder for source code, possibly src/todo/ with __init__.py, models.py, storage.py, cli.py, main.py.
- Type hints everywhere (use typing module).
- Comprehensive docstrings for all functions/classes.
- Error handling: graceful handling of invalid inputs (e.g., wrong ID, empty title).
- Tasks should have: unique auto-incrementing ID, title (required), description (optional), completed boolean (default False).
- CLI should be user-friendly: clear prompts, numbered menu, confirmation for delete.
- Code must be testable (though no tests required in Phase I, design for future testability).
- No persistence in this phase – data lost on exit.
- Prioritize simplicity and correctness over advanced features.

Project Deliverables:
- GitHub repo with:
  - This constitution file
  - Specs history folder containing all specification files
  - src/ folder with clean Python code
  - README.md with UV setup instructions and how to run the app
  - Fully working console application demonstrating all 5 features

Now, using /sp.constitution (or the Spec-Kit Plus constitution command), generate a strong, comprehensive constitution.md file that encodes ALL the above as immutable governing principles.

The constitution should:
- Clearly separate sections (e.g., Code Quality, Architecture, Constraints, User Experience).
- Be detailed enough to guide all future specs, plans, and implementation without deviation.
- Emphasize spec-driven workflow adherence.
- Prepare for future phases (e.g., mention that persistence is out of scope for Phase I).

Generate the full constitution content now.

## Response snapshot

Created a comprehensive constitution file for "The Evolution of Todo" Phase I project with the following key sections:

1. Core Principles:
   - Spec-Driven Development (NON-NEGOTIABLE)
   - Python 3.13+ Standard Library Only
   - In-Memory Storage (Phase I Constraint)
   - Clean Code Architecture
   - Type Safety and Documentation
   - Error Handling and User Experience

2. Technology and Implementation Constraints:
   - Python version and dependency requirements
   - Data model specifications
   - User interface specifications

3. Development Workflow and Quality Standards:
   - Code quality requirements
   - Project structure guidelines
   - Testing and validation standards

4. Governance section with versioning and compliance requirements

The constitution file (.specify/memory/constitution.md) has been created with version 1.0.0, ratification date 2025-12-29, and all the required principles and constraints encoded as immutable governing principles for the project.

## Outcome

- ✅ Impact: Created foundational governance document for the Todo app project
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md
- 🔁 Next prompts: Proceed with creating spec, plan, and implementation
- 🧠 Reflection: Constitution properly encodes all required constraints and principles for Phase I

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Create the initial specification document