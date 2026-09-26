from functools import reduce

def getMaximum(accumulator, number):
    if number > accumulator:
        return number
    else:
        return accumulator

print(reduce(getMaximum, [3,7,2,9,1]))


def concatenate(accumulator, word):
    accumulator += word
    return accumulator

print(reduce(concatenate, ["Hello", "", "World"]))

#def mergedList(accumulator, dictionary):
#    accumulator + dictionary
#    return accumulator
#
#print(reduce(mergedList, [{'a': 1}, {'b' : 2}, {'c', 3}]))

def getSquare(accumulator, number):
    return accumulator + (number**2)


print(reduce(getSquare, [1,2,3]))
