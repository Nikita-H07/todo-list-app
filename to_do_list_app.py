# To-Do List App
# By: Your Name

tasks = []

def show_menu():
    print("\n===== To-Do List App =====")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    print("==========================")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "status": "Pending"})
    print(f"✅ Task '{task}' added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found!")
        return
    print("\n📋 Your Tasks:")
    print("-" * 30)
    for i, t in enumerate(tasks):
        status = "✅" if t["status"] == "Done" else "⏳"
        print(f"{i+1}. {status} {t['task']} [{t['status']}]")
    print("-" * 30)

def mark_done():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        num = int(input("Enter task number to mark done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["status"] = "Done"
            print(f"✅ Task marked as done!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"🗑️ Task '{removed['task']}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Main Program
while True:
    show_menu()
    choice = input("Enter choice (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice!")