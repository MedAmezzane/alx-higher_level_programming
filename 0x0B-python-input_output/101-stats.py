#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After processing every ten lines or encountering a keyboard interruption
(CTRL + C), this script prints the following statistics:
- Total file size up to that point.
- Count of read status codes up to that point.
"""


def print_stats(total_file_size, status_code_counts):
    """Print accumulated metrics.

    Args:
        total_file_size (int): The accumulated total file size.
        status_code_counts (dict): The accumulated count of status codes.
    """
    print("Total file size: {}".format(total_file_size))
    for code in sorted(status_code_counts):
        print("{}: {}".format(code, status_code_counts[code]))


if __name__ == "__main":
    import sys

    total_file_size = 0
    status_code_counts = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_stats(total_file_size, status_code_counts)
                line_count = 1
            else:
                line_count += 1

            line_parts = line.split()

            try:
                total_file_size += int(line_parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line_parts[-2] in valid_codes:
                    if line_parts[-2] not in status_code_counts:
                        status_code_counts[line_parts[-2]] = 1
                    else:
                        status_code_counts[line_parts[-2]] += 1
            except IndexError:
                pass

        print_stats(total_file_size, status_code_counts)

    except KeyboardInterrupt:
        print_stats(total_file_size, status_code_counts)
        raise
