name1 = "Virat Kohli"
name2 = 'Glenn Maxwell'
# indexing in a string
print(name1[0])
# Traversing in a string
for i in name1:
    print(i)
# Using list comprehension
    list = [char for char in name1]
    for i in list:
        print(i)
# Find length of a string
print(len(name2))
# Find a character/substring in a string
print(name1.find('K'))
# slicing in string
# V I R A T  K O H L I
# 0 1 2 3 4 5 6 7 8 9 10
print(name1[6:])
print(name1[0:5])
