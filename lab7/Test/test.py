import unittest

from electric import calculate_wire_length


class TestCalculateWireLength(unittest.TestCase):

    def test_case1(self):
        w = 2
        heights = [3, 1, 3]
        result = calculate_wire_length(w, heights)
        self.assertAlmostEqual(result, 5.66, places=2)

    def test_case2(self):
        w = 100
        heights = [1, 1, 1, 1]
        result = calculate_wire_length(w, heights)
        self.assertEqual(result, 300.0)


if __name__ == '__main__':
    unittest.main()
