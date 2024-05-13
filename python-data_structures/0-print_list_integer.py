#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """
    This function prints all integers in a list, one per line.
    Args:
        my_list (list): A list of integers.
    """
    for number in my_list:
        print("{:d}".format(number))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)
