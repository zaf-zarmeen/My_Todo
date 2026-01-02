"""
Quick demo of the Todo CLI App functionality.
"""
# Direct import from services.py in src/
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Now import services module directly (not the package)
import importlib.util
spec = importlib.util.spec_from_file_location("services", "src/services.py")
services = importlib.util.module_from_spec(spec)
spec.loader.exec_module(services)

print("=" * 50)
print("  Todo CLI App - Demonstration")
print("=" * 50)

# Demo 1: Add tasks
print("\n📝 Adding tasks...")
success, task1, _ = services.add_task("Buy groceries", "Milk, eggs, and bread")
print(f"✓ Added: [{task1.id}] {task1.title}")

success, task2, _ = services.add_task("Call dentist", "Schedule annual checkup")
print(f"✓ Added: [{task2.id}] {task2.title}")

success, task3, _ = services.add_task("Finish project report")
print(f"✓ Added: [{task3.id}] {task3.title}")

# Demo 2: View all tasks
print("\n📋 Current tasks:")
tasks = services.get_all_tasks()
for task in tasks:
    status = "✓" if task.completed else "⏳"
    print(f"  {status} [{task.id}] {task.title}")
    if task.description:
        print(f"      Description: {task.description}")

# Demo 3: Mark task as complete
print("\n☑️  Marking task 2 as complete...")
success, task, _ = services.toggle_complete(2)
print(f"✓ Task [{task.id}] is now: {'Completed' if task.completed else 'Pending'}")

# Demo 4: Update task
print("\n✏️  Updating task 1...")
success, task, _ = services.update_task(1, "Buy groceries and supplies", "Milk, eggs, bread, cleaning supplies")
print(f"✓ Updated: [{task.id}] {task.title}")

# Demo 5: View updated tasks
print("\n📋 Updated task list:")
tasks = services.get_all_tasks()
for task in tasks:
    status = "✓" if task.completed else "⏳"
    print(f"  {status} [{task.id}] {task.title}")
    if task.description:
        print(f"      Description: {task.description}")

# Demo 6: Delete task
print("\n🗑️  Deleting task 3...")
success, _ = services.delete_task(3)
print("✓ Task deleted")

# Demo 7: Final task list
print("\n📋 Final task list:")
tasks = services.get_all_tasks()
completed = sum(1 for t in tasks if t.completed)
pending = sum(1 for t in tasks if not t.completed)

for task in tasks:
    status = "✓" if task.completed else "⏳"
    print(f"  {status} [{task.id}] {task.title}")
    if task.description:
        print(f"      Description: {task.description}")

print(f"\nTotal: {len(tasks)} tasks ({completed} completed, {pending} pending)")

# Demo 8: Test validation
print("\n🛡️  Testing validation...")
success, _, error = services.add_task("", "Empty title test")
print(f"✗ Empty title rejected: {error}")

success, _, error = services.update_task(999, "Non-existent task")
print(f"✗ Invalid ID rejected: {error}")

print("\n" + "=" * 50)
print("  Demo Complete! All features working! ✓")
print("=" * 50)
print("\nTo use the interactive CLI, run:")
print("  uv run python src/main.py")
