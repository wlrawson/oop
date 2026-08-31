
number1 = int(input("Enter number1:"))
number2 = int(input("Enter number2:"))
operator = input("Enter the operator:")

if operator == "+":
    c = number1 + number2
elif operator == "-":
    c = number1 - number2
elif operator == "*":
    c = number1 * number2
elif operator == "/":
    if number2 == 0:
        print ("invalid number")
    else:
        c = number1 / number2

print("The result is", c)
