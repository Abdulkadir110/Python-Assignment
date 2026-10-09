import unittest

from shape.Shape import Rectangle, Circle


class MyTestCase(unittest.TestCase):
    def test_something(self):
        rectangle = Rectangle("blue",50, 100)
        self.assertEqual(5000, rectangle.get_area())
        circle = Circle("red", 7)
        self.assertEqual(154, circle.get_area())

if __name__ == '__main__':
    unittest.main()
