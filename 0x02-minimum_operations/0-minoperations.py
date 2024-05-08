#!/usr/bin/python3


"""
This script defines a function to calculate the minimum number of operations
needed to result in exactly n 'H' characters in the file.

"""

def minOperations(n):
    """

    Calculate the minimum number of operations needed to result in exactly n
    'H' characters in the file.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations needed.
    """

    if n <= 1:
        return 0

    operations = 0
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1
    return operations


# Testing the function
if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format(
        n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(
        n, minOperations(n)))
