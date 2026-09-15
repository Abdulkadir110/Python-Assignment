
class checkOutSystem:
    def __init__(self):
        self.items = []
        self.discount_amount = 0.0
        self.deduced_amount = []

    def is_empty(self):
        return len(self.items) == 0

    def add(self, product, pieces, price_per_unit):
        order = [product, pieces, price_per_unit]
        self.items.append(order)

    def get_total_for_each(self):
        totals = []
        for item in self.items:
            totals.append(item[1] * item[2])
        return totals

    def get_subtotal(self):
        sum_total = 0
        totals = self.get_total_for_each()
        for total in totals:
            sum_total += total
        self.deduced_amount.append(sum_total)
        return sum_total

    def calculate_discount(self, discount_percent):
        sub_total = self.deduced_amount[0]
        discount_value = sub_total * (discount_percent / 100)
        discounted_total = sub_total - discount_value
        self.deduced_amount.append(discount_value)
        return discounted_total

    def calculate_vat(self):
        taxable_amount = self.deduced_amount[0]
        vat = round(taxable_amount * 0.175, 2)
        self.deduced_amount.append(vat)
        return vat
    
    def calculate_bill(self):
        total = self.deduced_amount[0] - self.deduced_amount[1] + self.deduced_amount[2]
        return total
    
    def get_balance_after_payment(self, amount):
        bill_total = self.calculate_bill()
        balance = amount - bill_total
        return balance
