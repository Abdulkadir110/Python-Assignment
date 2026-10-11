import unittest

from Fuel import Fuel


class MyTestCase(unittest.TestCase):
    def test_something(self):
        fuel = Fuel("diesel", 1600, 10)
        self.assertEqual(fuel.price_per_liter, 1600)

if __name__ == '__main__':
    unittest.main()
