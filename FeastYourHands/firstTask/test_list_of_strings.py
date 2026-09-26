from unittest import TestCase

from list_of_strings import *

class TestFunction(TestCase):
    def testThat_aStringLiteral_isConverted_toIntegers(self):
        letter = "10"
        
        self.assertEqual(convert_to_list_of_intergers(letter), 10)

    def test_list_ofStrings_converted_to_listOfIntegers(self):
        strings_list = ["1", "2", "3"]
        
        self.assertEqual(get_map(strings_list), [1,2,3])
