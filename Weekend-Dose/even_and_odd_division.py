number = int(input("Enter a number: "))
counter = 0
while(number >= 1) :
    if(number % 2 == 0) :
        number /= 2
    else :
        number /= 3 + 1

    counter +=1
 
print("The number of times it takes to reach for n to be 1 is:", counter)


