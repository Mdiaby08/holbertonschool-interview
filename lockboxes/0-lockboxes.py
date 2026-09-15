#!/usr/bin/python3
def canUnlockAll(boxes):
    opened = [0]                 # on commence avec la boîte 0
    keys = boxes[0].copy()       # clés trouvées dans la boîte 0

    for key in keys:
        if key < len(boxes) and key not in opened:
            opened.append(key)
            for new_key in boxes[key]:
                if new_key not in keys:
                    keys.append(new_key)

    return opened

