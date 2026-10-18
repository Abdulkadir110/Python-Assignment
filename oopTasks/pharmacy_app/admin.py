from customers import Customer


class Admin:
    def __init__(self, id: int, customers: list[Customer]):
        self.id = id
        self.customers = customers