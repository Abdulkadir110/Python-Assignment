from multi_fuel_dispenser_system import MFDFunctions
import datetime
petroleum = MFDFunctions()
transactions_list = []
menu_dict = {
    "Petrol" : 650,
    "Diesel" : 720,
    "Kerosene" : 550,
    "Gas" : 480
}
operation_dict = {
    1 : "Petrol",
    2: "Diesel" ,
    3: "Kerosene",
    4 : "Gas"
}
welcome_message = "Welcome to Bovas Station"
menu_functions = """
    Available Petroleum
        1. Buy Petroleum
        2. Show Transaction History
"""
banner_design = "====================================="
thank_you = "=  Thank you for your Patronage ="
print(welcome_message)
while True:
    print(menu_functions)
    choice = input("Enter operation: ")
    match choice:
        case "1" :
            count = 1
            for key,value in menu_dict.items():
                print(f"{count}.    {key}   =>  {value}/Litre")
                count += 1

            petrol_number = int(input("Enter operation: "))
            amount_or_liter = input("Litre or amount: ").lower()
            fuel_type = operation_dict.get(petrol_number)

            match amount_or_liter:
                case "amount" :
                    transaction_dict = {}
                    amount = float(input(f"How much {fuel_type} are you buying: "))
                    litres = petroleum.calculate_litres(fuel_type, amount)
                    if litres == -1:
                        print("amount must be above litre price")
                        continue
                    now = datetime.datetime.now().date()
                    transaction_dict.setdefault("Product", fuel_type)
                    transaction_dict.setdefault("Amount", amount)
                    transaction_dict.setdefault("Litres", litres)
                    transaction_dict.setdefault("Date", now)
                    transactions_list.append(transaction_dict)

                    print(banner_design)
                    for key,value in transaction_dict.items():
                        if key != "Date":
                            print(f"=   {key} \t\t:    {value} =")
                    print(thank_you)
                    print(banner_design)
                case "litre" :
                    transaction_dict_2 = {}
                    given_litre = float(input(f"How many litres of {fuel_type} are you buying: "))
                    if given_litre < 0 or given_litre > 50 :
                        print("Litres must be between 1 and 50")
                        continue
                    amount = petroleum.calculate_amount(fuel_type, given_litre)
                    now = datetime.datetime.now().date()
                    transaction_dict_2.setdefault("Product", fuel_type)
                    transaction_dict_2.setdefault("Amount", amount)
                    transaction_dict_2.setdefault("Litres", given_litre)
                    transactions_list.append(transaction_dict_2)
                    print(banner_design)
                    for key, value in transaction_dict_2.items():
                        if key != "Date":
                            print(f"=   {key} :    {value} =")
                    print(thank_you)
                    print(banner_design)
                case _:
                    print("Invalid operation")
                    continue
        case "2" :
            if len(transactions_list) == 0 :
                print("no transactions yet")
                continue
            for dictionary in transactions_list:
                print(banner_design)
                for key,value in dictionary.items():
                    print(f"=   {key} :    {value} =")
                print(banner_design)
            break
        case _:
            print("Invalid operation")
            continue