#Start
#collect three subjects scores from the user
#calculate the average of the three scores
#if the average falls within the score scale,
#it should print the letter grade associated with it.
#End

print("-" * 20, "Student Grade Application", "-" * 20)
print("-" * 20, "Enter scores for the subjects", "-" * 20)

mathematics_score = float(input("Mathematics: "))
english_score = float(input("English: "))
civic_education_score = float(input("Civic eduction: "))

average_score = float((mathematics_score + english_score + civic_education_score) / 3)

if 90<=average_score<=100 :
    print("Your grade is A")
    
elif 80<=average_score<90 :
    print("Your grade is B")
    
elif 70<=average_score<80 :
    print("Your grade is C")
    
elif 60<=average_score<70 :
    print("Your grade is D")
    
elif 0<=average_score<60 :
    print("Your grade is F")


    
    




