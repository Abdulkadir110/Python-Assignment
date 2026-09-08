from datetime import datetime
 
movies = []
movies_ratings = []
 
def add_movie_to(movie_name):
    if movie_name not in movies:
        movies.append(movie_name)
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
        movies_ratings.append([movie_name, current_datetime, []])
    return movies
 
 
def add_movie_and_rating_to(movie_name, rating):
        return [movie[2].append(rating) for movie in movies_ratings if movie[0] == movie_name]
 
def get_average_rating_for(movie_name):
    for movie in movies_ratings:
        if movie[0] == movie_name:
            total = 0
            count = 0
            if len(movie[2]) == 0 :
                return
            for rating in movie[2]:
                total += rating
                count += 1
            return total / count
   
        
def get_all_average_ratings():
    return [(movie[0] , get_average_rating_for(movie[0])) for movie in movies_ratings]
    


