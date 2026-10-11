
class Fuel:
    def __init__(self, fuel_name, price_per_liter, quantity):
        if not fuel_name.strip():
            raise ValueError("Fuel name cannot be empty.")

        if price_per_liter <= 0:
            raise ValueError("Price per liter must be positive.")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.fuel_name = fuel_name
        self.price_per_liter = price_per_liter
        self.quantity = quantity


