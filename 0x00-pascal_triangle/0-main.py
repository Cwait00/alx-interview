#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print("n = 5")
    print_triangle(pascal_triangle(5))

    print("\nn = 1")
    print_triangle(pascal_triangle(1))

    print("\nn = 0")
    print(pascal_triangle(0))

    print("\nn = 10")
    print_triangle(pascal_triangle(10))

    print("\nn = 100")
    triangle = pascal_triangle(100)
    print("[...]")  # Just to indicate output for large n is generated
    # Uncomment the following line to see the full output for n = 100
    # print_triangle(triangle)
