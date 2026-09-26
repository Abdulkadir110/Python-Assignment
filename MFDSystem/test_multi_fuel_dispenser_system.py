import unittest

from multi_fuel_dispenser_system import MFDFunctions


class MyTestCase(unittest.TestCase):
    def testToValidateLitres(self):
        petroleum = MFDFunctions()
        self.assertEqual(petroleum.validate_litres(40), 40)
        self.assertEqual(petroleum.validate_litres(-1), -1)
    def testToCalculateAmount(self):
        petroleum = MFDFunctions()
        self.assertEqual(petroleum.calculate_amount("Petrol",40), 26000)
    def testCalculateAmount2(self):
        petroleum = MFDFunctions()
        self.assertEqual(petroleum.calculate_amount("Diesel",30), 21600)
        self.assertEqual(petroleum.calculate_amount("Kerosene",20), 11000)
        self.assertEqual(petroleum.calculate_amount("Gas",5), 2400)
        self.assertEqual(petroleum.calculate_amount("Coal",2), -1)
    def testToCalculateLitres(self):
        petroleum = MFDFunctions()
        self.assertEqual(petroleum.calculate_litres("Petrol", 5000), 7.69)
        self.assertEqual(petroleum.calculate_litres("Diesel", 2160), 3)
        self.assertEqual(petroleum.calculate_litres("Kerosene", 2000), 3.64)
        self.assertEqual(petroleum.calculate_litres("Gas", 1100), 2.29)

if __name__ == '__main__':
    unittest.main()
