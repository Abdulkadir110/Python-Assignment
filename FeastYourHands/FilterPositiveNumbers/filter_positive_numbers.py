
def isPositive(number):
    return number >= 0

def filter_out_negatives(numbers):
    return list(filter(isPositive, numbers))
