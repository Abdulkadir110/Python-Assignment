from movie_rating_system import *

movies = []
movies_ratings = []

print("Welcome to my movie cinema")
exit = 0
while exit != -1:
    print("1. Add a Movie")
    print("2. Rate a Movie")
    print("3. View Average Ratings")
    print("4. Exit")
 
    choice = input("Enter your choice: ")
    
    if choice == "1":
        movie_name = input("Enter movie name: ").strip()
        add_movie_to(movie_name)
        print(f"Movie \"{movie_name}\" added.")
 
    elif choice == "2":
        movie_name = input("Enter movie name: ").strip()
 
        if movie_name not in movies:
            print(f"\"{movie_name}\" hasn't been added yet. Add it first.")
        else:
            rating_input = int(input("Enter rating (1-5): "))
            if 1 <= rating_input <= 5 : 
                add_movie_and_rating_to(movie_name, rating_input)
                print(f"Rated \"{movie_name}\" with {rating_input}.")
            else:
                print(f"Enter number between 1 to 5")
 
    elif choice == "3":
        averages = get_all_average_ratings()
        if not averages:
            print("No ratings yet.")
        else:
            print("Average Ratings:")
            for name, average in averages:
                print(f"- {name}: {average:.2f}")
 
    elif choice == "4":
        print("Goodbye!")
        exit = -1
 
    else:
        print("Oga commot my cinema joor, you no dey hear instructions")
