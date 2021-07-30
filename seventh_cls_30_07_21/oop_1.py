# class object principles-> abstraction, encapsulation, inheritance, polymorphism
# obejct => class, class properties-> variable/attributes, functions

class Student:
    # attr, constructor, functions
    # global variable/instance
    # name = ""
    # dept = ""
    # uid = ""

    # constructor
    def __init__(self, name, dept, uid):
        self.name = name
        self.dept = dept
        self.uid = uid

    def __str__(self):
        return self.name + " " + self.dept + " " + self.uid


# create an object
student = Student("Tamim", "CSE", "324123")
# print(student.name, student.dept, student.uid)
print(student)
