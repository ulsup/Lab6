from unittest import TestCase
from debugger import square_preceding


class TestSquarePreceding(TestCase):
    def test_square_preceding_1(self):
        L = [1, 2, 3]
        square_preceding(L)
        self.assertTrue([0, 1, 4] == L)
