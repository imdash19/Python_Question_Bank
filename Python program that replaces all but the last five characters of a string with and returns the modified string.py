# Write a Python program that replaces all but the last five characters of a string with "*" and returns the modified string.
# Original String: kdi39323swe
# new string: ******23swe
# Original String: 12345abcdef
# new string: ******bcdef
# Original String: 12345
# new string: 12345

s=input("Enter a string: ")

print('*'*(len(s)-5)+s[-5:]) if len(s)>5 else print(s)