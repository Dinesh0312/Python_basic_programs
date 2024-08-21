test_dict = {'Gfg': 4, 'is': 5, 'best': 9}
test_list = [8, 3, 2]

res = {}
for key, ele in zip(test_list, test_dict.items()):
    res[key] = dict([ele])

print(res)
#===================

res = {}

for i in test_list:
    res[i] = {}
    for k, v in test_dict.items():
        res[i][k] = v
print(res)

#===================

test_dict = {"Denu": 54, "Coder": 45, "Network": 87}
test_list = [11, 14, 7]

new_dict = {}

for i in test_list:
    new_dict[i] = {}
    for k, v in test_dict.items():
        new_dict[i][k] = v

print(new_dict)