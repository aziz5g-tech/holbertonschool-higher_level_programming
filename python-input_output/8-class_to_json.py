#!/usr/bin/python3
"""
8-class_to_json.py
Module containing function to create
a dictionary description from an object.
"""


def class_to_json(obj):
    """
    Function creating a dictionary description from an object.
    """
    return obj.__dict__
