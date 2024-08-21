myDict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}


# Sort by key
myDict = dict(sorted(myDict.items()))
print(myDict)

# Sort by value

short_dict = {}

for i in sorted(myDict, key=myDict.get):
    short_dict[i] = myDict[i]
print(short_dict)




