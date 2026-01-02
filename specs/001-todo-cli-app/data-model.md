# Data Model: Todo CLI App

**Feature**: 001-todo-cli-app
**Created**: 2026-01-01
**Status**: Approved

## Overview

The Todo CLI App uses a single entity (Task) stored in-memory using Python's built-in data structures. No database or persistence layer required for Phase 1.

## Entities

### Task

Represents a single todo item with lifecycle management (create, update, delete, toggle completion).

**Attributes**:

| Field | Type | Required | Default | Validation | Description |
|-------|------|----------|---------|------------|-------------|
| id | int | Yes | Auto-generated | Must be unique, positive integer | Unique identifier, auto-incremented |
| title | str | Yes | None | Non-empty, max 200 chars | Brief description of the task |
| description | str \| None | No | None | Max 1000 chars if provided | Detailed information about the task |
| completed | bool | Yes | False | Must be True or False | Completion status (False=Pending, True=Completed) |

**Constraints**:
- `id` must be unique across all tasks
- `id` values are never reused after deletion
- `title` cannot be empty string or whitespace-only
- `description` is optional but if provided, should be reasonable length
- `completed` can only be `True` or `False` (boolean type enforced)

**Validation Rules**:

```python
# Title validation
- Must not be None
- Must not be empty string ("")
- Must not be whitespace-only ("   ")
- Maximum length: 200 characters

# Description validation
- Can be None (optional field)
- If provided, maximum length: 1000 characters

# ID validation (for operations)
- Must be positive integer
- Must exist in the task list
```

**State Transitions**:

```text
[New Task] → completed=False (Pending)
    ↓
[Toggle] → completed=True (Completed)
    ↓
[Toggle] → completed=False (Pending)
    ...
```

Tasks can toggle between Pending and Completed states indefinitely.

## Storage Implementation

### In-Memory Storage Structure

**Primary Storage**:
```python
# Global list to store all tasks
tasks: list[dict] = []

# Global counter for ID generation
next_id: int = 1
```

**Task Representation** (as dictionary):
```python
{
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk and eggs",
    "completed": False
}
```

**Alternative**: Using Python dataclass (recommended for type safety):
```python
from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    description: str | None
    completed: bool
```

### ID Generation Strategy

**Algorithm**:
1. Maintain global counter `next_id` starting at 1
2. When creating new task, assign current `next_id` value
3. Increment `next_id` by 1
4. **Never decrement** `next_id`, even when tasks are deleted

**Example sequence**:
```text
Add task 1 → id=1, next_id=2
Add task 2 → id=2, next_id=3
Delete task 1 → next_id remains 3
Add task 3 → id=3, next_id=4 (NOT reusing id=1)
```

This ensures IDs are unique and never reused, satisfying the edge case requirement.

## Data Operations

### Create (Add Task)

**Input**:
- title: str (required)
- description: str | None (optional)

**Process**:
1. Validate title is non-empty
2. Assign `id = next_id`
3. Increment `next_id`
4. Set `completed = False`
5. Create task object
6. Append to tasks list

**Output**: Created task object or error message

### Read (View Tasks)

**Input**: None (retrieves all tasks)

**Process**:
1. Return copy of tasks list
2. If empty, return empty list

**Output**: List of all task objects

### Update (Modify Task)

**Input**:
- id: int (required)
- title: str | None (optional, update if provided)
- description: str | None (optional, update if provided)

**Process**:
1. Validate id exists in tasks list
2. Find task by id
3. If title provided, validate and update
4. If description provided, update
5. If neither provided, return error

**Output**: Updated task object or error message

### Delete (Remove Task)

**Input**:
- id: int (required)

**Process**:
1. Validate id exists in tasks list
2. Find task by id
3. Remove from tasks list
4. Do NOT decrement next_id

**Output**: Success message or error message

### Toggle Completion

**Input**:
- id: int (required)

**Process**:
1. Validate id exists in tasks list
2. Find task by id
3. Toggle: `completed = not completed`

**Output**: Updated task object with new status or error message

## Error Handling

### Validation Errors

| Error Condition | Error Message | Error Code |
|-----------------|---------------|------------|
| Empty title | "Title is required" | EMPTY_TITLE |
| Invalid ID (not found) | "Task with ID {id} not found" | TASK_NOT_FOUND |
| Update with no fields | "Please provide at least a title or description to update" | NO_UPDATE_FIELDS |
| Title too long (>200 chars) | "Title must be 200 characters or less" | TITLE_TOO_LONG |
| Description too long (>1000 chars) | "Description must be 1000 characters or less" | DESC_TOO_LONG |

**Error Handling Strategy**:
- Service functions return tuples: `(success: bool, result: Any, error: str | None)`
- CLI layer displays error messages to user
- No exceptions for expected validation errors

## Relationships

**None** - Task is a standalone entity with no relationships in Phase 1.

Future phases might add:
- Categories (one-to-many: Category → Tasks)
- Tags (many-to-many: Tasks ↔ Tags)
- Users (one-to-many: User → Tasks)

But these are explicitly out of scope for Phase 1.

## Data Constraints Summary

1. **Uniqueness**: Task IDs must be unique
2. **Non-reusability**: Deleted IDs never reused
3. **Required fields**: id, title, completed
4. **Optional fields**: description
5. **Type safety**: All fields strongly typed
6. **Length limits**: title ≤ 200 chars, description ≤ 1000 chars
7. **Immutability**: ID cannot be changed after creation
8. **State validity**: completed is always boolean

## Testing Considerations

**Unit Tests Required**:
- ✅ Task creation with valid data
- ✅ Task creation with empty title (must fail)
- ✅ Task creation with missing title (must fail)
- ✅ Task creation with only title (description=None)
- ✅ ID auto-increment behavior
- ✅ ID uniqueness across multiple tasks
- ✅ ID non-reuse after deletion
- ✅ Default completed=False on creation
- ✅ Toggle completion True → False → True

**Integration Tests Required**:
- ✅ Create 1000+ tasks, verify unique IDs
- ✅ Delete tasks, verify IDs not reused
- ✅ Mixed operations: add, update, delete, toggle
- ✅ Edge case: update non-existent task ID
- ✅ Edge case: delete non-existent task ID

## Performance Considerations

**Time Complexity**:
- Create: O(1) - append to list
- Read all: O(n) - iterate list
- Find by ID: O(n) - linear search (acceptable for Phase 1)
- Update by ID: O(n) - find + update
- Delete by ID: O(n) - find + remove
- Toggle by ID: O(n) - find + toggle

**Space Complexity**: O(n) where n = number of tasks

**Optimization Notes**:
- For Phase 1 with ~1000 tasks, O(n) linear search is acceptable
- Future phases could use dictionary for O(1) lookup: `{id: task}`
- Constitution principle II (YAGNI) says don't optimize prematurely

## Migration Path (Future Phases)

Phase 1 → Phase 2 potential changes:
- Add persistence (file or database)
- Add created_at, updated_at timestamps
- Add priority field
- Add due_date field
- Add category/tag relationships

**Backward Compatibility**: Current model is minimal, adding fields is non-breaking.
