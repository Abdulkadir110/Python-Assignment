
class MFDFunctions:
    def calculate_amount(self,fuel_type: str, litres: float):
        validated_litres = self.validate_litres(litres)
        if validated_litres != -1:
            if fuel_type == "Petrol":
                return litres * 650
            elif fuel_type == "Diesel":
                return litres * 720
            elif fuel_type == "Kerosene":
                return litres * 550
            elif fuel_type == "Gas":
                return litres * 480
        return -1
    def calculate_litres(self, fuel_type : str, amount: float):
        if fuel_type == "Petrol" and amount >= 650 :
            return round(amount / 650, 2)
        elif fuel_type == "Diesel" and amount >= 720 :
            return round(amount / 720, 2)
        elif fuel_type == "Kerosene" and amount >= 550 :
            return round(amount / 550, 2)
        elif fuel_type == "Gas" and amount >= 480 :
            return round(amount / 480, 2)
        return -1

    def validate_litres(self, litres: float):
        if 0 < litres <= 50:
            return litres
        return -1