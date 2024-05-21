#!/usr/bin/python3
"""
A module to validate UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if the given data set represents a valid UTF-8 encoding.

    :param data: List of integers
    :return: True if data is a valid UTF-8 encoding, else False
    """
    n_bytes = 0

    for num in data:
        # Get the least significant 8 bits
        byte = num & 0xFF

        if n_bytes == 0:
            # Determine the number of bytes in the character
            if (byte >> 5) == 0b110:
                n_bytes = 1
            elif (byte >> 4) == 0b1110:
                n_bytes = 2
            elif (byte >> 3) == 0b11110:
                n_bytes = 3
            elif (byte >> 7):
                return False
        else:
            # Check if the byte is a valid continuation byte
            if (byte >> 6) != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0
