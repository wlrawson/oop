from os import access

class Customer:

    def create_customer (self):
        self.customer_id = input("Enter customer id: ")
        self.name = input("Enter name: ")
        self.account_no = input("Enter account number: ")
        self.balance = input("Enter balance: ")
        self.credit_card = []


    def display_customer (self):
        print ("Customer id:", self.customer_id)
        print ("Name:", self.name)
        print ("Account number:", self.account_no)
        print ("Balance:", self.balance)
        print ("Credit card:", self.credit_card)


    def transfer_funds (self):
        self.amount = input("Enter the amount to transfer:")
        #self.balance -= amount
        #self.balance += amount

    def assign_card (card_obj):
        card_obj.credit_card.append(card_obj)


class Card:
    #def __init__ (self):

    def create_card (self):
        self.card_no = input("Enter card no: ")
        self.card_type = input("Enter card type: ")
        self.cvv = input("Enter cvv: ")
        self.expiry_date = input("Enter expiry date: ")
        self.balance = input("Enter balance: ")

    def display_card (self):
        print("Card No: ", self.card_no)
        print("Card Type: ", self.card_type)
        print("CVV: ", self.cvv)
        print("Expiry Date: ", self.expiry_date)
        print("Balance: ", self.balance)

#main code


while "true":
    print("1 Create Customer")
    print("2 Create Card")
    print("3 Transfer funds")
    print("4 Assign Card")
    print("5 Display Customer info")
    print("6 Display Card info")
    print("7 exit")
    choice = int(input())

    if choice == 1:
        Customer.create_customer()
    elif choice == 2:
        Card.display_card()
    elif choice == 3:
        Customer.transfer_funds()
    elif choice == 4:
        Customer.assign_card()
    elif choice == 5:
        Customer.display_customer()
    elif choice == 6:
        Card.display_card()
    else:
        exit(True)
