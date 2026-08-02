#ATM SIMULATOR

balance = 1000
is_running = True

while is_running :
    menu_functions = """

1 - Deposit
2 - Withdraw
3 - Check Balance
0 - Exit
"""

    print(menu_functions)
    user_input = int(input("Press a number: "))
    match (user_input) :
        case 1 : 
            deposit = int(input("How much do want to deposit: "))
            balance = balance + deposit
            print("New balance is: ", balance)
        
        case 2: 
            withdraw = int(input("How much do want to withdraw: "))
            if withdraw <= balance :
                balance = balance - withdraw
                print("New balance is: ", balance)
            else :
                print("Insufficient Funds, your balance is ", balance)
        
        case 3: 
            print("Balance is: ", balance)    
        
        case 0 : 
            is_running = False
            print("Thank you for using our services")

        case _:
            print("invalid input")
          
    
