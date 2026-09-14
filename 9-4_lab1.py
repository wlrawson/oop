while ("True"):
    print ("1. Area of a rectangle")
    print ("2. Volume of a cube")
    print ("3. Area of a circle")
    print ("4. Circumference of a circle")
    print ("5. Exit")

    choice = (input("Enter your choice:"))

    if choice == "1":
        w = int(input("Enter the width:"))
        l = int(input("Enter the length:"))
        a = l * w
        print("The area is:", a)

    elif choice == "2":
        h = int(input("Enter the height:"))
        w = int(input("Enter the width:"))
        l = int(input("Enter the length:"))
        a = h * w * l
        print("The volume is:", a)

    elif choice == "3":
        r = int(input("Enter the radius:"))
        a = r * r * 3.14
        print("the area is:", a)

    elif choice == "4":
        r = int(input("Enter the radius:"))
        a = r * 2 * 3.14
        print("the Circumference is:", a)

    if choice == "5":
        break

