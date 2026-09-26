def is_palindrome(word):
    word = word.lower()
    return word[::-1] == word

def get_list_of(words):
    return [is_palindrome(word)   for word in words]
