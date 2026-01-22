# find index of 64
marks = [23, 45, 64, 32, 36]
x = 64
idx = 0
for i in marks:
    if i == x:
        print(idx)
        break
    idx += 1
