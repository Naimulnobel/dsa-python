def count_word_frequency(words):
    obj={}
    for word in words:
        if word in obj:
            obj[word]+=1
        else:
            obj[word]=1
    return obj




print(count_word_frequency(["apple", "banana", "apple", "apple", "banana", "orange"]))
