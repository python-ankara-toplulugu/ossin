# Copyright (c) 2025 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Licensed under the MIT License

"""
CLI module for the ossin package.

This module provides a command-line interface for displaying system information
using Rich for beautiful terminal output and Typer for modern CLI experience.
"""

from enum import Enum
from importlib.metadata import version
from typing import List

import typer
from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from ossin.core import SystemInfo, get_system_info

app = typer.Typer(
    name="ossin",
    help="What is OS's sin? 🤔",
    add_completion=False,
    rich_markup_mode="rich",
)


class OutputFormat(str, Enum):
    """Enumeration for output format options."""

    TABLE = "table"
    PANELS = "panels"
    JSON = "json"


def create_system_table(system_info: SystemInfo) -> Table:
    """
    Create a Rich table with system information.

    Args:
        system_info: Dictionary containing system information

    Returns:
        Table: Rich table object with formatted system information
    """
    table = Table(
        title="[bold blue]System Information[/bold blue]",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold magenta",
    )

    table.add_column("Property", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")

    # Add system information to table
    table.add_row(
        "Operating System",
        f"{system_info['os_name']} {system_info['os_version']}",
    )
    table.add_row("Architecture", system_info["os_arch"])
    table.add_row("Platform", system_info["platform"])
    table.add_row("Python Version", system_info["python_version"].split()[0])
    table.add_row("Python Implementation", system_info["python_implementation"])

    return table


def create_info_panels(system_info: SystemInfo) -> List[Panel]:
    """
    Create information panels for different system aspects.

    Args:
        system_info: Dictionary containing system information

    Returns:
        list[Panel]: List of Rich panel objects
    """
    panels: List[Panel] = []

    # OS Information Panel
    os_text = Text()
    os_text.append(f"OS: {system_info['os_name']}\n", style="bold cyan")
    os_text.append(f"Version: {system_info['os_version']}\n", style="green")
    os_text.append(f"Architecture: {system_info['os_arch']}", style="yellow")

    os_panel = Panel(
        os_text,
        title="[bold]Operating System[/bold]",
        border_style="cyan",
        padding=(1, 2),
    )
    panels.append(os_panel)

    # Python Information Panel
    python_text = Text()
    python_text.append(
        f"Version: {system_info['python_version'].split()[0]}\n",
        style="bold cyan",
    )
    python_text.append(
        f"Implementation: {system_info['python_implementation']}",
        style="green",
    )

    python_panel = Panel(
        python_text,
        title="[bold]Python Environment[/bold]",
        border_style="green",
        padding=(1, 2),
    )
    panels.append(python_panel)

    # Platform Information Panel
    platform_text = Text()
    platform_text.append(f"Platform: {system_info['platform']}", style="bold yellow")

    platform_panel = Panel(
        platform_text,
        title="[bold]Platform Details[/bold]",
        border_style="yellow",
        padding=(1, 2),
    )
    panels.append(platform_panel)

    return panels


def display_system_info(
    console: Console,
    system_info: SystemInfo,
    format_type: OutputFormat = OutputFormat.TABLE,
) -> None:
    """
    Display system information in the specified format.

    Args:
        console: Rich console object
        system_info: Dictionary containing system information
        format_type: Format type ('table', 'panels', or 'json')
    """
    if format_type == OutputFormat.TABLE:
        table = create_system_table(system_info)
        console.print(table)
    elif format_type == OutputFormat.PANELS:
        panels = create_info_panels(system_info)
        columns = Columns(panels, equal=True, expand=True)
        console.print(columns)
    elif format_type == OutputFormat.JSON:
        console.print_json(data=system_info)


@app.command()
def main(
    _format: OutputFormat = typer.Option(
        OutputFormat.TABLE,
        "--format",
        "-f",
        help="Output format for system information",
        case_sensitive=False,
    ),
    no_color: bool = typer.Option(
        False,
        "--no-color",
        help="Disable colored output",
    ),
    _version: bool = typer.Option(
        False,
        "--version",
        help="Show version and exit",
    ),
) -> None:
    """
    Display system information in a beautiful format.

    Examples:
        ossin                    # Display system info in table format
        ossin --format panels    # Display system info in panel format
        ossin --format json      # Display system info in JSON format
        ossin --no-color         # Display without colors

    Raises:
        typer.Exit: If the version flag is provided.
    """
    # Handle version flag
    if _version:
        typer.echo(version("ossin"))
        raise typer.Exit

    # Create console with appropriate settings
    console = Console(color_system="auto" if not no_color else None)

    try:
        # Get system information
        system_info = get_system_info()

        # Display header
        console.print("\n[bold blue]System Information Tool[/bold blue]\n")

        # Display system information in requested format
        display_system_info(console, system_info, _format)

        console.print("\n[dim] Powered by ossin[/dim]\n")

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        console.print(
            "[dim]Please check if all required dependencies are installed.[/dim]",
        )
        raise typer.Exit(1) from e
