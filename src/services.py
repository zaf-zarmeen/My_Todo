"""
Task service - Business logic for task management.
In-memory storage with CRUD operations.
"""
from typing import Tuple, Optional, List
from src.models import Task


# In-memory storage
tasks: List[Task] = []
next_id: int = 1


def add_task(title: str, description: str | None = None) -> Tuple[bool, Optional[Task], Optional[str]]:
    """
    Add a new task with title and optional description.

    Args:
        title: Task title (required)
        description: Task description (optional)

    Returns:
        Tuple of (success, task, error_message)
    """
    global next_id

    # Validate title
    if not title or title.strip() == "":
        return (False, None, "Title is required")

    # Create task
    try:
        task = Task(
            id=next_id,
            title=title.strip(),
            description=description.strip() if description else None,
            completed=False
        )
        tasks.append(task)
        next_id += 1
        return (True, task, None)
    except ValueError as e:
        return (False, None, str(e))


def get_all_tasks() -> List[Task]:
    """
    Get all tasks.

    Returns:
        List of all tasks
    """
    return tasks.copy()


def get_task_by_id(task_id: int) -> Optional[Task]:
    """
    Find task by ID.

    Args:
        task_id: Task ID to find

    Returns:
        Task if found, None otherwise
    """
    for task in tasks:
        if task.id == task_id:
            return task
    return None


def update_task(task_id: int, title: str | None = None, description: str | None = None) -> Tuple[bool, Optional[Task], Optional[str]]:
    """
    Update task title and/or description.

    Args:
        task_id: ID of task to update
        title: New title (optional)
        description: New description (optional)

    Returns:
        Tuple of (success, task, error_message)
    """
    # Validate at least one field provided
    if title is None and description is None:
        return (False, None, "Please provide at least a title or description to update")

    # Find task
    task = get_task_by_id(task_id)
    if not task:
        return (False, None, f"Task with ID {task_id} not found")

    # Update fields
    if title is not None:
        if not title or title.strip() == "":
            return (False, None, "Title is required")
        task.title = title.strip()

    if description is not None:
        task.description = description.strip() if description else None

    return (True, task, None)


def delete_task(task_id: int) -> Tuple[bool, Optional[str]]:
    """
    Delete task by ID.

    Args:
        task_id: ID of task to delete

    Returns:
        Tuple of (success, error_message)
    """
    task = get_task_by_id(task_id)
    if not task:
        return (False, f"Task with ID {task_id} not found")

    tasks.remove(task)
    # Note: next_id is NOT decremented - IDs are never reused
    return (True, None)


def toggle_complete(task_id: int) -> Tuple[bool, Optional[Task], Optional[str]]:
    """
    Toggle task completion status.

    Args:
        task_id: ID of task to toggle

    Returns:
        Tuple of (success, task, error_message)
    """
    task = get_task_by_id(task_id)
    if not task:
        return (False, None, f"Task with ID {task_id} not found")

    task.completed = not task.completed
    return (True, task, None)


def reset_storage() -> None:
    """Reset storage for testing purposes."""
    global tasks, next_id
    tasks = []
    next_id = 1
