#4.9 Temperature conversion

def celsius_to_farenheit (celsius_value) :
    return (9/5) * celsius_value + 32
        

for celsius in range(101) :
    print(f"{celsius}\t{celsius_to_farenheit(celsius)}")

