#!/usr/bin/python3
"""Serialize and deserialize Python dictionaries to and from XML."""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save it to a file.

    Args:
        dictionary (dict): The Python dictionary to serialize.
        filename (str): The output XML filename.
    """
    root = ET.Element("data")  # Root element

    for key, value in dictionary.items():
        # Each key becomes a child element
        child = ET.SubElement(root, key)
        child.text = str(value)  # Convert value to string for XML

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file back into a Python dictionary.

    Args:
        filename (str): The XML file to read from.

    Returns:
        dict: The reconstructed dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}

    for child in root:
        # All values are read as strings from XML
        result[child.tag] = child.text

    return result
