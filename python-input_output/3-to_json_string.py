#!/usr/bin/python3
"""Module creates a function that returns JSON representation of object"""
import json
"""
This module creates a function that returns the JSON representation
of an object (string):
"""


def to_json_string(my_obj):
    """
    Returns JSON representation of an object
    """
    return json.dumps(my_obj)
