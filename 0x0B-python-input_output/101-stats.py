#!/usr/bin/python3
"""
Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


import sys


class StatusCodeTracker:
    """
    Class for tracking and printing status codes.
    """
    def __init__(self):
        """
        Initialize a StatusCodeTracker instance.
        """
        self.status_code_count = {
            '200': 0,
            '301': 0,
            '400': 0,
            '401': 0,
            '403': 0,
            '404': 0,
            '405': 0,
            '500': 0
        }
        self.total_file_size = 0

    def track_status_code(self, status):
        """
        Update status code counts.

        Args:
            status (str): The HTTP status code.
        """
        if status in self.status_code_count:
            self.status_code_count[status] += 1

    def print_statistics(self):
        """
        Print status code statistics.
        """
        print("Total file size: {:d}".format(self.total_file_size))
        for code, count in sorted(self.status_code_count.items()):
            if count > 0:
                print("{}: {:d}".format(code, count))


if __name__ == "__main__":
    code_tracker = StatusCodeTracker()
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count % 10 == 0 and line_count != 0:
                code_tracker.print_statistics()

            try:
                parts = [x for x in line.split() if x.strip()]
                status_code = parts[-2]
                code_tracker.track_status_code(status_code)
                code_tracker.total_file_size += int(parts[-1].strip("\n"))
            except (IndexError, ValueError):
                pass
            line_count += 1
    except KeyboardInterrupt:
        code_tracker.print_statistics()
        raise
    code_tracker.print_statistics()
