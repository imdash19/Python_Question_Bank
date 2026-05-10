# Write a Python program to find the character with maximum frequency in a string. 
# The program should accept a string. Ignore spaces. 
# If multiple characters have same frequency, output the first occurring one. 
# Output should be a single character.

s = input().replace(" ", "")

max_char = s[0]
max_count = s.count(s[0])

for ch in s:
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        max_char = ch

print(max_char)
