def max_value_key(my_dict):
    max_key = max(my_dict, key=my_dict.get)
    return max_key
print(max_value_key({"a": 1, "b": 2, "c": 3}))
