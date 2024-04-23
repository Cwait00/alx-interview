#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle

def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))

if __name__ == "__main__":
    triangle = pascal_triangle(5)
    print_triangle(triangle)
