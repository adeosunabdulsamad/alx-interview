#!/usr/bin/python3
"""
Determines the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Calculate the minimum number of coins required to meet a given total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount to meet.

    Returns:
        int: smallest coins to meet the total, or -1 if impossible.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        if total == 0:
            break
        count = total // coin
        num_coins += count
        total -= count * coin

    return num_coins if total == 0 else -1
