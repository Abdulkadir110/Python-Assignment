from unittest import TestCase

from temperature import *

class TestFunction(TestCase) :
    def testThatI_convertTofahrenheit(self):
        celsius = 20
        self.assertEqual(toFahrenheit(celsius), 68)
    def test_all_celsius_are_converted(self):
        celsius_temperatures = [0,20,37,100]
        self.assertEqual(getTheMapFor(celsius_temperatures), [32,68,98.6,212])
