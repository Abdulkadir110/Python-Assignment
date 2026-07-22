#Question 1 under String_conditional_questions

word = input("Enter the word: ")

word_length = len(word)

if word_length < 5 :
    print("The word, ", word, "is a short string")
elif 5 <= word_length <= 10 :
    print("The word, ", word, "is a medium string")
else :
    print("The word, ", word, "is a long string")
