# Data Model: Advanced Todo Features

## Task Entity

### Fields
- **id**: int - Unique identifier for the task (primary key)
- **description**: str - User-provided task description
- **completed**: bool - Whether the task is completed (default: False)
- **due_datetime**: datetime | None - Due date and time in YYYY-MM-DD HH:MM format (default: None)
- **recurrence**: str | None - Recurrence interval ("daily", "weekly", "monthly", "yearly") (default: None)
- **is_template**: bool - Whether this task is a recurrence template (default: False)
- **parent_id**: int | None - ID of parent template task for generated instances (default: None)

### Validation Rules
- **due_datetime**: Must be a valid datetime object or None
- **recurrence**: Must be one of ["daily", "weekly", "monthly", "yearly"] when not None
- **is_template**: Only True when recurrence is not None
- **parent_id**: Must reference an existing task ID when not None
- **recurrence constraints**: Template tasks cannot be marked complete (only instances)

### State Transitions
- **New Task**: id, description, completed=False, all other fields None/default
- **Recurring Task**: Set recurrence to interval, is_template=True, parent_id=None
- **Instance Generation**: Copy template, set is_template=False, parent_id to template ID, update due_datetime
- **Completion**: Set completed=True (for instances) or mark as disabled (for templates)

## RecurringTemplate Entity (Specialized Task)

### Characteristics
- **is_template**: True
- **recurrence**: Not None (one of the allowed intervals)
- **parent_id**: Always None (templates don't have parents)
- **Behavior**: Cannot be marked complete directly; serves as source for instances

## RecurringInstance Entity (Specialized Task)

### Characteristics
- **is_template**: False
- **recurrence**: Inherited from parent template
- **parent_id**: References parent template task ID
- **Behavior**: Can be marked complete, triggers new instance generation

## Relationships
- **One-to-Many**: RecurringTemplate → RecurringInstances (via parent_id reference)
- **Self-Reference**: RecurringInstance → RecurringTemplate (via parent_id)

## Backward Compatibility
- **Existing Tasks**: All new fields have safe defaults that preserve existing behavior
- **No Due Date**: due_datetime=None behaves identically to original tasks
- **No Recurrence**: recurrence=None behaves identically to original tasks
- **No Template**: is_template=False behaves identically to original tasks
- **No Parent**: parent_id=None behaves identically to original tasks