# arithmetric , smallest and largest

x = int(input("enter your fist number: "))
y = int(input("Enter your second number: "))
z = int(input("Enter our third number: "))

sum = x + y + z
product = x * y * z
average = sum / 3
smallest = 0
largest = 0

if x > y and y > z :
    largest = x
    smallest = z
if y > x and x > z :
    largest = y
    smallest = z
if z > x and x > y :
    largest = z
    smallest = y
if z > y and y > x :
    largest = z
    smallest = x
if x > z and z > y :
    largest = x
    smallest = y
if y > z and z > x :
    largest = y
    smallest = x
    
print("The sum of ",x,y,z, "is: ", sum)
print("The average of ",x,y,z, "is: ",average)
print("The smallest number is: ", smallest)
print("The largest number is: ",largest)

