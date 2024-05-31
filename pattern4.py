n = int(input("Enter n: "))
for i in range (n+1):
    # print spaces
    print(" "*(n-i),end="")
    # print digits
    for j in range (1,2*i):
        print(j,end="")
    print()