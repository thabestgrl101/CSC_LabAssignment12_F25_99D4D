import unittest

from sudoku_1_row import row_check
from sudoku_2_column import column_check
from sudoku_3_block import block_check
from sudoku_4_check import sudoku_grid_correct


class TestSudoku(unittest.TestCase):
    def setUp(self):
        # Valid Sudoku board
        self.sudoku_valid = [
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

        # Invalid Sudoku board (duplicate 5 in row 0)
        self.sudoku_invalid_row = [
            [5, 3, 5, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ]

        # Invalid Sudoku board (duplicate 6 in column 0)
        self.sudoku_invalid_col = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [5, 7, 2, 1, 9, 5, 3, 4, 8],  # duplicate 5 in column 0
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ]

        # Invalid Sudoku board (duplicate 9 in top-left block)
        self.sudoku_invalid_block = [
            [9, 3, 4, 6, 7, 8, 9, 1, 2],
            [9, 7, 2, 1, 9, 5, 3, 4, 8],  # duplicate 9 in top-left 3x3 block
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ]

    # --- Row checks ---
    def test_row_check_valid(self):
        for i in range(9):
            self.assertTrue(row_check(self.sudoku_valid, i))

    def test_row_check_invalid(self):
        self.assertFalse(row_check(self.sudoku_invalid_row, 0))

    # --- Column checks ---
    def test_column_check_valid(self):
        for i in range(9):
            self.assertTrue(column_check(self.sudoku_valid, i))

    def test_column_check_invalid(self):
        self.assertFalse(column_check(self.sudoku_invalid_col, 0))

    # --- Block checks ---
    def test_block_check_valid(self):
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                self.assertTrue(block_check(self.sudoku_valid, row, col))

    def test_block_check_invalid(self):
        self.assertFalse(block_check(self.sudoku_invalid_block, 0, 0))

    # --- Full grid check ---
    def test_full_grid_valid(self):
        self.assertTrue(sudoku_grid_correct(self.sudoku_valid))

    def test_full_grid_invalid_row(self):
        self.assertFalse(sudoku_grid_correct(self.sudoku_invalid_row))

    def test_full_grid_invalid_column(self):
        self.assertFalse(sudoku_grid_correct(self.sudoku_invalid_col))

    def test_full_grid_invalid_block(self):
        self.assertFalse(sudoku_grid_correct(self.sudoku_invalid_block))


if __name__ == "__main__":
    unittest.main()
