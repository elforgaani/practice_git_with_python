from storage import save_tasks, load_tasks

class TodoApp:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        save_tasks(self.tasks)

    def list_tasks(self):
        for i, t in enumerate(self.tasks, start=1):
            status = "✅" if t["done"] else "❌"
            print(f"{i}. {t['task']} [{status}]")

    def mark_done(self, index):
        try:
            self.tasks[index - 1]["done"] = True
            save_tasks(self.tasks)
        except IndexError:
            print("Invalid task number")

    def delete_task(self, index):
        try:
            del self.tasks[index - 1]
            save_tasks(self.tasks)
        except IndexError:
            print("Invalid task number")
