from task_manager import TaskManager

def print_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

def main():

    task_manager = TaskManager()
    
    while True:

        print_menu()
        
        try:
            
            choice = input("Choose an option: ")
            
            match choice:
                case '1':
                    description = input("Enter task description: ")
                    task = task_manager.add_task(description)
                    print(f"Task added: {task}")
                case '2':
                    tasks = task_manager.get_pending_tasks()   
                    if not tasks:
                        print("No pending tasks.")
                    else:
                        for task in tasks:
                            print(task)
                case '3':
                    id = int(input("Enter task ID to complete: "))  
                    task = task_manager.complete_task(id)
                    if task:
                        print(f"Task completed: {task}")
                    else:
                        print("Task not found.")    
                case '4':
                    id = int(input("Enter task ID to delete: "))
                    task = task_manager.delete_task(id)     
                    if task:
                        print(f"Task deleted: {task}")
                    else:
                        print("Task not found.")
                case '5':
                    print("Exiting...")
                    break   
                case _:
                    print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")  

if __name__ == "__main__":
    main()