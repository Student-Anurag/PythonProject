def outer_function():
    x = 1   # Variable in the outer function
    def inner_function():
        y = 2   # Variable in inner function
        res = x+y
        return res
    return inner_function()
output = outer_function()
print(output)