#!/usr/bin/python3
"""
Prime Game Module
"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game based on optimal play.

    Args:
        x (int): Number of rounds in the game.
        nums (list): List of integers representing the starting set
                     for each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben").
             None if the winner cannot be determined.
    """
    if not nums or x < 1:
        return None

    def sieve(n):
        """Implements the Sieve of Eratosthenes to find all primes up to n."""
        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False
        for p in range(2, int(n ** 0.5) + 1):
            if is_prime[p]:
                for multiple in range(p * p, n + 1, p):
                    is_prime[multiple] = False
        return is_prime

    max_num = max(nums)
    is_prime = sieve(max_num)

    # Create a prefix sum of primes up to the maximum number in nums
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None


if __name__ == "__main__":
    winner = isWinner(3, [4, 5, 1])
    print("Winner:", winner)
