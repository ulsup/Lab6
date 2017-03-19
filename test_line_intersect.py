from unittest import TestCase
from line_intersect import line_intersection


class Test_line_intersect(TestCase):
    def setUp(self):
        self.one = line_intersection([(4, 2), (2, 0)], [(0, 4), (4, 0)])
        self.two = line_intersection([(1, 1), (3, 3)], [(2, 2), (5, 5)])
        self.three = line_intersection([(1.0, 1.0), (3.0, 3.0)], [(1.0, 3.0), (3.0, 5.0)])
        self.four = line_intersection([(2.5, 3.0), (4.5, 4.7)], [(0.6, 2.1), (3.0, 4.8)])
        self.five = line_intersection([(4, 5), (2.0, 3)], [(2.0, -3.4), (-5.0, -7.0)])
        self.six = line_intersection([(-2, -3), (-4, 6)], [(45.7, 8), (34, 25)])

    def test_intersection(self):
        self.assertTrue(self.one == (3.0, 1.0))
        self.assertTrue(self.two == [(1, 1), (3, 3)])
        self.assertTrue(self.three == None)
        self.assertTrue(self.four == (-3.0, -1.0))
        self.assertTrue(self.five == (-12.0, -11.0))
        self.assertTrue(self.six == (-29.0, 115.0))
