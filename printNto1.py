def printNTo1(n):
    if n==0:
        return 
    print(n)
    printNTo1(n-1)

n = int(input("Enter n: "))
print(printNTo1(n))