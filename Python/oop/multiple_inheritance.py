class teacher:
    def __init__(self, salary):
        self.salary = salary


class student:
    def __init__(self, fee):

        self.fee = fee


class TA(teacher, student):
    def __init__(self, salary, fee, name):
        super().__init__(salary)
        student.__init__(self, fee)
        self.name = name


ta1 = TA(3000, 2300, "saphal")
print(ta1.name, ta1.salary, ta1.fee)
