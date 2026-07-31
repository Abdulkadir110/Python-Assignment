#Write a program that take a sentence input and returns the number of vowels, consonants, spaces, uppercase,lowercase and symbols in the sentence

sentence = input("Enter a sentence: ");

def count_vowels(sentence):
    counter = 0
    vowels = "aeiouAEIOU"
    for letter in sentence:
        if letter in vowels:
            counter += 1
    return counter
 
 
def count_consonants(sentence):
    counter = 0
    vowels = "aeiouAEIOU"
    for letter in sentence:
        if letter.isalpha() and letter not in vowels:
            counter += 1
    return counter
 
 
def count_spaces(sentence):
    counter = 0
    for letter in sentence:
        if letter == " ":
            counter += 1
    return counter
 
 
def is_symbol(char):
    return "!" <= char <= "/" or ":" <= char <= "@" or "[" <= char <= "`" or "{" <= char <= "~"
 
 
def count_symbols(sentence):
    counter = 0
    for letter in sentence:
        if is_symbol(letter):
            counter += 1
    return counter
 
 
def count_uppercase(sentence):
    counter = 0
    for letter in sentence:
        if letter.isupper():
            counter += 1
    return counter
 
 
def count_lowercase(sentence):
    counter = 0
    for letter in sentence:
        if letter.islower():
            counter += 1
    return counter

def count_digits(sentence):
    counter = 0
    for letter in sentence:
        if letter.isdigit():
            counter +=1
    return counter

def check_sentence(sentence) :
    print("The number of vowels is: ", count_vowels(sentence))
    print("The number of consonants is: ", count_consonants(sentence))
    print("The number of spaces is: ", count_spaces(sentence))
    print("The number of symbols is: ", count_symbols(sentence))
    print("The number of uppercases is: ", count_uppercase(sentence))
    print("The number of lowercases is: ", count_lowercase(sentence))
    print("The number of digits is: ", count_digits(sentence))


print(check_sentence(sentence))



