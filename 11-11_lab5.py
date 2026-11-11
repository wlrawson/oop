
class Student:
        def create_new_student (self):
            self.stu_id = input("Enter students id: ")
            self.stu_name = input("Enter name: ")
            self.stu_major = input("Enter mayor: ")
            self.stu_courses = input("Enter courses: ")
            self.stu_cgpa = input("Enter student GPA: ")

        def display_student (self):
            print ("students id: ", self.stu_id)
            print ("students name: ", self.stu_name)
            print ("students major: ", self.stu_major)
            print ("students courses: ", self.stu_courses)
            print ("students GPA: ", self.stu_cgpa)


class Faculty:
    def create_new_faculty(self):
        self.fac_id = input("Enter faculty id: ")
        self.fac_name = input("Enter faculty name: ")
        self.fac_department = input("Enter department: ")
        self.fac_teaches_courses = input("Enter teaches courses: ")

    def display_faculty(self):
        print ("faculty id: ", self.fac_id)
        print ("faculty name: ", self.fac_name)
        print ("faculty department: ", self.fac_department)
        print ("faculty teaches courses: ", self.fac_teaches_courses)


students = []
faculty = []

student = Student()
faculty = Faculty()



while "true":
    print ("1 Add student ")
    print ("2 Print students")
    print ("3 Create new faculty")
    print ("4 print faculty")
    print ("5 add course")
    print ("6 Print courses")
    print ("7 exit")
    choice = int(input())

    if choice == 1:
        student.create_new_student()
    elif choice == 2:
        student.display_student()
    elif choice == 3:
        faculty.create_new_faculty()
    elif choice == 4:
        faculty.display_faculty()
    elif choice == 5:
        user.create_database
        exit(True)