info = [
    ("alice", "math"),
    ("bob", "science"),
    ("alice", "science"),
    ("Charlie", "math"),
    ("bob", "math"),
    ("alice", "english"),
    ("Charlie", "english"),
]
# list all unique course
# unique_course = set()
# for tup in info:
#     unique_course.add(tup[1])
# print(unique_course)

# list students enrolled in english
# for name, course in info:
#     if course == "english":
#         print(name)

# create dictionary(student,set of courses)
dict = {}
for name, course in info:
    if dict.get(name) == None:
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)
