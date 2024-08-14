#clear
myDict={
    'name':'sachin',
    'age':34
}
myDict.clear()
print(myDict)
#copy
myDict={
    'name':'sachin',
    'age':34
}
newDict=myDict.copy()
print(newDict)
#fromkeys
keys={'a','b','c','d'}
value=10
myDict=dict.fromkeys(keys,value)
print(myDict)
#get
myDict={
    'name':'sachin',
    'age':34
}
print(myDict.get('name'))
#items
myDict={
    'name':'sachin',
    'age':34
}
print(myDict.items())
#keys
myDict={
    'name':'sachin',
    'age':34
}
print(myDict.keys())
#pop
myDict={
    'name':'sachin',
    'age':34
}
print(myDict.pop('name'))
print(myDict)
#popitem
myDict={
    'name':'sachin',
    'age':34
}
print(myDict.popitem())
print(myDict)
#setdefault
myDict={
    'name':'sachin',
    'age':34
}
print(myDict.setdefault('name','nobel'))
print(myDict.setdefault('designation','actor'))
print(myDict)
#update
myDict={
    'name':'sachin',
    'age':34
}
myDict.update({'name':'nobel','age':30,'designation':'actor'})
print(myDict)
#values
myDict={
    'name':'sachin',
    'age':34
}
print(myDict.values())
#output
#{}
#{'name': 'sachin', 'age': 34}
#{'a': 10, 'b': 10, 'c': 10, 'd': 10}
#sachin
#dict_items([('name', 'sachin'), ('age', 34)])
#dict_keys(['name', 'age'])
#sachin
#{'age': 34}
#('age', 34)
#{'name': 'sachin'}
#sachin
#actor
#{'name': 'nobel', 'age': 30, 'designation': 'actor'}
