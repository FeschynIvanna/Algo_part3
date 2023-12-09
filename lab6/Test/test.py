import unittest

from main import kmp_search, prefix_function


class TestKMP(unittest.TestCase):

    def test_kmp_search_found(self):
        haystack = "abcabcabcabcabd"
        needle = "abcabd"
        result = kmp_search(haystack, needle, 0)
        self.assertEqual(result, 9)

    def test_kmp_search_not_found(self):
        haystack = "aaatgaacgaaaatctgt"
        needle = "acga"
        result = kmp_search(haystack, needle, 0)
        self.assertEqual(result, 6)

    def test_prefix_function(self):
        needle = "abcabd"
        result = prefix_function(needle)
        self.assertEqual(result, [0, 0, 0, 1, 2, 0])

    def test_prefix_function_empty_needle(self):
        needle = ""
        result = prefix_function(needle)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
