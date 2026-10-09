
class Stock :
    def __init__(self, symbol, current_price):
        self.symbol = symbol
        self._current_price = current_price

    @property
    def current_price(self):
        return self._current_price