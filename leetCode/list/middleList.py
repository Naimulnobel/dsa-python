def middle(lst):
    #first find the length of the list
    length=len(lst)
    if length>2:
        return lst[1:length-1]
    else:
        return lst