"""
Task model - represents a todo item.
"""
from dataclasses import dataclass


@dataclass
class Task:
    """
    Represents a single todo task.

    Attributes:
        id: Unique identifier (auto-generated)
        title: Brief description of the task (required)
        description: Detailed information (optional)
        completed: Status indicator (False=Pending, True=Completed)
    """
    id: int
    title: str
    description: str | None
    completed: bool

    def __post_init__(self):
        """Validate task data after initialization."""
        if not self.title or self.title.strip() == "":
            raise ValueError("Title is required")
