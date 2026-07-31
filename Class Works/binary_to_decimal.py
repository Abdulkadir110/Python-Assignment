given_number = input("Enter your number: ")

total = 0
index = len(given_number) - 1
for number in given_number:
    total += int(number) * 2** index
    index -= 1

print("decimal: " ,total)




        
       
