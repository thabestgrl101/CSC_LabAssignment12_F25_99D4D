import unittest

from sudoku_1_row import row_check


class TestRowCheck(unittest.TestCase):
    def setUp(self):
        # A sample sudoku grid for testing
        self.sudoku = [
            [9, 0, 0, 0, 8, 0, 3, 0, 0],  # valid
            [2, 0, 0, 2, 5, 0, 7, 0, 0],  # invalid (two 2s)
            [0, 2, 0, 3, 0, 0, 0, 0, 4],  # valid
            [2, 9, 4, 0, 0, 0, 0, 0, 0],  # valid
            [0, 0, 0, 7, 3, 0, 5, 6, 0],  # valid
            [7, 0, 5, 0, 6, 0, 4, 0, 0],  # valid
            [0, 0, 7, 8, 0, 3, 9, 0, 0],  # valid
            [0, 0, 1, 0, 0, 0, 0, 0, 3],  # valid
            [3, 0, 0, 0, 0, 0, 0, 0, 2],  # valid
        ]

    def test_valid_row(self):
        self.assertTrue(row_check(self.sudoku, 0))
        self.assertTrue(row_check(self.sudoku, 2))
        self.assertTrue(row_check(self.sudoku, 4))

    def test_invalid_row(self):
        self.assertFalse(row_check(self.sudoku, 1))

    def test_all_zeros(self):
        sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertTrue(row_check(sudoku, 0))

    def test_row_with_duplicates(self):
        sudoku = [[1, 2, 3, 4, 5, 6, 7, 8, 1]]
        self.assertFalse(row_check(sudoku, 0))

    def test_row_with_valid_numbers(self):
        sudoku = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
        self.assertTrue(row_check(sudoku, 0))

    def test_empty_row(self):
        sudoku = [[]]
        self.assertTrue(row_check(sudoku, 0))

    def test_invalid_row_index(self):
        with self.assertRaises(IndexError):
            row_check(self.sudoku, 20)


if __name__ == "__main__":
    unittest.main()
