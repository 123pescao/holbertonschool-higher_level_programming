#!/usr/bin/python3
"""
Module that defines the Student class
"""


class Student:
    """
    Defines a student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        """

        if attrs is None:
            return self.__dict__
        return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
