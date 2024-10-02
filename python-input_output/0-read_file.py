#!/usr/bin/python3
"""
This module contains a function to read a file and print contents
"""

def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read())
