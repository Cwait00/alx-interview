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
        print("[", end="")
        for i, num in enumerate(row):
            if i > 0:
                print(",", end="")
            print(num, end="")
        print("]")

# Test cases
if __name__ == "__main__":
    # Correct output for n = 0
    triangle_0 = pascal_triangle(0)
    print("Pascal's triangle for n = 0:")
    display_triangle(triangle_0)
    
    # Correct output for n = 1
    triangle_1 = pascal_triangle(1)
    print("Pascal's triangle for n = 1:")
    display_triangle(triangle_1)
    
    # Correct output for n = 5
    triangle_5 = pascal_triangle(5)
    print("Pascal's triangle for n = 5:")
    display_triangle(triangle_5)
    
    # Correct output for n = 10
    triangle_10 = pascal_triangle(10)
    print("Pascal's triangle for n = 10:")
    display_triangle(triangle_10)
