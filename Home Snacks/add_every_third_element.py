
def addEveryThirdElementIn(numbers):
    total = 0
    for index in range(2, len(numbers), 3):
        total += numbers[index]
    return total
    
numbers = [2,4,5,6,7,8,9,11,2,5,3,4,6]
print("The sum is :",addEveryThirdElementIn(numbers))
