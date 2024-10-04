#!/usr/bin/python3
"""Script that adds all arguments to a Python list and
save them to a file"""
import sys
from os.path import exists
from 5_save_to_json_file import save_to_json_file
from 6_load_from_json_file import load_from_json_file

filename = "add_item.json"

if exists(filename):
    #Load existing list from file
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
