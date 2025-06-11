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
    