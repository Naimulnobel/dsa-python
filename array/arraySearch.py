import array
my_array = array.array('i', [1, 2, 3, 4, 5])
def linearSearch(array,element):
    for i in array:
        if i==element:
            return array.index(i)
    return "Element not found"
print(linearSearch(my_array, 5))