#!/usr/bin/python3
"""a project with the function minoperations"""


def minOperations(n):
    """
    returns the fewest number of operation need to result in exactly
    n H characters in the file
    """
    operations = 0
    b = 2
    while n > 1:
        while n % b == 0:
            operations += b
            n = n / b
        b += 1
    return operations
