def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    return list1 == list2
print(permutation([1, 2, 3], [3, 2, 1]))
