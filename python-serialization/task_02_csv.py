#!/usr/bin/python3
"""Convert CSV file to JSON file using serialization."""


import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON and write to data.json.

    Args:
        csv_filename (str): Path to the CSV file.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data_list = [row for row in reader]

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except (FileNotFoundError, IOError):
        return False
