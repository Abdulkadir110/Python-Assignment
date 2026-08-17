import random

questions = random.randint(1,10);
right_score = 0
failed_score = 0
count = 0


while count != 10 :
    while(count < 10):
        questions = random.randint(1,10); 
        match(questions) :
            case 1 :
                question_one = """
                            Question 1
                    What is the capital city of Australia?
                    
                    A) Sydney
                    B) Melbourne
                    C) Canberra
                    D) Brisbane
                """
                print(question_one)
                answer = input("Enter your correct option: ").lower()
                count += 1
                if answer == "c": 
                    print("Correct!")
                    right_score += 1
                else :
                    print("Wrong!")
                    failed_score += 1
            case 2 :
                question_two = """
                            Question 2                            
                    Which planet in our solar system is known as the Red Planet?
                    
                    A) Venus
                    B) Mars
                    C) Jupiter
                    D) Saturn
                """
                print(question_two)
                answer = input("Enter your correct option: ").lower()
                count += 1
                if answer == "b":
                    print("Correct!")
                    right_score += 1
                else :
                    print("Wrong!")
                    failed_score += 1
            case 3 :
                question_three = """
                            Question 3
                    Who painted the Mona Lisa?
                    
                    A) Vincent van Gogh
                    B) Pablo Picasso
                    C) Leonardo da Vinci
                    D) Claude Monet
                """
                print(question_three)
                answer = input("Enter your correct option: ").lower()
                count += 1
                if answer == "c": 
                    print("Correct!")
                    right_score += 1
                else :
                    print("Wrong!")
                    failed_score += 1
            case 4 :
                question_four = """
                            Question 4
                    What is the largest ocean on Earth?
                    
                    A) Atlantic Ocean
                    B) Indian Ocean
                    C) Arctic Ocean
                    D) Pacific Ocean
                """
                print(question_four)
                answer = input("Enter your correct option: ").lower()
                count += 1
                if answer == "d":
                    print("Correct!")
                    right_score += 1
                else :
                    print("Wrong!")
                    failed_score += 1
            case 5 :
                question_five = """
                            Question 5
                    How many bones are in the adult human body?
                    
                    A) 150
                    B) 206
                    C) 250
                    D) 310
                """
                print(question_five)
                answer = input("Enter your correct option: ").lower()
                count += 1
                if answer == "b": 
                    print("Correct!")
                    right_score += 1
                else :
                    print("Wrong!")
                    failed_score += 1
            case 6 :
                question_six = """
                            Question 6
                    Which element has the chemical symbol 'O'?
                    
                    A) Gold
                    B) Oxygen
                    C) Silver
                    D) Iron
                """
                print(question_six)
                answer = input("Enter your correct option: ").lower()
                count += 1
                if answer == "b":
                    print("Correct!")
                    right_score += 1
                else :
                    print("Wrong!")
                    failed_score += 1
            case 7 :
                question_seven = """
                            Question 7
                    In what year did the Titanic sink?
                    
                    A) 1905
                    B) 1912
                    C) 1920
                    D) 1931
                """
                print(question_seven)
                answer = input("Enter your correct option: ").lower()
                count += 1
                if answer == "b": 
                    print("Correct!")
                    right_score += 1
                else :
                    print("Wrong!")
                    failed_score += 1
            case 8 :
                question_eight = """
                            Question 8
                    What is the hardest natural substance on Earth?
                    
                    A) Gold
                    B) Iron
                    C) Diamond
                    D) Quartz
                """
                print(question_eight)
                answer = input("Enter your correct option: ").lower()
                count += 1
                if answer == "c":
                    print("Correct!")
                    right_score += 1
                else :
                    print("Wrong!")
                    failed_score += 1
            case 9 :
                question_nine = """
                            Question Nine
                    Which country is home to the ancient city of Petra?
                    
                    A) Egypt
                    B) Jordan
                    C) Greece
                    D) Turkey
                """
                print(question_nine)
                answer = input("Enter your correct option: ").lower()
                count += 1
                if answer == "b": 
                    print("Correct!")
                    right_score += 1
                else :
                    print("Wrong!")
                    failed_score += 1
            case 10 :
                question_ten = """
                            Question 10
                    What is the chemical formula for water?
                    
                    A) CO2
                    B) H2O
                    C) NaCl
                    D) O2
                """
                print(question_ten)
                answer = input("Enter your correct option: ").lower()
                count += 1
                if answer == "b":
                    print("Correct!")
                    right_score += 1
                else :
                    print("Wrong!")
                    failed_score += 1
                    

if right_score == 10 :
    print(f'You got {right_score} out of 10, Good job!')
    
else:
    print(f'you got {right_score} questions corretly and failed {failed_score}')
