import unittest
from studentGradeLevel.student import *

class MyTestCase(unittest.TestCase):
    def test_student_name_and_gradelevel_display(self):
        student1 = StudentClass("Abdulkadir")
        self.assertEqual("Abdulkadir, your grade level is 1", student1.introduce())
    def test_student_got_promoted(self):
        student1 = StudentClass("Abdulkadir")
        student1.promote()
        self.assertEqual("Abdulkadir, your grade level is 2", student1.introduce())
    def test_student_got_promoted_twice(self):
        student1 = StudentClass("Abdulkadir")
        student1.promote()
        student1.promote()
        self.assertEqual("Abdulkadir, your grade level is 3", student1.introduce())
    def test_student_passed(self):
        student1 = StudentClass("Abdulkadir")
        self.assertTrue(student1.has_passed(60))
        self.assertEqual("Abdulkadir, your grade level is 1", student1.introduce())
    def test_student_passed_got_promoted(self):
        student1 = StudentClass("Abdulkadir")
        self.assertTrue(student1.has_passed(60))
        student1.promote()
        self.assertEqual("Abdulkadir, your grade level is 2", student1.introduce())
    def test_student_inputed_wrong_score(self):
        student1 = StudentClass("Abdulkadir")
        self.assertRaises(ValueError,student1.has_passed, -7)
    def test_student_updated_name(self):
        student1 = StudentClass("Abdulkadir")
        student1.update_name("Opeyemi")
        self.assertEqual("Opeyemi, your grade level is 1", student1.introduce())

    def test_student_got_promoted_is_graduating(self):
        student1 = StudentClass("Abdulkadir")
        self.assertFalse(student1.is_graduating())
        student1.promote()
        student1.promote()
        student1.promote()
        student1.promote()
        student1.promote()
        student1.promote()
        student1.promote()
        student1.promote()
        student1.promote()
        student1.promote()
        student1.promote()
        student1.promote()
        self.assertTrue(student1.is_graduating())
if __name__ == '__main__':
    unittest.main()
