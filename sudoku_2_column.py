# The program is the 2nd part of the sudoku checking, checking the columns.
# The program sends a sudoku matrix to function `column_check()`,
# the function would check if the specific column is valid.


def column_check(sudoku, column_no):
    """
    Checks if a given column in a Sudoku grid is valid.
    A column is valid if numbers 1 to 9 appear at most once (0s are ignored).

    @param sudoku [list]: list of list of int, the Sudoku grid
    @param column_no [list]: the index of the column to check (0 based)

    @return [bool], returns True if the column is correct, False otherwise.
    """

    # TODO: use set() to create a new set to record checked position. Since set doesn't allow unique items, if the set contains the same number, we know that there is a conflict
    checked_numbers = set()

    for row in sudoku:
        # TODO: get the number using `column_no` as the index of the list item
        num = row[column_no]
        # TODO: If the number is not 0, then we check if the number is already in the set. If the number in the set, it means this number exists, directly return False; otherwise add this number to the set, and continue until all numbers are checked.
        if num != 0:
            if num in checked_numbers:
                return False
            else:
                checked_numbers.add(num)

    return True


if __name__ == "__main__":
    sudoku = [
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

    print(column_check(sudoku, 0))  # False (two 2s)
    print(column_check(sudoku, 1))  # True (no duplicates)
