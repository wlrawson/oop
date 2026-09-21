
while ("true"):
    print ("1 Addition")
    print ("2 Subtraction")
    print ("3 multiply")
    print ("4 Divide")
    print ("Enter your choice:")
    choice = int(input())

    def add():
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number:"))
        c = a + b
        print(c)


    def subtract():
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number:"))
        c = a - b
        print(c)

    def multiply():
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number:"))
        c = a * b
        print(c)

    def divide():
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number:"))
        c = a / b
        print(c)

    if choice == "1":
        add ()
    elif choice == "2":
        subtract ()
    elif choice == "3":
        multiply ()
    elif choice == "4":
        divide()

    exit(True)