list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

duplicate = []

for i in list1:
    if i not in duplicate:
        duplicate.append(i)
print(duplicate)

dict1 = {}

for i in duplicate:
    count = 0
    for j in list1:
        if i ==j:
            count += 1
        dict1[i] = count

print(dict1)


