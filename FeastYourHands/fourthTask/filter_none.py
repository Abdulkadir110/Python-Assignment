def is_not_None(number):
    return number != None

def filter_out_None(numbers):
    return list(filter(is_not_None, numbers))
