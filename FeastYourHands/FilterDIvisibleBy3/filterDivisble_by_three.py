
def is_divisible_by_three(number):
    return number % 3 == 0

def filter_out_numbers_not_divisible_byThree(numbers):
    return list(filter(is_divisible_by_three, numbers))
