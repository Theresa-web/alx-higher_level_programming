#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list[list[int or float]]): A matrix of integers or floats.
        div (int or float): The divisor.

    Raises:
        TypeError: If the matrix or its elements are not integers or floats, or if div is not an int or float.
        ZeroDivisionError: If div is 0.
        ValueError: If the rows of the matrix are not of the same length.

    Returns:
        list[list[float]]: A new matrix with the same dimensions as the original, representing the result of the division.
    """

    # Check the input types and values
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix elements must be integers or floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be an integer or float")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("rows of matrix must have the same length")

    # Perform the division and return the result
    return [[round(elem / div, 2) for elem in row] for row in matrix]

    #!/usr/bin/python3
"""Defines a matrix division function."""

def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If the matrix contains non-numeric values or is not a list of lists.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix representing the result of the division.
    """

    # Check that the matrix is a list of lists containing only ints or floats
    for row in matrix:
        if not isinstance(row, list) or not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check that all rows have the same length
    first_row_len = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_len:
            raise TypeError("Each row of the matrix must have the same size")

    # Check that div is a number and not 0
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div, rounded to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            new_elem = round(elem / div, 2)
            new_row.append(new_elem)
        new_matrix.append(new_row)

    return new_matrix
