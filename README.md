# Todo CLI App - Phase 1

A simple command-line todo application built with Python 3.13+ and UV. Manage your tasks efficiently from the terminal with full CRUD operations and status tracking.

## Features

- ✅ **Add Tasks**: Create tasks with titles and optional descriptions
- 📋 **View Tasks**: See all your tasks with their completion status
- ✏️ **Update Tasks**: Modify task titles and descriptions
- 🗑️ **Delete Tasks**: Remove completed or unwanted tasks
- ☑️ **Toggle Status**: Mark tasks as completed or pending
- 💾 **In-Memory Storage**: Fast, lightweight task management (data resets on exit)

## Prerequisites

- **Python 3.13+** - [Download from python.org](https://www.python.org/downloads/)
- **UV** - Python package manager

### Installing UV

**Windows** (PowerShell):
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Linux/macOS**:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd todoapp
   ```

2. **Install dependencies** (UV will create virtual environment automatically):
   ```bash
   uv sync
   ```

## Running the Application

Start the Todo CLI App:

```bash
uv run python src/main.py
```

You'll see the main menu:

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

## Usage Guide

### 1. Adding a Task

```text
Select an option: 1

--- Add Task ---
Enter task title: Buy groceries
Enter task description (optional, press Enter to skip): Milk, eggs, and bread

✓ Task added successfully!
  ID: 1
  Title: Buy groceries
  Description: Milk, eggs, and bread
  Status: Pending
```

### 2. Viewing All Tasks

```text
Select an option: 2

========================================
           Your Tasks
========================================

[ ] [1] Buy groceries
    Description: Milk, eggs, and bread
    Status: ⏳ Pending

[✓] [2] Call dentist
    Status: ✓ Completed

========================================
Total: 2 tasks (1 completed, 1 pending)
========================================
```

### 3. Updating a Task

```text
Select an option: 3

--- Update Task ---
Enter task ID: 1
Enter new values (press Enter to keep current):
Enter new title: Buy groceries and household items
Enter new description: Milk, eggs, bread, and cleaning supplies

✓ Task updated successfully!
  ID: 1
  Title: Buy groceries and household items
  Description: Milk, eggs, bread, and cleaning supplies
  Status: Pending
```

### 4. Deleting a Task

```text
Select an option: 4

--- Delete Task ---
Enter task ID: 2

Are you sure you want to delete this task?
  [2] Call dentist
Confirm (y/n): y

✓ Task deleted successfully!
```

### 5. Toggling Task Status

```text
Select an option: 5

--- Toggle Task Status ---
Enter task ID: 1

✓ Task marked as COMPLETED!
  ID: 1
  Title: Buy groceries
  Status: COMPLETED
```

### 6. Exiting

```text
Select an option: 0

Thank you for using Todo CLI App!
Goodbye!
```

## Project Structure

```text
todoapp/
├── src/
│   ├── __init__.py
│   ├── main.py          # CLI interface and main loop
│   ├── models.py        # Task data model
│   └── services.py      # Business logic (CRUD operations)
├── tests/
│   ├── unit/            # Unit tests
│   └── integration/     # Integration tests
├── pyproject.toml       # Project configuration
├── README.md            # This file
└── .gitignore           # Git ignore patterns
```

## Running Tests

Run all tests:
```bash
uv run pytest
```

Run specific test file:
```bash
uv run pytest tests/unit/test_task_model.py -v
```

Run with coverage:
```bash
uv run pytest --cov=src --cov-report=html
```

## Technical Details

### Architecture

- **Models**: Task dataclass with validation
- **Services**: In-memory storage with CRUD operations
- **CLI**: Menu-driven interface with user-friendly prompts

### Data Storage

- **In-Memory**: Tasks stored in Python list (resets on exit)
- **ID Generation**: Auto-incrementing counter (IDs never reused)
- **Performance**: Handles 1000+ tasks efficiently

### Validation

- Task titles are required (non-empty)
- Task IDs must exist for update/delete/toggle operations
- Clear error messages for invalid operations

## Phase 1 Limitations

By design, this is a minimal Phase 1 implementation:

- ❌ No persistence (tasks lost on exit)
- ❌ No file import/export
- ❌ No task search or filtering
- ❌ No categories, tags, or priorities
- ❌ No due dates or reminders
- ❌ No multi-user support

These features may be added in future phases.

## Development

### Code Quality

- Python 3.13+ with type hints
- PEP 8 style guidelines
- Test-Driven Development (TDD)
- Clear separation of concerns

### Testing Approach

- Unit tests for models and services
- Integration tests for complete workflows
- Given-When-Then test structure

## Troubleshooting

### App won't start

**Error**: `ModuleNotFoundError` or `ImportError`

**Solution**:
```bash
# Ensure you're in the project directory
cd todoapp

# Reinstall dependencies
uv sync

# Run the app
uv run python src/main.py
```

### Python version error

**Error**: Python 3.13+ required

**Solution**:
```bash
# Check your Python version
python --version

# If < 3.13, install Python 3.13+ from python.org
# Then run with UV
uv run python src/main.py
```

## Contributing

This is a Phase 1 implementation following strict requirements. No additional features should be added without updating the specification.

## License

MIT License - See LICENSE file for details

## Support

For issues or questions:
1. Check this README
2. Review error messages
3. Check project specifications in `specs/001-todo-cli-app/`

---

**Built with Python 3.13+ and UV** | **Phase 1: In-Memory Console Application**
