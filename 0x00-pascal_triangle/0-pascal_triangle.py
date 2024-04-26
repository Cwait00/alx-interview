#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates the Pascal's triangle up to the given number of rows.
    
    Args:
        n (int): Number of rows of the Pascal's triangle to generate.
        
    Returns:
        list: A list of lists representing the Pascal's triangle.
    """
    if n < 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle

# Display Pascal's triangle
def display_triangle(triangle):
    for row in triangle:
        print(" ".join(str(num) for num in row))

# Test cases
if __name__ == "__main__":
    triangle_5 = pascal_triangle(5)
    display_triangle(triangle_5)
