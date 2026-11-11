from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import json
from typing import List


DATA_DIR = Path.home() / ".taskflow"
DATA_FILE = DATA_DIR / "tasks.json"


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


class TaskStore:
    def __init__(self, path: Path = DATA_FILE):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _read(self) -> List[Task]:
        if not self.path.exists():
            return []
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []
        return [Task(**item) for item in data]

    def _write(self, tasks: List[Task]) -> None:
        self.path.write_text(json.dumps([asdict(task) for task in tasks], indent=2), encoding="utf-8")

    def list_tasks(self, all_tasks: bool = False) -> List[Task]:
        tasks = self._read()
        if all_tasks:
            return tasks
        return [task for task in tasks if not task.done]

    def add_task(self, title: str) -> Task:
        tasks = self._read()
        new_id = max((task.id for task in tasks), default=0) + 1
        task = Task(id=new_id, title=title.strip(), done=False)
        tasks.append(task)
        self._write(tasks)
        return task

    def complete_task(self, task_id: int) -> Task | None:
        tasks = self._read()
        for task in tasks:
            if task.id == task_id:
                task.done = True
                self._write(tasks)
                return task
        return None

    def remove_task(self, task_id: int) -> Task | None:
        tasks = self._read()
        for index, task in enumerate(tasks):
            if task.id == task_id:
                removed = tasks.pop(index)
                self._write(tasks)
                return removed
        return None

    def reset_ids(self) -> None:
        tasks = self._read()
        for new_id, task in enumerate(tasks, start=1):
            task.id = new_id
        self._write(tasks)
