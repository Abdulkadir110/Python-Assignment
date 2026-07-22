# Vowel And Consonant

letter = input("Enter a letter: ")


if letter.isalpha() :
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" :
        print("The letter is a vowel")

    elif letter != "a" or letter != "e" or letter != "i" or letter != "o" or letter != "u" :
        print("The letter is consonant")
else:
    print("Invalid input")
