#!/usr/bin/env python3
"""
Module for Shapes, Interfaces, and Duck Typing

This module defines an abstract Shape class using Python's ABC package,
implements concrete subclasses Circle and Rectangle, and demonstrates
duck typing with a shape_info function.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for all shapes.

    This class defines the interface that all shape subclasses must implement.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method that must be implemented by subclasses.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method that must be implemented by subclasses.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle class that inherits from Shape.

    Implements the area and perimeter methods for a circle.
    """

    def __init__(self, radius):
        """
        Initialize a Circle with the given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.

        Returns:
            float: The area of the circle (π * r²).
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate and return the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle (2 * π * r).
        """
        return 2 * (math.pi * self.radius)


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape.

    Implements the area and perimeter methods for a rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with the given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            float: The area of the rectangle (width * height).
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle (2 * (width + height)).
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape using duck typing.

    This function relies on duck typing - it doesn't check the type of the
    shape parameter, but simply calls its area() and perimeter() methods.

    Args:
        shape: Any object that implements area() and perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
