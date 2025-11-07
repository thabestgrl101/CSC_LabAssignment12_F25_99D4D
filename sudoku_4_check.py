# This program combines row checking, column checking, and block checking,
# it could use all three functions written in other Sudoku program.

from sudoku_1_row import row_check
from sudoku_2_column import column_check
from sudoku_3_block import block_check


def sudoku_grid_correct(sudoku: list):
    """
    Checks if the entire Sudoku grid is valid:
    - Each row is correct
    - Each column is correct
    - Each 3x3 block is correct
    """

    # Check all rows
    for row in range(9):
        # TODO: call function row_check(), if any row returns False, return False.
        if not row_check(sudoku, row):
             return False

    # Check all columns
    for col in range(9):
        #TODO: call function column_check(), if any column returns False, return False
        if not column_check(sudoku, col):
            return False

    # Check all 3x3 blocks
    # TODO: use two levels of for loop to send all the possible standing indices which are: (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6).
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):

            # the following two lines are inside the nested for loop
            if not block_check(sudoku, row, col):
                return False

    return True


if __name__ == "__main__":
    sudoku_invalid = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
    ]
    print(sudoku_grid_correct(sudoku_invalid))  # False

    sudoku_valid = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]
    print(sudoku_grid_correct(sudoku_valid))  # True
