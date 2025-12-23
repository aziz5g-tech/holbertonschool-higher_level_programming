#!/usr/bin/python3
"""
11-student.py
Module containing class Student.
"""


class Student:
    """
    A class to define a student.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not isinstance(attrs, list):
            return self.__dict__

        for element in attrs:
            if not isinstance(element, str):
                return self.__dict__

        dictionary = {}
        for element in attrs:
            if element in self.__dict__:
                dictionary[element] = self.__dict__[element]
        return dictionary

    def reload_from_json(self, json):
        if "first_name" in json:
            self.first_name = json['first_name']
        if "last_name" in json:
            self.last_name = json['last_name']
        if "age" in json:
            self.age = json['age']
