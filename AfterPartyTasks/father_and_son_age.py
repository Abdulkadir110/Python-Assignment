#Start
#Collect the father age and his son age inputs from the user.
#the father age is twice as old as the son after n years.
#so the father age + n years = 2(son age + n)
#set the son age multiply by 2
#so the twice of the son age is substracted from the father age
#then the result is added to their current age to know how old they will be after n years
#if the result is greater than 0, it should print it
#else -1 is multiplied by the number to make it positive for the n years ago or after.
#End




current_father_age = int(input("Enter the current age of the father's: "))
current_son_age = int(input("Enter the current age of his son: "))

twice_son_age = 2 * current_son_age

twice_year = current_father_age - twice_son_age

age_of_the_father = current_father_age + twice_year
age_of_the_son = current_son_age + twice_year

if twice_year > 0 :
     age_of_the_father = current_father_age + twice_year
     print("The father will be twice as old as the son after: ", twice_year, "years" ,sep ="")
if twice_year < 0 :
      new_twice_year = twice_year * -1
      print("The father will be twice as old as the son after: ", new_twice_year, "years" ,sep="")


                      
