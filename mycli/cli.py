import typer
import os
import json
from pathlib import Path

app = typer.Typer(help="A simple to-do CLI")

def get_storage_path() -> Path:
    # First look for MYCLI_STORAGE_FILE, then MYCLI_STORAGE, then default
    env_file = os.getenv("MYCLI_STORAGE_FILE") or os.getenv("MYCLI_STORAGE")
    if env_file:
        return Path(env_file)
    default_dir = Path.home() / ".mycli"
    default_dir.mkdir(parents=True, exist_ok=True)
    return default_dir / "tasks.json"

def load_tasks() -> list[dict]:
    path = get_storage_path()
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text())
        # migrate old string-list format
        if data and isinstance(data[0], str):
            return [{"text": t, "completed": False} for t in data]
        return data
    except json.JSONDecodeError:
        return []

def save_tasks(tasks: list[dict]):
    path = get_storage_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(tasks, indent=2))

@app.command()
def hello(name: str):
    """
    Say hello.
    """
    typer.echo(f"Hello, {name}!")

@app.command()
def add(task: str):
    """
    Add a to-do task.
    """
    tasks = load_tasks()
    tasks.append({"text": task, "completed": False})
    save_tasks(tasks)
    typer.echo(f"Added task: {task}")

@app.command(name="list")
def _list():
    """
    List all to-do tasks.
    """
    tasks = load_tasks()
    if not tasks:
        typer.echo("No tasks found.")
        raise typer.Exit()
    for i, task in enumerate(tasks, start=1):
        if task.get("completed"):
            typer.echo(f"{i}. [x] {task['text']}")
        else:
            typer.echo(f"{i}. {task['text']}")

@app.command()
def done(index: int):
    """
    Mark a task as done by its number.
    """
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        typer.echo(f"Error: task {index} does not exist.")
        raise typer.Exit(code=1)
    tasks[index-1]["completed"] = True
    save_tasks(tasks)
    typer.echo(f"Marked task {index} as done.")

@app.command()
def remove(index: int):
    """
    Remove a task by its number.
    """
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        typer.echo(f"Error: task {index} does not exist.")
        raise typer.Exit(code=1)
    removed_task = tasks.pop(index-1)
    save_tasks(tasks)
    typer.echo(f"Removed task: {removed_task['text']}")

if __name__ == "__main__":
    app()
