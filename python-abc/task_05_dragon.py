#!/usr/bin/env python3
"""
Module for Mixins - The Mystical Dragon

This module demonstrates the use of mixins in Python by creating
SwimMixin and FlyMixin classes, and a Dragon class that uses both mixins.
"""


class SwimMixin:
    """
    Mixin class that provides swimming functionality.

    This mixin can be combined with other classes to add swimming
    behavior without requiring a complex inheritance hierarchy.
    """

    def swim(self):
        """
        Method that provides swimming behavior.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying functionality.

    This mixin can be combined with other classes to add flying
    behavior without requiring a complex inheritance hierarchy.
    """

    def fly(self):
        """
        Method that provides flying behavior.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that combines SwimMixin and FlyMixin behaviors.

    This class demonstrates how mixins can be used to compose
    behaviors from multiple sources, allowing the Dragon to both
    swim and fly, plus have its own unique behaviors.
    """

    def roar(self):
        """
        Dragon-specific method that provides roaring behavior.
        """
        print("The dragon roars!")
