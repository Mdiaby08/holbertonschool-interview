#!/usr/bin/python3
"""
Module for the lockboxes problem.
Determines if all boxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Returns True if all boxes can be opened, else False.
    """
    n = len(boxes)
    opened = set([0])
    keys = set(boxes[0])

    changed = True
    while changed:
        changed = False
        for key in list(keys):
            if key < n and key not in opened:
                opened.add(key)
                keys.update(boxes[key])
                changed = True

    return len(opened) == n
