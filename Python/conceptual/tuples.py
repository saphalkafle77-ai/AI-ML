name = ("saphal",)  # to create a single value tuple
print(type(name))

# sum of values of tuples
tup = (23, 45, 67, 113)
sum = 0
for i in tup:
    sum += i
print(f"sum of tup is {sum}")

# tuple method
print(tup.index(45))
print(tup.count(45))
