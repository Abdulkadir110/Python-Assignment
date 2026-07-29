#Write a program that take a sentence input and returns the number of vowels, consonants, spaces, uppercase,lowercase and symbols in the sentence

sentence = input("Enter a sentence: ");

vowel_counter = 0;
consonant_counter = 0;
uppercase_counter = 0;
lowercase_counter = 0;
symbol_counter = 0;
space_counter = 0;

for characters in sentence:
        if(characters == 'a' or characters == 'e' or characters == 'i' or characters == 'o' or characters == 'u'):
            vowel_counter += 1

        elif (characters.isalpha()) :
            consonant_counter += 1

        if (characters.upper()) :
            uppercase_counter += 1

        if (characters.lower()) :
            lowercase_counter += 1
                
        if (characters.isspace()) :
            space_counter += 1
        
        if (characters.issymbol()) :
            symbol_counter += 1

       
        
print("Consonant: " + str(consonant_counter)) 
print("Uppercase: " + str(uppercase_counter))
print("lowercase: " + str(lowercase_counter))
print("Vowel: " + str(vowel_counter))
print("Symbol: " + str(symbol_counter))
print("Spaces: " + str(space_counter))




