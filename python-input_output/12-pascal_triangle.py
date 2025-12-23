#!/usr/bin/python3
"""
12-pascal_triangle.py
Module containing function to create a representation of a Pascal triangle.
"""


def pascal_triangle(n):
    """
    Creates a Pascal triangle of n.
    """
    triangle = []
    if n > 0:
        for row in range(n):
            numbers = [1]
            for i in range(1, row):
                sum = triangle[row - 1][i - 1] + triangle[row - 1][i]
                numbers.append(sum)
            if row > 0:
                numbers.append(1)
            triangle.append(numbers)

    return triangle
