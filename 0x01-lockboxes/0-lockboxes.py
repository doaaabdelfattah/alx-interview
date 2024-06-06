#!/usr/bin/python3
'''
Pascal Triangle
'''


def canUnlockAll(boxes):
    '''
    Lockboxes coding problem
    '''
    for key in range(1, len(boxes)):
        flag = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                flag = True
                break
        if not flag:
            return False

    return True


# 1. box is list of Lists
# boxes = [[], [], [], []]
# 2. boxes[0] UNLOCKED
# Each box contains a list of keys
# each key being an integer that corresponds to the number of another box
# ==== Target === Determine if all boxes can be opened starting from box 0.
# Example usage
