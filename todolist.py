class Task:
    def __init__(self, title, description='', completed=False):
        self.title = title
        self.description = description
        self.completed = completed

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("\n===== TASK LIST =====")
            for i, task in enumerate(self.tasks, start=1):
                status = 'X' if task.completed else ' '
                print(f"{i}. [{status}] {task.title} - {task.description}")

    def update_task_status(self, task_index, completed=True):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = completed
            print(f"Task '{self.tasks[task_index - 1].title}' marked as {'completed' if completed else 'not completed'}.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Task '{deleted_task.title}' deleted.")
        else:
            print("Invalid task index.")

def main():
    todo_list = TodoList()

    while True:
        print("\n===== TODO LIST MENU =====")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            new_task = Task(title, description)
            todo_list.add_task(new_task)

        elif choice == '2':
            todo_list.list_tasks()

        elif choice == '3':
            task_index = int(input("Enter task index to mark as completed: "))
            todo_list.update_task_status(task_index)

        elif choice == '4':
            task_index = int(input("Enter task index to delete: "))
            todo_list.delete_task(task_index)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
