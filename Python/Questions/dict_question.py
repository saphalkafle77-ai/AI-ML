operation = input("enter operation")
student = {"saphal kafle": 45}
if operation == "a":
    student.update({"sujan dhakal": 78})
    print("student added")
if operation == "b":
    student["sujan dhakal"] = 39
    print("marks updated")
if operation == "c":
    name = input("enter student name")
    print(student.get(name))
if operation == "d":
    for name, marks in student.items():
        print(name, marks)
