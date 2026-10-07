tasks=["run","drink","paint"]

def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")


def remove_task(task):
    try:
        tasks.remove(task)
        print("Removed successfully")
    except ValueError:
        print("Task doesn't exist")
    


print("Welcome")
while True:
    print("\n1. Add Task")
    print("2. view Tasks")
    print("3. remove Tasks")
    print("4. quit")

    choice=input("\nEnter your choice:")

    if choice == "1":
        new_task = input("Enter new task:")
        add_task(new_task)
    elif choice == "2":
        print("Printing tasks")
        view_tasks()
    elif choice == "3":
        to_remove = input("Enter the task to remove:")
        remove_task(to_remove)
    elif choice == "4":
        print("Thank you")
        break
    else:
        print("Invalid choice")
