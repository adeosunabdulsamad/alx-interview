#!/usr/bin/python3
"""
Module to calculate the minimum number of operations to obtain n 'H' characters
using Copy All and Paste operations.
"""

def minOperations(n):
    """
    Calculate the minimum number of operations needed to result in exactly n 'H' characters.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations needed, or 0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor  # Copy All + Paste (for each divisor)
            n //= divisor  # Reduce n
        else:
            divisor += 1  # Move to the next divisor

    return operations
