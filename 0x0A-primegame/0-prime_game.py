#!/usr/bin/python3

def sieve(n):
    """Use the Sieve of Eratosthenes to find all primes up to n."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(n + 1) if is_prime[p]]
    return primes

def play_game(n, primes):
    """Simulate the game for a given n."""
    if n < 2:
        return "Ben"
    remaining = set(range(1, n + 1))
    current_player = "Maria"
    while True:
        move_made = False
        for prime in primes:
            if prime in remaining:
                move_made = True
                multiples = set(range(prime, n + 1, prime))
                remaining -= multiples
                current_player = "Ben" if current_player == "Maria" else "Maria"
                break
        if not move_made:
            return current_player

def isWinner(x, nums):
    """Determine the winner of each game and return the overall winner."""
    max_n = max(nums)
    primes = sieve(max_n)
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_game(n, primes)
        if winner == "Maria":
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
