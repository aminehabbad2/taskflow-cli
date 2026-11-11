from __future__ import annotations

import argparse

from .models import TaskStore


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="A lightweight CLI task manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")

    list_parser = subparsers.add_parser("list", help="List open tasks")
    list_parser.add_argument("--all", action="store_true", help="Include completed tasks")

    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("task_id", type=int, help="Task ID to mark complete")

    remove_parser = subparsers.add_parser("remove", help="Remove a task")
    remove_parser.add_argument("task_id", type=int, help="Task ID to remove")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    store = TaskStore()

    if args.command == "add":
        task = store.add_task(args.title)
        print(f"Added task #{task.id}: {task.title}")
        return

    if args.command == "list":
        tasks = store.list_tasks(all_tasks=args.all)
        if not tasks:
            print("No tasks found.")
            return
        for task in tasks:
            status = "x" if task.done else " "
            print(f"{task.id}. [{status}] {task.title}")
        return

    if args.command == "done":
        task = store.complete_task(args.task_id)
        if task is None:
            print(f"Task #{args.task_id} not found.")
            return
        print(f"Completed task #{task.id}: {task.title}")
        return

    if args.command == "remove":
        task = store.remove_task(args.task_id)
        if task is None:
            print(f"Task #{args.task_id} not found.")
            return
        store.reset_ids()
        print(f"Removed task #{task.id}: {task.title}")
        return

    parser.error("Unknown command")


if __name__ == "__main__":
    main()
