from unittest import TestCase
from all_prefixes import all_prefixes


class TestPrefixes(TestCase):
    def setUp(self):
        self.one = all_prefixes('lead')
        self.two = all_prefixes('абабагаламага')
        self.three = all_prefixes('google')
        self.four = all_prefixes('lalaland')
        self.five = all_prefixes(' ')

    def test_them_all(self):
        self.assertEqual(self.one, {'le', 'lea', 'lead', 'l'})
        self.assertEqual(self.two, {'абабагаламаг', 'а', 'абаб', 'абабаг', 'абабагалам', 'абабагалама', 'абабагала',
                                    'абабагаламага', 'аба', 'абаба', 'абабагал', 'аб', 'абабага'})
        self.assertEqual(self.three, {'go', 'goo', 'goog', 'google', 'googl', 'g'})
        self.assertEqual(self.four, {'lalal', 'lalaland', 'lalalan', 'lal', 'l', 'lalala', 'la', 'lala'})
        self.assertEqual(self.five, {' '})
