str1 = 'Geeks123For123Geeks'

# O/P = GeeksForGeeks

for i in str1:
    if i.isdigit():
        continue
    else:
        print(i, end="")
print()

str2 = str1.replace(str(123), "")
print(str2)
