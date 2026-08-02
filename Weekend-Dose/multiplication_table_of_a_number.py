
def multiples_of(number):
    for numbers in range(1, 11):
        result = number * numbers        
        print(f"{number} x {numbers} = {result}")
    

number = int(input("Enter a number: "))

multiples_of(number)
