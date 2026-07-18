user_input = int(input("Enter a five digits number: "))
first_digit = int(user_input % 10)
second_digit = int((user_input /10) % 10)
third_digit = int((user_input /100) % 10)
fourth_digit = int((user_input /1000) % 10)
fifth_digit = int((user_input /10000) % 10)

print(fifth_digit,"\t",fourth_digit,"\t",third_digit,"\t",second_digit,"\t",first_digit)
