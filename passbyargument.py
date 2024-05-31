# pass by value
def addOne(x):
    x= x+1
    print("Inside function: ",x)

x = 5
addOne(x)
print("Outside function: ",x)

# Pass by reference
def modifyList(lst):
    lst.append(4)
    print("Inside function: ",lst)
lst = [1,2,3]
modifyList(lst)
print("Outside function: ",lst)