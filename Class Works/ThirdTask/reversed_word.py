
def is_exist(word, given_letter):
    for letter in word:
        if given_letter == letter :
            return True
            
    return False

def reversed_word(word, given_letter):
    if not is_exist(word, given_letter):
        return word
    length = len(word)
    newWord = ""
    for index in range(1, length) :
        if word[index] == given_letter :
            newWord += word[index: : -1]
            newWord += word[-1 : index - 1: -1]
            return newWord
    if word[0] == given_letter :
        newWord += given_letter
        newWord += word[length : : -1]
        return newWord
    return "" 


#def lefttoright(word, gletter):
#    for index, letter in enumerate(word):
#        if(letter == gletter) return word[index : : -1]
#
#def righttoleft(word, gletter):
#    for index, letter in enumerate(word):
#        if(letter == gletter) return word[-1 :index + 1 : -1]
#
#def newWods(word, gletter):
#    newWodsR = ""
#    newWodsR += righttoleft(word, gletter) + lefttoright(word, gletter)
#    
#    
