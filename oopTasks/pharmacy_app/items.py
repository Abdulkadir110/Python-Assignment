from datetime import date


class Item:
    def __init__(self, name: str, price: float, expiry_date: date):
        self.name = name
        self.price = price
        self.expiry_date = expiry_date