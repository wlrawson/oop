
while ("true"):
    print ("1 Addition")
    print ("2 Subtraction")
    print ("3 multiply")
    print ("4 Divide")
    print ("5 Exit")
    print ("Enter your choice:")
    choice = int(input())

    if choice == 5:
        break
    else:
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number:"))

    if choice == "1":
        c = a + b
        print (c)
    elif choice == "2":
        c = a - b
        print(c)
    elif choice == "3":
        c = a * b
        print(c)
    elif choice == "4":
        c = a / b
        print(c)
    elif choice == "5":
        break