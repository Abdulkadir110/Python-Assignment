class Account :
    def __init__(self,name: str) -> None:
        self.name = name.lower()
        self.balance = 0
        self.pin = 0000

    def deposit(self, amount: float):
        if amount < 0.0 :
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float, pin):
        if amount < 0 and pin == self.pin:
            raise ValueError("Amount must be positive")
        if amount <= self.balance:
            self.balance -= amount

    def set_pin(self, pin):
        self.pin = pin