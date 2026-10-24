from unittest import TestCase

from admin import Admin
from drug import Drug
from items import Item
from pharmacist import Pharmacist
from pharmacy import Pharmacy


class TestPharmacist(TestCase):
    def test_pharmacist_search_for_product_added_in_the_pharmacy(self):
        admin1 = Admin("Abdulkadir", 1)
        ade_pharmacy = Pharmacy("ade", admin1)
        malaria_drug = Drug()
        malaria_drug.name = "Malaria"
        malaria_drug.price = 2000
        ade_pharmacy.add_item(malaria_drug, 200)
        syrings = Item()
        syrings.name = "Syrings"
        syrings.price = 2000
        ade_pharmacy.add_item(syrings, 200)
        pharmacist = Pharmacist("ope", "081029221")
        pharmacist.employed_by(ade_pharmacy)
        found_product = pharmacist.search_product("syrings")
        self.assertIn(found_product, ade_pharmacy.inventory)
        self.assertEqual(found_product.name, "Syrings")
        self.assertEqual(found_product.price, 2000)
    def test_pharmacist_search_for_product_not_added_in_pharmacy(self):
        admin1 = Admin("Abdulkadir", 1)
        ade_pharmacy = Pharmacy("ade", admin1)
        malaria_drug = Drug()
        malaria_drug.name = "Malaria"
        malaria_drug.price = 2000
        ade_pharmacy.add_item(malaria_drug, 200)
        pharmacist = Pharmacist("ope", "081029221")
        pharmacist.employed_by(ade_pharmacy)
        found_product = pharmacist.search_product("syrings")
        self.assertIsNone(found_product)

    def test_pharmacist_check_a_product_available_quantity(self):
        admin1 = Admin("Abdulkadir", 1)
        ade_pharmacy = Pharmacy("ade", admin1)
        malaria_drug = Drug()
        malaria_drug.name = "Malaria"
        malaria_drug.price = 2000
        ade_pharmacy.add_item(malaria_drug, 200)
        pharmacist = Pharmacist("ope", "081029221")
        pharmacist.employed_by(ade_pharmacy)
        self.assertTrue(pharmacist.check_product_available("Malaria", 100))
        self.assertFalse(pharmacist.check_product_available("Malaria", 300))
        with self.assertRaises(ValueError) :
            pharmacist.check_product_available("syrings", 400)

    def test_pharmacist_check_all_products(self):
        admin1 = Admin("Abdulkadir", 1)
        ade_pharmacy = Pharmacy("ade", admin1)
        malaria_drug = Drug()
        malaria_drug.name = "Malaria"
        malaria_drug.price = 2000
        ade_pharmacy.add_item(malaria_drug, 200)
        syrings = Item()
        syrings.name = "Syrings"
        syrings.price = 2000
        ade_pharmacy.add_item(syrings, 200)
        pharmacist = Pharmacist("ope", "081029221")
        pharmacist.employed_by(ade_pharmacy)
        viewed_inventory = pharmacist.view_inventory()
        self.assertEqual(len(viewed_inventory), 2)
        self.assertEqual(viewed_inventory, ade_pharmacy.inventory)
