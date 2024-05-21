#!/usr/bin/python3
"""
This module contains the function `matrix_divided` that divides all
elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor, a number (integer or float).

    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix elements are not lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(ele, (int, float)) for row in matrix for ele in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(ele / div, 2) for ele in row] for row in matrix]
