#Days Selection

#ask your to enter day number between (1 to 7)
#then print the day the number falls in

day_number = int(input("Enter the day number(1 to 7): "))

match(day_number) :
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("Invalid number")


    
