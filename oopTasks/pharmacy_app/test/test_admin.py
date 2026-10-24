from unittest import TestCase

from admin import Admin
from pharmacist import Pharmacist
from pharmacy import Pharmacy


class TestAdmin(TestCase):
    def test_admin_has_an_id(self):
        admin = Admin("Abdulkadir" , 1)
        admin.admin_id = 2
        self.assertEqual(admin.admin_id, 2)

    # def test_register_a_pharmacist_Pharmacy_has_one_pharmacist(self):
    #     admin = Admin("Abdulkadir" , 1)
    #     pharmacist1 = Pharmacist("Abdulkadir", "081234574")
    #     pharmacist1.id = 1
    #     ade_pharmacy = Pharmacy("ade", admin)
    #     admin.register_pharmacist(pharmacist1)
    #     self.assertEqual(1, len(ade_pharmacy.pharmacists))
    #     self.assertIn(pharmacist1, ade_pharmacy.pharmacists)