def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append({'task': task, 'status': 'Pending'})
    print(f"Task '{task}' added successfully!")
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['task']} - {task['status']}")
    print("")
def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as done: "))
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1]['status'] = 'Completed'
            print(f"Task '{tasks[task_num - 1]['task']}' marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
def main():
    tasks = []
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()