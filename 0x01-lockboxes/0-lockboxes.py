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

    # Number of boxes
    n = len(boxes)

    # Set to keep track of visited boxes
    visited = set()
    visited.add(0)

    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key not in visited and key < n:
                visited.add(key)
                queue.append(key)

    return len(visited) == n


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Expected output: False
