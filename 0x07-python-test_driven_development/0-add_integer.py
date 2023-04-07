'''
    Adds two numbers together.

    Args:
        a (int or float): The first number to add.
        b (int or float, optional): The second number to add. Defaults to 98.

    Returns:
        int: The sum of the two numbers, rounded down to the nearest integer.
'''

def add_integer(a, b=98):
    '''
        Adds two numbers together, rounding down to the nearest integer.

        Raises:
            TypeError: If either argument is not an integer or float.
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)
