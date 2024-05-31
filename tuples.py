# CREATING A TUPLE
colours = ("red", "yellow", "green")
# CREATING A TUPLE WITH 1 ITEM
fruit = ("apple",)
# CHECK TYPE OF TUPLE
print(type(fruit))
# CHECK LENGTH OF TUPLE
print(len(colours))
# ACCESING ITEMS IN TUPLE
print(colours[0])
# CONCATENATING 2 TUPLES
more_colours = ("blue", "brown")
colours = colours + more_colours
print(colours)
# UNPACKING A TUPLE
colour1, colour2, colour3 = colours
print(colour1, colour2, colour3)