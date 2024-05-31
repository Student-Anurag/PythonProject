eng_marks = int(input("Enter marks in English: "))
math_marks = int(input("Enter marks in Math: "))
# if both are more than 80, print 'A' grade
if eng_marks > 80 and math_marks > 80:
    print("Grade -> A")
# if either of marks are more than 80, print 'B' garde
elif eng_marks > 80 or math_marks > 80:
    print("Grade -> B")
# if neither of marks are more than 80, print 'C' grade
else:
    print("Grade -> C")