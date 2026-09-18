mycourse = {}

while True:
    print ("1. add course")
    print ("2. remove course")
    print ("3. replace course")
    print ("4. print course")
    print ("5. exit")

    choice = input("Enter your choice:")

    if choice == 1:
        print ("Enter course to remove:")
        add_course = input ()
    if choice == 2:


    course_name = input("Enter course name:")

    mycourse.update({"c_name" + str(id): course_name})
    i = i+1