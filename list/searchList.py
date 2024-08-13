my_list=[1,2,3,4,5,6,7,8,9,10]

def listSearch(my_list,element):
    for i in my_list:
        if i==element:
            return my_list.index(i)
    return "Element not found"

print(listSearch(my_list,10))