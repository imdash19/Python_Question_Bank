# Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

def convert_string_to_uppercase(s):
    count= 0
    for v in s[:4]:
        if v.isupper():
            count+=1

    if count >= 2:
        return s.upper()
    return s

s= input()
print(convert_string_to_uppercase(s))