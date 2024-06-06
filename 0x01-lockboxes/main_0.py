#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes), "\t: True")

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes), "\t: True")

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes), "\t: False")

# All boxes can be opened, even if some boxes are empty
boxes = [[], [0, 2], [1]]
print(canUnlockAll(boxes), "\t: True")  # Output: True

# Only one box, which is already open
boxes = [[]]
print(canUnlockAll(boxes), "\t: True")  # Output: True

# Box 1 cannot be opened
boxes = [[1], [3], [2], []]
print(canUnlockAll(boxes), "\t: False")  # Output: False

# Cyclic dependency, but all can be opened
boxes = [[1], [2], [0, 3], []]
print(canUnlockAll(boxes), "\t: True")  # Output: True

# All boxes have keys to all others
boxes = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]
print(canUnlockAll(boxes), "\t: True")  # Output: True
