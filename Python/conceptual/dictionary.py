# key.value pairs
student = {"name": "saphal kafle", "Age": 20, "Address": "kathmandu"}
print(student["name"])  # print info of name

# mutable
student["Age"] = 21
print(student["Age"])

# dictionary method
print(student.keys())  # print keys
print(student.values())  # print values
print(student.items())  # print all items
print(student.get("name"))  # find value it will print none if using get


dict_student = list(student.values())
print(dict_student)


student.update({"COllege": "cab"})
print(student)
