# Write a python program that create a list of  10 random numbers between 1 and 50

import random
def lengthOf(list):
    length = 0
    for _ in list:
        length +=1
    return length
 
def sumOf(list):
    total = 0
    for element in list:
        total += element
    return total

def productOfEveryThirdElementsIn(list):
    product = 1
    for index in range(2, lengthOf(list), 3):
        product *= list[index]
    return product  

def averageOf(list):
    return sumOf(list) / lengthOf(list)

def getTheLargestIn(list):
    largest = list[0]
    temp = 0
    for index in range(lengthOf(list)):
        if list[index] > largest:
            temp = largest
            largest = list[index]
            list[index] = temp
    return largest

def getTheSmallestIn(list):
    smallest = list[0]
    for index in range(lengthOf(list)):
        if list[index] < smallest:
            temp = smallest
            smallest = list[index]
            list[index] = temp
    return smallest

def check(list): 
    for string in list:
        length = lengthOf(string)
        if length >= 2 and string[0] == string[length - 1] :
            return string



my_list = []
numbers = [2,3,4,5,7,8,9,12,15]
print(numbers)
print()
print("Length is:", lengthOf(numbers))
print("The sum is: ", sumOf(numbers))
print("The product is: ", productOfEveryThirdElementsIn(numbers))
print("The average is: ", averageOf(numbers))
print("The largest is: " , getTheLargestIn(numbers))
print("The smallest is: ", getTheSmallestIn(numbers))
print()
print("---------------------A program that count number of strings---------------------------------")
words = ["ade", "bolu", "emma", "tolu", "bola", "adebala", "bolu"]
print(words)
print()
print("The length of the given list of strings is: ", lengthOf(words))
print("The element that has length greather than 2 and the first char is equal to last char is: ", check(words))

list = []
for _ in range(10):
    numbers = random.randrange(1, 50)
    list += [numbers]
    

print("The list of 10 random numbers in range of 50 is:" , list)






for _ in range(11):
    number = random.randint(1,50)
    my_list += [number]




