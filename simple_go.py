# This program sends a Go board to the function `who_won()`, and the function
# returns who won the game based on the board.
#
# The scoring rules of Go is quite complex, but in this exercise, we just
# count the number of pieces each player has on the game board.
# Also, please notice that we don't have the size limitation on the board.


def who_won(board):
    """
    Determines the winner based on the number of stones on the board.

    @param board [list]: list of list of int, which is the Go board.
        On the board:
            0 represents the empty spot
            1 represents the player 1's stone
            2 represents the player 2's stone

    @return [int]: return 1 if player 1 won, 2 if player 2 won, 0 if tie.
    """

    # TODO: initialize two variables to record the stones of two players
    player1_count = 0
    player2_count = 0

    # TODO: use two level loop to check the value of every spot, which is the item of the nested list, read the documentation for details
    for row in board:
        for spot in row:
            if spot == 1:
                player1_count += 1
            elif spot == 2:
                player2_count += 1

    if player1_count > player2_count:
        return 1
    elif player2_count > player1_count:
        return 2
    else:
        return 0


if __name__ == "__main__":
    board = [[1, 0, 2], [2, 1, 1], [1, 2, 0]]
    print(who_won(board))
