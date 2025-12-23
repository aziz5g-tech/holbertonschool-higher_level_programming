#!/usr/bin/python3

'''
4-from_json_string.py
Function that return an object
represented by json string
'''
import json


def from_json_string(my_str):
    """
    Function that return an object
    represented by json string
    """
    return json.loads(my_str)
