students = {}
while True:

    print ("1 = Add a student")
    print ("2 = Remove student")
    print ("3 = Print")
    print ("4 = Exit")
    print ("Enter your choice:")
    choice = int(input())

    if choice == 1:
        name = input("Enter your name:")
        major = input("Enter your major:")
        year = input("Enter your year:")

        students.update({"s"+str(i):
        {
        "stu_name": name,
        "stu_major": major,
        "stu_year": year,
        }
        }
        )
        i =i+1



if choice == 2:
    print ("Enter a student to add:")
    new_student = int(input())
    if new_student in list01:
        print ("Element is in the list")
    else:
        list01.append(new_student)

if choice == 3:
    print ("Enter new number:")
    new_number = int(input())

    print ("enter number to remove:")
    remove_number = int(input())

    list01.append(new_number)
    list01.remove(remove_number)

    if new_number in list01:
        print ("Element is in the list")
    else:
        list01.append(new_element)

    if remove_number in list01:
        list01.remove(remove_number)
    else:
        print ("Element is not in the list")

if choice == 4:
    list01.sort()

if choice == 5:
    print ("The list is")
    print(list01)

if choice == 6:
    exit




