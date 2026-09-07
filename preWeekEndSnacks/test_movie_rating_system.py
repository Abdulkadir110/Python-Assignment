from unittest import TestCase
from movie_rating_system import *

class MovieRatingTest(TestCase) :
      
    def test_a_that_movie_name_and_a_rating_was_added_to_movies_list(self) :
        movie_name = "Game of thrones"
        movie_rating = 4
        add_movie_to(movie_name)
        expected_updated_movie_list = [["Game of thrones", [4]]     ]
        actual_updated_movie_list = add_movie_and_rating_to(movie_name, movie_rating)
        
        self.assertListEqual(actual_updated_movie_list, expected_updated_movie_list)
        
    def test_b_that_movie_name_and_rating_was_added_to_movies_list(self) :
        movie_name = "Game of thrones"
        movie_rating = 5
        add_movie_to(movie_name)
        expected_updated_movie_list = [["Game of thrones", [4, 5]]]
        actual_updated_movie_list = add_movie_and_rating_to(movie_name, movie_rating)
                
        self.assertListEqual(actual_updated_movie_list, expected_updated_movie_list)
    
    def test_c_that_movie_name_and_3_rating_was_added_to_movies_list(self) :
        movie_name = "Game of thrones"
        movie_rating = 1
        add_movie_to(movie_name)
        expected_updated_movie_list = [["Game of thrones", [4, 5, 1]]]
        actual_updated_movie_list = add_movie_and_rating_to(movie_name, movie_rating)
                
        self.assertListEqual(actual_updated_movie_list, expected_updated_movie_list)

    def test_e_average_rating_for_single_rating(self):
        add_movie_and_rating_to("Inception", 4)
        actual_average = get_average_rating_for("Inception")
        self.assertEqual(actual_average, 4.0)
        
    def test_d_average_rating_for_multiple_ratings(self):
        average = get_average_rating_for("Game of Thrones")
        
        self.assertAlmostEqual(average, 3.33, places=2)
