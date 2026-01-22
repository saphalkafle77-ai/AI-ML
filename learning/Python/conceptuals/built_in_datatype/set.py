# used to find unique value
s = {1, 2, 2, 3, 5}
print(len(s))

# to create empty set
empty_set = set()
print(empty_set)


# set method
s.add(6)  # add
print(s)

s.remove(2)  # remove
print(s)

s.pop()  # remove random value
print(s)

s.clear()  # empty the set
print(s)


a = {2, 3, 5}
b = {3, 5, 6}
print(a.union(b))
print(a.intersection(b))
