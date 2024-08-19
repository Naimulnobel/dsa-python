def check_same_frequency(list1, list2):
    # TODO
    my_dict={}
    my_dict2={}
    for item in list1:
        my_dict[item]=my_dict.get(item,0)+1

    for item in list2:
        my_dict2[item]=my_dict2.get(item,0)+1
    if my_dict==my_dict2:
        return True
    else:
        return False