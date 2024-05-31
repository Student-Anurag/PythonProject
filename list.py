fruits = ["apple", "banana", "guava"]
print(fruits)
print(type(fruits))
print(len(fruits))
#checking if an item is present in the list
if "banana" in fruits:
    print("Banana is part of the list")
# checking if an item is not present in the list
if "kiwi" not in fruits:
    print("kiwi is not part of the list")
    print(fruits[1])
    print(fruits[-3])
    print(fruits[1:3])
    print(fruits[-3:-1])
    fruits.append("watermelon") #inserting at the end of the list --> appending
    fruits.insert(2,"orange")   # inserting at any arbitary position of the list
    print(fruits)
    fruits.remove("guava")
    print(fruits)
    fruits.sort()
    print(fruits)
    fruits.append("kiwi")
#list comprehension
new_fruits = [fruit for fruit in fruits if "a" in fruit]
print(new_fruits)
# copy a list
new_fruits = fruits.copy()
print(new_fruits)
# nested list
fruits.insert(2,["mango","papaya"])
print(fruits)