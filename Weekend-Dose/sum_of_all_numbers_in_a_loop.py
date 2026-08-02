
def sum_of_all_numbers(number) :
    total = 0
    for numbers in range(1, number + 1) :
        
        total += numbers

    return total


number = int(input("Enter a number: "))

print("The total numbers is: " , sum_of_all_numbers(number))
