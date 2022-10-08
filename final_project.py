import random

class Course:

    def __init__(self,course_id,course_name,course_claas):
        self.course_id = course_id
        self.course_name = course_name
        self.course_class = course_claas

    def get_course_details(self):
        print(str(self.course_id) + "\t\t|" + self.course_name + "\t\t|" + self.course_class)

class Student:

    def __init__(self,student_number,student_name,student_class):
        self.student_number = student_number
        self.student_name = student_name
        self.student_class = student_class
        self.courses_list = []

    def enroll_course(self,course):
        if self.student_class == course.course_class:
            for i in self.courses_list:
                if course.course_id == i.course_id:
                    print("Course Already Enrolled")
                    return
            self.courses_list.append(course)
            print("Course Enrolled Successfully")
        else:
            print("Invalid Course Class")

    def get_student_details(self):
        print(str(self.student_number) + "\t\t|" + self.student_name + "\t\t|" + self.student_class)
        if len(self.courses_list) == 0:
            print("Courses List Empty")
            return
        print("Courses List >>>>")
        for course in self.courses_list:
            course.get_course_details()



