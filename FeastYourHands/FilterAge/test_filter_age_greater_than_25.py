from unittest import TestCase

from filter_age_greater_than_25 import *

class TestFunction(TestCase) :
    def test_tocheck_age_isGreaterThan25(self):
        self.assertTrue(isGreater_than_25({'name': 'Alice', 'age': 30}))
    def test_tocheck_Age_isNotGreaterThan25(self):
        self.assertFalse(isGreater_than_25({'name': 'Alice', 'age': 16}))  
    def test_to_get_distionary_of_ages_above25(self):
        details = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 20}]
        self.assertEqual(filter_out_ages_below25(details), [{'name': 'Alice', 'age': 30}])
