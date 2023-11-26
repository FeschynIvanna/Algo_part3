import unittest
from beer import set_cover_problem


class TestBeerType(unittest.TestCase):
    def test_example1(self):
        result = set_cover_problem(2, 2, ['YN', 'NY'])
        self.assertEqual(result, 2)

    def test_example2(self):
        result = set_cover_problem(3, 3, ['YYN', 'NYY', 'NYY'])
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
