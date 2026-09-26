from unittest import TestCase

from filter_positive_numbers import *

class TestFunction(TestCase) :
    def test_tocheck_ANumber_isPositive(self):
        self.assertTrue(isPositive(15))
    def test_tocheck_ifANumber_isNotPositive(self):
        self.assertFalse(isPositive(-5))  
    def test_to_get_list_of_positiveNumbers(self):
        numbers = [-2,-1,0,1,2]
        self.assertEqual(filter_out_negatives(numbers), [0,1,2])
