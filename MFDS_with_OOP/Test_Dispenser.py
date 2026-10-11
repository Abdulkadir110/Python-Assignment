import unittest

from Dispenser import Dispenser


class TestDispenserClass(unittest.TestCase):

    def test_add_and_get_fuel(self):
        self.dispenser = Dispenser()
        self.dispenser.add_fuel("Petrol", 600.0, 50.0)
        fuels = self.dispenser.get_available_fuel()
        self.assertIn("Petrol", fuels)
        self.assertEqual(fuels["Petrol"].price_per_liter, 600.0)

    def test_update_fuel_price(self):
        self.dispenser = Dispenser()
        self.dispenser.add_fuel("Petrol", 600.0, 50.0)
        self.dispenser.update_fuel_price("Petrol", 650.0)
        self.assertEqual(self.dispenser.fuels["Petrol"].price_per_liter, 650.0)

    def test_restock_fuel(self):
        self.dispenser = Dispenser()
        self.dispenser.add_fuel("Petrol", 600.0, 50.0)
        self.dispenser.restock_fuel( "Petrol", 50.0)
        self.assertEqual(self.dispenser.fuels["Petrol"].quantity, 100.0)

    def test_dispense_by_liters_above_quantity_raises_valueError(self):
        self.dispenser = Dispenser()
        self.dispenser.add_fuel("Petrol", 600.0, 50.0)
        self.assertRaises(ValueError, self.dispenser.dispense_by_liters, "Petrol", 0)
        self.assertRaises(ValueError, self.dispenser.dispense_by_liters,"Petrol", 55)

    def test_dispense_receipt_structure_and_values(self):
        self.dispenser = Dispenser()
        self.dispenser.add_fuel("Petrol", 600.0, 50.0)
        receipt = self.dispenser.dispense_by_liters("Petrol", 5.0)
        self.assertEqual(receipt["fuel_name"], "Petrol")
        self.assertEqual(receipt["liters"], 5.0)
        self.assertEqual(receipt["price_per_liter"], 600.0)
        self.assertEqual(receipt["total_cost"], 3000.0)


if __name__ == '__main__':
    unittest.main()
