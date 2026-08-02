input = int(input("Enter a number: "))

primecounter = 0
for number in range (2, input + 1,1) :
    primecounter = 2
    primecounter = 0
    for prime in range(1, input+1,1):
         if(number % prime == 0) :
            primecounter +=1
    if(primecounter == 2) :
        print(number)
