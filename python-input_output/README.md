Python - Input/Output

Amateur Level
By: Guillaume
Weight: 1
Your score will be updated as you progress.
Description

This project is focused on file handling in Python, including reading and writing to files, using JSON for serialization/deserialization, and learning about the Python standard library tools available for these purposes. You will implement various functions to work with files and JSON objects.
Resources

Read or watch:

    7.2. Reading and Writing Files
    8.7. Predefined Clean-up Actions
    Dive Into Python 3: Chapter 11. Files (until "11.4 Binary Files" included)
    JSON encoder and decoder
    Learn to Program 8: Reading / Writing Files
    Automate the Boring Stuff with Python (chapters 8 and 14)
    sys package

Learning Objectives

By the end of this project, you should be able to explain the following concepts:
General

    Why Python programming is awesome
    How to open a file
    How to write text in a file
    How to read the full content of a file
    How to read a file line by line
    How to move the cursor in a file
    How to make sure a file is closed after using it
    What is and how to use the with statement
    What is JSON
    What is serialization
    What is deserialization
    How to convert a Python data structure to a JSON string
    How to convert a JSON string to a Python data structure
    How to access command line parameters in a Python script

Requirements
Python Scripts

    Allowed editors: vi, vim, emacs
    All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
    All files should end with a new line
    The first line of all files should be #!/usr/bin/python3
    A README.md file, at the root of the project folder, is mandatory
    Code should follow pycodestyle (version 2.7.*)
    All files must be executable
    The length of the files will be tested using wc

Python Test Cases

    Allowed editors: vi, vim, emacs
    All test files should end with a new line
    All test files should be inside a folder named tests
    All test files should be text files (extension: .txt)
    All tests should be executed by using this command: python3 -m doctest ./tests/*
    All modules should have documentation (e.g., print(__import__("my_module").__doc__))
    All classes should have documentation (e.g., print(__import__("my_module").MyClass.__doc__))
    All functions (inside and outside a class) should have documentation (e.g., print(__import__("my_module").my_function.__doc__) and print(__import__("my_module").MyClass.my_function.__doc__))
    Documentation should be a real sentence explaining the purpose of the module, class, or method
    Collaborate on test cases to cover as many edge cases as possible

Tasks
0. Read File

Write a function that reads a text file (UTF8) and prints it to stdout.

    Prototype: def read_file(filename=""):
    Must use the with statement
    No need to manage file permission or file non-existence exceptions
    No imports allowed

1. Write to a File

Write a function that writes a string to a text file (UTF8) and returns the number of characters written.

    Prototype: def write_file(filename="", text=""):
    Must use the with statement
    Create the file if it doesn't exist, overwrite if it does
    No imports allowed

2. Append to a File

Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.

    Prototype: def append_write(filename="", text=""):
    If the file doesn’t exist, create it
    Must use the with statement
    No imports allowed

3. To JSON String

Write a function that returns the JSON representation of an object (string).

    Prototype: def to_json_string(my_obj):
    No need to manage exceptions if the object can’t be serialized

4. From JSON String to Object

Write a function that returns an object (Python data structure) represented by a JSON string.

    Prototype: def from_json_string(my_str):
    No need to manage exceptions if the JSON string doesn’t represent an object

5. Save Object to a File

Write a function that writes an Object to a text file, using a JSON representation.

    Prototype: def save_to_json_file(my_obj, filename):
    Must use the with statement
    No need to manage exceptions if the object can’t be serialized

6. Create Object from a JSON File

Write a function that creates an Object from a “JSON file”.

    Prototype: def load_from_json_file(filename):
    Must use the with statement

7. Load, Add, Save

Write a script that adds all arguments to a Python list, and then saves them to a file.

    Use save_to_json_file and load_from_json_file from previous tasks
    Save list as a JSON representation in a file named add_item.json

8. Class to JSON

Write a function that returns the dictionary description with simple data structure for JSON serialization of an object.

    Prototype: def class_to_json(obj):
    No imports allowed

9. Student to JSON

Write a class Student that defines a student.

    Public instance attributes: first_name, last_name, age
    Public method to_json(self): retrieves a dictionary representation of a Student instance

10. Student to JSON with Filter

Write a class Student that defines a student by filtering attributes.

    Public method to_json(self, attrs=None): retrieves a filtered dictionary representation

11. Student to Disk and Reload

Extend the Student class to include reloading from JSON.

    Public method reload_from_json(self, json): replaces all attributes from a JSON dictionary

12. Pascal's Triangle

Create a function that returns a list of lists of integers representing Pascal’s triangle of n.

    Prototype: def pascal_triangle(n):
    Returns an empty list if n <= 0

Repository Structure

    GitHub Repository: holbertonschool-higher_level_programming
    Directory: python-input_output
    Files: Tasks are implemented in separate Python scripts as specified in the project requirements.


Happy Coding!