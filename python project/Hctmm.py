# todo_cli.py
import os

TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        tasks = f.read().splitlines()
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Add a new task
def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {task}")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
    else:
        print("\n📝 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Delete a task
def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Task deleted: {removed}")
    else:
        print("⚠️ Invalid task number.")

# Main loop
def main():
    while True:
        print("\n====== TO-DO LIST APP ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == "1":
            task = input("Enter task: ").strip()
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                index = int(input("Enter task number to delete: "))
                delete_task(index)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
