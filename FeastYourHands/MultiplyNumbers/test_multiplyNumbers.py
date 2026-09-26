from unittest import TestCase

from multiplyNumbers import *

class TestFunction(TestCase) :
    def test_toMultiply_number(self):
        self.assertEqual(multiply(1,2), 2)
    def test_toMultiply_Allnumbers(self):
        numbers = [2,3,4]
        self.assertEqual(reduceNumbersIn(numbers),24)
