from typer.testing import CliRunner
import json
from pathlib import Path
from mycli.cli import app


runner = CliRunner()


def test_hello():
    result = runner.invoke(app, ["hello", "World"])
    assert result.exit_code == 0
    assert "Hello, World!" in result.output


def test_add():
    result = runner.invoke(app, ["add", "Buy milk"])
    assert result.exit_code == 0
    assert "Added task: Buy milk" in result.output


def test_list_empty(tmp_path, monkeypatch):
    storage_file = tmp_path / "tasks.json"
    monkeypatch.setenv("MYCLI_STORAGE_FILE", str(storage_file))
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    assert "No tasks found." in result.output


def test_add_and_list(tmp_path, monkeypatch):
    storage_file = tmp_path / "tasks.json"
    monkeypatch.setenv("MYCLI_STORAGE_FILE", str(storage_file))
    # Add a task
    runner.invoke(app, ["add", "Do laundry"])
    # List tasks
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    assert "1. Do laundry" in result.output


def test_remove_single_task(tmp_path, monkeypatch):
    storage_file = tmp_path / "tasks.json"
    monkeypatch.setenv("MYCLI_STORAGE_FILE", str(storage_file))
    # Add a task
    runner.invoke(app, ["add", "Clean the house"])
    # Remove the task
    tasks = json.loads(storage_file.read_text())
    tasks.pop(0)  # Simulate removing the first task
    storage_file.write_text(json.dumps(tasks, indent=2))
    # List tasks
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    assert "No tasks found." in result.output


def test_mark_done(tmp_path, monkeypatch):
    storage_file = tmp_path / "tasks.json"
    monkeypatch.setenv("MYCLI_STORAGE_FILE", str(storage_file))
    # Seed a task
    runner.invoke(app, ["add", "Finish homework"])
    # Mark Task #1 as done
    result = runner.invoke(app, ["done", "1"])
    assert result.exit_code == 0
    assert "Marked task 1 as done." in result.output


def test_list_shows_complete(tmp_path, monkeypatch):
    storage_file = tmp_path / "tasks.json"
    monkeypatch.setenv("MYCLI_STORAGE_FILE", str(storage_file))
    # Add and mark a task as done
    runner.invoke(app, ["add", "Read a book"])
    runner.invoke(app, ["done", "1"])
    result = runner.invoke(app, ["list"])
    # Expect a completed mark
    assert "1. [x] Read a book" in result.stdout
