# creating a set
names = {"Mia","Stefan","Damon"}
# print set
print(names)
print(type(names))
# accesing items of set
for x in names:
    print(x)
# check if item exists in set
if "Damon" in names:
    print("Damon is in the set")
names.add("Alaric")
print(names)
names_list = ["Matt","Bruno"]
names.update(names_list)
print(names)
# joining 2 sets
s1 = {'a', 'b', 'c'}
s2 = {'d', 'e', 'f'}
print(s1, s2)
s3 = s1.union(s2)
print(s3)
# keep only duplicates while joining
s1.intersection_update(s2)
print(s1)
# keep all values except intersection
s1.symmetric_difference_update(s2)
print(s1)