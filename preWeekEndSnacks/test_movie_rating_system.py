import unittest
from datetime import datetime
from movie_rating_system import *
class test_movie_rating_system(unittest.TestCase):
 
    def setUp(self):
        movies.clear()
        movies_ratings.clear()
 

    def test_add_movie_to(self):
        add_movie_to("Inception")
        self.assertEqual(len(movies_ratings), 1)
        
    def test_add_movie_to_creates_movies_ratings_entry(self):
        add_movie_to("Inception")
 
        self.assertEqual(len(movies_ratings), 1)
 
        movie_name = movies_ratings[0][0]
        movie_ratings_list = movies_ratings[0][2]
 
        self.assertEqual(movie_name, "Inception")
        self.assertEqual(movie_ratings_list, []) 
 
    def test_movie_datetime_is_current(self):
        add_movie_to("Inception")
 
        movie_datetime = movies_ratings[0][1]
        expected_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
 

        self.assertEqual(movie_datetime, expected_datetime)
 
    def test_movie_datetime_does_not_change_when_rated(self):
        add_movie_to("Inception")
        original_datetime = movies_ratings[0][1]
 
        add_movie_and_rating_to("Inception", 5)
        datetime_after_rating = movies_ratings[0][1]
 
        self.assertEqual(original_datetime, datetime_after_rating)

    def test_add_movie_and_rating_to_new_movie(self):
        add_movie_to("Inception")
        add_movie_and_rating_to("Inception", 4)
 
        self.assertEqual(len(movies_ratings), 1)
 
        movie_name = movies_ratings[0][0]
        movie_ratings_list = movies_ratings[0][2]
 
        self.assertEqual(movie_name, "Inception")
        self.assertEqual(movie_ratings_list, [4])
 
    def test_add_rating_to_existing_movie(self):
        add_movie_to("Inception")
        add_movie_and_rating_to("Inception", 4)
        add_movie_and_rating_to("Inception", 5)
 
        movie_ratings_list = movies_ratings[0][2]
        self.assertEqual(movie_ratings_list, [4, 5])

    def test_get_average_rating_for(self):
        add_movie_to("Interstellar")
        add_movie_and_rating_to("Interstellar", 3)
        add_movie_and_rating_to("Interstellar", 5)
 
        average = get_average_rating_for("Interstellar")
        self.assertEqual(average, 4.0)

    def test_get_all_average_ratings(self):
        add_movie_to("Inception")
        add_movie_and_rating_to("Inception", 4)
        add_movie_and_rating_to("Inception", 5)
        add_movie_to("Interstellar")
        add_movie_and_rating_to("Interstellar", 3)
 
        result = get_all_average_ratings()
        self.assertEqual(result, [("Inception", 4.5), ("Interstellar", 3.0)])
