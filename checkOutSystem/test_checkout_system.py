import unittest
from checkout_system import *
class checkOutSystemTest(unittest.TestCase) :
    
    def test_that_the_list_is_empty(self):
        self.cart = checkOutSystem()
        self.assertTrue(self.cart.is_empty())
    
    def test_that_add_an_order_list_is_not_empty(self):
        self.cart = checkOutSystem()
        self.cart.add("Bread", 50, 2000)
        self.assertFalse(self.cart.is_empty())

    def test_that_add_two_orders_and_it_reflected(self):
        self.cart = checkOutSystem()
        self.cart.add("Bread", 50, 2000)
        self.cart.add("Beans", 30, 1000)
        self.assertFalse(self.cart.is_empty())
        self.assertEqual([["Bread", 50, 2000],["Beans", 30, 1000]], self.cart.items)
    
    def test_that_add_three_orders_and_it_reflected(self):
        self.cart = checkOutSystem()
        self.cart.add("Bread", 50, 2000)
        self.cart.add("Beans", 30, 1000)
        self.cart.add("Rice", 10, 4000)
        self.assertFalse(self.cart.is_empty())
        self.assertEqual([["Bread", 50, 2000],["Beans", 30, 1000],["Rice", 10, 4000]], self.cart.items)
    
    def test_that_add_two_orders_and_get_totalForEachOrder(self):
        self.cart = checkOutSystem()
        self.cart.add("Bread", 50, 2000)
        self.cart.add("Beans", 30, 1000)
        self.assertFalse(self.cart.is_empty())
        self.assertEqual([["Bread", 50, 2000],["Beans", 30, 1000]], self.cart.items)
        self.assertEqual([100000,30000], self.cart.get_total_for_each())

    def test_that_add_two_orders_and_get_subTotal(self):
        self.cart = checkOutSystem()
        self.cart.add("Bread", 50, 2000)
        self.cart.add("Beans", 30, 1000)
        self.assertFalse(self.cart.is_empty())
        self.assertEqual([["Bread", 50, 2000],["Beans", 30, 1000]], self.cart.items)
        self.assertEqual([100000,30000], self.cart.get_total_for_each())
        self.cart.get_subtotal()
        self.assertEqual([130000], self.cart.deduced_amount)
    def test_that_a_discount_was_calculated_and_added_to_deducedAmountList(self):
        self.cart = checkOutSystem()
        self.cart.add("Bread", 2, 2100)
        self.cart.add("Beans", 2, 550)
        self.assertFalse(self.cart.is_empty())
        self.assertEqual([["Bread", 2, 2100],["Beans", 2, 550]], self.cart.items)
        self.assertEqual([4200,1100], self.cart.get_total_for_each())
        self.cart.get_subtotal()
        self.assertEqual([5300], self.cart.deduced_amount)
        self.cart.calculate_discount(8)
        self.assertEqual([5300, 424.00], self.cart.deduced_amount)
    
    def test_that_a_VAT_was_calculated(self):
        self.cart = checkOutSystem()
        self.cart.add("Bread", 2, 2100)
        self.cart.add("Beans", 2, 550)
        self.assertFalse(self.cart.is_empty())
        self.assertEqual([["Bread", 2, 2100],["Beans", 2, 550]], self.cart.items)
        self.assertEqual([4200,1100], self.cart.get_total_for_each())
        self.cart.get_subtotal()
        self.cart.calculate_discount(8)
        self.assertEqual([5300, 424.00], self.cart.deduced_amount)
        self.cart.calculate_vat()
        self.assertEqual([5300,424.00,927.5], self.cart.deduced_amount)
        
    def test_that_total_bill_was_calculated(self):
        self.cart = checkOutSystem()
        self.cart.add("Bread", 2, 2100)
        self.cart.add("Beans", 2, 550)
        self.assertFalse(self.cart.is_empty())
        self.assertEqual([["Bread", 2, 2100],["Beans", 2, 550]], self.cart.items)
        self.assertEqual([4200,1100], self.cart.get_total_for_each())
        self.cart.get_subtotal()
        self.cart.calculate_discount(8)
        self.assertEqual([5300, 424.00], self.cart.deduced_amount)
        self.cart.calculate_vat()
        self.assertEqual([5300,424.00,927.5], self.cart.deduced_amount)
        self.assertEqual(self.cart.calculate_bill(), 5803.50)
     
    def test_that_an_amount_was_paid_andbalanceWasGiven(self):
        self.cart = checkOutSystem()
        self.cart.add("Bread", 2, 2100)
        self.cart.add("Beans", 2, 550)
        self.assertFalse(self.cart.is_empty())
        self.assertEqual([["Bread", 2, 2100],["Beans", 2, 550]], self.cart.items)
        self.assertEqual([4200,1100], self.cart.get_total_for_each())
        self.cart.get_subtotal()
        self.cart.calculate_discount(8)
        self.assertEqual([5300, 424.00], self.cart.deduced_amount)
        self.cart.calculate_vat()
        self.assertEqual([5300,424.00,927.5], self.cart.deduced_amount)
        self.assertEqual(self.cart.calculate_bill(), 5803.50)
        self.assertEqual(self.cart.get_balance_after_payment(6000), 196.50)
        
