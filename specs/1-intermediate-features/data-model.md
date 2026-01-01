# Data Model: Intermediate Features for Todo Application

**Feature**: Intermediate Features for "The Evolution of Todo"
**Date**: 2025-12-30

## Entity: Task

**Description**: Extended task entity that maintains all Basic Level functionality while adding Intermediate Level features.

### Fields

| Field | Type | Default | Constraints | Basic Level Behavior | Intermediate Behavior |
|-------|------|---------|-------------|---------------------|----------------------|
| id | int | Auto-incrementing | Must be unique, positive integer | Required, auto-assigned | Unchanged |
| title | str | None | Required, non-empty after strip() | Required, validates on creation/update | Unchanged |
| description | Optional[str] | None | Optional string | Optional, can be None | Unchanged |
| completed | bool | False | Boolean value | Required, default False | Unchanged |
| due_date | Optional[date] | None | Valid date in YYYY-MM-DD format or None | Treated as None (no due date) | Full functionality |
| priority | str | "Medium" | One of "High", "Medium", "Low" | Treated as "Medium" | Full functionality |
| tags | List[str] | [] | List of non-empty strings | Treated as empty list | Full functionality |

### Validation Rules

1. **Due Date Validation**:
   - Format must be YYYY-MM-DD (e.g., "2025-12-31")
   - Must be a valid calendar date
   - None is allowed (no due date)

2. **Priority Validation**:
   - Must be one of: "High", "Medium", "Low" (case-sensitive)
   - Default is "Medium" if not specified
   - Case-insensitive input accepted but stored in canonical form

3. **Tags Validation**:
   - List of strings, each string must be non-empty after strip()
   - Duplicates should be removed
   - Each tag should be stripped of leading/trailing whitespace

### State Transitions

- **Creation**: Basic Level fields required, new fields get defaults
- **Update**: Any field can be modified, validation applies to all fields
- **Completion Toggle**: Only affects `completed` field, no impact on new fields
- **Deletion**: Complete removal, no special handling for new fields

### Relationships

- **Self-relationship**: No relationships with other entities
- **Backward Compatibility**: Old tasks without new fields are treated as having default values

## Entity: Search Query

**Description**: Parameters for searching tasks

### Fields

| Field | Type | Default | Constraints |
|-------|------|---------|-------------|
| keyword | str | "" | Non-empty string for search |
| case_sensitive | bool | False | Whether search is case sensitive |

## Entity: Filter Criteria

**Description**: Parameters for filtering tasks

### Fields

| Field | Type | Default | Constraints |
|-------|------|---------|-------------|
| status | Optional[bool] | None | True for completed, False for incomplete, None for any |
| priority | Optional[str] | None | "High", "Medium", "Low", or None for any |
| due_date_start | Optional[date] | None | Start date for due date range, None for no start |
| due_date_end | Optional[date] | None | End date for due date range, None for no end |
| tags | List[str] | [] | Tags to include, empty for any |
| tags_match_all | bool | False | If true, task must have ALL tags; if false, ANY tag |

## Entity: Sort Criteria

**Description**: Parameters for sorting tasks

### Fields

| Field | Type | Default | Constraints |
|-------|------|---------|-------------|
| sort_by | str | "due_date_priority" | One of: "due_date", "priority", "creation_time", "title", "due_date_priority" |
| ascending | bool | True | True for ascending, False for descending |

### Sort Behavior

1. **due_date_priority**: Sort by due date first (earliest first), then by priority (High to Low)
2. **due_date**: Sort by due date (earliest first), tasks without due dates go to end
3. **priority**: Sort by priority (High to Low to Medium)
4. **creation_time**: Sort by task ID (ascending = earliest first)
5. **title**: Sort by title alphabetically