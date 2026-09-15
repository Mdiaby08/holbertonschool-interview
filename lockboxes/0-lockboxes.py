#!/usr/bin/python3
"""
Module for the lockboxes problem.
Determines which boxes can be opened based on available keys.
"""

def canUnlockAll(boxes):
    """
    Returns a list of opened boxes.
    The first box (0) is always unlocked.
    """
    opened = [0]
    keys = boxes[0].copy()

    for key in keys:
        if key < len(boxes) and key not in opened:
            opened.append(key)
            for new_key in boxes[key]:
                if new_key not in keys:
                    keys.append(new_key)

    return opened
