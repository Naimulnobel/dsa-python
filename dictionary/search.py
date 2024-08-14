myDict={
    'name':'sachin',
    'age':34

}
def search(myDict,value):
    if value in myDict.values():
        print("present")
    else:
        print("not present")

search(myDict,34)