#!/usr/bin/python3
"""
9-student.py
Function to write a class Student
"""


class Student():
    """
    Student - Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        __init__ - Init new student
        @first_name: First name of the student
        @last_name: Last name of the student
        @age: Age of the student
        Return: Void
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        to_json - Retrieve dict representation of a Student instance
        Return: Dict representation
        """
        return self.__dict__
