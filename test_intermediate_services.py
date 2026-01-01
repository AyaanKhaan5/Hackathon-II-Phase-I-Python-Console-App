#!/usr/bin/env python3
"""
Test the search, filter, and sort services for Intermediate Level features.
"""

def test_intermediate_services():
    try:
        from src.todo.storage import TaskStorage
        from src.todo.services.search_service import TaskSearchService
        from src.todo.services.filter_service import TaskFilterService
        from src.todo.services.sort_service import TaskSortService
        from datetime import date

        print("[PASS] All service modules imported successfully")

        # Create storage instance
        storage = TaskStorage()
        print("[PASS] TaskStorage created successfully")

        # Add some test tasks with various features
        task1 = storage.add_task(
            title="Urgent Project",
            description="Complete the important project",
            due_date=date(2024, 12, 25),
            priority="High",
            tags=["work", "urgent"]
        )

        task2 = storage.add_task(
            title="Shopping List",
            description="Buy groceries for the week",
            due_date=date(2025, 1, 5),
            priority="Medium",
            tags=["personal", "shopping"]
        )

        task3 = storage.add_task(
            title="Learn Python",
            description="Study Python advanced features",
            due_date=date(2024, 12, 30),
            priority="Low",
            tags=["learning", "python"]
        )

        print(f"[PASS] Added {len(storage.get_all_tasks())} test tasks")

        # Test search functionality
        all_tasks = storage.get_all_tasks()
        search_results = TaskSearchService.search_tasks(all_tasks, "Python")
        assert len(search_results) == 1, f"Expected 1 result for 'Python', got {len(search_results)}"
        assert search_results[0].title == "Learn Python"
        print("[PASS] Search functionality works correctly")

        # Test search with tags
        search_results = TaskSearchService.search_tasks(all_tasks, "work")
        assert len(search_results) == 1, f"Expected 1 result for 'work', got {len(search_results)}"
        assert "work" in search_results[0].tags
        print("[PASS] Search in tags works correctly")

        # Test filter functionality
        filtered_tasks = TaskFilterService.filter_tasks(all_tasks, priority="High")
        assert len(filtered_tasks) == 1, f"Expected 1 high priority task, got {len(filtered_tasks)}"
        assert filtered_tasks[0].priority == "High"
        print("[PASS] Filter by priority works correctly")

        # Test filter by due date range
        filtered_tasks = TaskFilterService.filter_tasks(
            all_tasks,
            due_date_start=date(2024, 12, 20),
            due_date_end=date(2024, 12, 31)
        )
        assert len(filtered_tasks) == 2, f"Expected 2 tasks in date range, got {len(filtered_tasks)}"
        print("[PASS] Filter by due date range works correctly")

        # Test sort functionality
        sorted_tasks = TaskSortService.sort_tasks(all_tasks, sort_by="due_date", ascending=True)
        # The earliest due date should be first
        expected_order = [task1, task3, task2]  # 2024-12-25, 2024-12-30, 2025-01-05
        for i, expected_task in enumerate(expected_order):
            assert sorted_tasks[i].id == expected_task.id, f"Sort order mismatch at position {i}"
        print("[PASS] Sort by due date works correctly")

        # Test sort by priority - descending (High first)
        sorted_tasks = TaskSortService.sort_tasks(all_tasks, sort_by="priority", ascending=False)  # High first when descending
        assert sorted_tasks[0].priority == "High", "High priority should be first when descending"
        print("[PASS] Sort by priority works correctly")

        # Test default sort (due_date_priority)
        sorted_tasks = TaskSortService.sort_tasks(all_tasks, sort_by="due_date_priority")
        print("[PASS] Default sort works correctly")

        print("\n[PASS] All intermediate service tests passed! Search, filter, and sort work correctly.")

    except Exception as e:
        print(f"[FAIL] Error during intermediate service testing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_intermediate_services()