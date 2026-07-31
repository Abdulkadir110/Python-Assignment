problem_question = input("What is your problem: ")
problem_choice = input("Have you had this problem before(yes or no)? ").lower()

if problem_choice  == "yes" or problem_choice == "y" :
    print("Well, you have it again. ")
else :
    print("Well, you have it now. ")
