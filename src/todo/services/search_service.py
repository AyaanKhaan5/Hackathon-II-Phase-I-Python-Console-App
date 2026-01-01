"""
Search service for the Todo application.

This module provides functionality for searching tasks.
"""
from typing import List
from ..models import Task


class TaskSearchService:
    """Service class for searching tasks by various criteria."""

    @staticmethod
    def search_tasks(tasks: List[Task], keyword: str) -> List[Task]:
        """
        Search tasks by keyword across title, description, and tags.

        Args:
            tasks: List of tasks to search
            keyword: Keyword to search for (case-insensitive)

        Returns:
            List of tasks that match the search criteria
        """
        if not keyword:
            return tasks

        keyword_lower = keyword.lower()
        results = []

        for task in tasks:
            # Check if keyword is in title
            if keyword_lower in task.title.lower():
                if task not in results:  # Avoid duplicates
                    results.append(task)
                continue

            # Check if keyword is in description
            if task.description and keyword_lower in task.description.lower():
                if task not in results:  # Avoid duplicates
                    results.append(task)
                continue

            # Check if keyword is in tags
            for tag in task.tags:
                if keyword_lower in tag.lower():
                    if task not in results:  # Avoid duplicates
                        results.append(task)
                    break

        return results