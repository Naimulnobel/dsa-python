def count_word_frequency(words):
    obj={}
    for word in words:
        if word in obj:
            obj[word]+=1
        else:
            obj[word]=1
    return obj


def merge_dicts(dict1, dict2):
    for key in dict2:
        if key in dict1:
            dict1[key] += dict2[key]
        else:
            dict1[key] = dict2[key]
    return dict1

print(count_word_frequency(["apple", "banana", "apple", "apple", "banana", "orange"]))
print(merge_dicts({"a": 1, "b": 2}, {"a": 3, "c": 4}))