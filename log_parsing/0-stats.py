#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""
import sys


def print_stats(total_size, status_counts):
    """Print the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    total_size = 0
    status_counts = {}
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            # <IP> - [<date> <time>] "GET /projects/260 HTTP/1.1" <code> <size>
            if len(parts) < 7:
                continue
            try:
                size = int(parts[-1])
                code = parts[-2]
                if code in valid_codes:
                    status_counts[int(code)] = \
                        status_counts.get(int(code), 0) + 1
                total_size += size
                count += 1
            except (ValueError, IndexError):
                continue

            if count % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    print_stats(total_size, status_counts)
