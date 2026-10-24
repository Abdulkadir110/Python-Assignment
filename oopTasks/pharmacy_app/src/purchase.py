from datetime import date

from cart_item import CartItem


class Purchase:
    def __init__(self):
        self._transaction_id = None
        self._date : date | None = None
        self._total_amount : float
        self._purchased_items = list[CartItem]