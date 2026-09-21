#This works perfect

myQueue = []


def enqueue():
    myQueue.append(input("Enter a name: "))


def dequeue():
    myQueue.pop(0)


def display_queue():
    print(myQueue)


while ("true"):
    print ("1 Add")
    print ("2 Remove")
    print ("3 print")
    print ("4 exit")
    choice = int(input())

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        print(myQueue)
    elif choice == 4:
        exit(True)
