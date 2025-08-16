# Copyright (c) 2025 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Licensed under the MIT License

"""
Core module for the ossin package.

This module provides system information utilities and core functionality.
"""

import platform
import sys
from typing import TypedDict


class SystemInfo(TypedDict):
    """A dictionary containing system information.

    Attributes:
        os_name: The name of the operating system.
        os_version: The version of the operating system.
        os_arch: The architecture of the operating system.
        python_version: The version of Python.
        python_implementation: The implementation of Python.
        platform: The platform of the operating system.
    """

    os_name: str
    os_version: str
    os_arch: str
    python_version: str
    python_implementation: str
    platform: str


def get_system_info() -> SystemInfo:
    """
    Get system information.

    Returns:
        SystemInfo: A dictionary containing system information.

    Example:
        >>> info = get_system_info()
        >>> print(f"OS: {info['os_name']} {info['os_version']}")
    """
    os_name = platform.system()
    os_version = platform.release()
    os_arch = platform.machine()
    python_version = sys.version
    python_implementation = platform.python_implementation()
    platform_info = platform.platform()

    return {
        "os_name": os_name,
        "os_version": os_version,
        "os_arch": os_arch,
        "python_version": python_version,
        "python_implementation": python_implementation,
        "platform": platform_info,
    }
