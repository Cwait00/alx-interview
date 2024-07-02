#!/usr/bin/python3


def isWinner(x, nums):
    """
    This function determines the winner of the Prime Game based on
    optimal play.

    Args:
        x: Number of rounds in the game.
        nums: List of consecutive integers representing the starting
              set for each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben").
             None if the winner cannot be determined.
    """
    maria_wins = 0
    ben_wins = 0
    for _ in range(x):
        # Pre-calculate primes for efficiency (Sieve of Eratosthenes)
        primes = sieve(max(nums))
        # Track remaining numbers and removed numbers
        remaining = set(nums)
        removed = set()
        turn = "Maria"  # Maria always goes first

        while primes:
            # Find the smallest prime that can be removed by the current player
            smallest_prime = min(p for p in primes if p in remaining)
            removed.update(set(range(smallest_prime, max(nums) + 1,
                                     smallest_prime)))
            remaining.difference_update(removed)
            # Update turn and remove primes from available options
            primes.remove(smallest_prime)
            turn = "Ben" if turn == "Maria" else "Maria"

            if not remaining.intersection(primes):
                if turn == "Maria":
                    maria_wins += 1
                else:
                    ben_wins += 1
                break

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None


def sieve(n):
    """
    This function implements the Sieve of Eratosthenes to find all primes
    up to a limit.

    Args:
        n: Upper limit for finding primes.

    Returns:
        set: Set of all prime numbers less than or equal to n.
    """
    primes = set(range(2, n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if i in primes:
            primes.difference_update(set(range(i * i, n + 1, i)))
    return primes


if __name__ == "__main__":
    winner = isWinner(3, [4, 5, 1])
    print("Winner:", winner)
