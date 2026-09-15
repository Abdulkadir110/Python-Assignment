from checkout_system import *
from datatime import datetime
cart = checkOutSystem()

input("What is the customer's Name: ")
choice = ""
while choice != "no" :
    product = input("What did the user buy? ")
    quantity = float(input("How many pieces? "))
    price_per_unit = float(input("How much per unit"))
    cart.add(product, quantity, price_per_unit)
    choice = input("Add more Items?")
    

cashier_name = input("what is your name")
discount = float(input("How much discount will he get"))
print(cart.get_total_for_each())
cart.get_subtotal()

cart.calculate_discount(8)
cart.calculate_vat()




balance = float(input("How much did the customer give to you? "))
print(cart.get_balance_after_payment(balance))

print(f"SEMICOLON STORES\nMAIN BRANCH\nLOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.\nTEL : 08190909020\nDATE");

