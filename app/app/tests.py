"""
Sample test cases for the app
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """ Test cases for the calc app """

    def test_add_numbers(self):
        """ Test that two numbers are added together """

        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """ Test that values are subtracted and returned """

        res = calc.subtract(3, 10)
        self.assertEqual(res, 7)
