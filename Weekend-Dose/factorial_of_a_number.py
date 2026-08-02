
def factorial_of(number) :
    factorial = 1
    for numbers in range(1, number + 1) :
        
       factorial *= numbers

    return factorial


number = int(input("Enter a number: "))

print("The factorial is: " , factorial_of(number))
