#Question 4 under String Conditional questions

name = input("Enter your name: ")
name_length = len(name)


if 3 < name_length <= 5 :
    print("Hi, ", name, "!", sep="")
else :
    print("Hello, ", name, "!", sep="")
