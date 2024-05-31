def printNTo1(n):
    if n==0:
        return 
    printNTo1(n-1)
    print(n)

n = int(input("Enter n: "))
print(printNTo1(n))