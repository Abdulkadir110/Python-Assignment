#def is_palindrome(texts) :
#    is_palindromes = []
#    
#    for word in texts: 
#        if word[: : -1] == word :
#            is_palindromes.append(True)
#            
#        else: is_palindromes.append(False)
#    
#    return is_palindromes
#    
#random_text = ["madam", "honour", "12321", "carac", "carrace"]
#
#print(random_text)
#print()
#print(is_palindrome(random_text))
#
#print(is_palindrome("madam"))
#print(is_palindrome("honour"))
#print(is_palindrome("12321"))

#def is_palindrome(texts) :
#    
#    list_ = [True   for word in texts   if word[::-1] == word ]
#    return list_
#    
#    
#    
#random_text = ["madam", "honour", "12321", "carac", "carrace"]
#print(random_text)
#print()
#print(is_palindrome(random_text))
def get_prime(numbers):
    return [number    for number in numbers  if len([0 for divisor in range(2, number)   if number % divisor == 0]) == 0]


#def get_prime(numbers):
#    prime_numbers = []
#    for number in numbers:
#        counter = 0
#        for divisor in range(2, number) :
#            if number % divisor == 0 :
#                counter += 1
#        if counter == 0:
#            prime_numbers.append(number)
#    
#    return prime_numbers
# bug except using walrus operator        [counter += 1 for divisor in range(2, number) if number % divisor == 0]

#def get_prime(numbers):
#    prime_numbers = []
#    for number in numbers:
#        counter = 0
#        redundant_numbers = [counter for divisor in range(2, number) if number % divisor == 0]
#        
#        print("Sample: ", redundant_numbers)
#        if len(redundant_numbers) == 0:
#            prime_numbers.append(number)
#    
#    return prime_numbers

#def get_prime(numbers):
#    prime_numbers = []
#    counter = 0
#        
#    r = [number for number in numbers if len([0 for divisor in range(2, number) if number % divisor == 0]) == 0 ]
#        
#    print(r)   
#    prime_numbers.append(number)
#    
#    return prime_numbers

#def get_prime(numbers):
#    return [number for number in numbers if len([0 for divisor in range(2, number) if number % divisor == 0]) == 0 ]
#    
print([12,6,7,8,9,0,8,7,6,5,4,3])
print("List of prime numbers are: ", get_prime([12,6,7,8,9,0,8,7,6,5,4,3]))
    
