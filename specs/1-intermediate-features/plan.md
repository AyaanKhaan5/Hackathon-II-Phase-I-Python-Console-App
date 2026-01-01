# Implementation Plan: Intermediate Features - Due Dates, Priorities, Tags, Search, Filter, Sort

**Feature**: Intermediate Level Features for "The Evolution of Todo"
**Branch**: 1-intermediate-features
**Created**: 2025-12-30
**Status**: Draft

## Technical Context

The Basic Level of "The Evolution of Todo" is already implemented with core functionality:
- Task model with ID, title, description, and completion status
- In-memory storage with CRUD operations
- CLI with menu options (Add, List, Update, Toggle, Delete, Exit)
- All functionality is working and must remain unchanged

This plan adds Intermediate Level features (due dates, priorities, tags, search, filter, sort) while maintaining complete backward compatibility with Basic Level functionality.

**Unknowns needing clarification:**
- None - all requirements are clearly defined in the feature specification

## Architecture Sketch

```
┌─────────────────────────────────────────────────────────────┐
│                    CLI Layer                               │
├─────────────────────────────────────────────────────────────┤
│  Basic Commands:      │  Intermediate Commands:            │
│  - Add Task          │  - Search & Filter Tasks           │
│  - List Tasks        │  - Sort Tasks                      │
│  - Update Task       │                                    │
│  - Toggle Completion │                                    │
│  - Delete Task       │                                    │
│  - Exit              │                                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  Service Layer                             │
├─────────────────────────────────────────────────────────────┤
│  Basic Services:     │  Intermediate Services:            │
│  - TaskStorage      │  - TaskSearchService               │
│                     │  - TaskFilterService               │
│                     │  - TaskSortService                 │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                 Data Model Layer                           │
├─────────────────────────────────────────────────────────────┤
│  Extended Task Model:                                      │
│  - id: int (unchanged)                                     │
│  - title: str (unchanged)                                  │
│  - description: Optional[str] (unchanged)                  │
│  - completed: bool (unchanged)                             │
│  - due_date: Optional[date] (NEW)                          │
│  - priority: str (NEW, "High"/"Medium"/"Low")             │
│  - tags: list[str] (NEW)                                   │
└─────────────────────────────────────────────────────────────┘
```

## Section Structure

### Files to Create:
1. `src/todo/services/search_service.py` - Task search functionality
2. `src/todo/services/filter_service.py` - Task filtering functionality
3. `src/todo/services/sort_service.py` - Task sorting functionality

### Files to Modify:
1. `src/todo/models.py` - Extend Task dataclass with new fields
2. `src/todo/storage.py` - Update methods to handle new fields
3. `src/todo/cli.py` - Add new menu options and input prompts
4. `src/todo/main.py` - Update main loop to include new features

## Research Approach

### Concurrent Research Tasks:
- **Date parsing**: Use `datetime.date.fromisoformat()` for YYYY-MM-DD format validation
- **Priority validation**: Simple string enum validation with "High", "Medium", "Low" values
- **Tag handling**: Use comma-separated input with strip and validation
- **Sorting algorithms**: Implement stable sorting with multiple criteria (due date first, then priority, etc.)

### Research-While-Implementing:
- Menu number assignments for new features (will determine during CLI updates)
- Display formatting for new fields (will refine during implementation)
- Search algorithm efficiency (will optimize based on performance during testing)

## Quality Validation

### Acceptance Criteria for New Features:

**Due Dates:**
- AC-001: Users can add due dates to new tasks in YYYY-MM-DD format
- AC-002: Users can update existing tasks to add due dates
- AC-003: Tasks with due dates display the date in the list view
- AC-004: Overdue tasks are marked with "OVERDUE" label
- AC-005: Tasks without due dates display exactly as Basic Level

**Priorities & Tags:**
- AC-006: Users can set priority levels (High, Medium, Low) when creating/updating tasks
- AC-007: Users can add multiple tags to tasks as free-text labels
- AC-008: Priority and tags display in the task list view
- AC-009: Default priority is "Medium" for tasks without explicit priority
- AC-010: Default tags list is empty for tasks without explicit tags

**Search:**
- AC-011: Users can search across title, description, and tags
- AC-012: Search is case-insensitive
- AC-013: Search returns tasks matching any of the searchable fields
- AC-014: Search shows appropriate message when no results found

**Filter:**
- AC-015: Users can filter by status (completed/incomplete)
- AC-016: Users can filter by priority levels
- AC-017: Users can filter by due date range
- AC-018: Users can filter by specific tags
- AC-019: Multiple filters can be combined

**Sort:**
- AC-020: Users can sort by due date (earliest first)
- AC-021: Users can sort by priority (High to Low)
- AC-022: Users can sort by creation time
- AC-023: Users can sort by title
- AC-024: Default sort is by due date then priority

### Basic Functionality Validation:
- AC-025: All Basic Level functionality (Add, List, Update, Toggle, Delete) continues to work unchanged
- AC-026: Tasks created in Basic Level work seamlessly with new features
- AC-027: New tasks with extended fields work with Basic Level operations
- AC-028: Error handling remains consistent across all operations

## Decisions Needing Documentation

### Decision 1: Task Dataclass Extension
**Options:**
- A: Extend existing Task class with optional fields (default approach)
- B: Create new IntermediateTask class that inherits from Task
- C: Use composition with a metadata object

**Chosen**: A - Extend existing Task class with optional fields
**Rationale**: Maintains backward compatibility, follows the constitution's requirement for seamless handling of old and new formats, and keeps the data model simple

**Alternatives considered:**
- B: Would require complex migration logic and separate handling paths
- C: Would complicate the data model without significant benefits

### Decision 2: Default Values for New Fields
**Options:**
- A: due_date=None, priority="Medium", tags=[]
- B: due_date="", priority="", tags=[]
- C: due_date=Future date, priority="Low", tags=[]

**Chosen**: A - due_date=None, priority="Medium", tags=[]
**Rationale**: None for due_date allows easy checking for unset dates, "Medium" as default priority is reasonable, empty list for tags is appropriate default

### Decision 3: Menu Structure
**Options:**
- A: Add submenu for Intermediate features (e.g., option 7: "Advanced Features" → submenu)
- B: Add new top-level menu options with higher numbers
- C: Integrate new features into existing options

**Chosen**: B - Add new top-level menu options with higher numbers
**Rationale**: Maintains all Basic Level options with same numbers, makes new features easily discoverable, keeps menu structure simple

### Decision 4: Sorting Strategy
**Options:**
- A: Default sort by due date then priority, user can override
- B: User chooses sort method each time
- C: Remember user's last sort preference

**Chosen**: A - Default sort by due date then priority, user can override
**Rationale**: Provides intuitive default (urgent tasks first), allows user customization, doesn't require persistent preferences storage

### Decision 5: Display Enhancement
**Options:**
- A: Extend existing display format with new fields in parentheses
- B: Create new display format for tasks with extended fields
- C: Add toggle for detailed/compact view

**Chosen**: A - Extend existing display format with new fields in parentheses
**Rationale**: Maintains familiar Basic Level display, adds new information without major layout changes, keeps implementation simple