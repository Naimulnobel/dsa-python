def pair_sum(myList, sum):
    result = []
    b=set()
    for i in myList:
        complement=sum-i
        if complement in b:
            pair=f'{complement}+{i}'
            result.append(pair)
        b.add(i)
    return result

my_list=[1,2,3,4,5,6,7,8,9,10]
target=10
print(pair_sum(my_list,target))
