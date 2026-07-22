#BMI category


weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height * height)

if bmi < 18.5 :
    print("you are underweight")
elif 18.5 <= bmi <= 24.9 :
    print("You are normal")
elif 25 <= bmi <= 29.9 :
    print("You are overweight")
elif bmi >= 30 :
    print("You are obese")
