#!/usr/bin/python3

def canUnlockAll(box_keys):
    visited_boxes = set()

    def dfs(box):
        visited_boxes.add(box)
        for key in box_keys[box]:
            if key not in visited_boxes:
                dfs(key)

    dfs(0)
    return len(visited_boxes) == len(box_keys)

# Test the function
if __name__ == "__main__":
    box_keys = [[1], [2], [3], [4], []]
    print(canUnlockAll(box_keys)) # True

    box_keys = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(box_keys)) # True

    box_keys = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(box_keys)) # False
