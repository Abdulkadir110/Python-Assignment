from unittest import TestCase

from admin import Admin
from drug import Drug
from pharmacist import Pharmacist
from pharmacy import Pharmacy


class TestPharmacy(TestCase):
    def test_add_medical_item_numberOfItems_inPharmacyIsOne(self):
        admin1 = Admin("Abdulkadir", 1)
        ade_pharmacy = Pharmacy("ade", admin1)
        malaria_drug = Drug()
        malaria_drug.name = "Malaria"
        malaria_drug.price = 2000
        ade_pharmacy.add_item(malaria_drug, 200)
        self.assertEqual(1, len(ade_pharmacy.inventory))
    def test_add_medical_drug_numberOfItems_isOne_add_theSameDrug_raiseException(self):
        admin1 = Admin("Abdulkadir", 1)
        ade_pharmacy = Pharmacy("ade", admin1)
        malaria_drug = Drug()
        malaria_drug.name = "Malaria"
        malaria_drug.price = 2000
        ade_pharmacy.add_item(malaria_drug, 200)
        self.assertEqual(1, len(ade_pharmacy.inventory))
        with self.assertRaises(ValueError):
            ade_pharmacy.add_item(malaria_drug, 200)
        self.assertEqual(1, len(ade_pharmacy.inventory))

    def test_add_medical_drug_numberOfItems_isOne_restock_drug_quantities(self):
        admin1 = Admin("Abdulkadir", 1)
        ade_pharmacy = Pharmacy("ade", admin1)
        malaria_drug = Drug()
        malaria_drug.name = "Malaria"
        malaria_drug.price = 2000
        ade_pharmacy.add_item(malaria_drug, 200)
        self.assertEqual(1, len(ade_pharmacy.inventory))
        ade_pharmacy.restock_item("Malaria", 500)
        self.assertEqual(1, len(ade_pharmacy.inventory))
        self.assertEqual(700, ade_pharmacy.inventory[0].quantity)

    def test_to_restock_non_existing_item_raises_Exception(self):
        admin1 = Admin("Abdulkadir", 1, )
        ade_pharmacy = Pharmacy("ade", admin1)
        with self.assertRaises(ValueError):
            ade_pharmacy.restock_item("Malaria", 500)

    def test_to_search_for_an_existing_item(self):
        admin1 = Admin("Abdulkadir", 1)
        ade_pharmacy = Pharmacy("ade", admin1)
        malaria_drug = Drug()
        malaria_drug.name = "Malaria"
        malaria_drug.price = 2000
        ade_pharmacy.add_item(malaria_drug, 200)
        searched_item = ade_pharmacy.search_item("malaria")
        self.assertEqual(200, searched_item.quantity)

    def test_to_search_for_an_empty_item(self):
        admin1 = Admin("Abdulkadir", 1)
        ade_pharmacy = Pharmacy("ade", admin1)
        searched_item = ade_pharmacy.search_item("malaria")
        self.assertNotIn(searched_item, ade_pharmacy.inventory)
        self.assertIsNone(searched_item)
    def test_to_get_list_of_medical_items(self):
        admin1 = Admin("Abdulkadir", 1)
        ade_pharmacy = Pharmacy("ade", admin1)
        malaria_drug = Drug()
        malaria_drug.name = "Malaria"
        malaria_drug.price = 2000
        ade_pharmacy.add_item(malaria_drug, 200)
        cattarh_drug = Drug()
        cattarh_drug.name = "Cattarh"
        cattarh_drug.price = 2000
        ade_pharmacy.add_item(cattarh_drug, 500)
        self.assertEqual(2, len(ade_pharmacy.inventory))
        list_of_items = ade_pharmacy.get_inventory()
        self.assertIn(malaria_drug, list_of_items)
        self.assertEqual(len(list_of_items), len(ade_pharmacy.inventory))

    def test_to_register_a_pharmacist_list_of_pharmacist_is_one(self):
        admin1 = Admin("Abdulkadir", 1)
        ade_pharmacy = Pharmacy("ade", admin1)
        pharmacist = Pharmacist("pharmacist", "08192663")
        pharmacist.id = 1
        ade_pharmacy.register_pharmacist(pharmacist)
        self.assertEqual(1, len(ade_pharmacy.pharmacists))
        self.assertIn(pharmacist, ade_pharmacy.pharmacists)

    def test_to_register_a_pharmacist_twice_raises_exception(self):
        admin1 = Admin("Abdulkadir", 1)
        ade_pharmacy = Pharmacy("ade", admin1)
        pharmacist = Pharmacist("pharmacist", "08192663")
        pharmacist.id = 1
        ade_pharmacy.register_pharmacist(pharmacist)
        self.assertEqual(1, len(ade_pharmacy.pharmacists))
        with self.assertRaises(ValueError):
            ade_pharmacy.register_pharmacist(pharmacist)
        self.assertEqual(1, len(ade_pharmacy.pharmacists))
        self.assertIn(pharmacist, ade_pharmacy.pharmacists)
