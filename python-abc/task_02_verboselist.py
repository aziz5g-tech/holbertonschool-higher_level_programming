#!/usr/bin/env python3
"""
Module for Extending the Python List with Notifications

This module defines a VerboseList class that extends the built-in list class
and provides notification messages for list modification operations.
"""


class VerboseList(list):
    """
    A verbose version of the Python list class that prints notification
    messages whenever the list is modified.

    This class overrides the append, extend, remove, and pop methods
    to provide informative messages about list operations.
    """

    def append(self, item):
        """
        Append an item to the list and print a notification message.

        Args:
            item: The item to append to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with items from an iterable and print a notification message.

        Args:
            iterable: An iterable containing items to add to the list.
        """
        items_count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{items_count}] items.")

    def remove(self, item):
        """
        Remove an item from the list and print a notification message.

        Args:
            item: The item to remove from the list.

        Raises:
            ValueError: If the item is not found in the list.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return an item from the list at the given index and print a notification message.

        Args:
            index (int, optional): The index of the item to remove. Defaults to -1 (last item).

        Returns:
            The item that was removed from the list.

        Raises:
            IndexError: If the list is empty or the index is out of range.
        """
        if len(self) == 0:
            raise IndexError("pop from empty list")

        if index == -1:
            item = self[index]
        else:
            item = self[index]

        print(f"Popped [{item}] from the list.")
        return super().pop(index)
