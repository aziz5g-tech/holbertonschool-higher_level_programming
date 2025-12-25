#!/usr/bin/python3
"""
Module that defines append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific
    string

    Args:
        filename: the name of the file
        search_string: the string to search for in each line
        new_string: the string to insert after lines containing search_string
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
