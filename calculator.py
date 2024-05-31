num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
operator = input("Enter operator: ")
match operator:
    case "+":
        print("Sum is= ",num1+num2)
    case "-":
        print("Difference is= ",num1-num2)
    case "*":
        print("Product is= ",num1*num2)
    case "/":
        print("Quotient is= ",num1//num2)
    case _ :
        print("Enter valid operator!!!")