# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

ossin is a Python CLI utility that displays system information (OS, Python environment, platform) using Rich for terminal output. Built with Typer, it supports table, panel, and JSON output formats.

## Development Commands

```bash
uv sync                          # Install dependencies
uv run ossin                     # Run the CLI
uv run ossin --format json       # Run with JSON output
uv run pytest                    # Run tests
```

### Linting & Type Checking (CI runs these on Ubuntu only)

```bash
uv run ruff check src tests      # Lint
uv run ruff format --check .     # Format check
uv run mypy                      # Type check (strict mode)
uv run ty check                  # Type check with ty
uv run pyrefly check             # Type check with pyrefly
uv run pyright                   # Type check with pyright
uv run vulture src tests         # Dead code detection
uv run validate-pyproject pyproject.toml
```

## Architecture

- `src/ossin/core.py` — `SystemInfo` TypedDict and `get_system_info()` function (stdlib only: `platform`, `sys`)
- `src/ossin/cli.py` — Typer app with three output renderers (table, panels, JSON) using Rich
- `src/ossin/__main__.py` — Entry point, imports and runs `cli.app`
- Version is dynamic from VCS via hatch-vcs, generated into `src/ossin/_version.py` at build time

## Code Style

- **Ruff** with ALL rules selected, preview mode, unsafe fixes enabled. Ignored rules: B008, COM812, FBT001, FBT003
- No relative imports allowed (`ban-relative-imports = "all"`)
- McCabe complexity limit: 4
- Docstring convention: PEP 257
- All type checkers run in strict/error-on-warning mode
- Target Python version: 3.10

## CI/CD

- PR titles must follow **Conventional Commits** format (enforced by check-pr-title workflow)
- CI runs linters/type-checkers on Ubuntu only; runs the CLI on all three platforms (Ubuntu, macOS, Windows)
- CD publishes to PyPI via trusted publishing on GitHub release, then triggers Homebrew and Scoop manifest updates
