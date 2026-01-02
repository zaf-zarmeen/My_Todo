"""
Todo CLI App - Main entry point.
Phase 1: In-memory console application.
"""
from src import services


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("         Todo CLI App")
    print("=" * 40)
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete/Incomplete")
    print("0. Exit")
    print()


def display_tasks(tasks_list):
    """Display all tasks with formatted output."""
    if not tasks_list:
        print("\nNo tasks found. Add your first task to get started!")
        return

    print("\n" + "=" * 40)
    print("           Your Tasks")
    print("=" * 40 + "\n")

    pending_count = 0
    completed_count = 0

    for task in tasks_list:
        status = "✓ Completed" if task.completed else "⏳ Pending"
        status_symbol = "[✓]" if task.completed else "[ ]"

        print(f"{status_symbol} [{task.id}] {task.title}")
        if task.description:
            print(f"    Description: {task.description}")
        print(f"    Status: {status}\n")

        if task.completed:
            completed_count += 1
        else:
            pending_count += 1

    print("=" * 40)
    print(f"Total: {len(tasks_list)} tasks ({completed_count} completed, {pending_count} pending)")
    print("=" * 40)


def handle_add_task():
    """Handle adding a new task."""
    print("\n--- Add Task ---")
    title = input("Enter task title: ").strip()
    description = input("Enter task description (optional, press Enter to skip): ").strip()

    description = description if description else None

    success, task, error = services.add_task(title, description)

    if success:
        print(f"\n✓ Task added successfully!")
        print(f"  ID: {task.id}")
        print(f"  Title: {task.title}")
        if task.description:
            print(f"  Description: {task.description}")
        print(f"  Status: Pending")
    else:
        print(f"\n✗ Error: {error}")


def handle_view_tasks():
    """Handle viewing all tasks."""
    tasks_list = services.get_all_tasks()
    display_tasks(tasks_list)


def handle_update_task():
    """Handle updating a task."""
    print("\n--- Update Task ---")

    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("\n✗ Error: Invalid ID. Please enter a number.")
        return

    print("Enter new values (press Enter to keep current):")
    title = input("Enter new title: ").strip()
    description = input("Enter new description: ").strip()

    title = title if title else None
    description = description if description else None

    success, task, error = services.update_task(task_id, title, description)

    if success:
        print(f"\n✓ Task updated successfully!")
        print(f"  ID: {task.id}")
        print(f"  Title: {task.title}")
        if task.description:
            print(f"  Description: {task.description}")
        print(f"  Status: {'Completed' if task.completed else 'Pending'}")
    else:
        print(f"\n✗ Error: {error}")


def handle_delete_task():
    """Handle deleting a task."""
    print("\n--- Delete Task ---")

    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("\n✗ Error: Invalid ID. Please enter a number.")
        return

    # Show task before deletion
    task = services.get_task_by_id(task_id)
    if task:
        print(f"\nAre you sure you want to delete this task?")
        print(f"  [{task.id}] {task.title}")
        confirm = input("Confirm (y/n): ").strip().lower()

        if confirm != 'y':
            print("\n✗ Deletion cancelled.")
            return

    success, error = services.delete_task(task_id)

    if success:
        print(f"\n✓ Task deleted successfully!")
    else:
        print(f"\n✗ Error: {error}")


def handle_toggle_complete():
    """Handle toggling task completion status."""
    print("\n--- Toggle Task Status ---")

    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("\n✗ Error: Invalid ID. Please enter a number.")
        return

    success, task, error = services.toggle_complete(task_id)

    if success:
        status = "COMPLETED" if task.completed else "PENDING"
        symbol = "✓" if task.completed else "⏳"
        print(f"\n{symbol} Task marked as {status}!")
        print(f"  ID: {task.id}")
        print(f"  Title: {task.title}")
        print(f"  Status: {status}")
    else:
        print(f"\n✗ Error: {error}")


def main_loop():
    """Main application loop."""
    print("\nWelcome to Todo CLI App!")
    print("Manage your tasks efficiently from the command line.")

    while True:
        display_menu()

        try:
            choice = input("Select an option: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nThank you for using Todo CLI App!")
            print("Goodbye!")
            break

        if choice == "1":
            handle_add_task()
        elif choice == "2":
            handle_view_tasks()
        elif choice == "3":
            handle_update_task()
        elif choice == "4":
            handle_delete_task()
        elif choice == "5":
            handle_toggle_complete()
        elif choice == "0":
            print("\nThank you for using Todo CLI App!")
            print("Goodbye!")
            break
        else:
            print("\n✗ Invalid option. Please select 0-5.")


if __name__ == "__main__":
    main_loop()
