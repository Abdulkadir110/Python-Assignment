counter = 0
total = 0
while (counter <=10) : 
    number = int(input("Enter a number: "))
    total += number
    counter += 1
    if(counter == 10)   :
        average = total / 10
        print("The average is: ", average)
        break
    

