#!/usr/bin/python3

"""
Shapes, Interfaces, and Duck Typing
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Shape Abstract method to build geometric shape

    Args:
        ABC (class): Baseclass to build abstract method
    """
    @abstractmethod
    def area(self):
        """
        area empty (set up the abstrat method)
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        perimeter empty (set up the abstrat method)
        """
        pass


class Circle(Shape):
    """
    Circle Class representing a circle shape
        inherit from abstract method Shape

    Args:
        radius (int): The radius of the circle.
    """

    def __init__(self, radius):
        """
        __init__ Build the object

        Args:
            radius (int): Radius of the circle
        """
        self.radius = radius

    def area(self):
        """
        area calculation = pi * r^2

        Returns:
            int: area of the circle
        """
        result = math.pi * self.radius ** 2
        return (result)

    def perimeter(self):
        """
        perimeter calculation = 2 * pi * r

        Returns:
            int: perimeter
        """
        result = 2 * math.pi * self.radius
        return (result)


class Rectangle(Shape):
    """
    Rectangle Class representing a rectangle shape
        inherit from abstract method Shape

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        __init__ Constructor of the rectangle

        Args:
            width (int): width
            height (int): height
        """
        self.width = width
        self.height = height

    def area(self):
        """ Area calculation = W * H """
        return self.width * self.height

    def perimeter(self):
        """ Perimeter calculation = 2*W + 2*H """
        return (self.width * 2) + (self.height * 2)


def shape_info(item):
    """
    shape_info Retrieve information about a shape

    Args:
        item (obj): Instance of a shape
    """
    result_area = item.area()
    result_perimeter = item.perimeter()

    print(f"Area: {result_area}")
    print(f"Perimeter: {result_perimeter}")
