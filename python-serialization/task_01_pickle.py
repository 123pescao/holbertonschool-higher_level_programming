#!/usr/bin/python3
"""Module for class named Custom Object"""

import pickle


class CustomObject:
    """Custom object for demonstrating pickling."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        """Serialize the object to a file using pickle."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print("Serialization error:", e)
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file using pickle."""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print("Deserialization error:", e)
            return None
