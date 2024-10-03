#!/usr/bin/python3
"""This module creates a function that creates an Object from a 
JSON file
"""
import json


def load_from_json_file(filename):
    """Creates an object from JSON file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
