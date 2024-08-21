def common_elements(tuple1, tuple2):
    obj={}
    for i in tuple1:
        obj[i]=1
    for i in tuple2:
        if i in obj:
            obj[i]+=1
    common= ({k:v for k,v in obj.items() if v>1})
    #convert this to tuple
    return tuple(common.keys())


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (5, 2, 7, 8, 9)
print(common_elements(tuple1, tuple2))
