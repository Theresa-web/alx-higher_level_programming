#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""
def pascal_triangle(n):
     """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Compute each subsequent row of the triangle
    for i in range(1, n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
