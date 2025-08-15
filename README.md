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

### Using uv (recommended)

```sh
uv add ossin
```

### Using pip

```sh
pip install ossin
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

## Development

### Setup

Clone the repository and install dependencies using uv:

```sh
uv sync
```

### Running the CLI

```sh
uv run ossin
```

### Running tests

```sh
uv run pytest
```

## License

`ossin` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
