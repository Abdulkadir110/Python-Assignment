

from account_functions import *

def isDigit(balance, amount) :
    for digit in amount:
        if  not digit.isdigit():
            print("Invalid")
            break
    else: 
        amount = float(amount)
    
        new_balance =  deposit(amount,balance)
    
        if new_balance == balance:
            printd("Invalid Amount Inputted")
            
        else:
            balance  =  new_balance
            print("Deposit was Successful")
    return balance

    
def main():



    balance =  0
    
    
    print("Welcome to ORION Account . . . . . ")
    
    menu =  """
    
    
        1. check Balance 
        
        2. Deposit
        
        3. Withdrawal
        
        0. exit
    
    """
    
    tracker  = 1
        
    while (tracker != 0):
    
        choice =  input(f"{menu}\nEnter Your Choice:  ")

        match choice:

            case "1": 
                    current_balance  =  check_balance(balance)
                    print(f"Your Account Balance:  {current_balance}")
                    
            case "2":
                    amount  =  input("Enter your Amount to Deposit:  ")
#                    isDigit(balance, amount)
                    
                    for digit in amount:
                        if  not digit.isdigit():
                            print("Invalid")
                            break
                            
                            
                    else: 
                        amount = float(amount)
                    
                        new_balance =  deposit(amount,balance)
                    
                        if new_balance == balance:
                            print("Invalid Amount Inputted")
                            
                        else:
                            balance  =  new_balance
                            print("Deposit was Successful")
                        
            case "3": 
                    
                amount  =  float(input("Enter your Amount to Deposit:  "))
                    
                new_balance =  withdraw(amount, balance)
                if new_balance == balance:
                        print("Invalid Amount Inputted")
                        
                else:
                    balance  =  new_balance
                    print("Withdrawal was Successful")
            
                    
            case "0": 
                print("Oya Go Rest !!!!")
                tracker  = 0        
                break
            case _ : print("Pls Get sense !!!!!")

             
             

#if __name__ == "__main__":

main()    

    
    
    
    
    
    
    
    
