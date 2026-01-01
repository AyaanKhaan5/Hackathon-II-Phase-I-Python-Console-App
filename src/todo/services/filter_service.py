"""
Filter service for the Todo application.

This module provides functionality for filtering tasks.
"""
from typing import List, Optional
from datetime import date
from ..models import Task


class TaskFilterService:
    """Service class for filtering tasks by various criteria."""

    @staticmethod
    def filter_tasks(tasks: List[Task],
                    status: Optional[bool] = None,
                    priority: Optional[str] = None,
                    due_date_start: Optional[date] = None,
                    due_date_end: Optional[date] = None,
                    tags: Optional[List[str]] = None) -> List[Task]:
        """
        Filter tasks by multiple criteria.

        Args:
            tasks: List of tasks to filter
            status: Filter by completion status (True for completed, False for incomplete)
            priority: Filter by priority level
            due_date_start: Filter by due date start range
            due_date_end: Filter by due date end range
            tags: Filter by specific tags

        Returns:
            List of tasks that match all filter criteria
        """
        results = tasks.copy()

        # Filter by status
        if status is not None:
            results = [task for task in results if task.completed == status]

        # Filter by priority
        if priority is not None:
            results = [task for task in results if task.priority == priority]

        # Filter by due date range
        if due_date_start is not None:
            results = [task for task in results if task.due_date and task.due_date >= due_date_start]
        if due_date_end is not None:
            results = [task for task in results if task.due_date and task.due_date <= due_date_end]

        # Filter by tags (any of the specified tags)
        if tags:
            results = [task for task in results if any(tag in task.tags for tag in tags)]

        return results