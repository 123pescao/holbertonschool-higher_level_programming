#!/usr/bin/python3
"""This module creates a function that writes an object
to a text file, using a json representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
