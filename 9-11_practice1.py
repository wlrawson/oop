mylist_01 = [2, 56,43,18,29289, 9]

mylist_01.append(66)   # adding items
print(mylist_01)

mylist_01.remove(56)    # removing items
print (mylist_01)

mylist_01.sort()   # sorts the list
print (mylist_01)

mylist_01.pop()   # removes the last item

# newlist = mylist_02 ()
# newlist.append ("100")

newvalue = int(input())
if newvalue in mylist:
    print ("Element is in the list")
else:
    print ("Element is not in the list")
