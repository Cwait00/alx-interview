#!/usr/bin/python3
"""
This module contains a function to generate Pascal's Triangle up to a
given number of rows.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the given number of rows.

    Args:
        n (int): Number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle


def print_triangle(triangle):
    """
    Print Pascal's triangle.

    Args:
        triangle (list): A list of lists representing Pascal's triangle.
    """
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
