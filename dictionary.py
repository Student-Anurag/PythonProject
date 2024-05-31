phones ={
    "John" : 982624,
    "Ria" : 458902,
    "Joy" : 312200
}
# print the dictiobnary
print(phones)
# check length of the dictionary
print(len(phones))
# Access items of dictionary
print(phones["John"])
print(phones.keys())
# update value in dictionary
phones["John"] = 907752
print(phones)
# add elemets in dictionary
phones["Jia"] = 809950
print(phones)
# Remove elements in a dictionary
phones.pop("Ria")
print(phones)
# removing the last added item
phones.popitem()
print(phones)
# phones.clear()  # empty the dictionary
# print(phones)
# printing values of a dictionary
for x in phones.items():    # print both pairs
    print(x)
for x in phones:    # print just key
    print(x)
# Nested dictionary
phones = {
    "Area1" : {
        "x" : 0,
        "y" : 1,
        "z" : 2,
    },
    "Area2" : {
        "a" : 3,
        "b" : 4,
        "c" : 5
    }
}
print(phones["Area1"]["y"])
print(phones["Area2"]["c"])