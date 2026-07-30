
temperature = float(input("Enter your temperature: "))
temperature_unit = input("Enter the unit (C or F): ").lower()

threshold_for_farenheit = 100.4
threshold_for_celsius = 38.0

def temperature_checker(temperature, temperature_unit) :


    if temperature_unit == "c":
        converted_to_farenheit = (temperature * 1.8) + 32
        
        if threshold_for_farenheit > converted_to_farenheit :
             return "Cold advisory"
        else :
             return "Heat Alert"


    elif temperature_unit == "f" :
        converted_to_celsius = temperature - 32 * 0.56

        if threshold_for_celsius > converted_to_celsius :
             return "Cold advisory"
        else :
             return "Heat Alert"

    else :
        return("invalid input")



print(temperature_checker(temperature, temperature_unit))
    
