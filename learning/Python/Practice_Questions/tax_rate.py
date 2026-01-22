# program to calculate final tax rate

salary = float(input("enter salary:"))
if salary < 30000:
    finalrate = salary * (5 / 100)
    print(finalrate)
elif salary > 30000 and salary < 70000:
    finalrate = salary * (15 / 100)
    print(finalrate)
else:
    finalrate = salary * (25 / 100)
    print(finalrate)
