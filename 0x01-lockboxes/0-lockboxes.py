#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Parameters:
    boxes (list of lists): List of boxes, where each box contains keys
                           to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        current = stack.pop()
        for key in boxes[current]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [
        [1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]
    ]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [
        [1, 2], [0], [3], [4], [5], [6], [7], [8], [9], [10], [11], []
    ]
    print(canUnlockAll(boxes))  # Expected output: False

    boxes = [
        [4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]
    ]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [[0]]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [
        [10, 3, 8, 9, 6, 5, 8, 1], [8, 5, 3, 7, 1, 8, 6], [5, 1, 9, 1], [],
        [6, 6, 9, 4, 3, 2, 3, 8, 5], [9, 4], [4, 2, 5, 1, 1, 6, 4, 5, 6],
        [9, 5, 8, 8], [6, 2, 8, 6]
    ]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [
        [7, 5], [1, 10, 7], [9, 6, 10], [7, 9], [2], [7, 3],
        [7, 9, 10, 10, 8, 9, 2, 5], [7, 2, 2, 4, 4, 2, 4, 8, 7],
        [4, 2, 9, 6, 6, 5, 5]
    ]
    print(canUnlockAll(boxes))  # Expected output: False
