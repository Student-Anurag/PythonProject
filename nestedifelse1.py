num = int(input("Enter any number: "))
if (num % 5 == 0) or (num % 3 == 0):
    if (num % 15 != 0):
        print(num," is divisible by 5 or 3 but not divisble by 15")
    else:
        print(num," is divisble by 5 or 3 but also divisible by 15")