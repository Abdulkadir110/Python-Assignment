number = int(input ("Enter a number: "))

for numbers in range(0, number + 1, 1):
    print(firstNumber);
    firstNumber = 0
    secondNumber = 1
    sum = firstNumber + secondNumber
    firstNumber = secondNumber
    secondNumber = sum
    
