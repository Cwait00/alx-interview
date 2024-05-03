#!/usr/bin/python3

"""This module provides a function canUnlockAll to determine if all boxes
    in a given list of boxes can be unlocked."""

import subprocess


def canUnlockAll(boxes):
    """
    Determine if all boxes in the given list of boxes can be unlocked.

    Args:
        boxes (list): A list of lists where each sublist represents a box,
        and the elements of the sublist represent the keys
        contained in that box.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)


# Test the function with the given test cases
test_cases = [
    ([[1], [2], [3], [4], []], True),
    ([[1, 4, 5], [2], [5, 2], [3], [4, 1], [3, 5]], True),
    ([[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]], True),
    ([[0]], True),
    # Additional test cases
    # Test case: 12 boxes with random keys
    ([[1, 2], [0], [3], [4], [5], [6], [7], [8], [9], [10], [11], []], False),
    # Test case: 1000 boxes with all keys in each box
    ([[i for i in range(1000)] for _ in range(1000)], True),
    # Test case: Specific key configurations
    ([[10, 3, 8, 9, 6, 5, 8, 1], [8, 5, 3, 7, 1, 8, 6], [5, 1, 9, 1], [],
      [6, 6, 9, 4, 3, 2, 3, 8, 5], [9, 4],
      [4, 2, 5, 1, 1, 6, 4, 5, 6], [9, 5, 8, 8], [6, 2, 8, 6]], True),
    ([[7, 5], [1, 10, 7], [9, 6, 10], [7, 9], [2], [7, 3], [7, 9, 10],
      [10, 8, 9, 2, 5], [7, 2, 2, 4, 4, 2, 4, 8, 7],
      [4, 2, 9, 6, 6, 5, 5]], False)
]

for test_input, expected_output in test_cases:
    actual_output = canUnlockAll(test_input)
    if actual_output != expected_output:
        print("Test failed for input:")
        print(test_input)
        print("Expected output:", expected_output)
        print("Actual output:", actual_output)


# PEP8 validation
def pep8_check():
    result = subprocess.run(['flake8', __file__], stdout=subprocess.PIPE)
    if result.returncode == 0:
        print("PEP8 validation passed.")
    else:
        print("PEP8 validation failed.")
        print(result.stdout.decode('utf-8'))


pep8_check()
