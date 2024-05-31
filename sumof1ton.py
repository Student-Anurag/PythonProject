def sum1ToN(n):
    if n==0:
        return 0
    return n + sum1ToN(n-1)
n= int(input("Enter n: "))
print(sum1ToN(n))