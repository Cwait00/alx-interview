#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determines the winner of the Prime Game based on optimal play.

    Args:
        x: Number of rounds in the game.
        nums: List of consecutive integers representing the starting
              set for each round.

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
        return [p for p, prime in enumerate(is_prime) if prime]

    max_num = max(nums)
    primes = sieve(max_num)

    def count_primes(n):
        """Counts primes up to n."""
        count = 0
        for prime in primes:
            if prime <= n:
                count += 1
            else:
                break
        return count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes(n)
        if prime_count % 2 == 1:
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
