number = int(input("Enter a number: "))
prime_counter = 0
def is_palindrome_and_prime_number(number) :
    if(number % 10) == (number /10000) % 10 :
        if((number /10) % 10) == ((number /1000) % 10) :
             print("number is a palindrome")
    prime_counter = 0

    for prime in range(1 , number + 1) :
                if number % prime == 0:
                     prime_counter +=1
    return (prime_counter == 2)     


result = is_palindrome_and_prime_number(number)
print(result)
