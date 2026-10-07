task_list=[{"task":"run","status":"pending"},{"task":"walk","status":"done"}]

def add_task(task,status):
    task_list.append({"task":task,"status":status})
    print("New dictionary added successfully.")

def view_task():
    if len(task_list) == 0:
        print("No tasks available")
        return
    print("Task list:")
    for i in range(len(task_list)):
        print(f"{i+1}. {task_list[i]['task']} : {task_list[i]['status']}\n")

def remove_task(index):
    if index < 1 or index > len(task_list):
        print("No task with that number")
        return
    task_list.pop(index - 1)
    print("Task removed successfully")

def update_status(index, new_status):
    if index < 1 or index > len(task_list):
        print("No task with that number")
        return
    task_list[index - 1]["status"] = new_status
    print("status updated")

print("Welcome")
while True:
    print("\n1. Add Task")
    print("2. view Tasks")
    print("3. remove Tasks")
    print("4. update status")
    print("5. quit")

    choice=input("\nEnter your choice:")

    if choice == "1":
        task = input("Task name:")
        status = input("Task status:")
        add_task(task,status)
    elif choice == "2":
        view_task()
    elif choice == "3":
        try:
            index = input("Index of task to remove:")
            remove_task(int(index))
        except ValueError:
            print("Invalid index")
    elif choice == "4":
        try:
            index = input("Index of task to update:")
            new_status = input("New status:")
            update_status(int(index),new_status)
        except ValueError:
            print("Invalid index")
    elif choice == "5":
        print("Thank you")
        break
    else:
        print("Invalid choice")



