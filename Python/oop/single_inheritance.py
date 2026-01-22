class employee:
    start_time = "10 am"
    end_time = "6pm"

    def change_time(self, new_endtime):
        self.end_time = new_endtime


class teacher(employee):
    def __init__(self, subject):
        self.subject = subject


t1 = teacher("math")
t1.change_time("8pm")
print(t1.end_time)
