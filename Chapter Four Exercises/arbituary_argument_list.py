
def arbituary_list (*numbers) :
    product = 0
    for number in numbers: 
        product += number * number
    
    return product

print(arbituary_list(5,3,2,1,4,5,4,7,6,7))
