
list1 = ["One", "Two", "Three", "Four", "Five"]

list2 = [1, 2, 3, 4, 5]

dict1 = {}

for i in range(len(list1)):
    dict1[list1[i]] = list2[i]
print(dict1)


dict2 = dict(zip(list1,list2))

print(dict2)