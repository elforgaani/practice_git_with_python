from todo import TodoApp

def main():
    app = TodoApp()
    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Mark Task Done\n4. Delete Task\n5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            task = input("Enter task: ")
            app.add_task(task)
        elif choice == "2":
            app.list_tasks()
        elif choice == "3":
            index = int(input("Enter task number to mark done: "))
            app.mark_done(index)
        elif choice == "4":
            index = int(input("Enter task number to delete: "))
            app.delete_task(index)
        elif choice == "5":
            break

if __name__ == "__main__":
    main()

    #new Update
