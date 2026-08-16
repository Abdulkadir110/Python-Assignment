import random

first_number = random.randrange(1, 10)
second_number = random.randrange(1, 10)

print("How much is ", first_number," times ", second_number)
answer = int(input("Enter the correct answer: "))

product = int(first_number * second_number)

def correctOptionComment(number):
    match(number):
        case 1: print("Very Good")
        case 2: print("Nice Work")
        case 3: print("Keep up the good work")
    #            case _: print("Oga, select between 1 - 3")


def inCorrectOptionComment(number):
    match(number):
        case 1: print("No, please try again")
        case 2: print("Wrong. Try again")
        case 3: print("No, keep trying")
    #            case _: print("Oga, select between 1 - 3")

while True:
    if(product == answer):
        number = int(input("Enter a number between 1 to 3: "))
        print(correctOptionComment(number))
        break;
        
    else :
        number = int(input("Enter a number between 1 to 3: "))
        inCorrectOptionComment(number)
        
    answer = int(input("Enter the correct answer: "))
    
    

