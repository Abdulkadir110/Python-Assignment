from unittest import TestCase

from sum_of_all_numbers import *

class TestFunction(TestCase) :
    def test_toSum_number_to_zero(self):
        self.assertEqual(sumUp(0,2), 2)
    def test_to_get_distionary_of_ages_above25(self):
        numbers = [1,2,3,4]
        self.assertEqual(reduceNumbersIn(numbers),10)
