# SPDX-FileCopyrightText: 2025-present Hasan Sezer Taşan <hasansezertasan@gmail.com>
#
# SPDX-License-Identifier: MIT

"""
Core module for the ossin package.

This module provides system information utilities and core functionality.
"""

import platform
import sys
from typing import Any, Dict


def get_system_info() -> Dict[str, Any]:
    """
    Get system information.

    Returns:
        Dict[str, Any]: A dictionary containing system information.

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
