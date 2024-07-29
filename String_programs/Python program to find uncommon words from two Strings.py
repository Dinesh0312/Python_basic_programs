
str1 = "Geeks for Geeks starting"

str2 = "Learning from Geeks for Geeks"

str1 = str1.split()

str2 = str2.split()

uncommon_word = []

for i in str1:
    if i not in str2:
        uncommon_word.append(i)
for i in str2:
    if i not in str1:
        uncommon_word.append(i)

print(uncommon_word)