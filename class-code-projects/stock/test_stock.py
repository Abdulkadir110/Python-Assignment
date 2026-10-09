import unittest

from stock.stock import Stock


class MyTestCase(unittest.TestCase):
    def test_something(self):
        stock = Stock("AAPL", 10000)
        self.assertEqual(stock.current_price, 10000)


if __name__ == '__main__':
    unittest.main()
