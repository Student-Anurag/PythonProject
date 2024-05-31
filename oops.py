class Student:
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
student1 = Student()
student1.set_name("Shimran")
print(student1.name)