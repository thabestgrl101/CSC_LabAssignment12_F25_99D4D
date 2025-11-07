# This program sends a matrix to the function `count_matching()`, and the
# function returns the number of matched elements in the matrix.


def count_matching(matrix, target):
    """
    Counts how many elements in the 2-dimensional nested list (matrix) match
    the given target value.

    @param matrix [list]: list of list of integers
    @param target [int]: the value to match
    @return [int]: the number of matching elements
    """

    # TODO: set initial variable `count`
    count = 0

    # TODO: use external loop to get all nested list
    for row in matrix:
        
    # TODO: use inner loop to get every element of the inner list, if the element is equal to the target argument, increase `count` by 1
        for element in row:
            if element == target:
                count += 1


    return count


if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 1, 0]]
    print(count_matching(m, 1))
