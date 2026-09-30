#working. student database

class student :
    def __init__(self):
        self.id = ""
        self.department = ""

    def create_new_student (self):
        self.id = input("Enter your student ID: ")
        self.name = input("Enter student name: ")
        self.department = input("Enter student department: ")

    def display_student (self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("department:", self.department)


mystudents = []

Stu = student()

Stu.create_new_student()
Stu.display_student()

mystudents.append(Stu)

print(mystudents)