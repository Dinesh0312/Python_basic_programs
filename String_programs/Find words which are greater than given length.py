str1 = "hello geeks for geeks is computer science portal"

length = 4

str1 = str1.split()

greater_word = []

for i in str1:
    if len(i) > length:
        greater_word.append(i)
print(greater_word)

