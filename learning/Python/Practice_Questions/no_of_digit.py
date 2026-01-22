def digit(n):
    count = len(str(n))
    for i in range(count):
        print(n % 10)
        n = n // 10


digit(273)
