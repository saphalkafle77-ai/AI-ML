# static method(used when not using instance and class attribute)
# logic related to class
class Student:
    college_name = "cab"

    def __init__(self, name, batch):
        self.name = name
        self.batch = batch

    @classmethod
    def get_college_name(cls):
        print(f"college name is {cls.college_name}")

    def get_stud_info(self):
        print(f"student name is {self.name} and batch is {self.batch}")

    @staticmethod
    def total_price(fee, discount):
        price = (fee - discount) / 100
        print(f"final price is {price}")


s1 = Student("saphal", 13)
Student.get_college_name()
s1.get_stud_info()
s1.total_price(23000, 15)
