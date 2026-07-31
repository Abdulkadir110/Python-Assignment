#GUESS A NUMBER!

NUMBER = 7


number = 0
while number != NUMBER:
    number = int(input("Guess the number: "))
    if number <= 1000 :  
        if number == NUMBER :
            print("Congratulations.You guessed the number!")
        elif number > NUMBER :
            print("too high.Try again.") 
        elif number < NUMBER :
            print("Too low. Try again")
    else :
        print("The guess is between 1 to 1000, try again")
