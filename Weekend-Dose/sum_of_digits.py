
def sum_of_digits_in(number):
    total = 0 
    for digits in number:
        total += int(digits)
    return total

number = input("Enter number: ")

print("The sum of the digits is: ", sum_of_digits_in(number))
