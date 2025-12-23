#!/usr/bin/python3
# 2-append_write.py
# ABDULAZIZ ALRSHEDI <11937@holbertonschool.com>
"""Function to writes a string to a text file."""


def append_write(filename="", text=""):
    '''
    Function to append text
    '''
    with open(filename, 'a', encoding="utf-8") as f:
        write_data = f.write(text)

        return write_data
