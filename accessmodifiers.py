# Public modifier
class ABC:
    def __init__(self):
        self.public_attribute = None
    def public_function():
        pass
obj1 = ABC()
print(obj1.public_attribute)
print(obj1.public_function)
# Private modifier
class ABC:
    def __init__(self):
        self.private_attribute = 10
    def private_function():
        pass
obj2 = ABC()
print(obj2.private_attribute)
print(obj2.private_function)