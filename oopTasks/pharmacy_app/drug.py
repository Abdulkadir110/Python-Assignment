from datetime import date


class Drug :
    def __init__(self, name : str, given_date : date, price : float):
        self.name = name
        self.expiry_date = given_date
        self.price = price