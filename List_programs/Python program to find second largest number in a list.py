
list1 = [70, 11, 80, 20, 4, 100]

first = second = list1[0]

for i in list1:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i

print(second)

