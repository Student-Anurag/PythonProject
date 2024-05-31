def check_palindrome(str):
    # cleaning the string
    clean_str = str.replace(" ","").lower()
    reverse_str = clean_str[::-1]
    return clean_str == reverse_str
str = input("Enter a string: ")
if check_palindrome(str):
    print("True")
else:
    print("False")