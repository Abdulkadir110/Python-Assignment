
def exponient_of(base, exponient):
    total = 1
    for number in range(1, exponient+ 1, 1) :
        total *= base 
    return total

base = int(input("Enter the number: "))
exponient = int(input("Enter your exponient: "))

print(f"{base} raised to power of {exponient} is: ", exponient_of(base, exponient))
