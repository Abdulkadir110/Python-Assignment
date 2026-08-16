import random
 


def correctOptionComment():
    match(comment):
        comment = random.randrange(1, 4)
        if(comment == 1): print("Very Good")
        elif(comment == 2): print("Nice Work")
        elif(comment == 3): print("Keep up the good work")
            


def inCorrectOptionComment():
    match(comment):
        number = random.randrange(1, 4)
        if(number == 1): print("No, please try again")
        elif(number == 2): print("Wrong. Try again")
        elif(number == 3): print("No, keep trying")


def addition(difflicultyLevel) :
    match(difflicultyLevel):
            case 1: 
                first_number = random.randrange(1, 10)
                second_number = random.randrange(1, 10)
            case 2:
                first_number = random.randrange(1, 100)
                second_number = random.randrange(1, 100)
        
    print("How much is ", first_number," plus ", second_number)
    answer = int(input("Enter the correct answer: "))

    sum = int(first_number + second_number)


    while True:
        if(sum == answer):
            print(correctOptionComment())
            break

        else :
            inCorrectOptionComment()

    answer = int(input("Enter the correct answer: "))
    
    
def substract(difflicultyLevel) :
    match(difflicultyLevel):
            case 1: 
                first_number = random.randrange(1, 10)
                second_number = random.randrange(1, 10)
            case 2:
                first_number = random.randrange(1, 100)
                second_number = random.randrange(1, 100)

    print("How much is ", first_number," minus ", second_number)
    answer = int(input("Enter the correct answer: "))

    substract = int(first_number - second_number)


    while True:
        if(substract == answer):
            print(correctOptionComment())
            break

        else :
            inCorrectOptionComment()
            break
    answer = int(input("Enter the correct answer: "))

def multiply(difflicultyLevel) :
    match(difflicultyLevel):
            case 1: 
                first_number = random.randrange(1, 10)
                second_number = random.randrange(1, 10)
            case 2:
                first_number = random.randrange(1, 100)
                second_number = random.randrange(1, 100)
        
    print("How much is ", first_number," times ", second_number)
    answer = int(input("Enter the correct answer: "))

    substract = int(first_number * second_number)


    while True:
        if(substract == answer):
            print(correctOptionComment())
            break

        else :
            inCorrectOptionComment()
            break

    answer = int(input("Enter the correct answer: "))

def divide(difflicultyLevel) :
    match(difflicultyLevel):
            case 1: 
                first_number = random.randrange(1, 10)
                second_number = random.randrange(1, 10)
            case 2:
                first_number = random.randrange(1, 100)
                second_number = random.randrange(1, 100)
        
    print("How much is ", first_number," divide by ", second_number)
    answer = int(input("Enter the correct answer: "))

    quotient = int(first_number / second_number)


    while True:
        if(quotient == answer):
            print(correctOptionComment())
            break;

        else :
            inCorrectOptionComment()
            break;

    answer = int(input("Enter the correct answer: "))
    if(answer == quotient): print("Yayyyyy... You got it...........")
    
    
difflicultyLevel = int(input("Enter your diffliculty Level between 1 and 2: "))

arithmetric_problems = """
    Welcome to the CAI game!

    Press 1 : Addition
    Press 2 : Substraction
    Press 3 : Multiplication
    Press 4 : Division
    Press 5 : Random Mixture
"""

print(arithmetric_problems)
operator = int(input("Enter between 1 to 5: "))

match(operator):
    case 1 : addition(difflicultyLevel)
    case 2 : substract(difflicultyLevel)
    case 3 : multiply(difflicultyLevel)
    case 4 : divide(difflicultyLevel)
    case 5 : 
        number = random.randrange(1, 5)
        if(number == 1): addition(difflicultyLevel)
        elif(number == 2): substract(difflicultyLevel)
        elif(number == 3): multiply(difflicultyLevel)
        elif(number == 4): divide(difflicultyLevel)
        else: print("invalid input")

 

