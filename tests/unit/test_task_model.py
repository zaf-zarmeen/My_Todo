"""
Unit tests for Task model.
Following TDD: These tests are written BEFORE implementation.
"""
import pytest
from src.models.task import Task


# T006: Test Task model creation with valid data
def test_task_creation_with_valid_data():
    """Given valid title and description, When creating Task, Then task should be created successfully"""
    # Given
    task_id = 1
    title = "Buy groceries"
    description = "Milk and eggs"

    # When
    task = Task(id=task_id, title=title, description=description, completed=False)

    # Then
    assert task.id == 1
    assert task.title == "Buy groceries"
    assert task.description == "Milk and eggs"
    assert task.completed is False


# T007: Test Task model with empty title validation (must fail)
def test_task_with_empty_title_should_fail():
    """Given empty title, When creating Task, Then should raise validation error"""
    # Given
    task_id = 1
    empty_title = ""
    description = "Some description"

    # When/Then
    with pytest.raises(ValueError, match="Title is required"):
        Task(id=task_id, title=empty_title, description=description, completed=False)


# T008: Test Task model with only title (description=None)
def test_task_creation_with_title_only():
    """Given only title (no description), When creating Task, Then task should be created with description=None"""
    # Given
    task_id = 1
    title = "Call dentist"

    # When
    task = Task(id=task_id, title=title, description=None, completed=False)

    # Then
    assert task.id == 1
    assert task.title == "Call dentist"
    assert task.description is None
    assert task.completed is False


# T009: Test Task model default completed=False
def test_task_default_completed_false():
    """Given new task, When creating Task, Then completed should default to False"""
    # Given
    task_id = 1
    title = "Finish project"

    # When
    task = Task(id=task_id, title=title, description=None, completed=False)

    # Then
    assert task.completed is False
