"""
Recurrence service for the Todo application.

This module provides functionality for managing recurring tasks, generating new instances,
and handling task completion for recurring tasks.
"""
from datetime import datetime
from typing import List, Optional
from ..models import Task
from ..utils import add_interval_to_datetime, adjust_for_month_boundary


class RecurrenceService:
    """
    Service class for handling recurring tasks and their lifecycle.
    """

    @staticmethod
    def calculate_next_due_date(task: Task, current_datetime: datetime = None) -> Optional[datetime]:
        """
        Calculate the next due date for a recurring task based on its recurrence interval.

        Args:
            task: The recurring task template
            current_datetime: Current datetime for calculation (default: task.due_datetime or datetime.now())

        Returns:
            Next due datetime for the recurring task instance
        """
        if task.recurrence is None:
            return None

        if current_datetime is None:
            if task.due_datetime:
                current_datetime = task.due_datetime
            else:
                current_datetime = datetime.now()

        next_due_date = add_interval_to_datetime(current_datetime, task.recurrence)

        # Handle month boundary cases for monthly recurrence
        if task.recurrence == "monthly":
            next_due_date = adjust_for_month_boundary(current_datetime)

        return next_due_date

    @staticmethod
    def generate_next_instance(task: Task, current_datetime: datetime = None) -> Task:
        """
        Generate a new task instance from a recurring task template.

        Args:
            task: The recurring task template
            current_datetime: Current datetime for calculation (default: datetime.now())

        Returns:
            New task instance with updated due date and parent_id
        """
        if not task.is_template:
            raise ValueError("Can only generate instances from template tasks")

        next_due_date = RecurrenceService.calculate_next_due_date(task, current_datetime)

        # Create a new task instance with the same properties as the template
        # but with updated due date and parent_id
        new_task = Task(
            id=task.id,  # This will be updated by the task manager
            title=task.title,
            description=task.description,
            completed=False,  # New instances are not completed
            due_datetime=next_due_date,
            due_date=None,  # Use due_datetime instead of due_date for advanced features
            priority=task.priority,
            tags=task.tags.copy(),  # Copy the tags
            recurrence=task.recurrence,
            is_template=False,  # New instances are not templates
            parent_id=task.id  # Link to the template task
        )

        return new_task

    @staticmethod
    def handle_task_completion(task: Task, all_tasks: List[Task]) -> Optional[Task]:
        """
        Handle task completion for recurring tasks by generating new instances if needed.

        Args:
            task: The task being completed
            all_tasks: List of all tasks (for ID management)

        Returns:
            New task instance if task was recurring and instance was generated, None otherwise
        """
        if not task.is_template and task.recurrence is not None and task.parent_id is None:
            # This is a recurring task instance that should generate a new instance
            template_task = task  # The task itself is the template in this case
            new_instance = RecurrenceService.generate_next_instance(template_task)

            # Assign a new ID to the instance (assuming auto-increment)
            if all_tasks:
                new_id = max([t.id for t in all_tasks]) + 1
            else:
                new_id = 1

            new_instance.id = new_id
            return new_instance

        elif task.is_template:
            # Template tasks should not be marked as completed directly
            raise ValueError("Template tasks cannot be marked as completed directly")

        # For non-recurring tasks, just return None
        return None

    @staticmethod
    def validate_recurrence_interval(interval: str) -> bool:
        """
        Validate if a recurrence interval is one of the allowed values.

        Args:
            interval: Recurrence interval to validate

        Returns:
            True if valid, False otherwise
        """
        return interval in ["daily", "weekly", "monthly", "yearly"]

    @staticmethod
    def create_recurring_task(title: str, description: str = None, due_datetime: datetime = None,
                            priority: str = "Medium", tags: List[str] = None,
                            recurrence: str = None) -> Task:
        """
        Create a new recurring task template.

        Args:
            title: Task title
            description: Task description
            due_datetime: Due datetime for the task
            priority: Task priority
            tags: List of tags
            recurrence: Recurrence interval

        Returns:
            New recurring task template
        """
        if recurrence and not RecurrenceService.validate_recurrence_interval(recurrence):
            raise ValueError(f"Invalid recurrence interval: {recurrence}")

        if tags is None:
            tags = []

        # Create a template task
        template_task = Task(
            id=0,  # This will be updated by the task manager
            title=title,
            description=description,
            completed=False,
            due_datetime=due_datetime,
            due_date=None,  # Use due_datetime instead of due_date for advanced features
            priority=priority,
            tags=tags,
            recurrence=recurrence,
            is_template=True,  # Mark as template
            parent_id=None  # Templates don't have parents
        )

        return template_task

    @staticmethod
    def update_recurrence(task: Task, new_recurrence: str) -> Task:
        """
        Update the recurrence setting for a template task.

        Args:
            task: The template task to update
            new_recurrence: New recurrence interval

        Returns:
            Updated task
        """
        if not task.is_template:
            raise ValueError("Can only update recurrence for template tasks")

        if new_recurrence and not RecurrenceService.validate_recurrence_interval(new_recurrence):
            raise ValueError(f"Invalid recurrence interval: {new_recurrence}")

        task.recurrence = new_recurrence
        return task

    @staticmethod
    def disable_recurrence(task: Task) -> Task:
        """
        Disable recurrence for a template task.

        Args:
            task: The template task to update

        Returns:
            Updated task with recurrence disabled
        """
        if not task.is_template:
            raise ValueError("Can only disable recurrence for template tasks")

        task.recurrence = None
        return task