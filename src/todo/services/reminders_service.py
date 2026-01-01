"""
Reminders service for the Todo application.

This module provides functionality for detecting overdue tasks, due soon tasks,
and generating startup reminders for the advanced features.
"""
from datetime import datetime
from typing import List, Tuple
from ..models import Task
from ..utils import is_overdue_datetime, is_due_soon, is_due_today


class RemindersService:
    """
    Service class for handling task reminders and notifications.
    """

    @staticmethod
    def get_overdue_tasks(tasks: List[Task], current_datetime: datetime = None) -> List[Task]:
        """
        Get all tasks that are overdue based on their due_datetime.

        Args:
            tasks: List of tasks to check
            current_datetime: Current datetime for comparison (default: datetime.now())

        Returns:
            List of overdue tasks
        """
        if current_datetime is None:
            current_datetime = datetime.now()

        overdue_tasks = []
        for task in tasks:
            if is_overdue_datetime(task.due_datetime, current_datetime) and not task.completed:
                overdue_tasks.append(task)
        return overdue_tasks

    @staticmethod
    def get_due_soon_tasks(tasks: List[Task], current_datetime: datetime = None, hours: int = 2) -> List[Task]:
        """
        Get all tasks that are due soon (within specified hours) based on their due_datetime.

        Args:
            tasks: List of tasks to check
            current_datetime: Current datetime for comparison (default: datetime.now())
            hours: Number of hours to consider as "due soon" (default 2)

        Returns:
            List of tasks due soon
        """
        if current_datetime is None:
            current_datetime = datetime.now()

        due_soon_tasks = []
        for task in tasks:
            if is_due_soon(task.due_datetime, current_datetime, hours) and not task.completed:
                due_soon_tasks.append(task)
        return due_soon_tasks

    @staticmethod
    def get_due_today_tasks(tasks: List[Task], current_datetime: datetime = None) -> List[Task]:
        """
        Get all tasks that are due today based on their due_datetime.

        Args:
            tasks: List of tasks to check
            current_datetime: Current datetime for comparison (default: datetime.now())

        Returns:
            List of tasks due today
        """
        if current_datetime is None:
            current_datetime = datetime.now()

        due_today_tasks = []
        for task in tasks:
            if is_due_today(task.due_datetime, current_datetime) and not task.completed:
                due_today_tasks.append(task)
        return due_today_tasks

    @staticmethod
    def get_startup_reminders(tasks: List[Task], current_datetime: datetime = None) -> dict:
        """
        Get all startup reminder information including counts and task lists.

        Args:
            tasks: List of tasks to check
            current_datetime: Current datetime for comparison (default: datetime.now())

        Returns:
            Dictionary with reminder counts and task lists:
            {
                'overdue_count': int,
                'due_soon_count': int,
                'due_today_count': int,
                'overdue_tasks': List[Task],
                'due_soon_tasks': List[Task],
                'due_today_tasks': List[Task]
            }
        """
        if current_datetime is None:
            current_datetime = datetime.now()

        overdue_tasks = RemindersService.get_overdue_tasks(tasks, current_datetime)
        due_soon_tasks = RemindersService.get_due_soon_tasks(tasks, current_datetime, 2)
        due_today_tasks = RemindersService.get_due_today_tasks(tasks, current_datetime)

        # Filter out tasks that are already in overdue list to avoid double counting
        due_today_not_overdue = [task for task in due_today_tasks if task not in overdue_tasks]

        return {
            'overdue_count': len(overdue_tasks),
            'due_soon_count': len(due_soon_tasks),
            'due_today_count': len(due_today_not_overdue),
            'overdue_tasks': overdue_tasks,
            'due_soon_tasks': due_soon_tasks,
            'due_today_tasks': due_today_not_overdue
        }

    @staticmethod
    def format_startup_reminder_banner(reminders: dict) -> str:
        """
        Format a startup reminder banner string from reminder counts.

        Args:
            reminders: Dictionary with reminder counts from get_startup_reminders

        Returns:
            Formatted banner string
        """
        overdue_count = reminders['overdue_count']
        due_today_count = reminders['due_today_count']
        due_soon_count = reminders['due_soon_count']

        banner_parts = []
        if overdue_count > 0:
            banner_parts.append(f"{overdue_count} OVERDUE")
        if due_today_count > 0:
            banner_parts.append(f"{due_today_count} DUE TODAY")
        if due_soon_count > 0:
            banner_parts.append(f"{due_soon_count} DUE SOON")

        if banner_parts:
            return f"⚠️ REMINDERS: {' | '.join(banner_parts)}"
        else:
            return ""