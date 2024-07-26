list1 = [20, 10, 20, 5, 100]

smallest = list1[1]

for i in list1:
    if i < smallest:
        smallest = i
print(smallest)