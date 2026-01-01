"""
Utility functions for the Todo application.

This module provides helper functions for date validation, priority validation,
and other common operations.
"""
from datetime import date, datetime, timedelta
from typing import List, Optional
import re


def validate_date_format(date_str: str) -> date:
    """
    Validate and parse a date string in YYYY-MM-DD format.

    Args:
        date_str: Date string in YYYY-MM-DD format

    Returns:
        Parsed date object

    Raises:
        ValueError: If the date format is invalid or the date is not a valid calendar date
    """
    try:
        # Parse the date string in ISO format (YYYY-MM-DD)
        parsed_date = date.fromisoformat(date_str)
        return parsed_date
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD")


def validate_priority(priority: str) -> str:
    """
    Validate the priority value.

    Args:
        priority: Priority value to validate

    Returns:
        Validated priority value in title case

    Raises:
        ValueError: If the priority is not one of the allowed values
    """
    allowed_priorities = ["High", "Medium", "Low"]
    priority = priority.title()  # Convert to title case (High, Medium, Low)

    if priority not in allowed_priorities:
        raise ValueError(f"Priority must be one of {', '.join(allowed_priorities)}, got '{priority}'")

    return priority


def parse_tags(tag_str: str) -> List[str]:
    """
    Parse a comma-separated string of tags.

    Args:
        tag_str: Comma-separated string of tags

    Returns:
        List of cleaned tags
    """
    if not tag_str.strip():
        return []

    # Split by comma, strip whitespace, and filter out empty strings
    tags = [tag.strip() for tag in tag_str.split(',')]
    tags = [tag for tag in tags if tag]  # Remove empty tags

    # Remove duplicates while preserving order
    unique_tags = []
    for tag in tags:
        if tag not in unique_tags:
            unique_tags.append(tag)

    return unique_tags


def is_overdue_date(task_due_date: Optional[date]) -> bool:
    """
    Check if a task's due date is in the past (overdue).

    Args:
        task_due_date: The due date of the task (can be None)

    Returns:
        True if the task is overdue, False otherwise
    """
    if task_due_date is None:
        return False

    today = date.today()
    return task_due_date < today


def parse_datetime_string(datetime_str: str) -> Optional[datetime]:
    """
    Parse a datetime string in format 'YYYY-MM-DD HH:MM' or 'YYYY-MM-DD'.

    Args:
        datetime_str: String in format 'YYYY-MM-DD HH:MM' or 'YYYY-MM-DD'

    Returns:
        datetime object or None if invalid format
    """
    if not datetime_str or not datetime_str.strip():
        return None

    datetime_str = datetime_str.strip()

    # Match YYYY-MM-DD HH:MM format
    dt_pattern = r'^(\d{4})-(\d{2})-(\d{2})(?:\s+(\d{2}):(\d{2}))?$'
    match = re.match(dt_pattern, datetime_str)

    if not match:
        raise ValueError(f"Invalid datetime format: {datetime_str}. Expected format: YYYY-MM-DD HH:MM or YYYY-MM-DD")

    year, month, day = int(match.group(1)), int(match.group(2)), int(match.group(3))

    # If time part exists, parse it
    if match.group(4) and match.group(5):
        hour, minute = int(match.group(4)), int(match.group(5))
        try:
            return datetime(year, month, day, hour, minute)
        except ValueError as e:
            raise ValueError(f"Invalid datetime values: {datetime_str}. Error: {str(e)}")
    else:
        # If no time provided, default to end of day (23:59)
        try:
            return datetime(year, month, day, 23, 59)
        except ValueError as e:
            raise ValueError(f"Invalid date values: {datetime_str}. Error: {str(e)}")


def validate_datetime_format(datetime_str: str) -> bool:
    """
    Validate if a string matches the expected datetime format.

    Args:
        datetime_str: String to validate

    Returns:
        True if valid format, False otherwise
    """
    try:
        parse_datetime_string(datetime_str)
        return True
    except ValueError:
        return False


def add_interval_to_datetime(dt: datetime, interval: str) -> datetime:
    """
    Add a recurrence interval to a datetime.

    Args:
        dt: Original datetime
        interval: One of 'daily', 'weekly', 'monthly', 'yearly'

    Returns:
        New datetime with interval added
    """
    if interval == "daily":
        return dt + timedelta(days=1)
    elif interval == "weekly":
        return dt + timedelta(weeks=1)
    elif interval == "monthly":
        # Add approximately 30 days for monthly recurrence
        # For more accurate month handling, we would need to handle month boundaries
        # but for basic functionality, adding ~30 days is sufficient
        return dt + timedelta(days=30)
    elif interval == "yearly":
        return dt + timedelta(days=365)
    else:
        raise ValueError(f"Invalid interval: {interval}. Must be 'daily', 'weekly', 'monthly', or 'yearly'")


def is_overdue_datetime(task_datetime: Optional[datetime], current_datetime: datetime) -> bool:
    """
    Check if a task is overdue based on its due datetime.

    Args:
        task_datetime: Task's due datetime or None
        current_datetime: Current datetime for comparison

    Returns:
        True if task is overdue, False otherwise
    """
    if task_datetime is None:
        return False
    return task_datetime < current_datetime


def is_due_soon(task_datetime: Optional[datetime], current_datetime: datetime, hours: int = 2) -> bool:
    """
    Check if a task is due soon (within specified hours).

    Args:
        task_datetime: Task's due datetime or None
        current_datetime: Current datetime for comparison
        hours: Number of hours to consider as "due soon" (default 2)

    Returns:
        True if task is due soon, False otherwise
    """
    if task_datetime is None:
        return False
    future_time = current_datetime + timedelta(hours=hours)
    return current_datetime <= task_datetime <= future_time


def is_due_today(task_datetime: Optional[datetime], current_datetime: datetime) -> bool:
    """
    Check if a task is due today (same date as current date).

    Args:
        task_datetime: Task's due datetime or None
        current_datetime: Current datetime for comparison

    Returns:
        True if task is due today, False otherwise
    """
    if task_datetime is None:
        return False
    return task_datetime.date() == current_datetime.date()


def adjust_for_month_boundary(dt: datetime) -> datetime:
    """
    Adjust a datetime to handle month boundary cases (e.g., Jan 31 + 1 month -> Feb 28/29).

    Args:
        dt: Original datetime

    Returns:
        Adjusted datetime that handles month boundaries properly
    """
    year = dt.year
    month = dt.month + 1
    day = dt.day
    hour = dt.hour
    minute = dt.minute

    # Handle year overflow
    if month > 12:
        year += 1
        month = 1

    # Handle day overflow for months with fewer days
    # Use a loop to adjust the day until we get a valid date
    while True:
        try:
            # Try to create the date
            new_dt = datetime(year, month, day, hour, minute)
            return new_dt
        except ValueError:
            # Day is invalid for this month, decrement and try again
            day -= 1
            if day <= 0:
                # If we can't find a valid day, use the last day of the month
                if month in [1, 3, 5, 7, 8, 10, 12]:
                    day = 31
                elif month in [4, 6, 9, 11]:
                    day = 30
                else:  # February
                    # Check for leap year
                    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                        day = 29
                    else:
                        day = 28
                return datetime(year, month, day, hour, minute)