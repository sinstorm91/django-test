#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    # Enable PyCharm Remote Debugging
    if os.environ.get("DJANGO_DEBUG") == "True":
        try:
            import pydevd_pycharm
            pydevd_pycharm.settrace(
                'host.docker.internal',  # Use this for Mac/Windows
                port=5678,
                stdoutToServer=True,
                stderrToServer=True,
                suspend=False
            )
        except ImportError:
            print("PyCharm Debugger not installed. Skipping debugger attachment.")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
