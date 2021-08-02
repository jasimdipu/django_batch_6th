from student import Student


class StudentImpl(Student):

    # encapsulation => __private, _protected, public

    def __init__(self, name, dept):
        self.__name = name
        self.__dept = dept

    def get_stu_name(self):
        return self.__name

    def set_stu_name(self, name):
        self.__name = name

    def get_stu_dept(self):
        return self.__dept

    def set_stu_dept(self, dept):
        self.__dept = dept

    def __str__(self):
        return self.__name + " " + self.__dept
