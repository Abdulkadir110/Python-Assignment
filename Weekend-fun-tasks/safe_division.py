#Safe Division

# Ask the user for two integers x and y
# if y != 0, print x/y
# else if y == 0, print cannot divide by zero


x = int(input("Enter thr value of x: "))
y = int(input("Enter thr value of y: "))

if y != 0 :
    result = x / y
    print("x / y = ", result)
else :
    print("Cannot divide x by zero")
