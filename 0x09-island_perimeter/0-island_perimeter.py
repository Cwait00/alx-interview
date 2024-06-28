#!/usr/bin/python3
"""
This module contains the function to calculate the perimeter of an island
in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    :param grid: List of list of integers where 0 represents water
                 and 1 represents land.
    :return: Integer representing the perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4  # Each land cell contributes 4 initially

                # Check for adjacent land cells and subtract for shared edges
                if r > 0 and grid[r-1][c] == 1:  # Up
                    perimeter -= 1
                if r < rows-1 and grid[r+1][c] == 1:  # Down
                    perimeter -= 1
                if c > 0 and grid[r][c-1] == 1:  # Left
                    perimeter -= 1
                if c < cols-1 and grid[r][c+1] == 1:  # Right
                    perimeter -= 1

    return perimeter
