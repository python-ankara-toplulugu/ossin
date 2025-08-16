# ossin

[![PyPI - Version](https://img.shields.io/pypi/v/ossin.svg)](https://pypi.org/project/ossin)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ossin.svg)](https://pypi.org/project/ossin)

What is OS's sin? 🤔 A beautiful system information utility that displays basic information about your operating system, Python environment, and platform details using Rich for stunning terminal output.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Development](#development)
- [License](#license)

## Installation

```sh
uv add ossin
```

## Usage

### Basic Usage

Display system information in the default table format:

```sh
ossin
```

### Output Formats

Choose from different output formats:

**Table format (default):**

```sh
ossin --format table
```

**Panel format:**

```sh
ossin --format panels
```

**JSON format:**

```sh
ossin --format json
```

### Options

- `--format, -f`: Output format (`table`, `panels`, `json`) [default: table]
- `--no-color`: Disable colored output
- `--version`: Show version and exit
- `--help`: Show help message

### Examples

```sh
# Display system info in table format
ossin

# Display system info in panel format
ossin --format panels

# Display system info in JSON format
ossin --format json

# Display without colors
ossin --no-color

# Show version
ossin --version

# Show help
ossin --help
```

## Features

- **Beautiful Output**: Uses Rich library for stunning terminal formatting
- **Multiple Formats**: Support for table, panel, and JSON output formats
- **System Information**: Displays OS name, version, architecture, and platform details
- **Python Environment**: Shows Python version and implementation details
- **Modern CLI**: Built with Typer for excellent CLI experience with type hints and auto-completion
- **Cross-platform**: Works on Windows, macOS, and Linux

<!-- xc-heading -->
## Development

Clone the repository and cd into the project directory:

```sh
git clone https://github.com/python-ankara-toplulugu/ossin
cd ossin
```

The commands below can also be executed using the [xc task runner](https://xcfile.dev/), which combines the usage instructions with the actual commands. Simply run `xc`, it will pop up an interactive menu with all available tasks.

### `install`

Install the dependencies:

```sh
uv sync
```

### `start`

Start the CLI:

```sh
uv run ossin
```

### `test`

Run the tests:

```sh
uv run pytest
```

### `ci`

Run the linters and type checkers:

```sh
uv run ruff check
uv run ruff format
uv run mypy
uv run ty check
uv run pyrefly check
uv run pyright
uv run vulture
uv run validate-pyproject pyproject.toml
```

## License

`ossin` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
