
alpha_list = ['d', 'e', 'b', 'c', 'f', 'c', 'b', 'a', 'd', 'c', 'e', 'b', 'f', 'd', 'c', 'c', 'd', 'd', 'd', 'f']

sorted_alpha_list = sorted(alpha_list)

print(sorted_alpha_list)
reversed_alpha_list = sorted(alpha_list, reverse=True)
print()
print(reversed_alpha_list)

def get_unique_letters_in(given_list):
    unique_list = []
    for letter in alpha_list :
        count = 0
        for compare in alpha_list :
            if letter == compare :
                count += 1
        if count == 1 :
            unique_list.append(letter)
    return unique_list
  

print(get_unique_letters_in(alpha_list))  
     
