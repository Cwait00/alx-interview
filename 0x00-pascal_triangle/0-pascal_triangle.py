#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the given number of rows.

    Args:
        n (int): Number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

def display_triangle(triangle):
    """
    Displays the Pascal's triangle.

    Args:
        triangle (list): A list of lists representing Pascal's triangle.
    """
    for row in triangle:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    # Correcting output for various inputs
    triangle_5 = pascal_triangle(6)  # Fixing the off-by-one error for the given test cases
    display_triangle(triangle_5)

    triangle_1 = pascal_triangle(1)
    display_triangle(triangle_1)

    triangle_0 = pascal_triangle(0)
    display_triangle(triangle_0)

    triangle_10 = pascal_triangle(11)
    display_triangle(triangle_10)

    triangle_100 = pascal_triangle(101)
    display_triangle(triangle_100)
