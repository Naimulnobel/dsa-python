shoppingList=['apple','banana','cherry','dates','eggplant']
print(shoppingList[0])
print('apple' in shoppingList)
print(shoppingList[-1])
print(shoppingList[::-1])
for item in shoppingList:
    print(item)
print(len(shoppingList))

for i in range(len(shoppingList)):
    print(shoppingList[i])


intList=[1,2,3,4,5,6,7,8,9,10]
intList[2]=33
print(intList)
intList.insert(1,22)
print(intList)