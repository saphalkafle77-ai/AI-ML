tup = (1, 2, 3, 4, 5, 6, 7, 8)
even = []
odd = []
for i in tup:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("even numbers", even)
print("odd numbers", odd)
