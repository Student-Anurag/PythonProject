'''n = int(input("Enter n : "))
sum = 0
for i in range(1,n+1):
    sum += i
print("Sum of all numbers till n = ", sum)'''
# declaring function

def addAllNumbers(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
output = addAllNumbers(1,2,3,4,5,6,7,8)
print("Sum= ",output)