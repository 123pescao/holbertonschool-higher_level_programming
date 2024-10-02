#!/usr/bin/python3
""" This module writes a string to a text file and returns the number of
characters written
"""


def write_file(filename="", text=""):
    """
    This module writes string to a file and returns len
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)