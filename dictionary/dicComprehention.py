import random
new_dict={
    'name':'sachin',
    'age':34
}
print(new_dict)
new_dict1={key:value for key,value in new_dict.items()}
print(new_dict1)
arr=[1,2,3,4,5]
new_dict2={arr[i]:i for i in range(len(arr))}
print(new_dict2)

city_names=["delhi","mumbai","chennai"
            ,"kolkata","hyderabad"]
#city temperatures is above 25

new_dict3={city:random.randint(20,30) for city in city_names }

print(new_dict3)
new_dict4={key:value for key,value in new_dict3.items() if value>25}
print(new_dict4)