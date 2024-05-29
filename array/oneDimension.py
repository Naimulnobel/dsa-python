from array import *
my_array = array('i', [1, 2, 3, 4, 5])
for i in my_array:
    print(i)

print("Accessing element at index 2:")
print(my_array[2])

#append any value to the array using append() method
my_array.append(6)
print("Array after appending 6:")
print(my_array)

#insert any value at any index using insert() method
my_array.insert(3, 7)
print("Array after inserting 7 at index 3:")
print(my_array)

#extend the array using extend() method
my_array.extend([8, 9, 10])
print("Array after extending the array:")
print(my_array)
#add items from list into array using fromlist() method
tempList = [11, 12, 13]
my_array.fromlist(tempList)
print("Array after adding elements from list:")
print(my_array)

#remove any element using remove() method
my_array.remove(12)
print("Array after removing 12:")
print(my_array)
#remove last element using pop() method
my_array.pop()
print("Array after popping last element:")
print(my_array)
#fetch any element through its index using index() method
print("Index of 10:")
print(my_array.index(10))
#reverse the array using reverse() method
my_array.reverse()
print("Array after reversing:")
print(my_array)
#Get the buffer info of an array using buffer_info() method
print("Buffer info of the array:")
print(my_array.buffer_info())
#count the occurences of an element using count() method
print("Count of 10:")
print(my_array.count(10))
#convert array to string using tostring() method
# strTemp = my_array.tostring()
# print("String conversion of the array:")
# print(strTemp)
#convert array to list using tolist() method
listTemp = my_array.tolist()
print("List conversion of the array:")
print(listTemp)
#slice elements from array
print("Slicing elements from the array:")
print(my_array[1:4])
