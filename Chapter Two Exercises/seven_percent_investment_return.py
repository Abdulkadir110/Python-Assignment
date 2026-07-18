fixed_balance = 1000

deposit_after_ten_years = 0
deposit_after_twenty_years = 0
deposit_after_thirty_years = 0

fixed_rate = 0.07



deposit_after_ten_years = float(float(fixed_balance) * float(((1 + float(fixed_rate) ** 10))))
deposit_after_twenty_years = int(int(fixed_balance) * float(((1 + float(fixed_rate))** 20)))
deposit_after_thirty_years = int(int(fixed_balance) * int(((1 + int(fixed_rate))** 30)))

print("The deposit after ten years is: ", deposit_after_ten_years)
print("The deposit after twenty years is: ", deposit_after_twenty_years)
print("The deposit after thirty years is: ", deposit_after_thirty_years)                            


#xponient = 2 ** 10000
#print("exponient: ", xponient)

