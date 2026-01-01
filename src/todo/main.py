"""
Main entry point for the Todo application.

This module contains the main application loop and integrates all components.
"""
from datetime import datetime
from .storage import TaskStorage
from .cli import (
    display_tasks, prompt_add_task, prompt_update_task, prompt_toggle_task,
    prompt_delete_task, confirm_delete, display_main_menu, get_user_choice,
    display_message, display_error, prompt_task_id, prompt_update_task_id
)
from .services.search_service import TaskSearchService
from .services.filter_service import TaskFilterService
from .services.sort_service import TaskSortService
from .services.reminders_service import RemindersService
from .services.recurrence_service import RecurrenceService


def display_intermediate_menu():
    """
    Display the intermediate features menu options.
    """
    print("\n" + "="*40)
    print("Intermediate Features Menu")
    print("="*40)
    print("7. Search Tasks")
    print("8. Filter & Sort Tasks")
    print("9. Return to Main Menu")
    print("-"*40)


def prompt_search_tasks():
    """
    Prompt user for search criteria.

    Returns:
        The search keyword entered by the user
    """
    print("\nSearch Tasks")
    keyword = input("Enter keyword to search (title, description, tags): ").strip()
    return keyword


def prompt_filter_tasks():
    """
    Prompt user for filter criteria.

    Returns:
        A tuple of (status, priority, due_date_start, due_date_end, tags) entered by the user
    """
    print("\nFilter Tasks")

    # Filter by status
    status_input = input("Filter by status (completed/incomplete, or press Enter to skip): ").strip().lower()
    status = None
    if status_input:
        if status_input in ['completed', 'done', 'yes', 'true']:
            status = True
        elif status_input in ['incomplete', 'not done', 'no', 'false']:
            status = False

    # Filter by priority
    priority_input = input("Filter by priority (High/Medium/Low, or press Enter to skip): ").strip().title()
    priority = None
    if priority_input and priority_input in ["High", "Medium", "Low"]:
        priority = priority_input

    # Filter by due date start
    due_date_start_input = input("Filter by start due date (YYYY-MM-DD, or press Enter to skip): ").strip()
    due_date_start = None
    if due_date_start_input:
        try:
            from .utils import validate_date_format
            due_date_start = validate_date_format(due_date_start_input)
        except ValueError as e:
            print(f"Error: {e}")

    # Filter by due date end
    due_date_end_input = input("Filter by end due date (YYYY-MM-DD, or press Enter to skip): ").strip()
    due_date_end = None
    if due_date_end_input:
        try:
            from .utils import validate_date_format
            due_date_end = validate_date_format(due_date_end_input)
        except ValueError as e:
            print(f"Error: {e}")

    # Filter by tags
    tags_input = input("Filter by tags (comma-separated, or press Enter to skip): ").strip()
    tags = None
    if tags_input:
        from .utils import parse_tags
        tags = parse_tags(tags_input)

    return status, priority, due_date_start, due_date_end, tags


def prompt_sort_tasks():
    """
    Prompt user for sort criteria.

    Returns:
        A tuple of (sort_by, ascending) entered by the user
    """
    print("\nSort Tasks")
    print("Sort options:")
    print("  1. Due Date (earliest first)")
    print("  2. Priority (High to Low)")
    print("  3. Creation Time (oldest first)")
    print("  4. Title (A to Z)")
    print("  5. Due Date & Priority (default)")

    sort_choice = input("Choose sort option (1-5, default 5): ").strip()

    sort_by_map = {
        "1": "due_date",
        "2": "priority",
        "3": "creation_time",
        "4": "title",
        "5": "due_date_priority"
    }

    sort_by = sort_by_map.get(sort_choice, "due_date_priority")

    ascending_input = input("Sort ascending? (y/N, default N): ").strip().lower()
    ascending = ascending_input in ['y', 'yes']

    return sort_by, ascending


def display_startup_reminders(storage: TaskStorage):
    """
    Display startup reminders for overdue, due today, and due soon tasks.

    Args:
        storage: TaskStorage instance to get tasks from
    """
    tasks = storage.get_all_tasks()
    reminders = RemindersService.get_startup_reminders(tasks)
    banner = RemindersService.format_startup_reminder_banner(reminders)

    if banner:
        print(f"\n{banner}")
        print("-" * len(banner))


def main():
    """
    Main application loop for the Todo application.
    """
    storage = TaskStorage()

    # Display startup reminders before showing the main menu
    display_startup_reminders(storage)

    print("\nWelcome to The Evolution of Todo - Advanced Features")

    while True:
        try:
            display_main_menu()
            choice = get_user_choice()

            if choice == "1":
                # Add Task
                try:
                    title, description, due_date, due_datetime, priority, tags, recurrence, is_template, parent_id = prompt_add_task()
                    if not title:
                        display_error("Task title cannot be empty.")
                        continue

                    task = storage.add_task(title, description, due_date, due_datetime, priority, tags, recurrence, is_template, parent_id)
                    display_message(f"Task '{task.title}' added successfully with ID {task.id}")
                except ValueError as e:
                    display_error(str(e))
                except Exception as e:
                    display_error(f"An error occurred while adding task: {e}")

            elif choice == "2":
                # List Tasks
                tasks = storage.get_all_tasks()
                display_tasks(tasks)

            elif choice == "3":
                # Update Task
                try:
                    task_id = prompt_update_task_id()

                    task = storage.get_task_by_id(task_id)
                    if task is None:
                        display_error("Task not found.")
                        continue

                    print(f"Current task: {task.title}")
                    if task.description:
                        print(f"Current description: {task.description}")
                    if task.due_date:
                        print(f"Current due date: {task.due_date}")
                    if task.due_datetime:
                        print(f"Current due datetime: {task.due_datetime}")
                    print(f"Current priority: {task.priority}")
                    if task.tags:
                        print(f"Current tags: {', '.join(task.tags)}")
                    if task.recurrence:
                        print(f"Current recurrence: {task.recurrence}")
                        print(f"Is template: {task.is_template}")

                    title, description, due_date, due_datetime, priority, tags, recurrence, is_template, parent_id = prompt_update_task()

                    # If no changes were made, skip update
                    if all(field is None for field in [title, description, due_date, due_datetime, priority, tags, recurrence, is_template, parent_id]):
                        display_message("No changes made.")
                        continue

                    # Handle special case for due_date - if it's "CLEAR", set to None
                    if due_date == "CLEAR":
                        due_date = None
                    elif due_date is None:
                        # If due_date is None, keep the current value
                        due_date = task.due_date

                    # Handle special case for due_datetime - if it's "CLEAR", set to None
                    if due_datetime == "CLEAR":
                        due_datetime = None
                    elif due_datetime is None:
                        # If due_datetime is None, keep the current value
                        due_datetime = task.due_datetime

                    # Handle special case for priority - if it's "Medium" but user wanted to clear, it's already handled
                    if priority is None:
                        # If priority is None, keep the current value
                        priority = task.priority

                    # Handle special case for tags - if it's [], set to empty list
                    if tags is None:
                        # If tags is None, keep the current value
                        tags = task.tags

                    # Handle special case for recurrence - if it's "CLEAR", set to None
                    if recurrence == "CLEAR":
                        recurrence = None
                        is_template = False
                    elif recurrence is None:
                        # If recurrence is None, keep the current value
                        recurrence = task.recurrence
                        is_template = task.is_template

                    # Use current values if not updated
                    if title is None:
                        title = task.title
                    if description is None:
                        description = task.description
                    if parent_id is None:
                        parent_id = task.parent_id

                    updated = storage.update_task(task_id, title, description, due_date, due_datetime, priority, tags, recurrence, is_template, parent_id)
                    if updated:
                        display_message(f"Task {task_id} updated successfully.")
                    else:
                        display_error("Failed to update task.")
                except ValueError as e:
                    display_error(str(e))
                except Exception as e:
                    display_error(f"An error occurred while updating task: {e}")

            elif choice == "4":
                # Toggle Task Completion
                try:
                    task_id = prompt_task_id("toggle completion")
                    task = storage.get_task_by_id(task_id)
                    if task is None:
                        display_error("Task not found.")
                        continue

                    # Check if this is a recurring task and handle instance generation
                    if task.recurrence and not task.is_template:
                        # This is a recurring task instance, so we need to generate a new instance
                        # when it's completed
                        toggled = storage.toggle_task_completion(task_id)
                        if toggled:
                            # Get all tasks to pass to the recurrence service
                            all_tasks = storage.get_all_tasks()
                            new_instance = RecurrenceService.handle_task_completion(task, all_tasks)

                            if new_instance:
                                # Add the new instance to storage with a new ID
                                new_task = storage.add_task(
                                    title=new_instance.title,
                                    description=new_instance.description,
                                    due_date=new_instance.due_date,
                                    due_datetime=new_instance.due_datetime,
                                    priority=new_instance.priority,
                                    tags=new_instance.tags,
                                    recurrence=new_instance.recurrence,
                                    is_template=new_instance.is_template,
                                    parent_id=new_instance.parent_id
                                )
                                display_message(f"Task {task_id} marked as completed. New instance created with ID {new_task.id}.")
                            else:
                                status = "completed" if task.completed else "incomplete"
                                display_message(f"Task {task_id} marked as {status}.")
                    else:
                        # Regular task or template task
                        toggled = storage.toggle_task_completion(task_id)
                        if toggled:
                            task = storage.get_task_by_id(task_id)
                            status = "completed" if task.completed else "incomplete"
                            display_message(f"Task {task_id} marked as {status}.")
                        else:
                            display_error("Task not found.")
                except ValueError as e:
                    display_error(str(e))
                except Exception as e:
                    display_error(f"An error occurred while toggling task: {e}")

            elif choice == "5":
                # Delete Task
                try:
                    task_id = prompt_task_id("delete")
                    task = storage.get_task_by_id(task_id)
                    if task is None:
                        display_error("Task not found.")
                        continue

                    if confirm_delete():
                        deleted = storage.delete_task(task_id)
                        if deleted:
                            display_message(f"Task {task_id} deleted successfully.")
                        else:
                            display_error("Failed to delete task.")
                    else:
                        display_message("Deletion cancelled.")
                except Exception as e:
                    display_error(f"An error occurred while deleting task: {e}")

            elif choice == "6":
                # Search & Filter Tasks
                try:
                    print("\nSearch & Filter Tasks")
                    print("1. Search Tasks")
                    print("2. Filter & Sort Tasks")
                    print("3. Back to Main Menu")

                    sub_choice = input("Enter your choice (1-3): ").strip()

                    if sub_choice == "1":
                        # Search Tasks
                        keyword = prompt_search_tasks()
                        all_tasks = storage.get_all_tasks()
                        search_results = TaskSearchService.search_tasks(all_tasks, keyword)
                        if search_results:
                            print(f"\nSearch results for '{keyword}':")
                            display_tasks(search_results)
                        else:
                            display_message(f"No tasks found matching '{keyword}'.")
                    elif sub_choice == "2":
                        # Filter & Sort Tasks
                        status, priority, due_date_start, due_date_end, tags = prompt_filter_tasks()

                        all_tasks = storage.get_all_tasks()
                        filtered_tasks = TaskFilterService.filter_tasks(
                            all_tasks, status, priority, due_date_start, due_date_end, tags
                        )

                        if filtered_tasks:
                            sort_by, ascending = prompt_sort_tasks()
                            sorted_tasks = TaskSortService.sort_tasks(filtered_tasks, sort_by, ascending)
                            print("\nFiltered and sorted tasks:")
                            display_tasks(sorted_tasks)
                        else:
                            display_message("No tasks match the filter criteria.")
                    elif sub_choice == "3":
                        # Back to Main Menu
                        continue
                    else:
                        display_error("Invalid choice. Please enter 1, 2, or 3.")
                except Exception as e:
                    display_error(f"An error occurred in search/filter: {e}")

            elif choice == "7":
                # Add Recurring Task
                try:
                    print("\nAdd Recurring Task")
                    title = input("Enter task title: ").strip()
                    if not title:
                        display_error("Task title cannot be empty.")
                        continue

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
                    tags = []
                    if tags_input:
                        from .utils import parse_tags
                        tags = parse_tags(tags_input)

                    # Prompt for recurrence
                    recurrence_input = input("Enter recurrence (Daily/Weekly/Monthly): ").strip().lower()
                    if recurrence_input in ["daily", "d"]:
                        recurrence = "daily"
                    elif recurrence_input in ["weekly", "w"]:
                        recurrence = "weekly"
                    elif recurrence_input in ["monthly", "m"]:
                        recurrence = "monthly"
                    else:
                        display_error("Invalid recurrence. Use Daily, Weekly, or Monthly.")
                        continue

                    # Create the recurring task template
                    template_task = storage.add_task(
                        title=title,
                        description=description,
                        due_date=due_date,
                        due_datetime=due_datetime,
                        priority=priority,
                        tags=tags,
                        recurrence=recurrence,
                        is_template=True,
                        parent_id=None
                    )

                    # Generate the first instance of the recurring task
                    from .utils import add_interval_to_datetime
                    from datetime import datetime

                    # Determine the due datetime for the first instance
                    first_instance_due_datetime = due_datetime
                    if due_datetime is None and due_date is not None:
                        # Convert date to datetime (default to 23:59 if no time specified)
                        first_instance_due_datetime = datetime.combine(due_date, datetime.max.time().replace(hour=23, minute=59))

                    if first_instance_due_datetime is None:
                        # If no due date/time was specified, use current time as a default
                        first_instance_due_datetime = datetime.now()

                    # Create the first instance task
                    first_instance = storage.add_task(
                        title=template_task.title,
                        description=template_task.description,
                        due_date=template_task.due_date,
                        due_datetime=first_instance_due_datetime,
                        priority=template_task.priority,
                        tags=template_task.tags,
                        recurrence=template_task.recurrence,
                        is_template=False,
                        parent_id=template_task.id
                    )

                    display_message(f"Recurring task '{template_task.title}' created successfully. First instance has ID {first_instance.id}")
                except ValueError as e:
                    display_error(str(e))
                except Exception as e:
                    display_error(f"An error occurred while adding recurring task: {e}")

            elif choice == "8":
                # Manage Recurrence
                try:
                    print("\nManage Recurrence")
                    print("1. Update Recurrence")
                    print("2. Disable Recurrence")
                    print("3. Back to Main Menu")

                    sub_choice = input("Enter your choice (1-3): ").strip()

                    if sub_choice == "1":
                        # Update Recurrence
                        task_id = prompt_task_id("update recurrence")
                        task = storage.get_task_by_id(task_id)
                        if task is None:
                            display_error("Task not found.")
                            continue

                        if not task.is_template:
                            display_error("Only template tasks can have recurrence updated.")
                            continue

                        recurrence_input = input("Enter new recurrence (Daily/Weekly/Monthly/None): ").strip().lower()
                        if recurrence_input in ["none", "n"]:
                            recurrence = None
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
                            display_error("Invalid recurrence. Use Daily, Weekly, Monthly, or None.")
                            continue

                        # Update the task
                        updated = storage.update_task(task_id, recurrence=recurrence, is_template=is_template)
                        if updated:
                            display_message(f"Recurrence for task {task_id} updated successfully.")
                        else:
                            display_error("Failed to update recurrence.")
                    elif sub_choice == "2":
                        # Disable Recurrence
                        task_id = prompt_task_id("disable recurrence")
                        task = storage.get_task_by_id(task_id)
                        if task is None:
                            display_error("Task not found.")
                            continue

                        if not task.is_template:
                            display_error("Only template tasks can have recurrence disabled.")
                            continue

                        # Update the task to disable recurrence
                        updated = storage.update_task(task_id, recurrence=None, is_template=False)
                        if updated:
                            display_message(f"Recurrence for task {task_id} disabled successfully.")
                        else:
                            display_error("Failed to disable recurrence.")
                    elif sub_choice == "3":
                        # Back to Main Menu
                        continue
                    else:
                        display_error("Invalid choice. Please enter 1, 2, or 3.")
                except Exception as e:
                    display_error(f"An error occurred in recurrence management: {e}")

            elif choice == "9":
                # Exit
                print("\nThank you for using The Evolution of Todo - Advanced Features")
                print("Goodbye!")
                break

            else:
                display_error("Invalid choice. Please enter a number between 1 and 9.")

        except KeyboardInterrupt:
            print("\n\nApplication interrupted. Goodbye!")
            break
        except Exception as e:
            display_error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()