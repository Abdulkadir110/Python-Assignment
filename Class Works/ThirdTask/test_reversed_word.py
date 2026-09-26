import unittest
from reversed_word import *

class TestFunctions(unittest.TestCase):
    def testThatTheCharacterGiven_exist(self):
        word = "abcdegi"
        self.assertTrue(is_exist(word, "c"))

    def testThatTheCharacterGiven_exist2(self):
        word = "abcdegi"
        self.assertFalse(is_exist(word, "j")) 
    
    def testThatTheWordIsReversed(self):
        word = "abcdefgh"
        letter = "d"
        
        self.assertEqual(reversed_word(word,letter), "dcbahgfed")
    
    def testThatTheWordIsReversed2(self):
        word = "abcdefg"
        letter = "i"
        
        self.assertEqual(reversed_word(word,letter), word)
        
    def testThatTheWordIsReversed3(self):
        word = "nehfgxki"
        letter = "x"
        
        self.assertEqual(reversed_word(word,letter), "xgfhenikx")
        
    def testThatTheWordIsReversed4(self):
        word = "abcdefgh"
        letter = "a"
        
        self.assertEqual(reversed_word(word,letter), "ahgfedcba")
