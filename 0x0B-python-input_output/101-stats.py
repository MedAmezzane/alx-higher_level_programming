#!/usr/bin/python3
"""
Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_accumulated_metrics(total_file_size, status_code_counts):
    """Print accumulated metrics.

    Args:
        total_file_size (int): The accumulated total file size.
        status_code_counts (dict): The accumulated count of status codes.
    """
    print("Total file size: {}".format(total_file_size))
    for code, count in sorted(status_code_counts.items()):
        print("{}: {}".format(code, count))


if __name__ == "__main":
    import sys

    total_file_size = 0
    status_code_counts = {}
    valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_accumulated_metrics(total_file_size, status_code_counts)
                line_count = 1
            else:
                line_count += 1

            line = line.split()

            try:
                total_file_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_status_codes:
                    if line[-2] not in status_code_counts:
                        status_code_counts[line[-2]] = 1
                    else:
                        status_code_counts[line[-2]] += 1
            except IndexError:
                pass

        print_accumulated_metrics(total_file_size, status_code_counts)

    except KeyboardInterrupt:
        print_accumulated_metrics(total_file_size, status_code_counts)
        raise
