

str1 = "Nitin"

str1 = str1.lower()

rev_str1 = ""

for i in str1:
    rev_str1 = i + rev_str1
if rev_str1 == str1:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")
