#!/usr/bin/python3

import sys
import re
from collections import defaultdict

# Dictionary to store counts for each status code
status_counts = defaultdict(int)

# Total file size
total_file_size = 0

# Counter to keep track of lines read
line_count = 0


def parse_log_line(line):
    # Regular expression to extract relevant information from log line
    pattern = (
        r"(\d+\.\d+\.\d+\.\d+) - \[.*\] "
        r"\"GET /projects/260 HTTP/1.1\" (\d+) (\d+)"
    )
    # Match the pattern against the log line
    match = re.match(pattern, line)
    if match:
        ip_address, status_code, file_size = match.groups()
        return ip_address, int(status_code), int(file_size)
    else:
        return None, None, None


def print_statistics():
    global total_file_size
    global status_counts

    print("Total file size:", total_file_size)

    # Print status counts in ascending order
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        if count > 0:
            print(f"{status_code}: {count}")


def process_log_line(line):
    global total_file_size
    global line_count

    ip_address, status_code, file_size = parse_log_line(line)

    if ip_address is not None:
        # Increment the count for the status code
        status_counts[status_code] += 1

        # Add file size to the total
        total_file_size += file_size

        # Increment line count
        line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_statistics()


try:
    for line in sys.stdin:
        process_log_line(line)

except KeyboardInterrupt:
    # If Ctrl+C is pressed, print final statistics
    print_statistics()
    sys.exit(0)
