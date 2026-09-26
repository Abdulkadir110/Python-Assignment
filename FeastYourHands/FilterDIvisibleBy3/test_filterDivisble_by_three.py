from unittest import TestCase

from filterDivisble_by_three import *

class TestFunction(TestCase) :
    def test_tocheck_ifANumber_isDivisible_by_three(self):
        self.assertTrue(is_divisible_by_three(21))
    def test_tocheck_ifANumber_isNotDivisible_by_three(self):
        self.assertFalse(is_divisible_by_three(20))  
    def test_to_get_theListOfNumbers_Divisible_byThree(self):
        numbers = [1,3,4,6,9,12]
        self.assertEqual(filter_out_numbers_not_divisible_byThree(numbers), [3,6,9,12])
