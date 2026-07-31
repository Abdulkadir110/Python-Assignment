
number = input("Enter a number in base 10: ")
index = len(number) -1
total = 0
for digits in number:
    total += (int(number) / 2 ) % 2
    index -= 1

print(total)

