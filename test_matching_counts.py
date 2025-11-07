import unittest

from matching_counts import count_matching


class TestCountMatching(unittest.TestCase):
    def test_basic_case(self):
        matrix = [[1, 2, 1], [0, 3, 4], [1, 1, 0]]
        self.assertEqual(count_matching(matrix, 1), 4)

    def test_no_match(self):
        matrix = [[5, 6], [7, 8]]
        self.assertEqual(count_matching(matrix, 1), 0)

    def test_all_match(self):
        matrix = [[2, 2], [2, 2]]
        self.assertEqual(count_matching(matrix, 2), 4)

    def test_single_row(self):
        matrix = [[1, 1, 1, 0]]
        self.assertEqual(count_matching(matrix, 1), 3)

    def test_single_column(self):
        matrix = [[5], [5], [0]]
        self.assertEqual(count_matching(matrix, 5), 2)

    def test_empty_matrix(self):
        matrix = []
        self.assertEqual(count_matching(matrix, 1), 0)

    def test_matrix_with_empty_rows(self):
        matrix = [[], [], []]
        self.assertEqual(count_matching(matrix, 1), 0)

    def test_negative_numbers(self):
        matrix = [[-1, 0], [1, -1]]
        self.assertEqual(count_matching(matrix, -1), 2)


if __name__ == "__main__":
    unittest.main()
