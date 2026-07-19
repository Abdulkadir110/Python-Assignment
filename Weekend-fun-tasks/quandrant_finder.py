# Quandrant Finder

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))


if x > 0 and y > 0 :
    print("Q1")
elif x < 0 and y > 0 :
    print("Q2")
elif x < 0 and y < 0 :
    print("Q3")
elif x > 0 and y < 0 :
    print("Q4")
elif x == 0 and y == 0 :
    print("Origin")
elif x != 0 and y == 0 :
    print("X-axis")
elif x == 0 and y != 0 :
    print("Y- axis")
