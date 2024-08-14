def reverseArray(my_list):
    for i in range(len(my_list)//2):
       temp=my_list[i]
       other=my_list[len(my_list)-i-1]
       my_list[i]=other
       my_list[len(my_list)-i-1]=temp
    return my_list

my_list=[1,2,3,4,5,6,7,8,9,10]
print(reverseArray(my_list))