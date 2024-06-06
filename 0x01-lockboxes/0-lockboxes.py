#!/usr/bin/python3
from collections import deque
'''
Pascal Triangle
'''


def canUnlockAll(boxes):
    '''
    Lockboxes coding problem
    '''
    visited = set()
    boxesNumber = len(boxes)
    # Create a queue
    queue = deque([0])
    visited.add(0)

    # Iterate over the queue
    while queue:
        # get the current box
        current_box = queue.popleft()
        # Check if the current box has no keys
        if not boxes[current_box]:
            break
        # if the box is already opened
        # if current_box in visited:
        #     queue.append(key)
        #     continue
        # Open the box
        visited.add(current_box)
        # Add the keys from the current box to the queue
        for key in boxes[current_box]:
            if key not in visited:
                queue.append(key)
                visited.add(key)

    return len(visited) == boxesNumber


# 1. box is list of Lists
# boxes = [[], [], [], []]
# 2. boxes[0] UNLOCKED
# Each box contains a list of keys
# each key being an integer that corresponds to the number of another box
# ==== Target === Determine if all boxes can be opened starting from box 0.
# Example usage
