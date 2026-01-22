class student:
    def __init__(self, name, marks):  # storing current instance of class
        self.name = name
        self.marks = marks


stu1 = student("saphal", 45)
stu2 = student("neha", 78)
stu3 = student("rahul", 74)
stu4 = student("jeremy", 20)

print(stu1.name, stu1.marks)
print(stu2.marks)
