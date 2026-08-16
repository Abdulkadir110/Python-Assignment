decimal_number = int(input("Enter a decimal number: "))
binary_number = ""

if decimal_number == 0:
    binary_number = "0"
else:
    num = decimal_number
    while num > 0:
        remainder = num % 2
        binary_number = str(remainder) + binary_number
        num = num // 2

print("Binary:", binary_number)
