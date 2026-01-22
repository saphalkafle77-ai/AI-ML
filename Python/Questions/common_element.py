list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]
empty_set1 = set(list1)
empty_set2 = set(list2)
# print(empty_set1.intersection(empty_set2))
if empty_set1.intersection(empty_set2):
    print("share common element")
else:
    print("share no common element")
