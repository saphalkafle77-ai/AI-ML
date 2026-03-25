class organization:
    start_time = "10am"
    end_time = "5pm"


class school(organization):
    def __init__(self, subject):
        self.subject = subject


class tution(school):
    def __init__(self, teacher_name, subject):
        super().__init__(subject)  # used to invoke one class for inheritance
        self.teacher_name = teacher_name


tut1 = tution("ram", "math")
print(tut1.end_time, tut1.start_time, tut1.teacher_name, tut1.subject)
