str1 = "thishasboth12"

has_digit = False
has_alpha = False

# Iterate through each character in the string
for i in str1:
    if i.isdigit():
        has_digit = True
    if i.isalpha():
        has_alpha = True

    # If both conditions are met, we can exit early
    if has_digit and has_alpha:
        break

# Check the results
if has_digit and has_alpha:
    print("True")
else :
    print("False")


