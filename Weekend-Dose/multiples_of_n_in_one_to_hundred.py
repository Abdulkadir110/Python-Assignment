
def multiples_of(number):
    number_multiples_counter = 0

    for numbers in range(1, 101):

        if numbers % number == 0 :
            number_multiples_counter += 1

    return number_multiples_counter

number = int(input("Enter a number: "))

print(f"The multiples of {number} in the range of 100 is: ", multiples_of(number))
