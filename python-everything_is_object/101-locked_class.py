#!/usr/bin/python3
"""Module with LockedClass"""


class LockedClass:
    """Class that only allows first_name attribute"""
    __slots__ = ['first_name']
