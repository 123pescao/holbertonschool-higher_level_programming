Python - Inheritance
Project Overview

This project covers key concepts of inheritance in Python, which is essential for understanding object-oriented programming. The tasks will help you learn how to create classes that inherit from other classes, override methods, and validate data using inheritance.
Learning Objectives

By the end of this project, you will be able to:

    Understand what a superclass, base class, or parent class is.
    Define and use a subclass.
    List all attributes and methods of a class or an instance.
    Know when an instance can have new attributes.
    Understand how to inherit a class from another.
    Create classes with multiple base classes (multiple inheritance).
    Identify the default class every Python class inherits from.
    Override a method or attribute inherited from a base class.
    Use attributes or methods inherited by subclasses.
    Recognize the purpose of inheritance.
    Use built-in functions like isinstance(), issubclass(), type(), and super() in the context of inheritance.

Project Requirements

    Python version: All scripts will be interpreted with Python 3.8.5 on Ubuntu 20.04 LTS.
    Code Style: All Python code must follow the pycodestyle guidelines (version 2.7.*).
    Documentation:
        Each module should have a module-level docstring.
        Classes and functions must also have docstrings explaining their purpose.
        The first line of every script must be #!/usr/bin/python3.

Python Test Cases

    Test files must be inside a tests folder with the .txt extension.
    Run test cases using python3 -m doctest ./tests/*.

Project Tasks
0. Lookup

File: 0-lookup.py

Write a function lookup(obj) that returns a list of available attributes and methods of an object.
1. My List

File: 1-my_list.py

Create a class MyList that inherits from list. Implement a public instance method print_sorted(self) that prints the list but sorted in ascending order.
2. Exact Same Object

File: 2-is_same_class.py

Write a function is_same_class(obj, a_class) that returns True if obj is exactly an instance of a_class; otherwise False.
3. Same Class or Inherit From

File: 3-is_kind_of_class.py

Write a function is_kind_of_class(obj, a_class) that returns True if obj is an instance of, or if the object is an instance of a class that inherited from, the specified class.
4. Only Subclass of

File: 4-inherits_from.py

Write a function inherits_from(obj, a_class) that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class.
5. Geometry Module

File: 5-base_geometry.py

Create an empty class BaseGeometry.
6. Improve Geometry

File: 6-base_geometry.py

Add a public instance method area(self) to BaseGeometry that raises an Exception with the message area() is not implemented.
7. Integer Validator

File: 7-base_geometry.py

Add a public instance method integer_validator(self, name, value) that validates if value is an integer and greater than 0.
8. Rectangle

File: 8-rectangle.py

Create a class Rectangle that inherits from BaseGeometry. Instantiate with private attributes width and height, both validated using integer_validator.
9. Full Rectangle

File: 9-rectangle.py

Add an area() method and ensure __str__() returns [Rectangle] <width>/<height>.
10. Square #1

File: 10-square.py

Create a class Square that inherits from Rectangle, with a private size attribute. The area() method should also be implemented.
11. Square #2

File: 11-square.py

Extend Square so that __str__() returns [Square] <size>/<size>.
Testing

All test files are in the tests directory and can be executed with the following command:

bash

python3 -m doctest ./tests/*


Happy Coding!