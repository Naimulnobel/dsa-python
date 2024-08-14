#clear
myDict={
    'name':'sachin',
    'age':34
}
myDict.clear()
print('clear',myDict)
#copy
myDict={
    'name':'sachin',
    'age':34
}
newDict=myDict.copy()
print('copy',newDict)
#fromkeys
keys={'a','b','c','d'}
value=10
myDict=dict.fromkeys(keys,value)
print('fromkeys',myDict)
#get
myDict={
    'name':'sachin',
    'age':34
}
print('get',myDict.get('name'))
#items
myDict={
    'name':'sachin',
    'age':34
}
print('items',myDict.items())
#keys
myDict={
    'name':'sachin',
    'age':34
}
print('key',myDict.keys())
#pop
myDict={
    'name':'sachin',
    'age':34
}
print(myDict.pop('name'))
print('pop',myDict)
#popitem
myDict={
    'name':'sachin',
    'age':34
}
print(myDict.popitem())
print('popItem',myDict)
#setdefault
myDict={
    'name':'sachin',
    'age':34
}
print(myDict.setdefault('name','nobel'))
print(myDict.setdefault('designation','actor'))
print('setdefault',myDict)
#update
myDict={
    'name':'sachin',
    'age':34
}
myDict.update({'name':'nobel','age':30,'designation':'actor'})
print('update',myDict)
#values
myDict={
    'name':'sachin',
    'age':34
}
print('values',myDict.values())
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
