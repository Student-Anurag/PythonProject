# Writing a function for calculating sum from 1 to n
def SumOfN(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
n = int(input("Enter n: "))
# calling function
print("Sum of all numbers till n= ",SumOfN(n))