
import sqlite3

conn = sqlite3.connect("College.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Student_Master (
    stu_id TEXT PRIMARY KEY,
    stu_name TEXT,
    stu_major TEXT,
    stu_courses TEXT,
    stu_cgpa REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Faculty_Master (
    fac_id TEXT PRIMARY KEY,
    fac_name TEXT,
    fac_department TEXT,
    fac_teaches_courses TEXT
)
""")

conn.commit()

class Student:

    def create_new_student(self):
        stu_id = input("Enter student ID: ")
        stu_name = input("Enter name: ")
        stu_major = input("Enter major: ")
        stu_courses = input("Enter courses: ")
        stu_cgpa = float(input("Enter GPA: "))

        cursor.execute("""
        INSERT INTO Student_Master
        VALUES (?, ?, ?, ?, ?)
        """, (stu_id, stu_name, stu_major,
              stu_courses, stu_cgpa))

        conn.commit()
        print("Student saved to database!")

    def display_student(self):
        cursor.execute("SELECT * FROM Student_Master")
        records = cursor.fetchall()

        for record in records:
            print(record)


class Faculty:

    def create_new_faculty(self):
        fac_id = input("Enter faculty ID: ")
        fac_name = input("Enter faculty name: ")
        fac_department = input("Enter department: ")
        fac_teaches_courses = input("Enter teaches courses: ")

        cursor.execute("""
        INSERT INTO Faculty_Master
        VALUES (?, ?, ?, ?)
        """, (fac_id, fac_name, fac_department,
              fac_teaches_courses))

        conn.commit()
        print("Faculty saved to database!")

    def display_faculty(self):
        cursor.execute("SELECT * FROM Faculty_Master")
        records = cursor.fetchall()

        for record in records:
            print(record)

students = Student()
faculty = Faculty()

while True:

    print("\n1 Add student")
    print("2 Print students")
    print("3 Create new faculty")
    print("4 Print faculty")
    print("5 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        students.create_new_student()

    elif choice == 2:
        students.display_student()

    elif choice == 3:
        faculty.create_new_faculty()

    elif choice == 4:
        faculty.display_faculty()

    elif choice == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")

conn.close()
