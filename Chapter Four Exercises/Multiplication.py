import random

first_number = random.randrange(1, 11)
second_number = random.randrange(1, 11)

print("How much is ", {first_number}," times ", {second_number})
answer = int(input("Enter the correct answer: "))

product = int(first_number * second_number)

while True:
    if(product == answer):
        print("very good")
        break;
    else :
        print("No please try again")

    answer = int(input("Enter the correct answer: "))
