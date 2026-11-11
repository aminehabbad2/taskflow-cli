from __future__ import annotations

import json
from pathlib import Path

from taskflow_cli.models import TaskStore


def test_add_and_list(tmp_path, monkeypatch):
    data_path = tmp_path / "tasks.json"
    store = TaskStore(path=data_path)

    task = store.add_task("Write summary")
    assert task.id == 1
    assert task.title == "Write summary"
    assert store.list_tasks() == [task]


def test_complete_and_remove(tmp_path):
    data_path = tmp_path / "tasks.json"
    store = TaskStore(path=data_path)

    store.add_task("Plan release")
    store.complete_task(1)
    assert store.list_tasks() == []

    task = store.add_task("Ship update")
    removed = store.remove_task(task.id)
    assert removed is not None
    assert store.list_tasks() == []


def test_persists_json(tmp_path):
    data_path = tmp_path / "tasks.json"
    store = TaskStore(path=data_path)
    store.add_task("Refine README")

    payload = json.loads(data_path.read_text(encoding="utf-8"))
    assert payload[0]["title"] == "Refine README"
    assert payload[0]["done"] is False

