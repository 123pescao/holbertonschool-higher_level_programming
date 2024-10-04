#!/usr/bin/python3
""" This module contains a class Student with methods
to represent its attributes in JSON format with optional filtering.
"""


class Student:
    """Class that defines student"""
    def __init__(self, first_name, last_name, age):
        """Initializes Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """"Retrieves a dict representation of Student"""
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
