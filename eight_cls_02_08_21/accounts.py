from StudentImpl import StudentImpl


class Accounts(StudentImpl):

    def __init__(self, name, dept, credit, payment):
        super(Accounts, self).__init__(name=name, dept=dept)
        self.__credit = credit
        self.__payment = payment

    def get_credit(self):
        return self.__credit

    def get_total_payment(self):
        amount = self.__credit*self.__payment

        return amount
