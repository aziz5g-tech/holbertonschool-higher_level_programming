#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys


def print_stats(total_size, status_counts):
    """Print the current statistics"""
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")


def main():
    """Main function to process log lines and compute metrics"""
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0,
                     401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue

            # Parse the line
            try:
                parts = line.split()
                if len(parts) >= 2:
                    # Get status code and file size (last two elements)
                    status_code = int(parts[-2])
                    file_size = int(parts[-1])

                    # Update counters if status code is valid
                    if status_code in status_counts:
                        status_counts[status_code] += 1
                        total_size += file_size
                        line_count += 1

                        # Print stats every 10 lines
                        if line_count % 10 == 0:
                            print_stats(total_size, status_counts)
            except (ValueError, IndexError):
                # Skip invalid lines
                continue

    except KeyboardInterrupt:
        # Print final stats on CTRL+C
        print_stats(total_size, status_counts)

    # Print final stats at the end if there are any processed lines
    if line_count > 0:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
