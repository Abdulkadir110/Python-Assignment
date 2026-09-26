def is_square(number):
    return (number ** 0.5) % 1 == 0

def get_list_of(numbers):
    return [is_square(number) for number in numbers]  
