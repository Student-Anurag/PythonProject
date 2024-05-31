n = int(input("Enter n: "))
for i in range(n):          # loop for rows
    for j in range(1,n+1):  # loop for columns
        print(j, end="")
    print()