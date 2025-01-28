#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.
    Arguments:
    - x: number of rounds
    - nums: list of integers for each round
    Returns:
    - Name of player with most wins, or None if no winner.
    """
    if not nums or x < 1:
        return None

    def sieve_of_eratosthenes(limit):
        """Returns a list of primes up to the given limit."""
        is_prime = [True] * (limit + 1)
        is_prime[0], is_prime[1] = False, False
        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        return [i for i, prime in enumerate(is_prime) if prime]

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    prime_count = [0] * (max_num + 1)

    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1]
        if i in primes:
            prime_count[i] += 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
