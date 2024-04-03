
def menu():
    print("\nMenu: ")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark as done")
    print("4. Exit")

def add_tasks(tasks):
    task = input("Enter your task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks(tasks):
    print("\nTasks: ")

    """ enumerate adds a counter to list, 1 is the starting count  """
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def mark_done(tasks):
    if not tasks:
        print("No tasks to mark as done.")
        return
    
    view_tasks(tasks)
    index = int(input("Enter the task number to mark as done: ")) - 1

    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print("Task", removed_task, "marked as done and removed.")
    else:
        print("Invalid action.")


def main():
    tasks = []
    print(tasks)
    while True:
        menu()

        choice = input("Enter the number to use a menu: ")

        if choice == '1':
            add_tasks(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid action. Please inter  the number from 1 to 4.")

main()        
