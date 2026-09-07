
movies = []
movies_ratings = []
def add_movie_to(movie_name) :
    movies.append(movie_name)  
    
def add_movie_and_rating_to(movie_name, rating) :
    for movie in movies_ratings :
        if movie[0] == movie_name :
            movie[1].append(rating)
            return movies_ratings
    movies_ratings.append([movie_name, [rating]])
            
    return movies_ratings

def get_average_rating_for(movie_name):
    for movie in movies_ratings:
        if movie[0] == movie_name:
            ratings = movie[1]
            if len(ratings) == 0:
                return sum(ratings)
            return sum(ratings) / len(ratings)


