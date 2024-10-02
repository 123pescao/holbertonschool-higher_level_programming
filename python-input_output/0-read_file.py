#!/usr/bin/python3
"""
This module contains a function to read a file and print contents
"""


def read_file(filename=""):
    """
    Reads an text file and prints its contents
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
