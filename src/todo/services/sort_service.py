"""
Sort service for the Todo application.

This module provides functionality for sorting tasks.
"""
from typing import List
from datetime import date
from ..models import Task


class TaskSortService:
    """Service class for sorting tasks by various criteria."""

    @staticmethod
    def sort_tasks(tasks: List[Task], sort_by: str = "due_date_priority", ascending: bool = True) -> List[Task]:
        """
        Sort tasks by specified criteria.

        Args:
            tasks: List of tasks to sort
            sort_by: Sorting criteria ('due_date', 'priority', 'creation_time', 'title', 'due_date_priority')
            ascending: Sort order (True for ascending, False for descending)

        Returns:
            List of tasks sorted according to the specified criteria
        """
        if sort_by == "due_date_priority":
            # Sort by due date first (earliest first), then by priority (Low to High for ascending)
            def sort_key(task):
                # For due date: None dates should go to the end
                due_date_key = task.due_date if task.due_date is not None else date.max
                # For priority: Low=0, Medium=1, High=2 (for ascending order: low first)
                priority_key = {"Low": 0, "Medium": 1, "High": 2}[task.priority]
                return (due_date_key, priority_key)
        elif sort_by == "due_date":
            def sort_key(task):
                # None dates go to the end
                return task.due_date if task.due_date is not None else date.max
        elif sort_by == "priority":
            def sort_key(task):
                # For ascending: Low(0), Medium(1), High(2) - low importance first
                # For descending: reverse of ascending - high importance first
                return {"Low": 0, "Medium": 1, "High": 2}[task.priority]
        elif sort_by == "creation_time":
            # Sort by ID (creation order)
            def sort_key(task):
                return task.id
        elif sort_by == "title":
            def sort_key(task):
                return task.title.lower()
        else:
            # Default to due date priority
            def sort_key(task):
                due_date_key = task.due_date if task.due_date is not None else date.max
                priority_key = {"Low": 0, "Medium": 1, "High": 2}[task.priority]
                return (due_date_key, priority_key)

        return sorted(tasks, key=sort_key, reverse=not ascending)