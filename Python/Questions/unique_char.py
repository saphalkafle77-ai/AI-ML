string = input("enter the string:")
set1 = set(string)
character = []
count = []

for i in set1:
    character.append(i)
    count.append(string.count(i))
print("characters:", character)
print("count:", count)
