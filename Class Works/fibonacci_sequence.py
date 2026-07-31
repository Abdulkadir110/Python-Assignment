
def fibonacci(number) :
    total = 0
    for numbers in range(1, number + 1) :
        for add in range(number) :      
            total = add + numbers 
        
    return (numbers, total)

print(fibonacci(20))
