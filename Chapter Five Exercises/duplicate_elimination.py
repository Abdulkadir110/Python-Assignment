
def unique_numbers_in(numbers_list):
    unique_list = []
    for number in numbers_list :
        duplicate = 0
        for digit in numbers_list :
            if number == digit :
                duplicate += 1
        if duplicate == 1:
            unique_list.append(number)
    return unique_list
    
print([8,8,6,5,6,7,4,3,2,3])
print(unique_numbers_in([8,8,6,5,6,7,4,3,2,3]))
