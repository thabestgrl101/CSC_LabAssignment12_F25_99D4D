# The program is the 1st part of the sudoku checking, checking on the rows.
# The program sends a sudoku matrix to function `row_check()`,
# the function would check if the specific row is valid.


def row_check(sudoku, row_no):
    """
    Checks if a given row in a Sudoku grid is valid.
    A row is valid if numbers 1 to 9 appear at most once (0s are ignored).

    @param sudoku [list]: list of list of int, the Sudoku grid
    @param row_no [list]: the index of the row to check (0 based)

    @return [bool], returns True if the row is correct, False otherwise.
    """

    # TODO: use set() to create a new set to record checked position. Since set doesn't allow unique items, if the set contains the same number, we know that there is a conflict
    checked_numbers = set()

    row_to_check = sudoku[row_no]  # get the row to check

    for num in row_to_check:
        # TODO: use loop to check every item of the row. If the number is not 0, then we check if the number is already in the set. If the number in the set, it means this number exists, directly return False; otherwise add this number to the set, and continue until all numbers are checked.
        if num != 0:
            if num in checked_numbers:
                return False
            else:
                checked_numbers.add(num)

    # TODO: return True if the loop terminates normally (all numbers are checked without duplication found)
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

    print(row_check(sudoku, 0))  # True (no duplicates)
    print(row_check(sudoku, 1))  # False (two 2s)
