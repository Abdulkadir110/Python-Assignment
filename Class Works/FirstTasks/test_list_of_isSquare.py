import unittest
from list_of_isSquares import is_square,get_list_of

class TestFunctions(unittest.TestCase):
    def test_to_check_for_squaredNumbers(self):
        number = 36
        self.assertEqual(is_square(number), True)

    def test_to_check_for_squareNumbers2(self):
        number = 39
        self.assertEqual(is_square(number), False)
    
    def test_for_list_of_is_squaredNumbers(self):
        numbers = [4,9,25,49]
        self.assertEqual(get_list_of(numbers), [True, True, True, True])
    
    def test_for_list_of_is_squaredNumbers2(self):
        numbers = [8,36,49, 5]
        self.assertEqual(get_list_of(numbers), [False, True, True, False])

    def test_for_list_of_perfectSquares(self):
        numbers = [0,1,2,3,4,9,10,16,25,26]
        self.assertEqual(get_list_of(numbers), [True,True,False,False,True,True,False,True,True,False])
