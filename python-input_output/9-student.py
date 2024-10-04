#!/usr/bin/python3
"""" This module contains a class Student with methods to
represent its attributes in JSON format. """


class Student:
    """A class that defines a student """
    def __init__(self, first_name, last_name, age):
        """initializes Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation """
        return self.__dict__
