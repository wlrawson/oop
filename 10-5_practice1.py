works. but still needs more functions 


class student :
    def __init__(self):
        self.id = ""

    def create_new_student (self):
        self.id = input("Enter your student ID: ")
        self.name = input("Enter student name: ")
        self.advisor = input("Enter student advisor: ")

    def display_student (self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("advisor:", self.advisor)

class faculty :
    def __init__(self):
        self.id = ""
        self.name = ""
        self.enrolled_students = ""

    def create_new_faculty (self):
        self.id = input("Enter your faculty ID: ")
        self.name = input("Enter faculty name: ")
        self.enrolled_students = input("enter enrolled students: ")

    def display_faculty (self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Enrolled students:", self.enrolled_students)


class cources :
    def __init__(self):
        self.id = ""
        self.class_name = ""
        self.teaching_faculty = ""
        self.enrolled_students = ""

mystudents = []
myfaculty = []
mycources = []

stu = student()
fac = faculty()
cla = cources()


while "true":
    print ("1 Add student ")
    print ("2 Print students")
    print ("3 Create New Faculty")
    print ("4 print Employee's")
    print ("5 exit")
    choice = int(input())

    if choice == 1:
        stu.create_new_student()
        #faculty_id = (input("Enter faculty ID: ")
        #for x in myfacultylist:
            #if x.id == faculty_id:
                #stu.assign_advisor(x))
    elif choice == 2:
        stu.display_student()
    elif choice == 3:
        fac.create_new_faculty()
    elif choice == 4:
        fac.display_faculty()
    else:
        exit(True)


Stu.create_new_student()
Stu.display_student()

mystudents.append(Stu)

print(mystudents)