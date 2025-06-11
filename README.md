# MyCLI: A Simple To-Do CLI

**MyCLI** is a lightweight, terminal-based to-do list application built with [Typer](https://typer.tiangolo.com/) in Python. It demonstrates a full workflow from development, testing, and CI pipelines to packaging.

---

## 📦 Installation

1. Clone the repository

   ```bash
   git clone https://github.com/ChrisM922/mycli.git
   cd mycli
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   .\venv\Scripts\activate       # Windows PowerShell
   ```

3. Install dependencies

   ```bash
   pip install -e .
   ```

---

## 🚀 Usage

After installation, the `mycli` command is available. The commands include:

### `hello`

Greet a user by name.

```bash
mycli hello Alice
# → Hello, Alice!
```

### `add`

Add a new to-do item.

```bash
mycli add "Buy milk"
# → Added task: Buy milk
```

### `list`

List all to-do tasks (with completed status).

```bash
mycli list
# → 1. Buy milk
#   2. [x] Read book
```

### `done`

Mark a task as completed by its number.

```bash
mycli done 1
# → Marked task 1 as done.
```

### `remove`

Remove a task by its number.

```bash
mycli remove 2
# → Removed task 2: Read book
```

---

## 🔧 Configuration & Storage

* Tasks are stored in JSON format at `~/.mycli/tasks.json` by default.
* Override the location by setting the environment variable `MYCLI_STORAGE_FILE`:

  ```bash
  export MYCLI_STORAGE_FILE=/path/to/your/tasks.json
  ```

---

## 🧪 Testing

Automated tests are written with [pytest](https://pytest.org)

```bash
pytest
```

The suite covers:

* `hello`, `add`, `list`, `done`, and `remove` commands
* Empty-state handling
* Persistence in a temporary storage file via environment override

---

## 📈 Continuous Integration

A GitHub Actions workflow (`.github/workflows/ci.yml`) runs on every push and pull request:

* Installs dependencies
* Runs `pytest`

---

## 📦 Packaging & Publishing

This project uses a standard `setup.py` entry point:

```bash
pip install -e .
```

You can publish to PyPI by adding a `pyproject.toml` or extending the CI to build and upload distributions on tag.

---

## 🤝 Contributing

Contributions are welcome! To propose changes:

1. Fork the repo and create a feature branch.
2. Add tests for new behavior.
3. Submit a pull request against `main`.

Please follow the existing test-driven development style and update this README with any new commands or features.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it as you wish.
