myEmployee={
    "Employee1":{
        "Name": "",
        "Basic_pay": "",
        "Allowance": "",
        "Deductions": "",
        "Taxes": "",
        "Gross_pay": "",
        "Net_pay":"",}}



def add_employee():
    employee_name = input("Enter Employee name: ")
    basic_pay = input("Enter Basic pay: ")
    allowance = input("Enter Allowance: ")
    deductions = input("Enter Deductions: ")
    taxes = input("Enter Taxes: ")
    gross_pay = input("Enter Gross_pay: ")
    net_pay = input("Enter Net pay: ")
    myEmployee.update({"Employee1":{"name": employee_name, "basic_pay":basic_pay, "allowance":allowance, "deductions":deductions, "taxes":taxes, "gross_pay":gross_pay, "net_pay":net_pay}})

def delete_employee():
    myEmployee.pop("Employee1")

def modify_employee():
    remove_employee = input("Enter employee to remove: ")
    if remove_employee in dict:
        myEmployee.pop("Employee1")
        add_employee()
    else:
        print("Employee not found")

def display_myemployee():
    print(myEmployee)


while "true":
    print ("1 Add Employee")
    print ("2 Remove Employee")
    print ("3 modify Employee")
    print ("4 print Employee's")
    print ("5 exit")
    choice = int(input())

    if choice == 1:
        add_employee()
    elif choice == 2:
        delete_employee()
    elif choice == 3:
        modify_employee()
    elif choice == 4:
        print(myEmployee)
    else:
        exit(True)
