marks = int(input("Enter marks: "))
if marks > 80 and marks <= 100:
    print("Very Good")
elif marks > 60 and marks <= 80:
    print("Good")
elif marks > 40 and marks <= 60:
    print("Average")
elif marks <= 40:
    print("Fail")