Python - More Classes and Objects

Welcome to the Python - More Classes and Objects project! In this project, we dive deeper into Object-Oriented Programming (OOP) with Python, focusing on more advanced topics such as class and instance attributes, static and class methods, and the special methods __str__, __repr__, and __del__. You'll also explore the Pythonic way to handle OOP principles like encapsulation and abstraction.
Background Context

It’s very important to carefully follow the reading materials to get a solid understanding of the advanced concepts in this project. The focus is on experimenting with OOP, testing, and truly understanding how classes work in Python.
Resources

Be sure to read or watch the following resources in the recommended order:

    Object-Oriented Programming (stop before Inheritance)
    Class and Instance Attributes
    Class methods and static methods
    Properties vs. Getters and Setters
    __str__ vs __repr__

Learning Objectives

By the end of this project, you should be able to explain the following concepts clearly:
General

    What is Object-Oriented Programming (OOP)?
    What is a class, an object, and an instance?
    What is the difference between an object and an instance?
    What are class and instance attributes?
    What is the self keyword in a class?
    What is the __init__ method and how does it work?
    How does data abstraction and encapsulation work in Python?
    What are __str__ and __repr__ methods, and how do they differ?
    What is a class method, static method, and regular method?
    How does Python's attribute lookup work?
    How to dynamically bind attributes to an instance or class?
    How to use the getattr function to retrieve attributes?

Requirements
General

    Your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
    All files should end with a new line.
    The first line of each Python file should be exactly #!/usr/bin/python3.
    Your code should conform to the pycodestyle (version 2.7.*) style guide.
    Each file must be executable.
    Each class, module, and method should have proper documentation using docstrings.
    A README.md file at the root of the project is mandatory.

Tasks Overview
0. Simple Rectangle

    Task: Write an empty class Rectangle that defines a rectangle.

1. Real Definition of a Rectangle

    Task: Create a class Rectangle that defines a rectangle with private instance attributes width and height. Add validation for these attributes to ensure they are integers greater than or equal to 0.

2. Area and Perimeter

    Task: Add methods to compute the area and perimeter of a rectangle.

3. String Representation

    Task: Implement __str__ to print the rectangle using the # character.

4. Eval is Magic

    Task: Implement __repr__ to return a string that can recreate the rectangle object using eval().

5. Detect Instance Deletion

    Task: Print a message when an instance of the Rectangle class is deleted.

6. How Many Instances

    Task: Track the number of instances of the Rectangle class using a class attribute.

7. Change Representation

    Task: Add a class attribute print_symbol that can be changed to modify how the rectangle is printed.

8. Compare Rectangles

    Task: Implement a static method bigger_or_equal to compare two rectangles based on their area.

9. A Square is a Rectangle

    Task: Create a class method square that returns a new Rectangle instance where width == height.

Repository Information

    GitHub repository: holbertonschool-higher_level_programming
    Directory: python-more_classes

This project will give you a deeper understanding of Object-Oriented Programming and how to apply its principles in Python. Experiment with different attributes, methods, and special functions to master Python classes!

Happy coding!