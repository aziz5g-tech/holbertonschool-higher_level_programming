#!/usr/bin/env python3
"""
Module for Abstract Animal Class and its Subclasses

This module defines an abstract Animal class using Python's ABC package,
and implements two concrete subclasses: Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for all animals.

    This class defines the interface that all animal subclasses must implement.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.

        Returns:
            str: The sound that the animal makes.
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal.

    Implements the sound method to return a dog's bark.
    """

    def sound(self):
        """
        Returns the sound a dog makes.

        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal.

    Implements the sound method to return a cat's meow.
    """

    def sound(self):
        """
        Returns the sound a cat makes.

        Returns:
            str: "Meow"
        """
        return "Meow"
