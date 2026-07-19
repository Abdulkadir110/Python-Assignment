#Cost of Driving

#Collect input for distance, miles per gallon and price per gallon
#Calculate cost of Driving:
#The result from the division of distance by miles per gallon is multiplied by fuel price


driving_distance = float(input("Enter the driving distance: "))
miles_per_gallon = float(input("Enter miles per gallon: "))
price_per_gallon = float(input("Enter price per gallon: "))



division_of_driving_distance_by_miles_per_gallon = driving_distance / miles_per_gallon

cost_of_driving = division_of_driving_distance_by_miles_per_gallon * price_per_gallon

print("The cost of driving is: $", cost_of_driving, sep="")


