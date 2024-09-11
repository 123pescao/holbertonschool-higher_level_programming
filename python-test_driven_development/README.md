
Welcome to the **Python - Test-driven Development (TDD)** project! In this project, you will learn the importance of writing tests before writing the actual code, a methodology known as Test-Driven Development. You will explore different testing techniques, including writing interactive tests with doctest and using Python's unittest module.

## Background Context

To ensure high code quality, Python projects in this repository are evaluated using TDD principles:

- Always write the documentation (module(s) + function(s)) and tests first before coding.
- The intranet checks will not be released before their first deadline to encourage TDD practices.
- Collaboration on test cases is highly encouraged to cover all edge cases. However, avoid sharing implementations.

## Learning Objectives

By the end of this project, you should be able to:

- Understand why Python programming is awesome.
- Explain what interactive tests are and why tests are important.
- Write Docstrings to create tests.
- Write documentation for each module and function.
- Use basic option flags to create tests.
- Identify and test for edge cases.

## Requirements

### Python Scripts

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
- All files should end with a new line.
- The first line of all files should be `#!/usr/bin/python3`.
- A `README.md` file, at the root of the project folder, is mandatory.
- Your code should adhere to the `pycodestyle` style guide (version 2.7).
- All files must be executable.

### Python Test Cases

- All test files should be inside a folder named `tests`.
- Test files should be text files (extension: `.txt`).
- Use the following command to execute all tests: `python3 -m doctest ./tests/*`.
- All modules should have documentation that can be checked with:
  - `python3 -c 'print(__import__("my_module").__doc__)'`
  - `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
- A proper documentation should clearly explain the purpose of the module, class, or method.

## Tasks Overview

### 0. Integers addition
- **Function**: `add_integer(a, b=98)`
- Adds two integers and returns the result. Raises a `TypeError` if the inputs are not integers or floats.

### 1. Divide a matrix
- **Function**: `matrix_divided(matrix, div)`
- Divides all elements of a matrix by a given number and returns a new matrix. Raises `TypeError` and `ZeroDivisionError` where appropriate.

### 2. Say my name
- **Function**: `say_my_name(first_name, last_name="")`
- Prints the name in the format: `My name is <first name> <last name>`. Raises `TypeError` if inputs are not strings.

### 3. Print square
- **Function**: `print_square(size)`
- Prints a square of a given size using the character `#`. Raises `TypeError` or `ValueError` for invalid inputs.

### 4. Text indentation
- **Function**: `text_indentation(text)`
- Prints a text with two new lines after each of the characters: `.`, `?`, and `:`. Raises `TypeError` if the input is not a string.

### 5. Max integer - Unittest
- Write unittests for the function `max_integer(list=[])` using the `unittest` module. The test file should be inside the `tests` folder.

## Resources

To help you complete this project, refer to the following resources:

- **[doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)**
- **[doctest – Testing through documentation](https://docs.python.org/3/library/doctest.html#module-doctest)**
- **[Unit Tests in Python](https://docs.python.org/3/library/unittest.html)**

## Repository Information

- **GitHub repository**: [holbertonschool-higher_level_programming](https://github.com/holbertonschool-higher_level_programming)
- **Directory**: `python-test_driven_development`

## Additional Notes

- Focus on TDD to enhance your code quality and robustness.
- Make sure to handle all possible edge cases in your test cases.

Happy coding and testing!
