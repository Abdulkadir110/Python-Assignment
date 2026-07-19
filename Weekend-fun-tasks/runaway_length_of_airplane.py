#Question 2.12 (physcis: finding runaway length

#prompt the user to enter velocity(m/s) and acceleration(m/s^2)
# Calculate the minimum runaway length
# the velocity squared / 2 multiplied by acceleration

velocity = float(input("Enter the velocity: "))
acceleration = float(input("Enter the acceleration: "))


length_numerator = velocity * velocity
length_denomerator = 2 * acceleration

minimum_runaway_length = length_numerator / length_denomerator

print("The minimum runaway length for this airplane is: ", minimum_runaway_length)
