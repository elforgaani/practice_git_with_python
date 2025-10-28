# 🧠 Git Training Tasks — Todo App Project

Welcome to the **Git Training Workshop**!
This repository contains a simple Python Todo CLI app.
Your goal is to **practice Git commands, branching, merging, and collaboration** using real code changes.

---

## ⚙️ Setup Instructions

1. Clone this repository:

   ```bash
   git clone <repo-url>
   cd todo_app_python
   ```

2. Run the app:

   ```bash
   python main.py
   ```

3. (Optional) Create a new branch for your tasks:

   ```bash
   git checkout -b feature/<your-feature-name>
   ```

---

## 🧩 Project Overview

This app lets you:

- Add, list, mark, and delete tasks
- Save tasks in a `tasks.json` file

You’ll extend and improve it step by step using Git branches.

---

## 🪜 Training Roadmap

### 🟢 **Beginner Level**

| Task | Description                                                               | Suggested Branch     |
| ---- | ------------------------------------------------------------------------- | -------------------- |
| 1    | Fix the crash when `tasks.json` is empty (JSONDecodeError)                | `bugfix/empty-json`  |
| 2    | Add a new feature to **edit a task** description                          | `feature/edit-task`  |
| 3    | Add a summary showing total tasks and completed tasks count after listing | `feature/summary`    |
| 4    | Update `README.md` with instructions on how to use the app                | `docs/update-readme` |
| 5    | Change the prompt text from `"Choose:"` to `"Select an option:"`          | `chore/ui-text`      |

---

### 🟡 **Intermediate Level**

| Task | Description                                                          | Suggested Branch          |
| ---- | -------------------------------------------------------------------- | ------------------------- |
| 6    | Add due date field to each task                                      | `feature/due-date`        |
| 7    | Sort tasks: show incomplete tasks first, then completed ones         | `feature/sort-tasks`      |
| 8    | Handle invalid task indexes more gracefully when marking or deleting | `bugfix/index-error`      |
| 9    | Colorize the task list output using the `colorama` library           | `feature/color-output`    |
| 10   | Add a new command `Clear all completed tasks`                        | `feature/clear-completed` |

---

### 🔵 **Advanced Level**

| Task | Description                                               | Suggested Branch      |
| ---- | --------------------------------------------------------- | --------------------- |
| 11   | Add search functionality to find tasks by keyword         | `feature/search-task` |
| 12   | Add task priority (low, medium, high)                     | `feature/priority`    |
| 13   | Add a command to export all tasks to a `.txt` file        | `feature/export-txt`  |
| 14   | Add simple unit tests for `todo.py` using `pytest`        | `feature/tests`       |
| 15   | Refactor `TodoApp` to use a `Task` class instead of dicts | `refactor/task-class` |

---

## 🧑‍🤝‍🧑 Collaboration Challenges

| Challenge | Description                                                                                                                |
| --------- | -------------------------------------------------------------------------------------------------------------------------- |
| 1         | Two people work on the same file (`todo.py`) in different branches — intentionally create a merge conflict and resolve it. |
| 2         | Review a teammate’s pull request before merging.                                                                           |
| 3         | Create a tag for version `v1.0` after merging all beginner tasks.                                                          |
| 4         | Use `git revert` to undo a bad commit.                                                                                     |
| 5         | Use `git log`, `git diff`, and `git blame` to inspect changes.                                                             |

---

## 🏁 Completion Goals

By the end of this training, you should be comfortable with:

✅ Creating and switching branches
✅ Committing and pushing changes
✅ Merging branches and resolving conflicts
✅ Working with remote repositories
✅ Tagging and reverting changes
✅ Writing meaningful commit messages

---

### 💡 Pro Tip

Use small, meaningful commits — for example:

```bash
git add todo.py
git commit -m "Add edit task feature"
```

Keep each branch focused on **one feature or fix**.
When done, open a pull request or merge into `main`.

---

Happy coding and collaborating 🎯
