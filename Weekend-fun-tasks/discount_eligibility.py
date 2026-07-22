#Discount Eligibility

total_bill = float(input("Enter the total bill: "))
is_member = input("Are you a member(yes or no): ")

if total_bill >= 1000 and is_member == "yes" :
    print("The discount is 10% off")
elif total_bill >= 1000 and is_member == "no" :
    print("The discount is 5% off")

else :
    print("your final amount is ", total_bill ,"as there is no discount for you", end = "")
    print("thank you for your patronage.")
