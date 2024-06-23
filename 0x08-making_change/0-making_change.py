#!/usr/bin/python3
"""
This module contains the makeChange function.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total amount.
    :param coins: List of coin denominations.
    :param total: The total amount.
    :return: Fewest number of coins needed to meet the total,
    or -1 if it cannot be met.
    """
    if total <= 0:
        return 0

    max_coin = max(coins)
    if total > max_coin * total:
        return -1

    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case

    # Fill dp array using the recurrence relation
    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


# Main function for testing
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Expected output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
