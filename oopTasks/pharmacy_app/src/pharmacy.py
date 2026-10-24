import admin
import pharmacist
from items import Item


class Pharmacy:
    def __init__(self, name: str, employed_admin: admin.Admin):
        self.name = name
        self.address = "Lagos"
        self.admin = employed_admin
        self.inventory: list[Item] = []
        self.pharmacists: list[pharmacist.Pharmacist] = []

    def add_item(self, item: Item, quantity: int) -> None:
        self._validate_item(item)
        item.quantity = quantity
        self.inventory.append(item)

    def _validate_item(self, given_item: Item) -> None:
        found_item = self._find_item(given_item.name)
        if found_item is not None:
            raise ValueError("Pharmacy already has this item")

    def restock_item(self, item_name, restock_quantity: int) -> None:
        found_item = self._find_item(item_name)
        if found_item is None:
            raise ValueError("Pharmacy doesn't have this item")
        found_item.quantity += restock_quantity

    def _find_item(self, given_item_name: str) -> Item:
        for item in self.inventory:
            if item.name.lower() == given_item_name.lower():
                return item
        return None

    def search_item(self, item_name: str) -> Item:
        search_item = self._find_item(item_name)
        return search_item

    def get_inventory(self):
        return self.inventory

    @property
    def pharmacists(self) -> list[pharmacist.Pharmacist]:
        return self.pharmacists
    @pharmacists.setter
    def pharmacists(self, pharmacists):
        self.pharmacists = pharmacists
    @property
    def inventory(self) -> list[Item]:
        return self.inventory
    @inventory.setter
    def inventory(self, inventory: list[Item]):
        self.inventory = inventory