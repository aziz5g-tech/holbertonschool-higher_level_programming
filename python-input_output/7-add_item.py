#!/usr/bin/python3

"""
7-add_item.py
Script adding all arguments to a list saved as a file.
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    Adds all command-line arguments to a list saved as a file.
    """
    if len(sys.argv) < 2:
        my_list = []

    filename = "add_item.json"
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []

    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])

    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    main()
