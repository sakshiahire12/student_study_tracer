import json

FILE_NAME = "tasks.json"

try:
    with open(FILE_NAME, "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

def add_task():
    task = input("Enter your study task: ")

    tasks.append({
        "task": task,
        "completed": False
    })

    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Study Tasks:")

    for i, item in enumerate(tasks, start=1):
        status = "Completed" if item["completed"] else "Pending"
        print(f"{i}. {item['task']} - {status}")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))
    except ValueError:
        print("Please enter a valid task number.")
        return

    if 1 <= number <= len(tasks):
        tasks[number - 1]["completed"] = True

        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)

        print("Task completed!")
    else:
        print("Invalid task number.")


def search_task():
    keyword = input("Enter keyword to search: ").lower()

    found = False

    for item in tasks:
        if keyword in item["task"].lower():
            print("-", item["task"])
            found = True

    if not found:
        print("No matching task found.")


def show_progress():
    if not tasks:
        print("No tasks available.")
        return

    completed = sum(1 for item in tasks if item["completed"])
    total = len(tasks)

    percentage = (completed / total) * 100

    print(f"Progress: {percentage:.1f}%")


while True:

    print("\n===== STUDENT STUDY TRACKER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Search Task")
    print("5. Show Progress")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        search_task()

    elif choice == "5":
        show_progress()

    elif choice == "6":
        print("Thank you for using Student Study Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")