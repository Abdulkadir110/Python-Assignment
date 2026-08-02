
SECRET_NUMBER = 7
user_input = 0
while(user_input != SECRET_NUMBER) :
    user_input = int(input("Guess the number: "))
    
    if(user_input > SECRET_NUMBER) :
        print("The guessed number is too high, try again!")
    elif user_input < SECRET_NUMBER :
        print("The guessed number is too low, try again!")

print("Yayyyyy....You got it.")
