
def fatigueOfStudent(number):
        match(number):
            case 1: print("No, please Try again")
            case 2: print("Very good!, Nice work!")
            case 3: print("No, please Try again")
            case _: print("Oga, select between 1 - 3")
        return number;
        
        
number = int(input("Enter a number: "))
print(fatigueOfStudent(number))
