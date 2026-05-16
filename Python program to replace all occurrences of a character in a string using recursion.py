# Write a program to replace all occurrences of a character in a string using recursion.
# User enters string, target character, and replacement character.
# Each call checks first character: if matches, replace;
# else keep original. Recursion continues on remaining string.
# Output is modified string.

def replace_char(s, target, replacement):
    if s == "":
        return ""
    
    if s[0] == target:
        return replacement + replace_char(s[1:], target, replacement)
    else:
        return s[0] + replace_char(s[1:], target, replacement)

text = input("Enter a string: ")
target = input("Enter target character: ")
replacement = input("Enter replacement character: ")

print(replace_char(text, target, replacement))
