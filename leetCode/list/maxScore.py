# Given a list, write a function to get first, second best scores from the list.

# List may contain duplicates.

# Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
def first_second(myList):
    myList.sort()
    return myList[-1],myList[-2]

print(first_second(myList))


def first_second2(my_list):
    max1, max2 = float('-inf'), float('-inf')
    for i in my_list:
        if i>max1:
            max2 = max1
            max1 = i
        elif i>max2:
            max2 = i
    return max1, max2
 
my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second2(my_list))
#second best
def second_best(my_list):
    max2 = float('-inf')
    max1 = float('-inf')
    for i in my_list:
        if i>max1:
            max2 = max1
            max1 = i
        elif i>max2:
            max2 = i
    return max2

print(second_best(my_list))