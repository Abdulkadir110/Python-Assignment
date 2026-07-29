succesful_delivery = int(input("Enter the number of succesful deliveries: "))
collection_rate = 0;
BASEPAY = 5000
if succesful_delivery <= 100 :
    if succesful_delivery >= 70 :
        print("The rider wage for the day is: " , succesful_delivery * 500 + BASEPAY)
    elif 60 <= succesful_delivery > 70 :
        print("The rider wage for the day is: " , succesful_delivery * 250 + BASEPAY)
    elif 50 <= succesful_delivery > 60 :
        print("The rider wage for the day is: " , succesful_delivery * 200 + BASEPAY)
    elif succesful_delivery < 50 :
        print("The rider wage for the day is: " , succesful_delivery * 160 + BASEPAY)
else :
    print("Oga you be theif, who gave you ", succesful_delivery , "number of packages")

