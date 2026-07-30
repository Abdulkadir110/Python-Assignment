item_name = input("Enter the name of the item: ")
original_price = float(input("Enter the original Price: "))
promo_code = input("Enter your promo-code: ")


def discount_applier(item_name, original_price, promo_code) :
    if promo_code == "SAVE10" :
        discounted_price = original_price * 0.1
    elif promo_code == "HALFOFF" : 
        discounted_price = original_price * 0.5
    else :
        print("No discount applied, your bill still remains as ", original_price)
        discounted_price = original_price
    return discounted_price 

print("The discounted price is: ", discount_applier(item_name, original_price, promo_code))          
