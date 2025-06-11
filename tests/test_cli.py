from typer.testing import CliRunner
from mycli.cli import app

runner = CliRunner()

def test_hello():
    result = runner.invoke(app, ["hello", "World"])
    assert result.exit_code == 0
    assert "Hello, World!" in result.output