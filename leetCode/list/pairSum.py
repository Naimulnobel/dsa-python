def pair_sum(myList, sum):
    obj = {}
    for i in range(len(myList)):
        obj[myList[i]] = i
    for i in range(len(myList)):
        complement = sum - myList[i]
        if complement in obj and obj[complement] != i:
            return [i, obj[complement]]
    return "No pair found"

my_list=[1,2,3,4,5,6,7,8,9,10]
target=10
print(pair_sum(my_list,target))
