# Write a Python program that concatenates uncommon characters from two strings.

s1 = input()
s2 = input()

result = ""

for ch in s1:
    if ch not in s2:
        result += ch

for ch in s2:
    if ch not in s1:
        result += ch

if result:
    print(result)
else:
    print("No uncommon characters")