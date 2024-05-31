cp = float(input("Enter cost price: "))
sp = float(input("Enter sell price: "))
if cp < sp:
    print("Profit is: ", sp-cp)
if cp>sp:
    print("Loss is: ", cp-sp)
else:
    print("No profit No loss")