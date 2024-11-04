import hashlib
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    with open('credentials.txt', 'a') as file:
        file.write(f"{username},{hashed_password}\n")
    print("Registration successful!")

def add_task(username):
    task = input("Enter task: ")
    with open(f"{username}_tasks.txt", 'a') as file:
        file.write(f"{task},False\n")  # False indicates task is not yet completed
    print("Task added!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    with open('credentials.txt', 'r') as file:
        credentials = file.readlines()

    for credential in credentials:
        user, stored_hash = credential.strip().split(',')
        if user == username and stored_hash == hashed_password:
            print("Login successful!")
            return username  # Return username to track the logged-in user
    print("Login failed. Invalid credentials.")
    return None

def view_tasks(username):
    try:
        with open(f"{username}_tasks.txt", 'r') as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks available.")
            else:
                for index, task in enumerate(tasks, start=1):
                    task_name, completed = task.strip().split(',')
                    status = "Completed" if completed == "True" else "Pending"
                    print(f"{index}. {task_name} - {status}")
    except FileNotFoundError:
        print("No tasks found.")


def mark_task_completed(username):
    view_tasks(username)
    task_no = int(input("Enter task number to mark as completed: "))

    with open(f"{username}_tasks.txt", 'r') as file:
        tasks = file.readlines()

    with open(f"{username}_tasks.txt", 'w') as file:
        for index, task in enumerate(tasks, start=1):
            task_name, completed = task.strip().split(',')
            if index == task_no:
                file.write(f"{task_name},True\n")  # Mark the task as completed
            else:
                file.write(f"{task_name},{completed}\n")
    print("Task marked as completed.")


def delete_task(username):
    view_tasks(username)
    task_no = int(input("Enter task number to delete: "))

    with open(f"{username}_tasks.txt", 'r') as file:
        tasks = file.readlines()

    with open(f"{username}_tasks.txt", 'w') as file:
        for index, task in enumerate(tasks, start=1):
            if index != task_no:
                file.write(task)
    print("Task deleted.")


def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            username = login()
            if username:
                task_manager(username)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


def task_manager(username):
    while True:
        print(f"\n--- Task Manager ({username}) ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            add_task(username)
        elif choice == '2':
            view_tasks(username)
        elif choice == '3':
            mark_task_completed(username)
        elif choice == '4':
            delete_task(username)
        elif choice == '5':
            print("Logged out.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main_menu()