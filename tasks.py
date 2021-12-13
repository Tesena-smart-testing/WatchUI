"""Deployment tasks"""
import os

from pathlib import Path
from robot.libdoc import libdoc
from robot import run

ROOT_DIR = Path(os.path.dirname(__file__))

def docs():
    """Generate library keyword documentation.
    Args:
        version: Creates keyword documentation with version
        suffix in the name. Documentation is moved to docs/vesions
        folder.
    """
    lib_name = "WatchUI"
    output = str(ROOT_DIR) + "/docs/" + lib_name + ".html"
    libdoc(lib_name, output)


def test():
    """Run tests."""
    run("tests/test.robot")
