# Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt

def first_threee(s):
    return s[:3]

s= input("Enter a string: ")
print(first_threee(s))