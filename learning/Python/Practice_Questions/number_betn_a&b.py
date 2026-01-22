def number(a, b):
    count = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)
        i += 1
        # print(i)


number(1, 16)
