#!/usr/bin/python3
"""
Module qui calcule le nombre minimal d'opérations 
"""


def minOperations(n):
    if n < 2:
        return 0

    total_operations = 0
    divisor = 2

    while divisor <= n:
        while n % divisor == 0:
            total_operations += divisor
            n //= divisor
        divisor += 1

    return total_operations
