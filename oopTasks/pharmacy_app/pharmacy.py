import admin
import pharmacist
from drug import Drug


class Pharmacy:
    def __init__(self, drugs : Drug, items : list[Item]):
        self.drugs = drugs
        self.items = items
        self.admin = admin
        self.pharmacist = pharmacist