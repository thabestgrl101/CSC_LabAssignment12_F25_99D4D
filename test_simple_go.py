import unittest

from simple_go import who_won


class TestWhoWon(unittest.TestCase):
    def test_player1_wins(self):
        board = [[1, 0, 2], [2, 1, 1], [1, 2, 0]]
        self.assertEqual(who_won(board), 1)

    def test_player2_wins(self):
        board = [[2, 2, 0], [0, 2, 1], [1, 2, 1]]
        self.assertEqual(who_won(board), 2)

    def test_tie(self):
        board = [[1, 2], [2, 1]]
        self.assertEqual(who_won(board), 0)

    def test_all_empty(self):
        board = [[0, 0], [0, 0]]
        self.assertEqual(who_won(board), 0)

    def test_player1_only(self):
        board = [[1, 1, 1], [1, 1, 1]]
        self.assertEqual(who_won(board), 1)

    def test_player2_only(self):
        board = [[2, 2], [2, 2], [2, 2]]
        self.assertEqual(who_won(board), 2)

    def test_irregular_board_size(self):
        board = [[1, 1, 2], [2], [1, 2, 1, 2, 2]]
        self.assertEqual(who_won(board), 2)

    def test_large_board(self):
        board = [[1] * 10 + [2] * 9] * 5  # player 1 always wins by 5 stones
        self.assertEqual(who_won(board), 1)

    def test_empty_board(self):
        board = []
        self.assertEqual(who_won(board), 0)


if __name__ == "__main__":
    unittest.main()
