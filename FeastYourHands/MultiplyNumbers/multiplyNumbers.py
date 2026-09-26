from functools import reduce

def multiply(accumulator, number):
    return accumulator * number

def reduceNumbersIn(numbers):
    return reduce(multiply,numbers)
