
from functools import reduce
def sumUp(accumulator, number):
    return accumulator + number

def reduceNumbersIn(numbers) :
    return reduce(sumUp, numbers)
