import unittest

from sudoku_2_column import column_check


class TestColumnCheck(unittest.TestCase):
    def setUp(self):
        # New Sudoku matrix for testing
        self.sudoku = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
        # This is a valid starting Sudoku board (no duplicate in any column)

    def test_valid_column(self):
        # Column 0 (5,6,0,8,4,7,0,0,0)
        self.assertTrue(column_check(self.sudoku, 0))

    def test_invalid_column(self):
        sudoku_invalid = [row[:] for row in self.sudoku]
        sudoku_invalid[0][0] = 6  # duplicate '6' in column 0
        self.assertFalse(column_check(sudoku_invalid, 0))

    def test_all_zeros_column(self):
        sudoku = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertTrue(column_check(sudoku, 1))

    def test_column_with_duplicates(self):
        sudoku = [
            [1, 2, 3],
            [4, 5, 3],
            [7, 8, 3],
        ]
        self.assertFalse(column_check(sudoku, 2))

    def test_column_with_valid_numbers(self):
        sudoku = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self.assertTrue(column_check(sudoku, 2))

    def test_invalid_column_index(self):
        with self.assertRaises(IndexError):
            column_check(self.sudoku, 15)

    def test_irregular_sudoku(self):
        sudoku = [
            [1, 2],
            [3],
            [4, 5, 6],
        ]
        self.assertTrue(column_check(sudoku, 0))


if __name__ == "__main__":
    unittest.main()
