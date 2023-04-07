#!/usr/bin/python3

def print_square(size):
    """Print a square with the # character.

    Args:
        size (int): The height/width of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    # Use nested loops to print out the square
    for i in range(size):
        # Loop over each column of the current row and print a # character
        for j in range(size):
            print("#", end="")

        # After printing all the characters in the current row, move to the next line
        print()
