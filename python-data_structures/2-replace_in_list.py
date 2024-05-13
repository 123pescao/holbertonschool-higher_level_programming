#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position if the index is valid.

    Args:
        my_list (list): The list to modify.
        idx (int): The index at which to replace an element.
        element (Any): The new element to insert at the specified index.

    Returns:
        list: The modified list if the index is valid, otherwise the original list.
    """
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = replace_in_list(my_list, idx, new_element)
    print(new_list)
    print(my_list)
