# This program sends a list of strings into function `longest_string()`
# The function returns the index of the longest string in the list.


def longest_string(strings):
    """
    Returns the longest string in the given list of strings.

    @param strings [list]: The list of strings to search.
    @retrurn [int]: The index of the longest string in the given list.
    """

    index_of_longest = 0  # assume the longest string is the first one

    # TODO: write a loop, if the string in current iteration is longer
    # update the variable `index_of_longest`
    for i in range(1, len(strings)):
        if len(strings[i]) > len(strings[index_of_longest]):
            index_of_longest = i

    return index_of_longest


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest_string(strings))
