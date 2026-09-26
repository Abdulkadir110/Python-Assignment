from university_main import student_dict


class Functions:
    def __init__(self):
        self.students_dict = {}
        self.courses_list = ["Math", "Physics", "Computer Science", "Biology", "Chemistry",
"Statistics", "English", "Economics", "History", "Philosophy",
"Sociology", "Political Science", "Geography", "Psychology", "Art",
"Music", "Engineering", "Law", "Medicine", "Business"]

    def add_student(self,user_id, student_record):
        self.students_dict[user_id] = student_record

    def display_student_record(self, user_id) -> dict:
        for key in self.students_dict.keys():
            if key == user_id:
                return self.students_dict[key]
        return {}

    def display_courses(self, user_id) ->dict:
        student_dict = self.display_student_record(user_id)
        for key in student_dict.keys():
            if key == "courses":
                return student_dict[key]
        return {}
    def get_zip_for(self, user_id) -> str:
        student_dict = self.display_student_record(user_id)
        for key in student_dict.keys():
            if key == "address":
                for item in student_dict[key]:
                    if item == "zip code":
                        return student_dict[key][item]
        return ""

    def display_student_city(self, user_id) -> str:
        student_dict = self.display_student_record(user_id)
        for key in student_dict.keys():
            if key == "address":
                for item in student_dict[key]:
                    if item == "city":
                        return student_dict[key][item]
        return ""

    def add_new_course(self, user_id : str, new_course: str):
        student_dict = self.display_student_record(user_id)
        if new_course in self.courses_list:
            for key in student_dict.keys():
                if key == "courses":
                    student_dict[key].add(new_course)

    def pop_course(self, user_id: str, course :str ):
        student_dict = self.display_student_record(user_id)
        for key in student_dict.keys():
            if key == "courses":
                for item in student_dict[key]:
                    if item == course:
                        student_dict[key].remove(course)
                        break

    def update_details(self, user_id : str, age : int, city : str, name : str, zip_code : str):
        student_dict = self.display_student_record(user_id)
        student_dict["name"] = name
        student_dict["age"] = age
        student_dict["address"]["city"] = city
        student_dict["address"]["zip code"] = zip_code

    def get_number_of_student(self) -> int:
        count = 0
        for dictionary in self.students_dict:
            count +=1
        return count
