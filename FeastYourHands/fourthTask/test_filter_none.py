from unittest import TestCase

from filter_none import *

class TestFunction(TestCase) :
    def test_that_isNumber_notNone(self):
        number = 20
        self.assertTrue(is_not_None(number))
    def test_toGetAListofNumbersOnly(self):
        numbers = [1,None,3,None, 5]
        self.assertEqual(filter_out_None(numbers), [1,3,5])
