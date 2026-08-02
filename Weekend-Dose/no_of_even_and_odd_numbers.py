
def no_of_even_numbers(numbers):
    even_counter = 0
    odd_counter = 0
    for number in numbers :
        if(int(number) % 2 == 0) :
            even_counter +=1
        else:
            odd_counter +=1
    print("Number of even numbers: ", even_counter ,"\nNumber of Odd numbers: ", odd_counter)


numbers = "123456789"
no_of_even_numbers(numbers)
