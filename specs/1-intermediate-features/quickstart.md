# Quickstart Guide: Intermediate Features Implementation

**Feature**: Intermediate Features for "The Evolution of Todo"
**Date**: 2025-12-30

## Implementation Steps

### Step 1: Extend Task Model
1. Update `src/todo/models.py` to add new fields to the Task dataclass
2. Add validation for new fields
3. Ensure backward compatibility for existing tasks

### Step 2: Update Storage Layer
1. Modify `src/todo/storage.py` to handle new fields in all operations
2. Update add_task, update_task methods to accept new parameters
3. Ensure existing methods continue to work unchanged

### Step 3: Create Service Layers
1. Create `src/todo/services/search_service.py` for search functionality
2. Create `src/todo/services/filter_service.py` for filtering functionality
3. Create `src/todo/services/sort_service.py` for sorting functionality

### Step 4: Update CLI Layer
1. Add new functions to `src/todo/cli.py` for handling new features
2. Update display_tasks() to show new fields
3. Add new menu options and input prompts
4. Maintain all existing Basic Level functionality

### Step 5: Update Main Application
1. Modify `src/todo/main.py` to include new features in the main loop
2. Ensure menu navigation works correctly
3. Test all Basic Level functionality remains unchanged

## Key Implementation Notes

### Date Handling
- Use `datetime.date.fromisoformat()` for parsing YYYY-MM-DD format
- Handle ValueError exceptions for invalid date formats
- Compare dates directly for overdue detection

### Priority Validation
- Create a constant list of valid priorities: `["High", "Medium", "Low"]`
- Validate input against this list
- Use case-insensitive matching for user input

### Tag Processing
- Split user input on commas
- Strip whitespace from each tag
- Filter out empty strings
- Remove duplicates while preserving order

### Display Format
- Extend existing display format to include new fields
- Show due date in parentheses if present
- Show priority as [H], [M], [L] format
- Show tags in brackets: [tag1, tag2]
- Mark overdue tasks with "OVERDUE" indicator

## Testing Strategy

### Before Implementation
1. Test all Basic Level functionality works correctly
2. Verify existing tests pass
3. Create backup of working Basic Level code

### During Implementation
1. Implement one feature at a time
2. Test backward compatibility after each change
3. Verify new functionality works as expected

### After Implementation
1. Test all Basic Level functionality still works
2. Test all new Intermediate Level features
3. Test combination of features (search + filter + sort)
4. Test edge cases and error conditions