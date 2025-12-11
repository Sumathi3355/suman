import os

FILE_NAME = "todo.txt"

# Load existing tasks
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return [task.strip() for task in f.readlines()]

# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_menu():
    print("\n=== TO-DO LIST ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Clear All Tasks")
    print("5. Exit")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            if not tasks:
                print("No tasks yet. Stop being lazy.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "2":
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("Task added.")
            else:
                print("Invalid task.")

        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
                continue
            
            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Enter a valid number.")

        elif choice == "4":
            confirm = input("Are you sure? (y/n): ")
            if confirm.lower() == "y":
                tasks.clear()
                save_tasks(tasks)
                print("All tasks cleared.")

        elif choice == "5":
            print("Exiting. Now go get things done.")
            break

        else:
            print("Invalid choice.")

if _name_ == "_main_":
    main()
