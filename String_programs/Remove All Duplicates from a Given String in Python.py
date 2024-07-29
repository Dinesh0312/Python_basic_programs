str1 = "geeksforgeeks"

str1 = list(str1)
print(str1)

new_str =[]

for i in str1:
    if i not in new_str:
        new_str.append(i)
print(new_str)

new = "".join(new_str)
print(new)


def removeDuplicate(str):
    s = set(str)
    s = "".join(s)
    print("Without Order:", s)

    t = ""
    for i in str:
        if i in t:
            pass
        else:
            t = t + i

    print("With Order:", t)


str = "geeksforgeeks"
removeDuplicate(str)