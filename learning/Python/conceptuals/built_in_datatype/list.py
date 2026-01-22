Marks = [23, 43, 56, 73, 22]
# mutable
Marks[3] = 66
print(Marks)

# slicing in list
print(Marks[0 : len(Marks)])


# list method
Marks.append(81)  # add value in string
Marks.insert(5, 12)  # add value at certain index
Marks.sort()  # sort
Marks.reverse()  # sort in reverse order
print(Marks)
