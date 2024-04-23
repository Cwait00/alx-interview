#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.
    
    Parameters:
        n (int): The number of rows in the triangle.
        
    Returns:
        list of lists: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # Start each row with 1
        prev_row = triangle[-1]  # Get the previous row
        for j in range(1, i):
            # Calculate each element by summing the numbers above and to the left
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle

def print_triangle(triangle):
    """
    Prints Pascal's Triangle.
    
    Parameters:
        triangle (list of lists): Pascal's Triangle.
    """
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))

if __name__ == "__main__":
    triangle = pascal_triangle(5)
    print_triangle(triangle)
