# TaskFlow CLI

TaskFlow CLI is a simple command-line task manager for everyday planning. It helps you keep track of short tasks, mark them complete, and review your work without needing a heavy app or external service.

## Features

- Add tasks from the terminal
- List all open tasks
- Mark tasks as complete
- Remove a task
- Keep data locally in a JSON file
- Lightweight, dependency-free design

## Installation

### Using pip

```bash
pip install .
```

### From source

```bash
git clone https://github.com/aminehabbad2/taskflow-cli.git
cd taskflow-cli
python -m pip install -e .
```

## Usage

```bash
taskflow add "Write project summary"
taskflow list
taskflow done 1
taskflow remove 2
```

### Commands

- `taskflow add "Task name"` — add a new task
- `taskflow list` — show pending tasks
- `taskflow done <id>` — complete a task
- `taskflow remove <id>` — remove a task
- `taskflow all` — show all tasks including completed

## Configuration

TaskFlow stores data in:

```bash
~/.taskflow/tasks.json
```

## Example

```bash
$ taskflow add "Review README"
Added task #1: Review README

$ taskflow list
1. Review README

$ taskflow done 1
Completed task #1: Review README
```

## License

MIT
