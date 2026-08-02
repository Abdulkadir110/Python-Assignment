
def reverse(number):
    reversed_number = 0
    for digits in number:
        if(int(number) > 0) :
            number = int(number)
            digits = number % 10
            reversed_number = reversed_number * 10 + digits
            number //=10
        
    return reversed_number

number = input("Enter a number: ")
print(reverse(number))
        
