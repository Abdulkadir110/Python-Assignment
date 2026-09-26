import unittest
from list_of_isPalindrome import is_palindrome, get_list_of

class TestFunctions(unittest.TestCase):
    def testThatA_word_is_palindrome(self) :
        word = "Madam"
        self.assertEqual(is_palindrome(word), True)
    def testThata_word_isNot_palindrome(self) :
        word = "Hello"
        self.assertEqual(is_palindrome(word), False)
    
    def test_for_list_of_is_palindromeWords(self):
        words = ["Madam", "hello", "noon", "racecar"]
        self.assertEqual(get_list_of(words), [True, False, True, True])

    def test_for_list_of_is_palindromeWords2(self):
        words = ["Mismatch", "Radio", "False", "Kilik"]
        self.assertEqual(get_list_of(words), [False, False, False, True])
    
