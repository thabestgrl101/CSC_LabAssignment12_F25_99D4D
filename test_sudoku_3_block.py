import unittest

from sudoku_3_block import block_check


class TestBlockCheck(unittest.TestCase):
    def setUp(self):
        # A Sudoku board adapted from a valid configuration
        self.sudoku = [
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
        # This Sudoku board is fully valid — all 3x3 blocks are correct

    def test_valid_block(self):
        # Top-left block (0,0)
        self.assertTrue(block_check(self.sudoku, 0, 0))
        # Center block (3,3)
        self.assertTrue(block_check(self.sudoku, 3, 3))
        # Bottom-right block (6,6)
        self.assertTrue(block_check(self.sudoku, 6, 6))

    def test_invalid_block_duplicate(self):
        sudoku_invalid = [row[:] for row in self.sudoku]
        sudoku_invalid[0][0] = 3  # Duplicate 3 in top-left block
        self.assertFalse(block_check(sudoku_invalid, 0, 0))

    def test_block_with_zeros(self):
        sudoku = [
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
        self.assertTrue(block_check(sudoku, 0, 0))  # No duplicates among nonzero values

    def test_invalid_indices(self):
        # row_no or column_no outside 0–6 should cause IndexError
        with self.assertRaises(IndexError):
            block_check(self.sudoku, 7, 0)
        with self.assertRaises(IndexError):
            block_check(self.sudoku, 0, 7)

    def test_partial_block(self):
        # a smaller board, not full 9x9
        sudoku = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self.assertTrue(block_check(sudoku, 0, 0))

    def test_duplicate_in_middle_block(self):
        sudoku_invalid = [row[:] for row in self.sudoku]
        sudoku_invalid[3][3] = 5  # duplicate 5 in middle block (3,3)
        self.assertFalse(block_check(sudoku_invalid, 3, 3))


if __name__ == "__main__":
    unittest.main()
