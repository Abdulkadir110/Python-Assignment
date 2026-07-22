# Rock Paper Scissors
print("--" * 10, "Let the game begins", "--" * 10)
player_one = input("Enter either rock, paper or scissors: ")
player_two = input("Enter either rock, paper or scissors: ")



if player_one == "rock" and player_two == "scissors" :
    print("Congratulations to player 1 , you won!")
elif player_one == "paper" and player_two == "rock" :
    print("Congratulations to player 1 , you won!")
elif player_one == "scissors" and player_two == "paper" :
    print("Congratulations to player 1 , you won!")
elif player_two == "rock" and player_one == "scissors" :
    print("Congratulations to player 2 , you won!")
elif player_two == "paper" and player_one == "rock" :
    print("Congratulations to player 1 , you won!")
elif player_two == "scissors" and player_one == "paper" :
    print("Congratulations to player 1 , you won!")
   
else :
    print("This is tie")
