#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys


def print_stats(total_size, status_counts):
    """Print the current statistics"""
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_counts[status_code]))


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

            # Parse the line according to the expected format
            try:
                # Split by spaces and get the last two parts (status code and file size)
                parts = line.split()
                if len(parts) < 2:
                    continue

                # Try to get status code and file size from end
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                # Only count if status code is in our valid list
                if status_code in status_counts:
                    status_counts[status_code] += 1
                    total_size += file_size
                    line_count += 1

                    # Print stats every 10 lines
                    if line_count % 10 == 0:
                        print_stats(total_size, status_counts)

            except (ValueError, IndexError):
                # Try alternative parsing - maybe there are extra spaces
                try:
                    # Remove extra whitespace and try again
                    clean_line = ' '.join(line.split())
                    parts = clean_line.split()
                    if len(parts) >= 2:
                        status_code = int(parts[-2])
                        file_size = int(parts[-1])

                        if status_code in status_counts:
                            status_counts[status_code] += 1
                            total_size += file_size
                            line_count += 1

                            # Print stats every 10 lines
                            if line_count % 10 == 0:
                                print_stats(total_size, status_counts)
                except (ValueError, IndexError):
                    # Skip lines that don't match any expected format
                    continue

    except KeyboardInterrupt:
        pass

    # Print final stats
    print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
