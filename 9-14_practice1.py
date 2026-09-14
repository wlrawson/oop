
while ("true"):
    print ("1 = Addition")
    print ("2 Subtraction")
    print ("3 multiply")
    print ("4 Divide")
    print ("5 Exit")
    print ("Enter your choice:")
    choice = int(input())

list01 = [40, 30, 50, 10]

print ("Enter number to remove:")
new_remove = int(input())
if new_remove in list01:
    list01.remove(new_remove)
else:
    print ("Element is not in the list")

print ("Enter a number to add:")

new_element = int(input())
if new_element in list01:
    print ("Element is in the list")
else:
    list01.append(new_element)

print ("Enter new number:")
new_number = int(input())

print ("enter number to remove:")
remove_number = int(input())

list01.append(new_number)
list01.remove(remove_number)

if new_number in list01:
    print ("Element is in the list")
else:
    list01.append(new_element)

list01.sort()

print ("The list is")
print(list01)

exit


