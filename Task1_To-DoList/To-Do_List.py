import os

def show_menu():
    print("--------------------")
    print("1. Show To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Mark Task as Done")
    print("5. Delete Task")
    print("6. Exit")
    print("--------------------")

def show_todo_list():
    try:
        with open("Task1_To-DoList/todo.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("To-Do List is empty.")
            else:
                print("Tasks")
                for idx, task in enumerate(tasks, start=1):
                    
                    print(f"{idx}. {task.strip()}")
    except FileNotFoundError:
        print("To-Do List is empty.")

def add_task():
    task = input("Enter the task: ")
    with open("Task1_To-DoList/todo.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

def update_task():
    show_todo_list()
    try:
        task_index = int(input("Enter the task number to update: ")) - 1
        with open("Task1_To-DoList/todo.txt", "r") as file:
            tasks = file.readlines()
            if 0 <= task_index < len(tasks):
                new_task = input("Enter the updated task: ")
                tasks[task_index] = new_task + "\n"
                with open("Task1_To-DoList/todo.txt", "w") as file:
                    file.writelines(tasks)
                print("Task updated successfully.")
            else:
                print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def mark_task_done():
    show_todo_list()
    try:
        task_index = int(input("Enter the task number to mark as done: ")) - 1
        with open("Task1_To-DoList/todo.txt", "r") as file:
            tasks = file.readlines()
            if 0 <= task_index < len(tasks):
                del tasks[task_index]
                with open("Task1_To-DoList/todo.txt", "w") as file:
                    file.writelines(tasks)
                print("Task marked as done.")
            else:
                print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_task():
    show_todo_list()
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        with open("Task1_To-DoList/todo.txt", "r") as file:
            tasks = file.readlines()
            if 0 <= task_index < len(tasks):
                del tasks[task_index]
                with open("Task1_To-DoList/todo.txt", "w") as file:
                    file.writelines(tasks)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    while True:
        show_menu()

        print()
        choice = input("Enter your choice (1-6): ")
        print("--------------------")
        print()

        if choice == "1":
            show_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            mark_task_done()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Exiting To-Do List application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
