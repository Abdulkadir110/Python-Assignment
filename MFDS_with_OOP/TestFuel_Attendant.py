import unittest

from Dispenser import Dispenser
from Fuel_Attendant import FuelAttendant


class TestFuelAttendantClass(unittest.TestCase):
    def test_attendant_add_and_manage_fuel(self):
        self.dispenser = Dispenser()
        self.attendant = FuelAttendant("Jane Doe", self.dispenser)
        self.attendant.add_new_fuel("Diesel", 700.0, 150.0)
        fuels = self.attendant.get_available_fuel()
        self.assertIn("Diesel", fuels)

    def test_attendant_dispense_and_show_transactions(self):
        self.dispenser = Dispenser()
        self.attendant = FuelAttendant("Jane Doe", self.dispenser)
        self.attendant.add_new_fuel("Petrol", 600.0, 100.0)
        self.attendant.dispense_fuel_by_liters("Petrol", 10.0)

        transactions = self.attendant.show_all_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["liters"], 10.0)


if __name__ == '__main__':
    unittest.main()
