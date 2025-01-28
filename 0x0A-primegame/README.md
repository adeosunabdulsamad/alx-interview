# 0x0A. Prime Game

## Description

This project involves solving the **Prime Game**, a strategic game played between two players, Maria and Ben. The game is based on prime numbers and requires leveraging concepts of algorithms, prime number computation, and game theory to determine the winner.

## Rules of the Game

1. Maria and Ben take turns; Maria always starts first.
2. The game is played with a set of consecutive integers from `1` to `n`.
3. During their turn, a player picks a prime number from the set and removes that number and all its multiples from the set.
4. The player who cannot make a move loses the game.

The task is to determine the winner after `x` rounds, where each round has a different value of `n`. Both players play optimally.

## Prototype

```python
def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Arguments:
    - x (int): Number of rounds.
    - nums (list of int): Array of integers representing the upper bound for each round.

    Returns:
    - str: "Maria" if Maria wins more rounds, "Ben" if Ben wins more rounds, or None if there's no clear winner.
    """
