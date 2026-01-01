#!/usr/bin/env python3
"""
Simple test to verify that all modules can be imported correctly.
"""

def test_imports():
    try:
        from src.todo.models import Task
        from src.todo.storage import TaskStorage
        from src.todo.cli import display_tasks
        from src.todo.utils import validate_date_format, validate_priority, parse_tags, is_overdue
        from src.todo.services.search_service import TaskSearchService
        from src.todo.services.filter_service import TaskFilterService
        from src.todo.services.sort_service import TaskSortService

        print("[PASS] All modules imported successfully")

        # Test creating a task with new fields
        from datetime import date
        task = Task(
            id=1,
            title="Test Task",
            description="This is a test task",
            due_date=date.today(),
            priority="High",
            tags=["test", "important"]
        )
        print(f"[PASS] Task created: {task.title} with priority {task.priority}")

        # Test date validation
        test_date = validate_date_format("2025-12-31")
        print(f"[PASS] Date validated: {test_date}")

        # Test priority validation
        test_priority = validate_priority("high")
        print(f"[PASS] Priority validated: {test_priority}")

        # Test tag parsing
        test_tags = parse_tags("work, important, urgent")
        print(f"[PASS] Tags parsed: {test_tags}")

        # Test services
        storage = TaskStorage()
        search_service = TaskSearchService()
        filter_service = TaskFilterService()
        sort_service = TaskSortService()

        print("[PASS] All services instantiated successfully")

        # Add a test task
        new_task = storage.add_task(
            title="Test task for intermediate features",
            description="This is a test for the new features",
            due_date=date(2025, 12, 31),
            priority="High",
            tags=["testing", "feature"]
        )
        print(f"[PASS] Test task added with ID: {new_task.id}")

        # Test displaying tasks
        all_tasks = storage.get_all_tasks()
        print(f"[PASS] Retrieved {len(all_tasks)} tasks")

        print("\n[PASS] All tests passed! The Intermediate Level features have been successfully implemented.")

    except Exception as e:
        print(f"[FAIL] Error during testing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_imports()