def two_pair(my_list,target):
    for i in range(len(my_list)):
        for j in range(i+1,len(my_list)):
            if my_list[i]==my_list[j]:
                continue
            if my_list[i]+my_list[j]==target:
                return [i,j]
    return "No pair found"

my_list=[1,2,3,4,5,6,7,8,9,10]
target=10
print(two_pair(my_list,target)) 

def two_pair2(my_list,target):
    obj={}
    for i in range(len(my_list)):
        obj[my_list[i]]=i
    for i in range(len(my_list)):
        complement=target-my_list[i]
        if complement in obj and obj[complement]!=i:
            return [i,obj[complement]]
    return "No pair found"

print(two_pair2(my_list,target))