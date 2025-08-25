import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self):
        self.filename = "tasks.json"
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except:
                return []
        return []
    
    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)
    
    def add_task(self, task_description):
        """Add a new task"""
        task = {
            "id": len(self.tasks) + 1,
            "description": task_description,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Task added: {task_description}")
    
    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("📝 No tasks found!")
            return
        
        print("\n" + "="*50)
        print("📋 YOUR TO-DO LIST")
        print("="*50)
        
        for task in self.tasks:
            status = "✅" if task["completed"] else "❌"
            print(f"{task['id']}. {status} {task['description']}")
            print(f"   Created: {task['created_at']}")
            print("-" * 30)
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                print(f"✅ Task {task_id} marked as completed!")
                return
        print(f"❌ Task {task_id} not found!")
    
    def delete_task(self, task_id):
        """Delete a task"""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                deleted_task = self.tasks.pop(i)
                # Reassign IDs
                for j, remaining_task in enumerate(self.tasks):
                    remaining_task["id"] = j + 1
                self.save_tasks()
                print(f"🗑️ Task deleted: {deleted_task['description']}")
                return
        print(f"❌ Task {task_id} not found!")
    
    def show_menu(self):
        """Display menu options"""
        print("\n" + "="*40)
        print("🎯 TO-DO LIST MANAGER")
        print("="*40)
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        print("="*40)
    
    def run(self):
        """Main application loop"""
        print("🚀 Welcome to To-Do List Manager!")
        
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == "1":
                task = input("Enter task description: ").strip()
                if task:
                    self.add_task(task)
                else:
                    print("❌ Task description cannot be empty!")
            
            elif choice == "2":
                self.view_tasks()
            
            elif choice == "3":
                try:
                    task_id = int(input("Enter task ID to complete: "))
                    self.complete_task(task_id)
                except ValueError:
                    print("❌ Please enter a valid task ID!")
            
            elif choice == "4":
                try:
                    task_id = int(input("Enter task ID to delete: "))
                    self.delete_task(task_id)
                except ValueError:
                    print("❌ Please enter a valid task ID!")
            
            elif choice == "5":
                print("👋 Thanks for using To-Do List Manager!")
                break
            
            else:
                print("❌ Invalid choice! Please select 1-5.")

# Run the application
if __name__ == "__main__":
    app = TodoApp()
    app.run()