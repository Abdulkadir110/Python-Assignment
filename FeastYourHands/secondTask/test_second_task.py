from unittest import TestCase

from second_task import *

class TestFunction(TestCase) :
    def testThatI_add_ten_toNumber(self):
        number = 5
        self.assertEqual(add_ten_to(number), 15)
    def test_a_list_ofNumbers_with_ten_added(self):
        numbers = [7,9,3,4]
        self.assertEqual(getTheMapFor(numbers), [17,19,13,14])
