
def summarize_letters(texts):
    texts.lower()
    lists = []
    for letter in texts:
        count = 0
        for compare in texts:
            if letter == compare :
                count += 1
        if count == 1 :  
            turple = letter, count      
            lists.append(turple)
    return lists
    

print("retyur")
print(summarize_letters("retyur"))    


