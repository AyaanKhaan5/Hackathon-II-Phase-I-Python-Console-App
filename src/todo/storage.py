"""
In-memory storage for the Todo application.

This module provides CRUD operations for tasks stored in memory.
"""
from typing import List, Optional
from datetime import date, datetime
from .models import Task


class TaskStorage:
    """
    In-memory storage manager for tasks.
    Provides CRUD operations for tasks stored in a list.
    """
    def __init__(self):
        """Initialize the storage with an empty list of tasks."""
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, title: str, description: Optional[str] = None, due_date: Optional[date] = None,
                 due_datetime: Optional[datetime] = None, priority: str = "Medium",
                 tags: Optional[List[str]] = None, recurrence: Optional[str] = None,
                 is_template: bool = False, parent_id: Optional[int] = None) -> Task:
        """
        Add a new task to the storage.

        Args:
            title: The title of the task (required)
            description: The description of the task (optional)
            due_date: The due date of the task (optional)
            due_datetime: The due datetime of the task (optional)
            priority: The priority level of the task (default "Medium")
            tags: List of tags for the task (optional, default empty list)
            recurrence: Recurrence interval for recurring tasks (optional)
            is_template: Whether this is a template task (default False)
            parent_id: ID of parent template task (optional)

        Returns:
            The newly created Task object

        Raises:
            ValueError: If the title is empty or priority is invalid
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        if priority not in ["High", "Medium", "Low"]:
            raise ValueError(f"Priority must be one of 'High', 'Medium', or 'Low', got '{priority}'")

        if recurrence is not None and recurrence not in ["daily", "weekly", "monthly", "yearly"]:
            raise ValueError(f"Recurrence must be one of 'daily', 'weekly', 'monthly', 'yearly', got '{recurrence}'")

        task = Task(
            id=self._next_id,
            title=title.strip(),
            description=description,
            completed=False,
            due_date=due_date,
            due_datetime=due_datetime,
            priority=priority,
            tags=tags if tags is not None else [],
            recurrence=recurrence,
            is_template=is_template,
            parent_id=parent_id
        )
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks from storage.

        Returns:
            A list of all Task objects
        """
        return self._tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None,
                   due_date: Optional[date] = None, due_datetime: Optional[datetime] = None,
                   priority: Optional[str] = None, tags: Optional[List[str]] = None,
                   recurrence: Optional[str] = None, is_template: Optional[bool] = None,
                   parent_id: Optional[int] = None) -> bool:
        """
        Update an existing task.

        Args:
            task_id: The ID of the task to update
            title: New title for the task (optional)
            description: New description for the task (optional)
            due_date: New due date for the task (optional)
            due_datetime: New due datetime for the task (optional)
            priority: New priority for the task (optional)
            tags: New tags for the task (optional)
            recurrence: New recurrence setting for the task (optional)
            is_template: New template status for the task (optional)
            parent_id: New parent ID for the task (optional)

        Returns:
            True if the task was updated, False if the task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        if title is not None:
            if not title or not title.strip():
                raise ValueError("Task title cannot be empty")
            task.title = title.strip()

        if description is not None:
            task.description = description

        if due_date is not None:
            task.due_date = due_date

        if due_datetime is not None:
            task.due_datetime = due_datetime

        if priority is not None:
            if priority not in ["High", "Medium", "Low"]:
                raise ValueError(f"Priority must be one of 'High', 'Medium', or 'Low', got '{priority}'")
            task.priority = priority

        if tags is not None:
            task.tags = tags

        if recurrence is not None:
            if recurrence not in ["daily", "weekly", "monthly", "yearly"]:
                raise ValueError(f"Recurrence must be one of 'daily', 'weekly', 'monthly', 'yearly', got '{recurrence}'")
            task.recurrence = recurrence

        if is_template is not None:
            task.is_template = is_template

        if parent_id is not None:
            task.parent_id = parent_id

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False if the task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        self._tasks.remove(task)
        return True

    def toggle_task_completion(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            True if the task completion was toggled, False if the task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        # Check if this is a template task - templates cannot be completed directly
        if task.is_template:
            raise ValueError("Template tasks cannot be marked as completed directly")

        task.completed = not task.completed
        return True