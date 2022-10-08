from finalproject.final_project import Course
from finalproject.final_project import Student

courses_list = []
students_list = []

def get_courses_list(courses):
    print("ID\t\t|Name\t\t|Class")
    for course in courses:
        course.get_course_details()

def get_students_details(students):
    print("ID\t\t|Name\t\t|Class")
    for student in students:
        print(student.get_student_details())


def find_course(course_id,courses):
    index = 0
    for course in courses:
        if course.course_id == course_id:
            return index
        index += 1
    return -1

def find_student(student_number,students):
    index = 0
    for student in students:
        if student.student_number == student_number :
            return index
        index += 1
    return -1


while True:
    x = int(input("Select Choice Please\n"
                  "1.Add New Student\n"
                  "2.Remove Student\n"
                  "3.Edit Student\n"
                  "4.Display All Students\n"
                  "5.Create New Course\n"
                  "6.Add Course to student\n"
                  "0.Exit: "))

    if x ==0:
        exit()
    elif x == 1:
        student_name = input("Enter Student Name: ")
        while True:
            student_class = input("Enter Student Class (A-B-C): ")
            if student_class in ["A","B","C"]:
                break
        student_number = len(students_list) + 1
        student = Student(student_number,student_name,student_class)
        students_list.append(student)
        print("Student Save Successfully")
    elif x == 2:
        get_students_details(students_list)
        student_number = int(input("Enter Student Number: "))
        search = find_student(student_number,students_list)
        if search == -1:
            print("Student not exist")
        else:
            students_list.pop(search)
            print("Delete Done Successful")
            get_students_details(students_list)
    elif x == 3:
        get_students_details(students_list)
        student_number = int(input("Enter Student Number: "))
        search = find_student(student_number, students_list)
        if search == -1:
            print("Student not exist")
        else:
            student_name = input("Enter Student Name: ")
            while True:
                student_class = input("Enter Student Class (A-B-C): ")
                if student_class in ["A", "B", "C"]:
                    break
            students_list[search].student_name = student_name
            students_list[search].student_class = student_class

            print("Edit Done")
    elif x == 4:
        get_students_details(students_list)

    elif x == 5:
        course_name = input("Enter Course Name: ")
        while True:
            course_class = input("Select Course Class (A,B,C): ")
            if course_class in ["A","B","C"]:
                break
        course_id = len(courses_list) + 1
        course = Course(course_id,course_name,course_class)
        courses_list.append(course)
        print("Course Created Successfully")

    elif x == 6:
        get_courses_list(courses_list)
        student_number = int(input("Enter Student Number: "))
        search = find_student(student_number,students_list)
        if search == -1:
            print("Student Not Exist")
        else:
            course_id = int(input("Enter Course ID: "))
            course_index = find_course(course_id,courses_list)
            if course_index == -1:
                print("Course Not Exist")
            else:
                students_list[search].enroll_course(courses_list[course_index])
    else:
        exit()




