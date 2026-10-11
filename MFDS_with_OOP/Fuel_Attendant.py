from Dispenser import Dispenser


class FuelAttendant:
    def __init__(self, full_name: str, dispenser: Dispenser):
        self.full_name = full_name
        self.dispenser = dispenser

    def add_new_fuel(self, fuel_name: str, price_per_liter: float, quantity: float):
        self.dispenser.add_fuel(fuel_name, price_per_liter, quantity)

    def get_available_fuel(self) -> dict:
        return self.dispenser.get_available_fuel()

    def update_fuel_price(self, fuel_name: str, new_price: float):
        self.dispenser.update_fuel_price(fuel_name, new_price)

    def restock_fuel(self, fuel_name: str, quantity: float):
        self.dispenser.restock_fuel(fuel_name, quantity)

    def dispense_fuel_by_amount(self, fuel_name: str, amount: float) -> dict:
        return self.dispenser.dispense_by_amount(fuel_name, amount)

    def dispense_fuel_by_liters(self, fuel_name: str, liters: float) -> dict:
        return self.dispenser.dispense_by_liters(fuel_name, liters)

    def show_all_transactions(self) -> list:
        return self.dispenser.transactions