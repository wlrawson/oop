class Car :

    def create_new_book (self):
        self.car_id = input("Enter the car's ID: ")
        self.car_make = input("Enter the car's make: ")
        self.car_model = input("Enter enter the car's model: ")
        self.year = input("Enter the car's year: ")
        self.color = input("Enter the car's color: ")

    def display_book (self):
        print("Car's ID:", self.car_id)
        print("Car's make:", self.car_make)
        print("Car's model:", self.car_model)
        print("Car's year:", self.year)
        print("Car's color:", self.color)

class Modifications :

    def create_new_mod (self):
        self.modification_id = input("Enter the modification's ID: ")
        self.modification = input("Enter author's name: ")
        self.affiliation = input("Enter author's affiliation: ")
        self.country = input("Enter author's country: ")

    def display_author (self):
        print("Author's ID:", self.author_id)
        print("Author's Name:", self.auhtor_name)
        print("Author's affiliation:", self.affiliation)
        print("Author's country:", self.country)


class User :

    def assign_new_user(self):
        self.user_id = input("Enter user's ID: ")
        self.user_name = input("Enter User's name: ")
        self.user_password = input("Enter user's password: ")
        self.user_adress = input("Enter user's address: ")
        self.user_phone = input("Enter user's phone number: ")
        self.user_email_id = input("Enter user's email address: ")
        self.user_books_borrowed = input("Enter books borrowed: ")

    def display_user(self):
        print ("User's ID: ",self.user_id)
        print ("User's name: ", self.user_name)
        print ("Enter user's password: ", self.user_password)
        print ("Enter user's address: ", self.user_adress)
        print ("Enter user's phone number: ", self.user_phone)
        print ("Enter user's email address: ", self.user_email_id)
        print ("Enter books borrowed: ", self.user_books_borrowed)


mybooks = []
myauthors = []
myusers = []

book = Book()
auth = Author()
user = User()

while "true":
    print ("1 Add student ")
    print ("2 Print students")
    print ("3 Create new faculty")
    print ("4 print faculty")
    print ("5 add course")
    print ("6 Print courses")
    print ("7 exit")
    choice = int(input())

    if choice == 1:
        book.create_new_book()
    elif choice == 2:
        book.display_book()
    elif choice == 3:
        auth.create_new_author()
    elif choice == 4:
        auth.display_author()
    elif choice == 5:
        user.assign_new_user()
    elif choice == 6:
        user.display_user()
    else:
        exit(True)