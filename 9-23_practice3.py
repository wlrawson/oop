mystudents={
    "Student1:{
        "name": "",
        "lab1": "",
        "lab2": "",
        "lab3": "",
        "lab4": "",
        "lab5": "",
        "total":"",
        "percent":""  = (total/50)*100
        "average":""  = (total)/5


def add_student():
    stu_name = input("Enter students name: ")
    lab1 = input("Enter lab 1 grade: ")
    mystudents.update({"student1":{"name": stu_name, "lab1":lab1}})


def delete_student():
    mystudents.pop ("student1")


def display_queue():
    print(mystudents)


while ("true"):
    print ("1 Add")
    print ("2 Remove")
    print ("3 print")
    print ("4 exit")
    choice = int(input())

    if choice == 1:
        add_student()
    elif choice == 2:
        delete_student()
    elif choice == 3:
        print(mystudents)
    elif choice == 4:
        exit(True)
