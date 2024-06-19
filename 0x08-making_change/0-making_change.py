#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Initialize dp array with infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Build the dp array
    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still infinity, return -1 as total cannot be met
    return dp[total] if dp[total] != float('inf') else -1

# Testing the function
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Expected output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
