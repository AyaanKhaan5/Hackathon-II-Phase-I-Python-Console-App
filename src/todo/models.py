"""
Task model for the Todo application.

This module defines the Task data structure with type hints and proper validation.
"""
from typing import Optional, List
from dataclasses import dataclass, field
from datetime import date, datetime


@dataclass
class Task:
    """
    Represents a single todo task.

    Attributes:
        id: Unique identifier for the task (auto-incrementing)
        title: Required title of the task
        description: Optional description of the task
        completed: Boolean indicating if the task is completed (default False)
        due_date: Optional due date for the task (default None)
        due_datetime: Optional due date and time for the task (default None)
        priority: Priority level of the task (default "Medium")
        tags: List of tags associated with the task (default empty list)
        recurrence: Optional recurrence interval ("daily", "weekly", "monthly", "yearly") (default None)
        is_template: Boolean indicating if this is a recurrence template (default False)
        parent_id: Optional ID of parent template task (default None)
    """
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    due_date: Optional[date] = None
    due_datetime: Optional[datetime] = None
    priority: str = "Medium"
    tags: List[str] = field(default_factory=list)
    recurrence: Optional[str] = None
    is_template: bool = False
    parent_id: Optional[int] = None

    def __post_init__(self):
        """Validate the task after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty")
        if self.priority not in ["High", "Medium", "Low"]:
            raise ValueError(f"Priority must be one of 'High', 'Medium', or 'Low', got '{self.priority}'")
        if self.recurrence is not None and self.recurrence not in ["daily", "weekly", "monthly", "yearly"]:
            raise ValueError(f"Recurrence must be one of 'daily', 'weekly', 'monthly', 'yearly', got '{self.recurrence}'")
        if self.is_template and self.recurrence is None:
            raise ValueError("Template tasks must have a recurrence value")
        if self.parent_id is not None and self.is_template:
            raise ValueError("Template tasks cannot have a parent_id")