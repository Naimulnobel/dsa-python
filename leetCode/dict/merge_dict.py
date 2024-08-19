def merge_dicts(dict1, dict2):
    for key in dict2:
        if key in dict1:
            dict1[key] += dict2[key]
        else:
            dict1[key] = dict2[key]
    return dict1
print(merge_dicts({"a": 1, "b": 2}, {"a": 3, "c": 4}))
