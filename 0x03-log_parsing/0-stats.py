#!/usr/bin/python3
import sys
import re
import signal
from collections import defaultdict

# Regular expression pattern to match the log line format
log_pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+) \-\ \[(.+)\]'
                         r' "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$')

# Initialize variables to store metrics
total_file_size = 0
status_code_count = defaultdict(int)
line_count = 0


# Function to print statistics
def print_statistics():
    print("Total file size:", total_file_size)
    print("Number of lines by status code:")
    for code in sorted(status_code_count.keys()):
        print(f"{code}: {status_code_count[code]}")
    print()


# Signal handler for KeyboardInterrupt
def signal_handler(sig, frame):
    print("\nCtrl+C detected. Printing statistics:")
    print_statistics()
    sys.exit(0)


# Register signal handler for KeyboardInterrupt
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            groups = match.groups()
            if len(groups) == 4:
                ip_address, date, status_code, file_size = groups
                status_code = int(status_code)
                file_size = int(file_size)

                total_file_size += file_size
                status_code_count[status_code] += 1
                line_count += 1

                # Print statistics after every 10 lines
                if line_count % 10 == 0:
                    print_statistics()
            else:
                print(f"Invalid log line format: {line}", file=sys.stderr)
        else:
            print(f"Invalid log line format: {line}", file=sys.stderr)

except KeyboardInterrupt:
    print("\nCtrl+C detected. Printing statistics:")
    print_statistics()
