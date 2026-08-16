

def check_balance(balance):

    return balance
    
    
def deposit(deposited_amount,balance):

    if deposited_amount > 0.0:
        balance +=  deposited_amount
    
    return balance


    	
def withdraw(amount, balance):

    if balance >= amount > 0:

        balance -= amount
    
    return balance
    




