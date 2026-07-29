sum = 0;
total = 0;
for numbers in range(1, 10) :
    if numbers % 4 == 0 :
        
        for power in range(1, 6) :
            number = pow(numbers, power)
            sum += number
            total += sum
            
                
print(sum, end = " ")

