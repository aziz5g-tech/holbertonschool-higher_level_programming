#!/usr/bin/env python3
"""
Module for CountedIterator - Keeping Track of Iteration

This module defines a CountedIterator class that extends the functionality
of built-in iterators by keeping track of how many items have been iterated.
"""


class CountedIterator:
    """
    A wrapper around iterator objects that keeps track of the number
    of items that have been iterated over.

    This class provides the same iteration functionality as a regular
    iterator but adds a counter to track how many items have been fetched.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.

        Args:
            iterable: Any iterable object (list, tuple, string, etc.)
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """
        Return the current count of iterated items.

        Returns:
            int: The number of items that have been fetched so far.
        """
        return self.count

    def __next__(self):
        """
        Fetch the next item from the iterator and increment the counter.

        Returns:
            The next item from the iterator.

        Raises:
            StopIteration: When there are no more items to iterate.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """
        Return the iterator object itself.

        This makes the CountedIterator compatible with for loops
        and other iteration constructs.

        Returns:
            self: The iterator object itself.
        """
        return self
