
weight = int(input("Enter the weight: "))  

height = int(input("Enter the height: "))  

 #       print(f" 1 x {number : ^ 3} = {number * 1: ^8} 2 x {number: ^ 3} = {number * 2: < 8} 3 x {number: ^ 3} = {number * 3: < 8} 4 x {number: ^ 3} = {number * 4: < 8} 5 x {number: ^ 3} = {number * 5: < 8} 6 x {number: ^ 3}  = {number * 6: < 8} 7 x {number: ^ 3}  = {number * 7: <8} 8 x {number: ^ 3} = {number * 8: <8} 9 x {number: ^ 3}  = {number * 9: <8} 10 x {number: ^ 3}  = {number * 10: <8} 11 x {number: ^ 3}  = {number * 11: <8} 12 x {number: ^ 3}  = {number * 12: <8}")


for index in range(1, height + 1) :
         
    for number in range(1, weight + 1) :
    

        print(f"{index} x {number} = {number * index} ", end = "")

    print()
