str1 = "geeks quiz practice code"
# O/P code practice quiz geeks

str1 = str1.split()

print(str1)

rev_list = []

for i in str1:
    rev_list.insert(0, i)
print(rev_list)

rev_str1 = " ".join(rev_list)
print(rev_str1)


