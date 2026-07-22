#Ticket Price Calculator

age = int(input("Enter your age: "))

if age < 5 :
    print("It is for free")
elif 5 <= age <= 12 :
    print("price is: $5")
elif 13 <= age <= 64 :
    print("price is: $12")
elif age >= 65 :
    print("price is: $8")

