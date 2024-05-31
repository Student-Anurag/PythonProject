def pow(a,b):
    if b==0:
        return 1
    return a*pow(a,b-1)
a = int(input("Enter base: "))
b = int(input("Enter power: "))
print(pow(a,b))