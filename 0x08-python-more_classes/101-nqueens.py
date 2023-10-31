#!/usr/bin/python3
"""
N-Queens Backtracking Solver to Find Non-Attacking Queen Placements
Prints the coordinates of N queens on an NxN chessboard, ensuring that they are
in non-attacking positions.
"""

from sys import argv

if __name__ == "__main__":
    chessbd = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # Initialize the chessboard representation
    for row in range(n):
        chessbd.append([row, None])

    def is_queen_in_column(column):
        """Check if a queen already exists in the same column."""
        for row in range(n):
            if column == chessbd[row][1]:
                return True
        return False

    def is_solution_rejected(row, column):
        """Determine whether or not to reject the solution."""
        if is_queen_in_column(column):
            return False
        current_row = 0
        while current_row < row:
            if abs(chessbd[current_row][1] - column) == abs(current_row - row):
                return False
            current_row += 1
        return True

    def clear_board_from_row(row):
        """Clear the board from the point of failure onward."""
        for r in range(row, n):
            chessbd[r][1] = None

    def solve_nqueens(row):
        """Recursive backtracking function to find the solution."""
        for column in range(n):
            clear_board_from_row(row)
            if is_solution_rejected(row, column):
                chessbd[row][1] = column
                if row == n - 1:
                    print(chessbd)  # Accepts the solution
                else:
                    solve_nqueens(row + 1)  # Move on to the next row to cont

    # Start the recursive process at row = 0
    solve_nqueens(0)
