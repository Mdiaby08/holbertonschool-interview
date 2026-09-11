#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
 triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev = triangle[-1]
