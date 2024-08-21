dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

dict1.update({'c': 3})
print(dict1)

dict1['c'] = 3

print(dict1)

# dict3 = dict1.update(dict2)
# print(dict3)


for i in dict2.keys():
    dict1[i] = dict2[i]
print(dict1)

dict3 = dict1 | dict2

print(dict3)