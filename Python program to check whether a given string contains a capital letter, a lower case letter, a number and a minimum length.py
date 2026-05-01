# Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length.
# Sample Output:
# Input the string: W3resource
# ['Valid string.']

s = input("Input the string: ")
if any(c.isupper() for c in s) and any(c.islower() for c in s) and any(c.isdigit() for c in s) and len(s) >= 8:
    print(['Valid string.'])
else:
    print(['Invalid string.'])