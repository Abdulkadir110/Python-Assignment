from Dispenser import Dispenser


class FuelAttendant:
    def __init__(self, full_name: str, load_dispenser: Dispenser):
        self.full_name = full_name
        self.dispenser = load_dispenser
        self.transactions = self.populate_transactions()

    @staticmethod
    def populate_transactions() -> list:
        with open("Transactions.txt", "r") as file_object:
            file_object.seek(0)
            transactions = file_object.readlines()
            return transactions

    def add_new_fuel(self, fuel_name: str, price_per_liter: float, quantity: float):
        self.dispenser.add_fuel(fuel_name, price_per_liter, quantity)

    def get_available_fuel(self) -> dict:
        return self.dispenser.get_available_fuel()

    def update_fuel_price(self, fuel_name: str, new_price: float):
        self.dispenser.update_fuel_price(fuel_name, new_price)

    def restock_fuel(self, fuel_name: str, quantity: float):
        self.dispenser.restock_fuel(fuel_name, quantity)

    def dispense_fuel_by_amount(self, fuel_name: str, amount: float) -> dict:
        liters = self.dispenser.dispense_by_amount(fuel_name, amount)
        with open("Transactions.txt", "a") as file_object:
            receipt = file_object.write(f"fuel_name: {fuel_name} | liters: {liters} | total_cost: {amount}\n")
        return receipt

    def dispense_fuel_by_liters(self, fuel_name: str, liters: float) -> dict:
        amount = self.dispenser.dispense_by_liters(fuel_name, liters)
        with open("Transactions.txt", "a") as file_object:
            receipt = file_object.write(f"fuel_name: {fuel_name} | liters: {liters} | total_cost: {amount}\n")
        return receipt

    def show_all_transactions(self) -> list:
        return self.transactions