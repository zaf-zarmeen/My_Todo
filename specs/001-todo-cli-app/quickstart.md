# Quickstart Guide: Todo CLI App

**Feature**: 001-todo-cli-app
**Version**: Phase 1
**Last Updated**: 2026-01-01

## Prerequisites

Before running the Todo CLI App, ensure you have:

- **Python 3.13 or higher** installed
- **UV** (Python package manager) installed

### Installing UV

If you don't have UV installed:

**Windows**:
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Linux/macOS**:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Installation

1. **Clone or navigate to the project**:
   ```bash
   cd todoapp
   ```

2. **Initialize the project** (if not already done):
   ```bash
   uv init
   ```

3. **Install dependencies** (pytest for testing):
   ```bash
   uv add --dev pytest
   ```

4. **Verify installation**:
   ```bash
   uv run python --version
   # Should output: Python 3.13.x or higher
   ```

## Running the Application

### Start the CLI

```bash
uv run python src/cli/menu.py
```

Or create an alias in your shell:

**Bash/Zsh**:
```bash
alias todo="uv run python src/cli/menu.py"
todo
```

**Windows (PowerShell)**:
```powershell
function todo { uv run python src/cli/menu.py }
todo
```

### Expected Output

```text
========================================
         Todo CLI App
========================================

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
0. Exit

Select an option: _
```

## User Guide

### 1. Adding a Task

**Steps**:
1. Select option `1` (Add Task)
2. Enter task title when prompted (required)
3. Enter task description when prompted (optional, press Enter to skip)

**Example**:
```text
Select an option: 1

--- Add Task ---
Enter task title: Buy groceries
Enter task description (optional): Milk, eggs, and bread

✓ Task added successfully!
  ID: 1
  Title: Buy groceries
  Description: Milk, eggs, and bread
  Status: Pending
```

**Validation**:
- ❌ Empty title → "Title is required"
- ✓ Title only (no description) → Allowed
- ✓ Title + description → Allowed

### 2. Viewing All Tasks

**Steps**:
1. Select option `2` (View Tasks)

**Example Output** (with tasks):
```text
Select an option: 2

========================================
           Your Tasks
========================================

[1] Buy groceries
    Description: Milk, eggs, and bread
    Status: ⏳ Pending

[2] Call dentist
    Status: ✓ Completed

[3] Finish project report
    Description: Due next week
    Status: ⏳ Pending

========================================
Total: 3 tasks (1 completed, 2 pending)
========================================
```

**Example Output** (no tasks):
```text
Select an option: 2

No tasks found. Add your first task to get started!
```

### 3. Updating a Task

**Steps**:
1. Select option `3` (Update Task)
2. Enter task ID
3. Enter new title (or press Enter to keep current)
4. Enter new description (or press Enter to keep current)

**Example**:
```text
Select an option: 3

--- Update Task ---
Enter task ID: 1
Enter new title (press Enter to keep current): Buy groceries and household items
Enter new description (press Enter to keep current): Milk, eggs, bread, and cleaning supplies

✓ Task updated successfully!
  ID: 1
  Title: Buy groceries and household items
  Description: Milk, eggs, bread, and cleaning supplies
  Status: Pending
```

**Validation**:
- ❌ Invalid ID → "Task with ID [X] not found"
- ❌ No changes provided → "Please provide at least a title or description to update"
- ✓ Title only → Updates title, keeps description
- ✓ Description only → Updates description, keeps title
- ✓ Both → Updates both fields

### 4. Deleting a Task

**Steps**:
1. Select option `4` (Delete Task)
2. Enter task ID
3. Confirm deletion

**Example**:
```text
Select an option: 4

--- Delete Task ---
Enter task ID: 2

Are you sure you want to delete this task?
  [2] Call dentist
Confirm (y/n): y

✓ Task deleted successfully!
```

**Validation**:
- ❌ Invalid ID → "Task with ID [X] not found"
- ✓ Valid ID + confirm → Task permanently removed
- ✓ Valid ID + cancel → Operation cancelled, task kept

**Note**: Deleted task IDs are never reused. If you delete task #2, the next new task will still get ID #3 (or higher).

### 5. Marking Task Complete/Incomplete

**Steps**:
1. Select option `5` (Mark Task Complete/Incomplete)
2. Enter task ID

**Example** (marking as complete):
```text
Select an option: 5

--- Toggle Task Status ---
Enter task ID: 1

✓ Task marked as COMPLETED!
  ID: 1
  Title: Buy groceries
  Status: ✓ Completed
```

**Example** (marking back to pending):
```text
Select an option: 5

--- Toggle Task Status ---
Enter task ID: 1

✓ Task marked as PENDING!
  ID: 1
  Title: Buy groceries
  Status: ⏳ Pending
```

**Validation**:
- ❌ Invalid ID → "Task with ID [X] not found"
- ✓ Pending → Completed (toggle)
- ✓ Completed → Pending (toggle back)

### 6. Exiting the Application

**Steps**:
1. Select option `0` (Exit)

**Example**:
```text
Select an option: 0

Thank you for using Todo CLI App!
Goodbye!
```

**Note**: All tasks are lost on exit (in-memory only for Phase 1).

## Common Workflows

### Daily Task Management

```text
1. Start app → View Tasks (option 2)
2. Add new tasks for today (option 1)
3. Mark completed tasks (option 5)
4. Update task details as needed (option 3)
5. Delete irrelevant tasks (option 4)
6. Exit when done (option 0)
```

### Quick Task Entry

```text
1. Start app
2. Add Task (option 1) → Enter title only → Repeat
3. Exit (option 0)
```

### Review and Update

```text
1. Start app → View Tasks (option 2)
2. Update tasks with more details (option 3)
3. Mark progress (option 5)
4. Exit (option 0)
```

## Error Messages Reference

| Error Message | Cause | Solution |
|---------------|-------|----------|
| "Title is required" | Empty or whitespace-only title | Provide a non-empty title |
| "Task with ID [X] not found" | Invalid task ID | View tasks (option 2) to see valid IDs |
| "Please provide at least a title or description to update" | No fields provided during update | Provide title and/or description |
| "Invalid option. Please select 0-5." | Invalid menu selection | Enter a number between 0 and 5 |
| "Title must be 200 characters or less" | Title exceeds limit | Shorten the title |
| "Description must be 1000 characters or less" | Description exceeds limit | Shorten the description |

## Tips and Best Practices

**✅ DO**:
- Use descriptive titles (e.g., "Buy groceries" not "Shopping")
- Add descriptions for complex tasks
- Review tasks regularly (option 2)
- Delete completed old tasks to reduce clutter
- Mark tasks as complete immediately when done

**❌ DON'T**:
- Don't use empty titles (app will reject them)
- Don't rely on task IDs staying the same after deletions
- Don't expect data to persist after closing the app (Phase 1 limitation)

## Performance Notes

- The app handles **1000+ tasks** efficiently
- All operations complete in **< 100ms**
- No noticeable delay for user actions
- Memory usage scales linearly with number of tasks (~1KB per task)

## Troubleshooting

### App Won't Start

**Problem**: `ModuleNotFoundError` or `ImportError`

**Solution**:
```bash
# Ensure you're in the project directory
cd todoapp

# Run with uv
uv run python src/cli/menu.py
```

### Python Version Error

**Problem**: `Python 3.13+ is required`

**Solution**:
```bash
# Check your Python version
python --version

# If < 3.13, install Python 3.13+ from python.org
# Then retry with uv
uv run python src/cli/menu.py
```

### Tests Failing

**Problem**: `pytest` command not found or tests fail

**Solution**:
```bash
# Install pytest
uv add --dev pytest

# Run tests
uv run pytest

# Run specific test file
uv run pytest tests/unit/test_task_service.py
```

## Running Tests

### All Tests

```bash
uv run pytest
```

### Unit Tests Only

```bash
uv run pytest tests/unit/
```

### Integration Tests Only

```bash
uv run pytest tests/integration/
```

### Verbose Output

```bash
uv run pytest -v
```

### Coverage Report

```bash
uv add --dev pytest-cov
uv run pytest --cov=src --cov-report=html
```

## Phase 1 Limitations

**Current Limitations** (by design):
- ✗ No data persistence (tasks lost on exit)
- ✗ No file import/export
- ✗ No task search or filtering
- ✗ No categories, tags, or priorities
- ✗ No due dates or reminders
- ✗ No multi-user support
- ✗ No web or GUI interface

**Why**: Phase 1 focuses on core CRUD functionality with in-memory storage to validate the concept quickly.

**Future Phases**: Will add persistence, advanced features, and potentially GUI.

## Next Steps

After using the app:
1. **Provide feedback**: What features do you need most?
2. **Report bugs**: If something doesn't work as documented
3. **Request features**: What would make this more useful for you?

## Support

For issues or questions:
- Check this guide first
- Review error messages
- Run tests to verify functionality: `uv run pytest`
- Check the specification: `specs/001-todo-cli-app/spec.md`
- Check the implementation plan: `specs/001-todo-cli-app/plan.md`

---

**Happy task managing!** 🎯
