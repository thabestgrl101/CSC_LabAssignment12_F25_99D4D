import unittest

from longest_string import longest_string


class TestLongestString(unittest.TestCase):
    def test_basic_list(self):
        strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
        self.assertEqual(longest_string(strings), 3)

    def test_first_is_longest(self):
        strings = ["longest", "short", "tiny"]
        self.assertEqual(longest_string(strings), 0)

    def test_last_is_longest(self):
        strings = ["a", "ab", "abc", "abcd"]
        self.assertEqual(longest_string(strings), 3)

    def test_same_length(self):
        strings = ["dog", "cat", "bat"]
        # All are length 3, expect first (index 0)
        self.assertEqual(longest_string(strings), 0)

    def test_with_empty_strings(self):
        strings = ["", "a", "ab", "", "abc"]
        self.assertEqual(longest_string(strings), 4)

    def test_all_empty_strings(self):
        strings = ["", "", ""]
        self.assertEqual(longest_string(strings), 0)


if __name__ == "__main__":
    unittest.main()
