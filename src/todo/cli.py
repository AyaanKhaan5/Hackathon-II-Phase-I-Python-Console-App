"""
Command-line interface for the Todo application.

This module handles user input and output formatting.
"""
from typing import Optional, List
from datetime import date, datetime
from .models import Task
from .utils import is_overdue_date, is_overdue_datetime, is_due_soon, is_due_today


def display_tasks(tasks: List[Task]) -> None:
    """
    Display all tasks in a formatted list.

    Args:
        tasks: List of Task objects to display
    """
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\nYour Tasks:")
    print("-" * 100)
    for task in tasks:
        status = "[x]" if task.completed else "[ ]"
        description = task.description if task.description else ""
        # Truncate description to 50 characters if too long
        if len(description) > 50:
            description = description[:47] + "..."

        # Format due date/datetime information
        due_info = ""
        if task.due_datetime:
            # Use datetime format for advanced features
            due_info = f" (Due: {task.due_datetime.strftime('%Y-%m-%d %H:%M')}"

            # Check for overdue status
            if is_overdue_datetime(task.due_datetime, datetime.now()):
                due_info += " - OVERDUE)"
            # Check for due soon status
            elif is_due_soon(task.due_datetime, datetime.now(), 2):
                due_info += " - DUE SOON)"
            # Check for due today status
            elif is_due_today(task.due_datetime, datetime.now()):
                due_info += " - DUE TODAY)"
            else:
                due_info += ")"
        elif task.due_date:
            # Use date format for backward compatibility
            due_info = f" (Due: {task.due_date}"
            if is_overdue_date(task.due_date):
                due_info += " - OVERDUE)"
            else:
                due_info += ")"

        # Format priority information
        priority_info = f" [P:{task.priority[0]}]"  # Show first letter of priority

        # Format tags information
        tags_info = ""
        if task.tags:
            tags_info = f" [{', '.join(task.tags)}]"

        # Format recurrence information
        recurrence_info = ""
        if task.recurrence:
            if task.is_template:
                recurrence_info = f" [Template: {task.recurrence.upper()}]"
            else:
                recurrence_info = f" [🔁 {task.recurrence.upper()}]"

        # Print the task with all information
        print(f"{task.id:2d}. {status} {task.title}{due_info}{priority_info}{tags_info}{recurrence_info}")
        if description:
            print(f"    - {description}")
    print("-" * 100)


def prompt_add_task() -> tuple[str, Optional[str], Optional[date], Optional[datetime], str, Optional[List[str]], Optional[str], bool, Optional[int]]:
    """
    Prompt user for task title, description, due date, due datetime, priority, tags, and recurrence.

    Returns:
        A tuple of (title, description, due_date, due_datetime, priority, tags, recurrence, is_template, parent_id) entered by the user
    """
    print("\nAdd New Task")
    title = input("Enter task title: ").strip()

    description_input = input("Enter task description (optional, press Enter to skip): ").strip()
    description = description_input if description_input else None

    # Prompt for due date/datetime
    due_datetime_input = input("Enter due date and time (YYYY-MM-DD HH:MM, optional, press Enter to skip): ").strip()
    due_datetime = None
    due_date = None

    if due_datetime_input:
        try:
            from .utils import parse_datetime_string
            due_datetime = parse_datetime_string(due_datetime_input)
        except ValueError as e:
            print(f"Error: {e}")
            print("Falling back to date-only format...")
            # Ask for date-only format as fallback
            due_date_input = input("Enter due date (YYYY-MM-DD, optional, press Enter to skip): ").strip()
            if due_date_input:
                try:
                    from .utils import validate_date_format
                    due_date = validate_date_format(due_date_input)
                except ValueError as e:
                    print(f"Error: {e}")
                    due_date = None
    else:
        # If no datetime was entered, ask for date-only format
        due_date_input = input("Enter due date (YYYY-MM-DD, optional, press Enter to skip): ").strip()
        if due_date_input:
            try:
                from .utils import validate_date_format
                due_date = validate_date_format(due_date_input)
            except ValueError as e:
                print(f"Error: {e}")
                due_date = None

    # Prompt for priority
    priority_input = input("Enter priority (High/Medium/Low, optional, press Enter for Medium): ").strip()
    priority = "Medium"  # Default value
    if priority_input:
        try:
            from .utils import validate_priority
            priority = validate_priority(priority_input)
        except ValueError as e:
            print(f"Error: {e}")
            priority = "Medium"  # Default to Medium if invalid

    # Prompt for tags
    tags_input = input("Enter tags (comma-separated, optional, press Enter to skip): ").strip()
    tags = None
    if tags_input:
        from .utils import parse_tags
        tags = parse_tags(tags_input)

    # Prompt for recurrence
    recurrence_input = input("Enter recurrence (None/Daily/Weekly/Monthly, optional, press Enter to skip): ").strip()
    recurrence = None
    is_template = False
    parent_id = None

    if recurrence_input:
        recurrence_input = recurrence_input.lower()
        if recurrence_input in ["none", "n", ""]:
            recurrence = None
        elif recurrence_input in ["daily", "d"]:
            recurrence = "daily"
            is_template = True
        elif recurrence_input in ["weekly", "w"]:
            recurrence = "weekly"
            is_template = True
        elif recurrence_input in ["monthly", "m"]:
            recurrence = "monthly"
            is_template = True
        else:
            print(f"Invalid recurrence: {recurrence_input}. Using None.")
            recurrence = None

    return title, description, due_date, due_datetime, priority, tags, recurrence, is_template, parent_id


def prompt_update_task() -> tuple[Optional[str], Optional[str], Optional[date], Optional[datetime], Optional[str], Optional[List[str]], Optional[str], Optional[bool], Optional[int]]:
    """
    Prompt user for updated task fields.

    Returns:
        A tuple of (title, description, due_date, due_datetime, priority, tags, recurrence, is_template, parent_id) entered by the user (None if not updated)
    """
    print("\nUpdate Task")
    title_input = input("Enter new title (or press Enter to keep current): ").strip()
    title = title_input if title_input else None

    description_input = input("Enter new description (or press Enter to keep current): ").strip()
    description = description_input if description_input else None

    # Prompt for due date/datetime
    due_datetime_input = input("Enter new due date and time (YYYY-MM-DD HH:MM, or press Enter to keep current): ").strip()
    due_datetime = None
    due_date = None

    if due_datetime_input:
        if due_datetime_input.lower() == "none" or due_datetime_input.lower() == "clear":
            # Special case to clear the due datetime
            due_datetime = "CLEAR"  # Special marker to indicate clearing the datetime
        else:
            try:
                from .utils import parse_datetime_string
                due_datetime = parse_datetime_string(due_datetime_input)
            except ValueError as e:
                print(f"Error: {e}")
                print("Falling back to date-only format...")
                # Ask for date-only format as fallback
                due_date_input = input("Enter new due date (YYYY-MM-DD, or press Enter to keep current): ").strip()
                if due_date_input and due_date_input.lower() != "none" and due_date_input.lower() != "clear":
                    try:
                        from .utils import validate_date_format
                        due_date = validate_date_format(due_date_input)
                    except ValueError as e:
                        print(f"Error: {e}")
                        due_date = None
    else:
        # If no datetime was entered, ask for date-only format
        due_date_input = input("Enter new due date (YYYY-MM-DD, or press Enter to keep current): ").strip()
        if due_date_input:
            if due_date_input.lower() == "none" or due_date_input.lower() == "clear":
                due_date = "CLEAR"  # Special marker to indicate clearing the date
            else:
                try:
                    from .utils import validate_date_format
                    due_date = validate_date_format(due_date_input)
                except ValueError as e:
                    print(f"Error: {e}")
                    due_date = None

    # Prompt for priority
    priority_input = input("Enter new priority (High/Medium/Low, or press Enter to keep current): ").strip()
    priority = None  # None means don't update
    if priority_input:
        if priority_input.lower() == "none" or priority_input.lower() == "clear":
            # Special case to reset to default priority
            priority = "Medium"
        else:
            try:
                from .utils import validate_priority
                priority = validate_priority(priority_input)
            except ValueError as e:
                print(f"Error: {e}")
                priority = None

    # Prompt for tags
    tags_input = input("Enter new tags (comma-separated, or press Enter to keep current): ").strip()
    tags = None  # None means don't update
    if tags_input:
        if tags_input.lower() == "none" or tags_input.lower() == "clear":
            # Special case to clear tags
            tags = []
        else:
            from .utils import parse_tags
            tags = parse_tags(tags_input)

    # Prompt for recurrence (only for template tasks)
    recurrence_input = input("Enter new recurrence (None/Daily/Weekly/Monthly, or press Enter to keep current): ").strip()
    recurrence = None  # None means don't update
    is_template = None
    parent_id = None

    if recurrence_input:
        recurrence_input = recurrence_input.lower()
        if recurrence_input in ["none", "n"]:
            recurrence = "CLEAR"  # Special marker to indicate clearing recurrence
            is_template = False
        elif recurrence_input in ["daily", "d"]:
            recurrence = "daily"
            is_template = True
        elif recurrence_input in ["weekly", "w"]:
            recurrence = "weekly"
            is_template = True
        elif recurrence_input in ["monthly", "m"]:
            recurrence = "monthly"
            is_template = True
        else:
            print(f"Invalid recurrence: {recurrence_input}. Skipping update.")
            recurrence = None

    return title, description, due_date, due_datetime, priority, tags, recurrence, is_template, parent_id


def prompt_task_id(action: str) -> int:
    """
    Prompt user for task ID for a specific action.

    Args:
        action: The action to perform (e.g., "toggle completion", "delete", "update")

    Returns:
        The task ID entered by the user
    """
    while True:
        try:
            task_id = int(input(f"\nEnter task ID to {action}: "))
            return task_id
        except ValueError:
            print("Please enter a valid number.")


def prompt_toggle_task() -> int:
    """
    Prompt user for task ID to toggle completion status.

    Returns:
        The task ID entered by the user
    """
    return prompt_task_id("toggle completion")


def prompt_update_task_id() -> int:
    """
    Prompt user for task ID to update.

    Returns:
        The task ID entered by the user
    """
    return prompt_task_id("update")


def prompt_delete_task() -> int:
    """
    Prompt user for task ID to delete.

    Returns:
        The task ID entered by the user
    """
    while True:
        try:
            task_id = int(input("\nEnter task ID to delete: "))
            return task_id
        except ValueError:
            print("Please enter a valid number.")


def confirm_delete() -> bool:
    """
    Ask user to confirm deletion.

    Returns:
        True if user confirms deletion, False otherwise
    """
    confirmation = input("Are you sure you want to delete this task? (y/N): ").strip().lower()
    return confirmation in ['y', 'yes']


def display_main_menu() -> None:
    """
    Display the main menu options.
    """
    print("\n" + "="*40)
    print("The Evolution of Todo - Advanced Features")
    print("="*40)
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Toggle Task Completion")
    print("5. Delete Task")
    print("6. Search & Filter Tasks")
    print("7. Add Recurring Task")
    print("8. Manage Recurrence")
    print("9. Exit")
    print("-"*40)


def get_user_choice() -> str:
    """
    Get user's menu choice.

    Returns:
        The user's menu choice as a string
    """
    choice = input("Enter your choice (1-9): ").strip()
    return choice


def display_message(message: str) -> None:
    """
    Display a message to the user.

    Args:
        message: The message to display
    """
    print(f"\n{message}")


def display_error(error: str) -> None:
    """
    Display an error message to the user.

    Args:
        error: The error message to display
    """
    print(f"\nError: {error}")