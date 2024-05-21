#!/usr/bin/python3
"""
This module contains the function `text_indentation` that prints a text
with 2 new lines after each of these characters: ., ? and :.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text: The text to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = {'.', '?', ':'}
    result = ""
    skip_space = False

    for char in text:
        if char in chars:
            result += char + "\n\n"
            skip_space = True
        elif char == " " and skip_space:
            continue
        else:
            result += char
            skip_space = False

    print(result.strip())
