def delete_task(task_list):
    if not task_list:
        print("You have no tasks to delete.")
        return

    try:
        task_num = int(input("Enter the number of the task to be deleted -> ")) - 1
        if 0 <= task_num < len(task_list):
            removed_task = task_list.pop(task_num)
            print(f"Task '{removed_task}' has been deleted.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid task number!")


def display_tasks(task_list):
    if not task_list:
        print("You currently have no tasks.")
        return

    print("Here are your tasks:")
    for i, task in enumerate(task_list, start=1):
        print(f"{i}. {task}")


def add_task(task_list):
    task = input("Enter the task description -> ").strip()
    if task:
        task_list.append(task)
        print(f"Task '{task}' has been added.")
    else:
        print("Task description cannot be empty!")


task_list = []


def menu():
    while True:
        print(
            "Welcome to your task journal. What would you like to do?"
            "\n1. Add a task."
            "\n2. View tasks."
            "\n3. Delete a task."
            "\n4. Exit"
        )
        user_input = input("(1/2/3/4) -> ")
        if user_input == '1':
            add_task(task_list)
        elif user_input == '2':
            display_tasks(task_list)
        elif user_input == '3':
            delete_task(task_list)
        elif user_input == '4':
            break
        else:
            print("Invalid choice. Please try again.")


print("----- YOUR TASK JOURNAL -----")
while True:
    in_menu = input("\nType 'menu' to open the menu or 'exit' to close the program -> ").strip().lower()
    if in_menu == 'menu':
        menu()
    elif in_menu == 'exit':
        print("Closing program...")
        break
    else:
        print("Please type 'menu' or 'exit'.")
