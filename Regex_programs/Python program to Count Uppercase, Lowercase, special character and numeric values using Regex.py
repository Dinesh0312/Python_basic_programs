import re

string = "ThisIsGeeksforGeeks!, @123"

uppercase_characters = re.findall(r"[A-Z]", string)
lowercase_characters = re.findall(r"[a-z]", string)
numerical_characters = re.findall(r"[0-9]", string)
special_characters = re.findall(r"[,@ .!?]", string)

print(uppercase_characters)
print(lowercase_characters)
print(numerical_characters)
print(special_characters)