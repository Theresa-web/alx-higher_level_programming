#!/usr/bin/python3
"""Open file for writing using with statement"""

def write_file(filename="", text=""):
    '''Write text to file and get the number of characters written
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        Return the number of characters written
    '''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
