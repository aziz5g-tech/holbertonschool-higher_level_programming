#!/usr/bin/python3

"""
6-load_from_json_file.py
Module containing function to
create an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Function creating an object from a JSON file.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        string = f.read()
    return json.loads(string)
