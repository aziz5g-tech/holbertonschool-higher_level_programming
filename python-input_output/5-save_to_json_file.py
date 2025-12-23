#!/usr/bin/python3

'''
5-save_to_json_file.py
function that writes an Object
to a text file, using a JSON representation
'''
import json


def save_to_json_file(my_obj, filename):
    """
    Function writing an object as a JSON to a file.
    """
    with open(filename, 'w', encoding="UTF-8") as f:
        n = f.write(json.dumps(my_obj))

    return n
