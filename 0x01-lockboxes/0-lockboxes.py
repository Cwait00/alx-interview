#!/usr/bin/python3

"""
This module provides a function `canUnlockAll` to determine if all boxes
in a given list of boxes can be unlocked.
"""


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
if __name__ == "__main__":
    test_cases = [
        ([[1], [2], [3], [4], []], True),
        ([[1, 4, 5], [2], [5, 2], [3], [4, 1], [3, 5]], True),
        ([[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]], True),
        ([[0]], True),
        ([[1, 2], [0], [3], [4], [5], [6], [7], [8], [9], [10], [11], []],
         False),
        ([[i for i in range(1000)] for _ in range(1000)], True),
        ([[10, 3, 8, 9, 6, 5, 8, 1], [8, 5, 3, 7, 1, 8, 6], [5, 1, 9, 1], [],
          [6, 6, 9, 4, 3, 2, 3, 8, 5], [9, 4],
          [4, 2, 5, 1, 1, 6, 4, 5, 6], [9, 5, 8, 8], [6, 2, 8, 6]], True),
        ([[7, 5], [1, 10, 7], [9, 6, 10], [7, 9], [2], [7, 3], [7, 9, 10],
          [10, 8, 9, 2, 5], [7, 2, 2, 4, 4, 2, 4, 8, 7],
          [4, 2, 9, 6, 6, 5, 5]], False)
    ]

    for test_input, expected_output in test_cases:
        actual_output = canUnlockAll(test_input)
        assert actual_output == expected_output, (
            f"Test failed for input: {test_input}\n"
            f"Expected: {expected_output}\n"
            f"Got: {actual_output}"
        )
