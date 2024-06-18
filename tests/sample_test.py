"""
Sample test module
"""

from src.folder.test import hello_world


def test_hello_world():
    assert hello_world() == "Hello, world!"
