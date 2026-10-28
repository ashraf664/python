class Stack:
    """تمثيل بسيط للمكدس باستخدام قائمة."""

    def __init__(self):
        # آخر عنصر في القائمة هو قمة المكدس.
        self.tasks = []

    def push(self, task):
        """إضافة مهمة إلى قمة المكدس."""
        self.tasks.append(task)

    def pop(self):
        """حذف آخر مهمة وإرجاعها، أو إرجاع None إذا كان المكدس فارغًا."""
        if self.is_empty():
            return None
        return self.tasks.pop()

    def peek(self):
        """إرجاع آخر مهمة دون حذفها، أو إرجاع None إذا كان المكدس فارغًا."""
        if self.is_empty():
            return None
        return self.tasks[-1]

    def is_empty(self):
        """التحقق مما إذا كان المكدس لا يحتوي على مهام."""
        return len(self.tasks) == 0

    def display(self):
        """عرض جميع المهام من الأحدث إلى الأقدم."""
        if self.is_empty():
            print("The stack is empty.")
            return

        print("Tasks from newest to oldest:")
        for task in reversed(self.tasks):
            print(f"- {task}")


def main():
    tasks_stack = Stack()

    while True:
        print("\n=== Task Manager Using a Stack ===")
        print("1. Add a task")
        print("2. Remove the last task")
        print("3. Show the last task")
        print("4. Show all tasks")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            task = input("Enter a task: ")
            tasks_stack.push(task)
            print("Task added.")
        elif choice == "2":
            task = tasks_stack.pop()
            if task is None:
                print("There are no tasks to remove; the stack is empty.")
            else:
                print(f"Removed the last task: {task}")
        elif choice == "3":
            task = tasks_stack.peek()
            if task is None:
                print("There are no tasks to show; the stack is empty.")
            else:
                print(f"Last task added: {task}")
        elif choice == "4":
            tasks_stack.display()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
