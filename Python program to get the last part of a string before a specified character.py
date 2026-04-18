# Write a Python program to get the last part of a string before a specified character.

s = input("Enter a string: ")
ch = input("Enter a character: ")

pos = s.rfind(ch)

if pos != -1:
    result = s[:pos]
    print(result)
else:
    print("Character not found in string")