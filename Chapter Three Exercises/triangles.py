#Question 3.18 (Nested Looping)

for vertical in range (1, 11):
    for first_triangle in range(1, vertical + 1) :    
        print("*", end = "")
    for first_space in range(11, vertical, -1) :
        print(" ", end = "")
    for second_triangle in range(11, vertical, -1)  :
        print("*", end = "")
    for second_space in range(1, vertical + 1) :
        print(" ", end = "")
    for third_space in range(1, vertical + 1) :
        print(" ", end = "")
    for third_triangle in range(11, vertical, -1)  :
        print("*", end = "")
    for fouth_space in range(12, vertical, -1)  :
        print(" ", end = "")
    for fourth_triangle in range(1, vertical + 1) :
        print("*", end = "")
    print()
