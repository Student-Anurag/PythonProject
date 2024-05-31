# For converting characters to uppercase
str1 = "adelaide oval"
str2 = str1.upper()
print(str2)
# For coverting a string to lowercase
str3 = "EDEN PARK"
str4 = str3.lower()
print(str4)
# For capitalising the first character of a string
str5 = "johanesburg"
str6 = str5.capitalize()
print(str6)
# For stripping/removing any trailing whitespace
str7 = "   hello, world?"
print(str7.strip())
print(str7)
# replacing substring
str8 = "Hello world, what a beautiful world this is!"
print(str8.replace("world", "earth", 1))
# Splitting string
str9 = "ria,pia,dia,tia"
list = str9.split(",",2)
print(list)
# Concatenation in a string
str10 = "Kolkata "
str11 = "The city of Joy"
print(str10 + str11)
# String formatting
student_name = "Srinjay"
student_marks = 99
str = "The student name is {s}, and marks is {m}".format(s = student_name, m = student_marks)
print(str)