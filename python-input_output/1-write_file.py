#!/usr/bin/python3
# 1-write_file.py
# ABDULAZIZ ALRSHEDI <11937@holbertonschool.com>
"""Defines a text file line-counting function."""


def number_of_lines(filename=""):
    """Return the number of lines in a text file."""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
