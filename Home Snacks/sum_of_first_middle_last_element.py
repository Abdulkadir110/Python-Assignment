# write a python function to calculate the sum of the first, middle and last elements within a designated list. 

def sumOfFirstMiddleLastIn(list):
    total = 0
    middle = 0
    length = len(list)
    if length & 2 == 0 :
        middle = (list[length // 2] + list[(length // 2 - 1)]) / 2
    else :
        middle = list[length // 2]

    total += list[0] + middle + list[- 1] 
    
    return total
    

numbers = [1,2,3,4,5,6,7,8,9,10]
print(sumOfFirstMiddleLastIn(numbers))           
