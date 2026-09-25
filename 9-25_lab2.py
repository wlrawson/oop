myEmployee={
    }

def add_employee():
    employee_id = "Employee" + str(len(myEmployee) + 1)

    employee_name = input("Enter Employee name: ")
    basic_pay = int(input("Enter Basic pay: "))
    allowance = int(input("Enter Allowance: "))
    deductions = int(input("Enter Deductions: "))
    taxes = int(input("Enter Taxes: "))
    gross_pay = (basic_pay + allowance)
    net_pay = (gross_pay - deductions - taxes)

    myEmployee.update({
        employee_id: {
            "name": employee_name,
            "basic_pay": basic_pay,
            "allowance": allowance,
            "deductions": deductions,
            "taxes": taxes,
            "gross_pay": gross_pay,
            "net_pay": net_pay
        }
    })

def delete_employee():
    myEmployee.pop(input("Enter Employee to delete: "))

def modify_employee():
    myEmployee.pop(input("Enter Employee to modify: "))
    employee_id = "Employee" + str(len(myEmployee) + 1)

    employee_name = input("Enter New Employee name: ")
    basic_pay = int(input("Enter New Basic pay: "))
    allowance = int(input("Enter New Allowance: "))
    deductions = int(input("Enter New Deductions: "))
    taxes = int(input("Enter New Taxes: "))
    gross_pay = (basic_pay + allowance)
    net_pay = (gross_pay - deductions - taxes)

    myEmployee.update({
        employee_id: {
            "name": employee_name,
            "basic_pay": basic_pay,
            "allowance": allowance,
            "deductions": deductions,
            "taxes": taxes,
            "gross_pay": gross_pay,
            "net_pay": net_pay
        }
    })

def display_myemployee():
    for employee_id, employee in myEmployee.items():
        print(employee_id, employee)

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
        display_myemployee()
    else:
        exit(True)