#!/usr/bin/env python3
"""
Module for Multiple Inheritance - The Enigmatic FlyingFish

This module demonstrates multiple inheritance in Python by creating
Fish and Bird classes, and a FlyingFish class that inherits from both.
"""


class Fish:
    """
    Fish class representing aquatic creatures.

    This class provides basic methods for fish behavior.
    """

    def swim(self):
        """
        Method representing fish swimming behavior.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Method representing fish habitat.
        """
        print("The fish lives in water")


class Bird:
    """
    Bird class representing aerial creatures.

    This class provides basic methods for bird behavior.
    """

    def fly(self):
        """
        Method representing bird flying behavior.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Method representing bird habitat.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish class demonstrating multiple inheritance.

    This class inherits from both Fish and Bird classes and overrides
    methods from both parents to provide specialized behavior.
    """

    def fly(self):
        """
        Override the fly method from Bird class.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Override the swim method from Fish class.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Override the habitat method from both parent classes.
        """
        print("The flying fish lives both in water and the sky!")
