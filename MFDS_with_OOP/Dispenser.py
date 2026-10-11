from Fuel import Fuel


class Dispenser:
    def __init__(self):
        self.fuels = {}  # Dictionary collection of Fuel
        self.transactions = []

    def add_fuel(self, fuel_name: str, price_per_liter: float, quantity: float):
        if fuel_name in self.fuels:
            raise ValueError(f"{fuel_name} already exists.")
        self.fuels[fuel_name] = Fuel(fuel_name, price_per_liter, quantity)

    def get_available_fuel(self) -> dict:
        return self.fuels

    def update_fuel_price(self, fuel_name: str, new_price: float):
        if fuel_name not in self.fuels:
            raise ValueError(f"{fuel_name} not found.")
        if new_price <= 0:
            raise ValueError("Price must be greater than zero.")
        self.fuels[fuel_name].price_per_liter = new_price

    def restock_fuel(self, fuel_name: str, quantity: float):
        if fuel_name not in self.fuels:
            raise ValueError(f"Fuel '{fuel_name}' not found.")
        if quantity <= 0:
            raise ValueError("Restock quantity must be greater than zero.")
        self.fuels[fuel_name].quantity += quantity

    def dispense_by_liters(self, fuel_name: str, liters: float) -> dict:
        if fuel_name not in self.fuels:
            raise ValueError(f"Fuel '{fuel_name}' not found.")
        if not (1 <= liters <= 50):
            raise ValueError("Liters must be between 1 and 50.")

        fuel = self.fuels[fuel_name]
        if fuel.quantity < liters:
            raise ValueError("Insufficient fuel quantity.")

        total_cost = liters * fuel.price_per_liter
        fuel.quantity -= liters

        receipt = {
            "fuel_name": fuel_name,
            "liters": liters,
            "price_per_liter": fuel.price_per_liter,
            "total_cost": total_cost
        }
        self.transactions.append(receipt)
        return receipt

    def dispense_by_amount(self, fuel_name: str, amount: float) -> dict:
        if fuel_name not in self.fuels:
            raise ValueError(f"Fuel '{fuel_name}' not found.")

        fuel = self.fuels[fuel_name]
        if amount <= fuel.price_per_liter:
            raise ValueError("Amount must be above the price of a liter.")

        liters = amount / fuel.price_per_liter
        if not (1 <= liters <= 50):
            raise ValueError("liters must be between 1 and 50.")

        if fuel.quantity < liters:
            raise ValueError("Insufficient fuel quantity.")

        fuel.quantity -= liters

        receipt = {
            "fuel_name": fuel_name,
            "liters": liters,
            "price_per_liter": fuel.price_per_liter,
            "total_cost": amount
        }
        self.transactions.append(receipt)
        return receipt