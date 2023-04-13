#!/usr/bin/python3
"""text file-reading function."""


def read_file(filename=""):
    """output the contents of a UTF8 text file to stout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
