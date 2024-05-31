def factorial(n):
    # base case
    if n==0:
        return 1
    return n * factorial(n-1)

n = int(input("Enter n: "))
print(factorial(n))