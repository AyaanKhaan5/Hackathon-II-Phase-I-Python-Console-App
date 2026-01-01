#!/usr/bin/env python3
"""
Test backward compatibility to ensure Basic Level functionality still works.
"""

def test_backward_compatibility():
    try:
        from src.todo.storage import TaskStorage
        from datetime import date

        print("[PASS] Storage module imported successfully")

        # Create storage instance
        storage = TaskStorage()
        print("[PASS] TaskStorage created successfully")

        # Test adding a basic task (old way - without new fields)
        basic_task = storage.add_task("Basic Task", "This is a basic task without new features")
        print(f"[PASS] Basic task added: {basic_task.title}")

        # Verify the task has default values for new fields
        assert basic_task.due_date is None, "Due date should be None by default"
        assert basic_task.priority == "Medium", "Priority should be Medium by default"
        assert basic_task.tags == [], "Tags should be empty list by default"
        print("[PASS] Basic task has correct default values for new fields")

        # Test getting all tasks
        all_tasks = storage.get_all_tasks()
        assert len(all_tasks) == 1, f"Expected 1 task, got {len(all_tasks)}"
        print(f"[PASS] Retrieved {len(all_tasks)} task(s)")

        # Test updating just the basic fields (title and description)
        updated = storage.update_task(basic_task.id, "Updated Basic Task", "Updated description")
        assert updated == True, "Update should return True"

        updated_task = storage.get_task_by_id(basic_task.id)
        assert updated_task.title == "Updated Basic Task", "Title should be updated"
        assert updated_task.description == "Updated description", "Description should be updated"
        print("[PASS] Basic fields updated successfully")

        # Test toggle completion
        toggled = storage.toggle_task_completion(basic_task.id)
        assert toggled == True, "Toggle should return True"

        toggled_task = storage.get_task_by_id(basic_task.id)
        assert toggled_task.completed == True, "Task should be completed after toggle"
        print("[PASS] Task completion toggled successfully")

        # Test deleting the task
        deleted = storage.delete_task(basic_task.id)
        assert deleted == True, "Delete should return True"

        remaining_tasks = storage.get_all_tasks()
        assert len(remaining_tasks) == 0, f"Expected 0 tasks after deletion, got {len(remaining_tasks)}"
        print("[PASS] Task deleted successfully")

        print("\n[PASS] All backward compatibility tests passed! Basic Level functionality preserved.")

    except Exception as e:
        print(f"[FAIL] Error during backward compatibility testing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_backward_compatibility()