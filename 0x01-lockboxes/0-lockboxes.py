#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    visited = set()
    queue = [0]  # Start with the first box

    while queue:
        box = queue.pop(0)
        visited.add(box)
        keys = boxes[box]

        for key in keys:
            if key < n and key not in visited:
                queue.append(key)

    return len(visited) == n
