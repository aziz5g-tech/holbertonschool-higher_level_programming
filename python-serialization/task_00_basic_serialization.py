#!/usr/bin/python3
"""Basic JSON serialization/deserialization module."""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary into JSON format and save it to a file.
    The file will be overwritten if it already exists.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it
    back into a Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
