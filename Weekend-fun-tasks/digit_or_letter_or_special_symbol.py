# Question 5 under String conditional questions

character = input("Enter a character: ")
character_length = len(character)

if character_length == 1 :
    if character.isdigit() :
        print(chracter, "is a digit")
    elif character.isalpha() :
        print(character, "is a letter")
    else :
        print(character, "is a special symbol")
