import unittest
from university_functions import Functions

class MyTestCase(unittest.TestCase):
    def testThatAStudentRecord_canBeDisplayed(self):
        log = Functions()
        student1_record = {
                "name": "Paul",
                "age": 22,
                "courses": {"Math", "Physics", "History", "Law", "Medicine", "Business"},
                "address": {"city": "Ilorin", "zip code": "002420"}
            }

        log.add_student("user001", student1_record)
        self.assertEqual(log.display_student_record("user001"), student1_record)

    def testThat_aSpecific_studentRecord_Display_amongStudentsRecord(self):
        log = Functions()
        student1_record = {
                "name": "Paul",
                "age": 22,
                "courses": {"Math", "Economics", "History", "Law", "Medicine", "Business"},
                "address": {"city": "Ilorin", "zip code": "002420"}
            }
        log.add_student("user001", student1_record)
        student2_record = {
            "name": "Abdulkadir",
            "age": 21,
            "courses": {"Philosophy", "Physics", "History", "Engineering", "Medicine", "Business"},
            "address": {"city": "Lagos", "zip code": "09212"}
        }
        log.add_student("user002", student2_record)
        self.assertEqual(log.display_student_record("user002"), student2_record)
    def testThat_DisplayCourses_AStudentIsOffering(self):
        log = Functions()
        student1_record = {
            "name": "Abdulkadir",
            "age": 22,
            "courses": {"Math", "Economics", "Engineering", "Law", "Medicine", "Business"},
            "address": {"city": "Abuja", "zip code": "09172"}
        }
        log.add_student("user001", student1_record)
        expected_courses = {"Math", "Economics", "Engineering", "Law", "Medicine", "Business"}
        self.assertEqual(log.display_courses("user001"), expected_courses)
    def testThatUserNameWasIncorrect_soNothingWasDisplayed(self):
        log = Functions()
        student1_record = {
            "name": "Abdulkadir",
            "age": 22,
            "courses": {"Math", "Economics", "Engineering", "Law", "Medicine", "Business"},
            "address": {"city": "Abuja", "zip code": "09172"}
        }
        log.add_student("user001", student1_record)
        self.assertEqual(log.display_student_record("user0012"), {})
    def testTo_DisplayAStudentZipCode(self):
        log = Functions()
        student1_record = {
            "name": "Abdulkadir",
            "age": 22,
            "courses": {"Math", "Economics", "Engineering", "Law", "Medicine", "Business"},
            "address": {"city": "Abuja", "zip code": "09172"}
        }
        log.add_student("user001", student1_record)
        expected_zip_code = "09172"
        self.assertEqual(log.get_zip_for("user001"), expected_zip_code)
    def testTo_DisplayAStudentCity(self):
        log = Functions()
        student1_record = {
            "name": "Abdulkadir",
            "age": 22,
            "courses": {"Math", "Economics", "Engineering", "Law", "Medicine", "Business"},
            "address": {"city": "Abuja", "zip code": "09172"}
        }
        log.add_student("user001", student1_record)
        expected_city = "Abuja"
        self.assertEqual(log.display_student_city("user001"), expected_city)
    def testThat_A_Student_can_add_newCourse(self):
        log = Functions()
        student1_record = {
            "name": "Abdulkadir",
            "age": 22,
            "courses": {"Math", "Economics", "Engineering", "Law", "Medicine", "Business"},
            "address": {"city": "Abuja", "zip code": "09172"}
        }
        log.add_student("user001", student1_record)
        expected_courses = {"Math", "Economics", "Engineering", "Law", "Medicine", "Business", "Art"}
        log.add_new_course("user001", "Art")
        self.assertEqual(log.display_courses("user001"), expected_courses)
    def testThat_A_Student_add_an_existing_course_it_replaces_the_previous_one(self):
        log = Functions()
        student1_record = {
            "name": "Abdulkadir",
            "age": 22,
            "courses": {"Math", "Economics", "Engineering", "Law", "Medicine", "Business"},
            "address": {"city": "Abuja", "zip code": "09172"}
        }
        log.add_student("user001", student1_record)
        expected_courses = {"Math", "Economics", "Engineering", "Law", "Medicine", "Business"}
        log.add_new_course("user001", "Engineering")
        self.assertEqual(log.display_courses("user001"), expected_courses)
    def testThat_A_Student_add_an_Unofficial_course_it_doesnt_add(self):
        log = Functions()
        student1_record = {
            "name": "Abdulkadir",
            "age": 22,
            "courses": {"Math", "Economics", "Engineering", "Law", "Medicine", "Business"},
            "address": {"city": "Abuja", "zip code": "09172"}
        }
        log.add_student("user001", student1_record)
        expected_courses = {"Math", "Economics", "Engineering", "Law", "Medicine", "Business"}
        log.add_new_course("user001", "Finance")
        self.assertEqual(log.display_courses("user001"), expected_courses)

    def test_that_A_Student_can_remove_a_course(self):
        log = Functions()
        student1_record = {
            "name": "Abdulkadir",
            "age": 22,
            "courses": {"Math", "Economics", "Engineering", "Law", "Medicine", "Business"},
            "address": {"city": "Abuja", "zip code": "09172"}
        }
        log.add_student("user001", student1_record)
        log.pop_course("user001", "Engineering")
        expected_courses = {"Math", "Economics", "Law", "Medicine", "Business"}
        self.assertEqual(log.display_courses("user001"), expected_courses)
    def test_that_student_can_update_his_details(self):
        log = Functions()
        student1_record = {
            "name": "Abdulkadir",
            "age": 22,
            "courses": {"Math", "Economics", "Engineering", "Law", "Medicine", "Business"},
            "address": {"city": "Abuja", "zip code": "09172"}
        }
        log.add_student("user001", student1_record)
        log.update_details("user001", 21, name = "Opeyemi", city = "Lagos", zip_code = "087212")
        student1_updated_record = {
            "name": "Opeyemi",
            "age": 21,
            "courses": {"Math", "Economics", "Engineering", "Law", "Medicine", "Business"},
            "address": {"city": "Lagos", "zip code": "087212"}
        }
        self.assertEqual(log.display_student_record("user001"), student1_updated_record)
    def test_to_get_overall_number_of_students(self):
        log = Functions()
        student1_record = {
            "name": "Abdulkadir",
            "age": 21,
            "courses": {"Biology", "Philosophy", "English", "Law", "Medicine", "Business"},
            "address": {"city": "Abuja", "zip code": "09172"}
        }
        student2_record = {
            "name": "Opeyemi",
            "age": 20,
            "courses": {"Math", "Economics", "Engineering", "Law", "Medicine", "Business"},
            "address": {"city": "Lagos", "zip code": "02492"}
        }
        student3_record = {
            "name": "Zakariyah",
            "age": 22,
            "courses": {"Art", "Geography", "Music", "Sociology", "Medicine", "Business"},
            "address": {"city": "Kwara", "zip code": "03251"}
        }
        log.add_student("user001", student1_record)
        log.add_student("user002", student2_record)
        log.add_student("user003", student3_record)
        self.assertEqual(log.get_number_of_student(), 3)
if __name__ == '__main__':
    unittest.main()
