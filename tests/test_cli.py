from typer.testing import CliRunner
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