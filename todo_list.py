import os

# Load tasks from tasks.txt file
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        tasks = [task.strip() for task in tasks]  # Clean extra spaces or newlines
    else:
        tasks = []
    return tasks

# Add a new task
def add_task(tasks):
    task = input("Enter the task: ")
    category=input("Enter the category(personal/professional): ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")
    tasks.append(f"{task} - {category} - Incomplete - Due: {due_date}")
    print(f"Task '{task}' added!")

# View all tasks
def view_tasks(tasks):
    if tasks:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("Your to-do list is empty.")

# Remove a task from the list
def remove_task(tasks):
    task_to_remove = input("Enter the task to remove: ")
    # Find the task in the list and remove it
    tasks = [task for task in tasks if task.split(" - ")[0] != task_to_remove]
    print(f"Task '{task_to_remove}' removed!")
    return tasks

# Mark a task as completed
def mark_completed(tasks):
    task_to_mark = input("Enter the task to mark as completed: ")
    for index, task in enumerate(tasks):
        if task.split(" - ")[0] == task_to_mark:
            tasks[index] = task_to_mark + " - Completed"
            print(f"Task '{task_to_mark}' marked as completed!")
            break
    else:
        print(f"Task '{task_to_mark}' not found!")

# Save the tasks back to tasks.txt file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display the menu
def display_menu():
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

# Main function to run the todo list application
def todo_list_app():
    tasks = load_tasks()  # Load tasks from the file at the start

    while True:
        display_menu()  # Show the menu
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)  # Save after adding a task
        elif choice == '3':
            tasks = remove_task(tasks)  # Remove the task and get updated list
            save_tasks(tasks)  # Save after removing a task
        elif choice == '4':
            mark_completed(tasks)
            save_tasks(tasks)  # Save after marking task as completed
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the todo list app
if __name__ == "__main__":
    todo_list_app()
