from accounts import Accounts

# class Dog:
#     def shout(self):
#         print("dogs are shouting")
#
#
# class Cat:
#     def shout(self):
#         print("cats are shouting")
#
#
# class Animal(Dog, Cat):
#     def __init__(self):
#         super().shout()
#
#     def shout(self):
#         print("Animals shouting")
#
#
# animal = Animal()
# print(animal.shout())

# from StudentImpl import StudentImpl
# from accounts import Accounts
# student = StudentImpl("Hasan", "CSE")
# print(student)
# print(StudentImpl("Tareq", 'BBA'))
# # print(StudentImpl("Abdul Karim", 'MBA'))
# student1 = StudentImpl("Feroj Ahmed", 'IT')
#
# print(student.get_stu_name())
# print(student1.get_stu_name())
#
#
acc = Accounts("Abdul Karim", 'MBA', 16, 5500)
print(acc.set_stu_name("Said Sindit"))
print(acc.set_stu_dept("BBA"))
print(acc.get_stu_name())
print(acc.get_stu_dept())
print(acc.get_credit(), " ", acc.get_total_payment())


