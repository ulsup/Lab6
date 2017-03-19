from unittest import TestCase
from is_sorted import is_sorted


class Test_Sort(TestCase):
    def setUp(self):
        self.one = is_sorted([-30, 45, 80, 0, 100])
        self.two = is_sorted([1, 2, 3, 4, 5, 6.999, 7])
        self.three = is_sorted([-4, 5, 5, 8.6, 9, 15])
        self.four = is_sorted([45.0, 42])
        self.five = is_sorted([20])
        self.six = is_sorted([])

    def test_sorted(self):
        self.assertEqual(self.one, False)
        self.assertEqual(self.two, True)
        self.assertEqual(self.three, True)
        self.assertEqual(self.four, False)
        self.assertEqual(self.five, True)
        self.assertEqual(self.six, True)
